<div align="center">

<img src="skills/universal-expert-team/assets/icon.svg" alt="Universal Expert Team" width="88" height="88">

# Universal Expert Team

**依任務組隊，用證據驗收，交付可用成果。**

通用多專家協作技能 · 研究、寫作、程式、分析與跨領域工作

[![License: MIT](https://img.shields.io/badge/License-MIT-2563eb.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/jerry0327/universal-expert-team?color=2563eb)](https://github.com/jerry0327/universal-expert-team/releases/latest)
[![Language](https://img.shields.io/badge/繁體中文-English-475569)](README.en.md)

[下載版本](https://github.com/jerry0327/universal-expert-team/releases/latest) · [安裝指南](docs/installation.md) · [使用範例](docs/usage.md) · [技能原文](skills/universal-expert-team/SKILL.md)

</div>

---

Universal Expert Team 讓具備代理工具的 AI 助手，依你的目標規劃分工、委派工作、整合成果，並在需要時安排獨立審查與修正。團隊專長由任務決定；可以是研究與資料核對，也可以是程式實作、使用者體驗與整合測試。

這個專案提供完整、可閱讀的技能與參考文件。**實際的子代理、搜尋、檔案、瀏覽器和模型設定由執行平台提供。** 沒有相應工具時，技能會要求助手說明限制，完成仍可進行的工作，並如實標示尚未驗證的部分。

## 它協助你完成什麼

| 需求 | 工作方式 |
| --- | --- |
| 任務跨越多種專長 | 由成果、相依關係與風險設計團隊；不套用固定名單或代理數量。 |
| 希望直接拿到成果 | 在已授權範圍內研究、編寫、修改、驗證與整合，預設一次完整交付。 |
| 重要內容需要再確認 | 視風險選擇來源核對、獨立審查、反例搜尋或實際操作驗證。 |
| 反覆修正容易失焦 | 先定義可觀察的驗收條件，只修復具體缺陷；達標或遇到明確阻礙就停止。 |
| 平台能力不一致 | 先確認本次工作實際可用的工具、權限與容量，再決定執行方式。 |

適合可拆分、需要多種判斷的工作。若工作很簡單，或沒有值得獨立處理的部分，助手可以直接完成；多列幾個角色名稱不代表真的建立了團隊。

## 三種工作模式

| 模式 | 何時使用 | 交付行為 |
| --- | --- | --- |
| **一次完整交付** | 預設；「一次做完」「直接交付」 | 完成必要分工、事實核對與整合，修正已知重大問題後交付。 |
| **反覆審查與修正** | 「反覆驗證」「修到好」「直到符合驗收條件」 | 在可用時由非作者審查，修正具體缺陷，再驗證受影響部分。沒有預設輪數。 |
| **混合範圍** | 不同部分需要不同強度的驗收 | 例如：數據分析反覆核對，摘要一次交付。這是前兩種模式的分區組合。 |

「深入」「專業」「高品質」本身不代表無限循環。任何模式都必須處理已知重大錯誤；「反覆」也不代表可以任意擴大工作範圍。

## 下載與開始使用

1. 開啟 [Releases](https://github.com/jerry0327/universal-expert-team/releases/latest)，選擇技能套件 `universal-expert-team-v1.0.0.zip`。也可從本儲存庫取得 `skills/universal-expert-team/` 完整資料夾，並依[安裝指南](docs/installation.md)將儲存庫根目錄的 `LICENSE` 一併複製至安裝資料夾內。
2. **支援技能上傳的 ChatGPT 環境：**上傳完整 ZIP，請平台安裝並確認載入。是否可安裝取決於你的帳號與目前介面；附件上傳成功不等於技能安裝成功。
3. **Codex 本機環境：**將完整技能資料夾放入專案的 `.agents/skills/universal-expert-team/`，再確認技能已被偵測。指令與其他安裝範圍見[安裝指南](docs/installation.md)。此路徑依據 [OpenAI 官方文件](https://learn.chatgpt.com/docs/build-skills)。
4. 安裝完成後，提供你的目標、來源與驗收條件，再明確請助手使用這個技能。

```text
使用 universal-expert-team，根據以下任務自主設計分工並一次完整交付。

目標：［希望得到的成果］
來源：［檔案、連結、資料或工作目錄］
限制：［時間、格式、可修改範圍、不得執行的動作］
驗收：［怎樣才算完成］

請先確認本次可用的代理與工具；實際委派有助益的獨立工作。
交付成果、必要的驗證證據，以及仍無法確認的部分。
```

已安裝且介面支援時，可在 ChatGPT 的技能選單以 `@` 選取，或在 Codex 使用 `$universal-expert-team`。**單獨輸入 `@universal-expert-team` 不會下載或安裝技能。** 單純貼上指令也不會新增多代理執行能力。[官方技能呼叫說明](https://learn.chatgpt.com/docs/build-skills)

## 可直接複製的任務

**研究與決策**

```text
使用 universal-expert-team，比較［方案 A／B／C］對［使用情境］的適用性。
依問題決定需要的專長，一次交付比較表、建議與來源。
將來源事實、推論與缺少證據的部分分清楚。
若無法搜尋或讀取原始資料，請交付可支持的分析並標示限制。
```

**程式開發與反覆驗收**

```text
使用 universal-expert-team，在此儲存庫修復［可重現問題］。
自主安排實作與可用的獨立審查；反覆修正直到重現案例通過、
相關既有檢查通過，且沒有未解決的重大缺陷。
可修改必要程式與測試；不要部署或對外發送訊息。
交付變更、驗證結果與尚存風險。
```

**寫作與混合範圍**

```text
使用 universal-expert-team，把提供的資料整理成［讀者］能使用的報告。
數據與引用反覆核對，直到每項主要主張都有可追溯來源；
文案與版面一次完整交付。不要補寫來源沒有提供的事實。
輸出報告，以及必要的來源與限制說明。
```

更多例子與驗收寫法見[使用指南](docs/usage.md)。

## 如何判斷成果可信

- **角色、代理與成果分開記錄。** 真正建立了幾位工作者、實際做了什麼，必須與可觀察的執行一致。
- **審查要能找到問題。** 審查者取得成果、來源與驗收條件；作者再讀一次不算獨立審查。
- **以證據處理分歧。** 多位代理引用同一來源，不會增加獨立證據；意見多數也不等於正確。
- **修改後重新確認相關部分。** 舊版本通過的審查不能直接保證新版本；無須反覆重做未受影響的工作。
- **停止條件清楚。** 達成約定要求且沒有未解決的重大缺陷就交付；重要資料或能力不足時說明阻礙。

完整方法見[審查策略](skills/universal-expert-team/references/review-strategies.md)與[工作分包](skills/universal-expert-team/references/work-packages.md)。

## 平台與能力邊界

技能優先使用平台原生代理介面。在平台允許選擇時，依其實際可用能力選擇最高能力層級與最深支援推理設定，並區分「請求的設定」與「已觀察到的設定」。它不保證任一模型、並行數量或背景執行能力。

| 平台實際提供 | 可以期待 |
| --- | --- |
| 技能載入與真正的子代理工具 | 依可用容量派工、收集成果、安排審查與整合。 |
| 技能載入，沒有子代理工具 | 由單一助手依工作流程處理；不宣稱完成多代理或獨立審查。 |
| 只能貼上文字 | 可以參考流程；不代表已安裝技能、載入所有參考文件或取得新工具。 |
| 缺少搜尋、資料、寫入或驗證能力 | 完成不受影響的部分，將受影響成果標為受阻或尚未驗證。 |

這個公開版自含所需參考文件，不依賴私人工作區技能。平台權限、使用者授權與適用的執行限制仍然有效；技能文字不能建立不存在的 API、授權或存取能力。詳見[執行邊界](skills/universal-expert-team/references/execution-boundaries.md)與[執行環境配接](skills/universal-expert-team/references/runtime-adapters.md)。

## 專案內容

| 路徑 | 用途 |
| --- | --- |
| [`skills/universal-expert-team/`](skills/universal-expert-team/) | 完整安裝單位：技能、介面資訊、圖示與參考文件。 |
| [`docs/installation.md`](docs/installation.md) | 下載、ChatGPT 與 Codex 安裝、確認載入及更新。 |
| [`docs/usage.md`](docs/usage.md) | 中英文提示範例、模式選擇、驗收與限制處理。 |
| [`README.en.md`](README.en.md) | English project overview. |

## 授權與回饋

採用 [MIT License](LICENSE)，可使用、修改與散布，請保留授權聲明。歡迎透過 [Issues](https://github.com/jerry0327/universal-expert-team/issues) 提供可重現問題，或以 Pull Request 改善流程與文件。回報時請說明平台、預期行為與實際結果，並移除私人資料。

本專案為獨立開源技能，未宣稱獲 OpenAI 或其他平台官方認證。
