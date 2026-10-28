# 安裝 / Installation

[繁體中文首頁](../README.md) · [English overview](../README.en.md) · [English instructions](#english)

## 先選擇你的執行環境

| 使用環境 | 安裝方式 | 完成後仍需確認 |
| --- | --- | --- |
| 可安裝或匯入技能的 ChatGPT 環境 | 使用完整技能 ZIP，透過該環境支援的方式安裝。 | 技能是否已載入；目前是否有真實子代理工具。 |
| 可存取本機檔案的 Codex | 複製完整技能資料夾至技能搜尋位置。 | 路徑正確、技能被偵測、工作階段工具可用。 |
| 其他支援技能的代理平台 | 依平台文件匯入完整資料夾。 | 格式相容性、參考文件可讀性與工具對應。 |
| 僅能貼上文字的一般聊天介面 | 可閱讀並套用流程。 | 這不構成技能安裝，也不提供子代理或其他工具。 |

本專案發佈的是技能資料夾與下載套件。GitHub 上公開可下載，不代表它已進入任何平台的官方技能或外掛目錄。

## 1. 取得完整套件

前往 [最新版本](https://github.com/jerry0327/universal-expert-team/releases/latest)，下載技能資產 `universal-expert-team-v1.0.0.zip`。這個技能 ZIP 的頂層資料夾是 `universal-expert-team/`。

GitHub 自動產生的 **Source code (zip)** 是整份儲存庫原始碼，不是相同的技能套件。使用原始碼也可以安裝：複製其中的 `skills/universal-expert-team/` 完整資料夾，再將儲存庫根目錄的 `LICENSE` 複製進安裝後的 `universal-expert-team/`，與 `SKILL.md` 放在同一層。

完整技能包含：

| 檔案 | 用途 |
| --- | --- |
| `SKILL.md` | 核心流程與觸發描述。 |
| `agents/openai.yaml` | 支援平台使用的介面資訊。 |
| `assets/icon.svg` | 技能圖示。 |
| `references/work-packages.md` | 工作分包、相依關係與驗收。 |
| `references/review-strategies.md` | 審查方法與獨立性。 |
| `references/execution-boundaries.md` | 授權、工具限制與受阻處理。 |
| `references/runtime-adapters.md` | 不同執行環境的能力對應。 |

發行 ZIP 另外包含 `LICENSE`，請一併保留。只複製 `SKILL.md` 會遺失參考文件；請保留完整目錄結構。技能本身不需要 API 金鑰或額外套件，但執行平台與任務使用的服務可能另有需求。

## 2. ChatGPT：使用支援的技能安裝能力

在你的帳號與介面確實支援技能上傳或安裝時，上傳完整 ZIP，並提出明確要求：

```text
請將附件中的 universal-expert-team 完整安裝為可重複使用的技能，
保留 references、agents 與 assets。
安裝後請確認技能已可載入，並說明本次環境是否提供真正的子代理工具。
如果目前介面無法安裝，請明確說明，不要把讀取附件視為已安裝。
```

請依平台回覆確認實際完成了安裝，而非只摘要檔案。若目前介面沒有安裝能力，這份套件仍可用於支援技能的環境；不應假定其他裝置會自動取得它。

已安裝的技能可在支援介面透過 `@` 技能選單選取；這個動作是呼叫技能，並非安裝。[官方說明](https://learn.chatgpt.com/docs/build-skills)

## 3. Codex：複製至本機技能目錄

以下使用目前官方文件列出的路徑：專案範圍 `.agents/skills/`，個人範圍 `~/.agents/skills/`。Codex CLI／IDE 可用 `/skills` 檢查或以 `$` 選取；變更未出現時重新啟動。[官方來源](https://learn.chatgpt.com/docs/build-skills)

以下為 macOS、Linux 或相容 shell 的手動複製方式。將 `/path/to/your-project` 換成實際專案路徑。**目標若已有同名技能，先依後面的更新步驟處理。**

```bash
git clone https://github.com/jerry0327/universal-expert-team.git
cd universal-expert-team

project_skill_parent="/path/to/your-project/.agents/skills"
mkdir -p "$project_skill_parent"

if [ -e "$project_skill_parent/universal-expert-team" ]; then
  echo "Skill already exists; review the update instructions before replacing it."
else
  cp -R skills/universal-expert-team "$project_skill_parent/"
  cp LICENSE "$project_skill_parent/universal-expert-team/LICENSE"
fi
```

複製後，專案內應存在 `.agents/skills/universal-expert-team/SKILL.md` 與同層的 `LICENSE`。在該專案開啟 Codex，再進行載入確認。Windows 使用者也可以用檔案管理員複製同一完整資料夾，再將儲存庫根目錄的 `LICENSE` 複製進安裝後的 `universal-expert-team/`；以你的 Codex 執行環境實際讀取的檔案系統為準。

若希望在同一台電腦的不同專案使用，可改用個人範圍：

```bash
# 從下載的儲存庫根目錄執行
personal_skill_parent="$HOME/.agents/skills"
mkdir -p "$personal_skill_parent"

if [ -e "$personal_skill_parent/universal-expert-team" ]; then
  echo "Skill already exists; review the update instructions before replacing it."
else
  cp -R skills/universal-expert-team "$personal_skill_parent/"
  cp LICENSE "$personal_skill_parent/universal-expert-team/LICENSE"
fi
```

也可以在確實提供 `$skill-installer` 的環境，請該工具安裝本儲存庫的 `skills/universal-expert-team`，並將儲存庫根目錄的 `LICENSE` 保留在安裝後的技能資料夾內。安裝工具的存在與成功結果仍須確認，不應只憑輸入指令判斷完成。

## 4. 確認載入，再測試能力

```text
請確認 universal-expert-team 技能已安裝且可讀取。
指出實際載入的技能來源，並確認其 references 可以讀取。
列出本次工作實際可用的子代理、搜尋、檔案與驗證工具；
沒有提供的能力請明確標示。這一步只做檢查，不要執行外部操作。
```

有效的確認應包含實際可讀取的技能來源或技能選單中的項目，以及目前工具能力的說明。僅回覆「我可以扮演多位專家」並未證明子代理工具存在。

接著用一個小型、可判定結果的任務確認工作方式：

```text
使用 universal-expert-team，根據我提供的兩份短文，整理差異表。
若有真實代理工具且分工有益，可獨立核對兩份文字；否則由單一助手完成。
只使用提供的文字，列出共同點、矛盾與缺少資訊；一次交付。
```

技能能被載入與多代理真的執行是兩項不同的檢查。一次成功也不保證不同帳號、裝置或下一次工作階段具備相同能力。

## 更新與移除

更新前先比較版本與內容，備份自己修改過的技能資料夾。以新版本的完整資料夾取代舊版本，避免混用不同版本的核心與參考文件；從原始碼更新時，也將該版本根目錄的 `LICENSE` 複製進安裝資料夾，再重新確認載入。若有同名技能存在不同搜尋位置，先查清本次載入的是哪一份。

移除時，透過平台的技能管理能力移除，或刪除自己安裝的 `universal-expert-team/` 技能資料夾。不要刪除整個 `.agents/skills/`，其中可能有其他技能。

## 常見問題

| 現象 | 處理方式 |
| --- | --- |
| 上傳後只得到 ZIP 內容摘要 | 請求確認是否真的完成安裝；若平台不支援，使用支援技能的環境。 |
| 找不到技能 | 確認路徑、`SKILL.md` 與整份資料夾；重新整理或重啟支援的執行環境。 |
| 技能存在，但沒有多代理 | 確認本次平台是否提供原生代理工具；技能不會新增此能力。 |
| 無法搜尋或存取檔案 | 提供可讀取的來源或在授權範圍內接通所需工具；未完成的核對須保留標示。 |
| 不同裝置的行為不同 | 逐一確認技能可見性、工具、權限與目前工作階段。 |

平台安裝與呼叫機制查核日期：**2026-10-28**。來源：[OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills)；技能與工具的職責區別見 [OpenAI — Skills](https://developers.openai.com/plugins/concepts/skills)。版本與產品能力可能改變，請以你使用的平台現況為準。

---

## English

### Choose the installation route

The downloadable unit is a complete skill folder. A public GitHub repository does not automatically place it in an official skill or plugin catalog.

- **ChatGPT with skill import or installation:** use the complete ZIP through the capability your account actually provides.
- **Local Codex:** copy the complete folder into a supported skill location.
- **Another agent host:** follow that host's skill import documentation and check reference access and tool mapping.
- **Text-only chat:** the guidance can inform a prompt; pasting it is not installation and does not create subagents.

### Download

Open [the latest release](https://github.com/jerry0327/universal-expert-team/releases/latest) and choose `universal-expert-team-v1.0.0.zip`. The skill archive has a single top-level `universal-expert-team/` folder. GitHub's automatic **Source code (zip)** instead contains the repository; copy its complete `skills/universal-expert-team/` folder, then copy the repository-root `LICENSE` into the installed `universal-expert-team/` directory alongside `SKILL.md`.

Preserve `SKILL.md`, `agents/`, `assets/`, and all four files in `references/`, together with the `LICENSE` included in the release archive. Copying only the main instructions omits material used by the workflow. The skill itself needs no API key or additional package, although the host and the task's services may have their own requirements.

### Install in ChatGPT where supported

Upload the complete ZIP only in an environment that supports skill installation, then ask:

```text
Install the attached universal-expert-team as a reusable skill.
Preserve references, agents, and assets. Confirm the installed skill can be
loaded, and identify whether this session exposes real subagent tools.
If this interface cannot install skills, say so; reading the attachment
must not be reported as installation.
```

Confirm the actual installation result. Do not assume an attachment was installed, that another device will inherit it, or that an `@` mention can install it. In supported interfaces, the `@` skill selector invokes an available skill. [Official guidance](https://learn.chatgpt.com/docs/build-skills)

### Install in local Codex

Current official locations are `.agents/skills/` for a project and `~/.agents/skills/` for a user. In Codex CLI or IDE, use `/skills` or `$` to select a skill; restart if a change is not detected. [Official guidance](https://learn.chatgpt.com/docs/build-skills)

From a macOS, Linux, or compatible shell:

```bash
git clone https://github.com/jerry0327/universal-expert-team.git
cd universal-expert-team

# Replace this with your actual project path.
project_skill_parent="/path/to/your-project/.agents/skills"
mkdir -p "$project_skill_parent"

if [ -e "$project_skill_parent/universal-expert-team" ]; then
  echo "Skill already exists; review it before replacing it."
else
  cp -R skills/universal-expert-team "$project_skill_parent/"
  cp LICENSE "$project_skill_parent/universal-expert-team/LICENSE"
fi
```

The resulting project path should be `.agents/skills/universal-expert-team/SKILL.md`, with `LICENSE` beside it. Open Codex in that project. To install for the local user instead, run this from the downloaded repository root:

```bash
personal_skill_parent="$HOME/.agents/skills"
mkdir -p "$personal_skill_parent"

if [ -e "$personal_skill_parent/universal-expert-team" ]; then
  echo "Skill already exists; review it before replacing it."
else
  cp -R skills/universal-expert-team "$personal_skill_parent/"
  cp LICENSE "$personal_skill_parent/universal-expert-team/LICENSE"
fi
```

Windows users can copy the complete folder through their file manager, then copy the repository-root `LICENSE` into the installed `universal-expert-team/` folder. Use the filesystem visible to the Codex environment.

Where `$skill-installer` is actually available, you may ask it to install `skills/universal-expert-team` from this repository and preserve the repository-root `LICENSE` inside the installed skill folder. Verify its result rather than assuming the request succeeded.

### Verify installation and runtime separately

```text
Confirm that universal-expert-team is installed and readable.
Identify the actual skill source and confirm its references are accessible.
List the subagent, search, file, and validation tools this session provides.
Mark unavailable capabilities explicitly. Only inspect; do not perform
external actions during this check.
```

A readable skill source or an installed selector entry supports the installation check. Actual exposed tools support the capability check. “I can play multiple expert roles” establishes neither real delegation nor independent review.

Then try a small task with a clear result:

```text
Use universal-expert-team to compare the two short texts I provide.
If real agent tools are available and delegation is useful, check the texts
independently. Otherwise, use one assistant. Use only the supplied text.
Deliver a table of agreements, contradictions, and missing information once.
```

### Update, remove, or troubleshoot

Before updating, compare versions and back up local changes. Replace the complete skill directory to avoid mixing core instructions and references from different versions. When updating from source, also copy that version's repository-root `LICENSE` into the installed directory, then verify loading again. If copies with the same name exist in different locations, identify which copy is active.

To remove it, use the host's skill management or remove only the installed `universal-expert-team/` directory. Preserve the parent skills directory and other skills.

If discovery fails, inspect the path and folder contents, then refresh or restart the relevant host. If the skill loads but delegation does not work, check whether the current session actually exposes subagent tools. Missing sources, permissions, or verification tools must remain visible as limits on the result.

Platform documentation checked **2026-10-28**: [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills) and [OpenAI — Skills](https://developers.openai.com/plugins/concepts/skills). The host's current capabilities govern actual execution.
