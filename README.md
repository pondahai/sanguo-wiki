# 三國演義 Wiki

> 「如果我拿一本三國演義原文文字檔 能夠一鍵變成wiki資料庫嗎」

這個專案就是那句話的答案:把一本《三國演義》原文 PDF,自動變成可瀏覽、可查證的 wiki 資料庫。

全書 120 回正文自動切分、人名自動連結,137 位人物各有條目——生平由本地 LLM
以 map-reduce 方式「全文閱讀」原著後生成,**每條事蹟都附回數出處,可回溯查證**。

- **Obsidian vault**(`vault/`):`[[人名]]` 點擊跳轉,graph view 看人物關係網
- **靜態網站**(`site/`,261 頁):零相依,雙擊 `site/index.html` 就能看;
  索引頁即時篩選、自動深色模式,可直接部署 GitHub Pages

## 運作原理

核心想法:**能用純程式做的絕不用 LLM;必須用 LLM 的,不讓它憑記憶說話**。

規則性的工作(切章節、認人名、算統計)交給 regex 和字典,又快又不會錯;
需要「理解」的工作(讀情節、抽事實、寫生平)才交給 LLM,而且強制它只根據
餵給它的原文說話——這是防幻覺的關鍵,詳見下方〈防幻覺設計〉。

### 處理流程

```mermaid
flowchart TD
    A[sango.pdf 648頁] -->|"pypdf 抽文字(不用LLM)"| B[sanguo_raw.txt 187萬字]
    B -->|"build_wiki.py(不用LLM)<br>regex 切回·人名字典連結·統計"| C["vault/ 骨架<br>120回正文 + 137人物頁 + 索引"]
    B -->|"extract_facts.py(LLM·Map)<br>逐回全文閱讀,抽本人言行"| D["data/facts/ch_*.json<br>~1萬條事實,每條綁回數"]
    D -->|"compose_bios.py(LLM·Reduce)<br>只准根據事實清單撰寫"| E["人物生平<br>每條事蹟附回數出處"]
    C --> F
    E --> F["vault/ 完整版"]
    F -->|"build_html.py(不用LLM)<br>Markdown→HTML"| G["site/ 靜態網站 261頁"]
```

### 哪裡用 LLM,哪裡不用

| 步驟 | 工具 | 為什麼 |
|---|---|---|
| PDF 抽文字 | pypdf,**不用 LLM** | 機械轉換,程式做零錯誤 |
| 切 120 回 | regex「第○○回」,**不用 LLM** | 章回標題格式固定 |
| 人名連結 | 人物字典(`characters.py`)+ 最長優先匹配,**不用 LLM** | 「孔明→諸葛亮」是查表,不需要理解 |
| 出場統計、索引、導航 | 純 Python,**不用 LLM** | 數數而已 |
| 逐回抽事實(Map) | **LLM** | 「這一回趙雲做了什麼」需要讀懂情節 |
| 撰寫人物生平(Reduce) | **LLM** | 把 499 條零散事實組織成通順傳記,需要語言能力 |
| Markdown → HTML | 純 Python,**不用 LLM** | 格式轉換 |

不用 LLM 的步驟全部秒級完成;用 LLM 的兩步在本地 vLLM(Qwen3.6-35B)上跑約
3-4 小時,零 API 費用。

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

LLM 寫歷史人物最大的問題是幻覺(憑訓練記憶腦補)。第一版直接讓模型
「讀 12,000 字摘錄 + 常識補充」,結果生出「趙雲是結義四弟」這種民間戲曲
才有的說法。改成 map-reduce 後:

1. **Map**:逐回把「完整正文」餵給模型(每回約 5 千~1.5 萬字,遠小於
   context 上限),只准抽取本回正文中該人物「本人言行」的事實,輸出 JSON
   存於 `data/facts/ch_*.json`,每條綁定回數——模型從頭到尾每個字都真的讀過
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
