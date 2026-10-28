# 使用指南 / Usage

[繁體中文首頁](../README.md) · [English overview](../README.en.md) · [安裝 / Installation](installation.md) · [English instructions](#english)

## 把任務交代清楚，讓助手決定分工

你不需要先列出一套專家職稱。提供目標、來源、限制與完成條件，助手再根據工作設計專長與分包。只在角色確有必要時指定，例如「請安排未參與作者工作的審查者核對主要數據」。

```text
使用 universal-expert-team 完成以下工作。

目標與讀者：［誰要使用什麼成果］
輸入：［檔案、資料、連結、專案目錄，以及優先依據］
交付格式：［文章、程式變更、比較表、簡報、資料檔等］
可執行範圍：［可修改內容、可使用的來源、允許的外部動作］
限制：［不能做什麼、時間與資源要求］
模式：［一次完整交付／反覆審查與修正／指定範圍混合］
驗收條件：［可以觀察或檢查的完成標準］

先確認本次實際可用能力，依任務設計團隊與工作順序。
在已授權範圍內自主完成；重要不確定性與真正阻礙請說明。
```

安裝後可使用平台支援的技能選擇方式，或明確要求「使用 universal-expert-team」。貼上這段文字本身不會安裝技能。[安裝與載入確認](installation.md)

## 模式選擇與停止條件

| 你想要的工作方式 | 建議用語 | 合理的停止條件 |
| --- | --- | --- |
| 一次拿到可用成果 | 「一次完整交付，完成必要檢查」 | 已完成要求與必要驗證，沒有已知重大缺陷。 |
| 持續修復直到達標 | 「反覆審查與修正，直到下列驗收成立」 | 驗收成立，或缺少必要來源、權限、能力造成具體阻礙。 |
| 只對高風險部分反覆驗證 | 「數據反覆核對，摘要一次交付」 | 各部分分別符合指定模式與條件。 |

反覆模式沒有固定輪數。每一輪應由新的缺陷、修正或未解問題驅動，而不是重複相同提問。若方法不再帶來進展，應改變方法或交代限制。使用者改變方向時，保留仍有效的工作，只更新受影響部分。

「獨立審查」需要實際不同的工作者與可用能力。若你明確要求獨立審查作為必要門檻，而平台沒有可用代理或審查渠道，成果可以先完成，但該門檻仍須標為未完成。

## 可觀察的驗收條件

| 模糊要求 | 更容易驗收的寫法 |
| --- | --- |
| 「研究完整」 | 「逐一回答這四個問題，優先使用原始來源，主要主張附來源，缺少全文的部分標示出來。」 |
| 「程式要正常」 | 「提供的重現案例通過、相關既有檢查通過，並說明未執行的驗證。」 |
| 「報告要專業」 | 「讀者能找到問題、方法、主要結果與建議；每個關鍵數字可追溯至輸入資料。」 |
| 「簡報要漂亮」 | 「輸出指定比例與頁數範圍，文字沒有裁切，圖表標籤可讀；以實際渲染確認。」 |
| 「資料要正確」 | 「列數、欄位、單位與總計符合指定規則；缺失與重複值有明確處理紀錄。」 |

驗收應與用途相稱。小幅、可逆的修改不需要為了湊數增加測試；可操作產品或視覺成果的驗收若包含實際行為、外觀，則應使用相應工具確認。

## 任務範例

### 研究：比較方案與證據品質

```text
使用 universal-expert-team，評估［方案 A／B／C］是否適合［具體情境］。
依研究問題自主分工，一次完整交付比較表與建議。

優先使用原始研究、官方文件或可直接核對的資料。
主要結論附來源，區分來源事實、推論與不確定性。
如果資訊互相矛盾，說明差異可能來自哪些條件，避免直接以多數決裁定。
若無法取得全文或最新來源，請縮小結論到實際證據可以支持的程度。
```

多位工作者讀到同一篇文章，並不構成多份獨立證據。需要的是來源品質、適用範圍與主張之間的關係。

### 程式：修復可重現問題

```text
使用 universal-expert-team，在目前儲存庫修復［問題描述］。
重現方式：［步驟／輸入／錯誤訊息］。
預期行為：［可觀察的結果］。

可以修改必要程式與相關測試，請保留既有使用者變更。
自主分工實作、問題分析與可用的獨立審查。
反覆修正直到重現案例與相關既有檢查通過，且沒有未解決的重大缺陷。
不要部署、合併至主分支或對外發送訊息。
交付變更原因、行為差異、驗證結果與剩餘限制。
```

同一共享檔案同時由多位工作者修改會造成衝突；應分配寫入範圍或使用真正隔離的候選版本，由明確的整合者合併。

### 寫作：忠於來源的說明文件

```text
使用 universal-expert-team，將附件整理成給［讀者］的［文件種類］。
使用［語言／語氣／篇幅］，保留來源能支持的實質內容。
來源沒有交代的日期、數字或因果關係請勿補寫。

事實與引用反覆核對；文案與結構一次完整交付。
驗收：每個關鍵事實都能追溯至輸入，術語一致，讀者能理解下一步。
請交付完成文件與必要的限制說明。
```

### 資料：分析與可重現的結果

```text
使用 universal-expert-team，分析附件中的［資料］並回答［問題］。
先核對欄位意義、單位、缺失值、重複列與時間範圍。
可以建立分析程式與結果檔，保留原始資料。

資料清理與計算反覆驗證，文字摘要一次交付。
驗收：總數可對帳、主要指標有明確定義，輸出可由提供的步驟重現。
不清楚的欄位不要自行假定；先完成不受影響的分析並指出需補資訊。
```

### 計畫：先產出方案，不執行外部動作

```text
使用 universal-expert-team，為［活動／遷移／課程／專案］制定可執行計畫。
根據相依關係與風險安排所需專長。
目前只做規劃，不採購、不發訊息、不更動外部系統。
一次交付里程碑、所需輸入、主要風險與可檢查的完成條件。
```

這些範例的角色不是固定名單。助手應根據來源、目標與真正可用能力調整分工，而不是在每個任務建立相同團隊。

## 能力不足時，成果應如何呈現

| 缺少的能力或輸入 | 合理處理 |
| --- | --- |
| 沒有真實子代理 | 以單一助手完成可行部分，明說沒有獨立代理執行。 |
| 無法搜尋或讀取必要來源 | 使用已有資料，標示無法核對的範圍，不宣稱取得最新證據。 |
| 沒有寫入權限 | 交付分析或可套用變更，說明實際檔案尚未修改。 |
| 無法執行測試或渲染 | 清楚區分靜態檢查與實際執行；需要操作證據的驗收仍未通過。 |
| 沒有模型選擇權 | 使用平台提供的能力，說明無法確認或控制的設定。 |
| 重要授權或決策缺失 | 完成不受影響的工作，再指出需要補足的具體事項。 |

技能優先採用平台原生代理介面，並在允許選擇時採用最高可用能力與最深支援推理。這項原則不能繞過權限、建立不存在的工具，或把未知設定描述為已生效。

## 預期收到的交付

成果應直接可用，並包含理解結果所需的證據：完成的文章、檔案或程式變更；相關來源或驗證結果；尚存不確定性及其影響。若有受阻門檻，指出哪一項未通過與如何解除。

不需要把內部派工對話、冗長審查紀錄或私人筆記塞進成品。若確有必要知道執行情況，簡要區分實際工作者、已執行的檢查與尚未測試的行為即可。

延伸閱讀：[工作分包](../skills/universal-expert-team/references/work-packages.md) · [審查策略](../skills/universal-expert-team/references/review-strategies.md) · [執行邊界](../skills/universal-expert-team/references/execution-boundaries.md) · [環境配接](../skills/universal-expert-team/references/runtime-adapters.md)

---

## English

### Describe the outcome; let the work determine the team

You do not need a predetermined list of expert titles. Provide the outcome, inputs, boundaries, and acceptance evidence. Specify a role only when it matters, such as a reviewer who did not author the calculation.

```text
Use universal-expert-team for this task.

Outcome and audience: [who needs what]
Inputs: [files, data, links, project directory, authoritative sources]
Deliverable: [report, code changes, comparison, slides, data file]
Authorized scope: [editable content, permitted sources and external actions]
Constraints: [excluded actions, time and resource limits]
Mode: [single delivery / iterative review and repair / mixed scope]
Acceptance: [observable completion criteria]

Check this session's actual capabilities, then design the team and sequence.
Complete the authorized work autonomously. Identify material uncertainty
and concrete blockers.
```

Use the host's supported selector or explicitly ask to use the installed skill. Pasting this prompt is not installation. See [installation and verification](installation.md#english).

### Choose the review scope

| Intent | Useful wording | Stop when |
| --- | --- | --- |
| A usable result in one delivery | “Finish once, with the necessary checks.” | The outcome and required checks are complete, with no known material defect. |
| Repair until the result meets a standard | “Keep reviewing and repairing until these criteria hold.” | Acceptance holds or a specific essential source, permission, or capability is unavailable. |
| Extra scrutiny for selected components | “Verify the calculations iteratively; deliver the narrative once.” | Each component meets its own mode and acceptance conditions. |

There is no fixed number of review rounds. A new round should address an identified defect, changed evidence, or unresolved question. Change methods when progress stalls, or report the limit. Preserve still-valid work when the user changes direction.

Independent review requires an actual non-author and an available review channel. If that is an explicit acceptance gate and the host cannot provide it, useful work may still be delivered, but the gate remains unmet.

### Make acceptance observable

| Vague request | More useful criterion |
| --- | --- |
| “Research this thoroughly.” | Answer the named questions, prioritize original sources, cite material claims, and identify unavailable full texts. |
| “Make the code work.” | Pass the supplied reproducer and relevant existing checks; state which verification was not run. |
| “Make the report professional.” | Explain the problem, method, result, and recommendation; trace every key number to an input. |
| “Make the slides look good.” | Use the requested aspect ratio and length, ensure readable labels and no clipped text, and inspect a rendered output. |
| “Clean the data correctly.” | Reconcile rows and totals, define units and fields, and explain missing-value and duplicate handling. |

Choose checks proportional to the actual failure risk. A small reversible edit does not need artificial tests. If appearance or interaction is part of acceptance, source inspection alone does not establish that result.

### Research and evidence

```text
Use universal-expert-team to assess [options A, B, and C] for [specific use].
Design the division of work around the questions. Deliver a comparison
and recommendation once, using original research or official sources
where appropriate.
Separate sourced facts, inference, and uncertainty. Explain conflicts
through source conditions and scope rather than voting on a conclusion.
If full texts or current sources are unavailable, limit the conclusion
to what the accessible evidence supports.
```

Several workers reading one article do not produce several independent sources. The relationship between evidence, scope, and claims matters more than agreement among agents.

### Software repair

```text
Use universal-expert-team to fix [problem] in this repository.
Reproduction: [steps, inputs, error]. Expected behavior: [observable result].
You may change necessary code and tests; preserve existing user changes.
Arrange implementation, investigation, and independent review where available.
Keep repairing until the reproducer and relevant existing checks pass,
with no unresolved material defect.
Do not deploy, merge into the main branch, or message anyone.
Deliver the reason for the change, resulting behavior, checks, and limits.
```

Assign one writer per shared resource, or use truly isolated candidates and an integration owner. Separate agent contexts do not isolate shared files.

### Writing from supplied sources

```text
Use universal-expert-team to turn the attached material into [document]
for [audience], using [language, tone, length].
Do not invent dates, numbers, or causal explanations absent from the sources.
Verify facts and citations iteratively; deliver prose and structure once.
Acceptance: key facts are traceable, terminology is consistent,
and the reader can understand the next step.
Deliver the completed document with necessary limitations.
```

### Data analysis

```text
Use universal-expert-team to analyze [data] and answer [question].
Check field meanings, units, missing values, duplicate rows, and date coverage.
You may create analysis code and result files; preserve the original data.
Verify cleaning and calculations iteratively; deliver the narrative once.
Acceptance: totals reconcile, metrics are defined, and the supplied steps
can reproduce the main results.
Do not guess ambiguous field meanings. Complete unaffected analysis
and identify the information needed to finish.
```

### Planning without external action

```text
Use universal-expert-team to plan [event, migration, course, or project].
Choose specialties based on dependencies and risks.
This is planning only: do not purchase, message anyone, or alter external systems.
Deliver milestones, required inputs, key risks, and observable completion
conditions in one response.
```

These examples do not define a fixed roster. The work, sources, and available capabilities determine the useful team.

### Missing capabilities and honest delivery

| Missing capability | Expected response |
| --- | --- |
| Real subagent tools | Use one assistant where feasible; do not claim delegation or independent review. |
| Search or essential source access | Use available material and mark the unverified scope; do not claim current evidence was retrieved. |
| Write permission | Deliver analysis or a proposed change; state that the actual files were not modified. |
| Test execution or rendering | Distinguish static inspection from execution; keep affected acceptance gates open. |
| Model selection | Use the host's provided capability and disclose settings that cannot be controlled or confirmed. |
| Essential authorization or decision | Complete unaffected work and identify the precise missing requirement. |

The skill prefers native agent interfaces and the highest available capability with deepest supported reasoning when selection is permitted. It cannot override permissions, create missing tools, or turn unknown settings into observed facts.

Deliver the usable result, relevant sources or verification evidence, and material remaining uncertainty. Identify any blocked gate and what would resolve it. Internal coordination transcripts and lengthy review logs need not appear in the public-facing artifact. Where execution details matter, distinguish actual workers, completed checks, and untested behavior.

Further reading: [Work packages](../skills/universal-expert-team/references/work-packages.md) · [Review strategies](../skills/universal-expert-team/references/review-strategies.md) · [Execution boundaries](../skills/universal-expert-team/references/execution-boundaries.md) · [Runtime adapters](../skills/universal-expert-team/references/runtime-adapters.md)
