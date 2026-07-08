# -*- coding: utf-8 -*-
"""用 vLLM (Qwen3.6) 為人物頁生成生平摘要。
可重複執行:已生成的頁面自動跳過。用法: python enrich_llm.py [人數上限,預設30]
"""
import json
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from characters import CHARACTERS
from build_wiki import RAW, VAULT, parse_chapters, reflow, build_alias_map

API = "http://100.89.149.50:8002/v1/chat/completions"
MODEL = "nvidia/Qwen3.6-35B-A3B-NVFP4"
MAX_EXCERPT = 12000  # 每人物的原文摘錄字數上限
PLACEHOLDER = "_(待 LLM 生成)_"


def collect_excerpts():
    """人物 -> [(回數, 段落)]"""
    chapters = parse_chapters(RAW.read_text(encoding="utf-8"))
    amap, pattern = build_alias_map()
    hits = defaultdict(list)
    for num, _, body in chapters:
        for par in reflow(body):
            found = {amap[m] for m in pattern.findall(par)}
            for c in found:
                hits[c].append((num, par))
    return hits


def make_prompt(canon, aliases, excerpts):
    # 平均取樣:全書出場段落中最多取 ~MAX_EXCERPT 字
    total = 0
    picked = []
    step = max(1, len(excerpts) // 60)
    for i in range(0, len(excerpts), step):
        num, par = excerpts[i]
        if total + len(par) > MAX_EXCERPT:
            continue  # 跳過過長段落,繼續取後期章回
        picked.append(f"(第{num}回) {par}")
        total += len(par)
    names = "、".join(CHARACTERS.keys())
    alias_str = f"(別名:{'、'.join(aliases)})" if aliases else ""
    return (
        f"你是《三國演義》wiki 的編輯。根據以下小說原文摘錄,為人物「{canon}」{alias_str}"
        "撰寫 wiki 條目內容,使用繁體中文、Markdown 格式,只輸出以下三節:\n\n"
        "### 生平概述\n(2-4 段,依小說情節,不要引入正史中小說沒有的內容)\n\n"
        "### 重要事蹟\n(條列 3-8 項,每項註明大約回數)\n\n"
        "### 人物關係\n(條列,如主公、部下、兄弟、對手)\n\n"
        f"提到下列人物時請用 Obsidian 連結格式 [[人物名]](僅限這些正名:{names})。"
        "不要輸出標題以外的前言、結語、編輯註記或修正說明;摘錄未涵蓋的情節可依小說常識補充,直接寫成定稿。\n\n"
        "=== 原文摘錄 ===\n" + "\n\n".join(picked)
    )


def call_llm(prompt):
    body = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4000,
        "temperature": 0.4,
        "chat_template_kwargs": {"enable_thinking": False},
    }).encode()
    req = urllib.request.Request(API, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        out = json.load(r)["choices"][0]["message"]["content"]
    return re.sub(r"<think>.*?</think>", "", out, flags=re.S).strip()


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    hits = collect_excerpts()
    ranked = sorted(CHARACTERS, key=lambda c: -len(hits.get(c, [])))[:limit]
    done = skipped = 0
    for canon in ranked:
        page = VAULT / "人物" / f"{canon}.md"
        text = page.read_text(encoding="utf-8")
        if PLACEHOLDER not in text:
            skipped += 1
            continue
        print(f"generating {canon} ...", flush=True)
        try:
            bio = call_llm(make_prompt(canon, CHARACTERS[canon], hits.get(canon, [])))
        except Exception as e:
            print(f"  FAILED {canon}: {e}", flush=True)
            continue
        page.write_text(text.replace(PLACEHOLDER, bio), encoding="utf-8")
        done += 1
        print(f"  ok ({len(bio)} chars)", flush=True)
    print(f"done={done} skipped={skipped}")


if __name__ == "__main__":
    main()
