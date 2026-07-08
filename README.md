# 三國演義 Wiki

把一本《三國演義》原文 PDF,自動變成可瀏覽、可查證的 wiki 資料庫。

全書 120 回正文自動切分、人名自動連結,137 位人物各有條目——生平由本地 LLM
以 map-reduce 方式「全文閱讀」原著後生成,**每條事蹟都附回數出處,可回溯查證**。

- **Obsidian vault**(`vault/`):`[[人名]]` 點擊跳轉,graph view 看人物關係網
- **靜態網站**(`site/`,261 頁):零相依,雙擊 `site/index.html` 就能看;
  索引頁即時篩選、自動深色模式,可直接部署 GitHub Pages

## 快速開始

只是想看:用 Obsidian 開啟 `vault/`,或用瀏覽器開 `site/index.html`,完事。

想自己生成(或換一本書),需要:

- Python 3 + `pypdf`
- 一個 OpenAI 相容的 LLM 端點(本專案用 vLLM 跑 Qwen3.6-35B,
  端點與模型名在 `scripts/extract_facts.py` 開頭兩行,自行修改)

```bash
# 0. 把原文 PDF 抽成純文字 data/sanguo_raw.txt(見下方「換一本書」)
python scripts/build_wiki.py      # 1. 切章回 + 人名連結 + 人物頁/索引(秒級)
python scripts/extract_facts.py   # 2. Map:逐回全文餵 LLM,抽結構化事實(~2-3 小時)
python scripts/compose_bios.py    # 3. Reduce:依事實清單撰寫人物生平(~1 小時)
python scripts/build_html.py      # 4. vault → site 靜態網站(秒級)
```

每一步都可中斷重跑:已完成的章回與人物自動跳過。

## 防幻覺設計

LLM 寫歷史人物最大的問題是幻覺(憑訓練記憶腦補)。本專案的做法:

1. **Map**:逐回把「完整正文」餵給模型,只准抽取本回正文中該人物「本人言行」的
   事實,輸出 JSON 存於 `data/facts/ch_*.json`,每條綁定回數
2. **Reduce**:生平只准根據事實清單撰寫,清單外的內容「即使是常識」也禁止;
   重要事蹟逐條標註回數
3. **輸出防護**:repetition_penalty 抑制小模型的重複迴圈,退化自動偵測 →
   升溫重試 → 程式化去重,三層保底

看到可疑敘述時,打開對應回數的 facts JSON 即可查證來源;錯了就刪那條事實、
重生成該人物(單人約 30 秒),不必重跑全部。

## 專案結構

```
data/sanguo_raw.txt   原文純文字(PDF 抽出)
data/facts/           逐回事實清單(map 產物,生平的可查證來源)
scripts/characters.py 人物表:正名 + 別名(字、號、稱呼)
scripts/*.py          四步流水線
vault/                Obsidian vault(回目/、人物/、索引)
site/                 靜態 HTML 網站(自動生成)
```

## 換一本書

1. 用 `pypdf` 把 PDF 抽成純文字放 `data/`(或直接放 txt)
2. 改 `build_wiki.py` 的章節切分 regex(本專案認「第○○回」)
3. 換掉 `characters.py` 的人物表
4. 照跑四步

## 授權

《三國演義》原文為公有領域。腳本部分隨意使用。
