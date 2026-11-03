# 学术论文写作 Skill · 通用公开版

## 第一原则：仅作补充，由用户决定是否采用

**安装不等于启用；不得改写现有 Skill，不得干扰其他对话；AI 自主调用前必须询问用户。** 这一限制优先于本包内的写作规则、历史偏好和所有示例。

- 不修改、覆盖、删除或替换已有技能；同名安装立即停止。组合调用仅在当前任务中协作，不改写其他 Skill 的文件、全局指令或共享记忆。
- 可单独调用，也可经用户同意与其他 Skill 配合。用户明确点名即为当前任务授权；AI 自主选择时必须先询问，收到明确同意后才应用。普通论文请求和安装行为不构成调用同意。
- **建议安装后在新建的独立聊天中，用副本或示例先测试。** 不自动影响其他聊天的学术写作；在一个对话中的授权不能传递到另一个对话。
- **建议在自己的 Fork 或本地副本中，按需修改、删减、停用和迭代升级。** 不向作者仓库直接推送、合并或自动同步，不解除作者主分支保护；Fork 的演化不改变作者当前版本。 本包提供参考方法，不是统一学术标准，也不要求其他技能或用户迁就本包。

完整约束是 `SKILL.md` 正文的首个章节。Codex 元数据设为 `allow_implicit_invocation: false`；其他宿主须遵守先询问的文本规则。这些文件不能保证每一种 AI 产品都在技术上强制执行权限或隔离，宿主实际支持情况仍需测试。

用于中英文学术论文、学位论文、文献综述、理论论证与审稿修订。保留研究边界，组织论证链，核查引文与证据，提供可直接替换的修订文本。

**公开地址：** https://github.com/HZQ5/academic-paper-writing-skill-public

采用 [Agent Skills](https://agentskills.io/specification) 的 `SKILL.md + references/ + scripts/ + assets/` 结构。不依赖作者的私有仓库、API 密钥或其他 Skill。这是写作规则与辅助工具，不是模型权重；安装不会训练模型。

## 不只是期刊目录：公开包内置哪些写作规则？

`references/` 是与入口一起安装的本地模块，不是需要访问作者私有库的子 Skill。普通写作与语言修改不要求额外安装 `academic-language-calibration`，也不要求作者的论文、历史对话或 Zotero 文库。

| 内置模块 | 能帮助完成什么 |
| --- | --- |
| [各章节写作指南](references/04-academic-writing.md) | 标题与摘要；引言五个逻辑环节；综合式文献综述；理论与假设；不同研究类型的方法与结果；讨论、理论贡献、实践启示、局限与结论；审稿回应 |
| [中英文语言规范](references/11-language-calibration.md) | 保留原意，统一概念与主体，减少空泛表述，使措辞与证据强度匹配，节省读者精力；翻译时保留条件、否定与数量 |
| [八组构造写作示例](references/12-writing-examples.md) | 对照修改缺口、综述、贡献、因果措辞、中英文学术表达、语义及引用边界；示例不冒充真实研究 |
| [数据与证据](references/07-data-evidence.md) | 区分原始发现、转引、摘要和全文；建立论断与来源定位的对应关系 |
| [规范与期刊目录](references/03-standards-and-registries.md) | 查阅附带的历史目录；区分期刊分级、论文质量和投稿格式 |

入口会按当前任务路由到相应模块，不要求每次把所有文件读完。章节结构是可调整的指导，不将某门课程的页数、某一种方法或作者个人偏好变成通用硬标准。

**能力边界：** 这些规则支持独立写作和修订；下载受限论文、操作 Word 动态字段、访问 Zotero 等仍需要使用者自己的授权与工具。缺少这些工具时可以处理文本与静态引用，但不能声称已经下载、阅读全文或插入动态引文。

## 安装到 AI 工具

下载本库 ZIP 并解压，或克隆到名称匹配的目录：

```bash
git clone https://github.com/HZQ5/academic-paper-writing-skill-public.git academic-paper-writing
cd academic-paper-writing
```

安装器只使用 Python 标准库，不联网；目标目录已存在时会停止，不覆盖旧版本。需要 Python 3.10+；Windows 可将 `python3` 替换为 `py -3`。

| 工具 | 安装命令 | 安装位置 |
| --- | --- | --- |
| Codex | `python3 install.py --target codex` | `$CODEX_HOME/skills/academic-paper-writing`；未设置时为 `~/.codex/skills/academic-paper-writing` |
| Claude Code | `python3 install.py --target claude` | `~/.claude/skills/academic-paper-writing` |
| Cursor | `python3 install.py --target cursor` | `~/.cursor/skills/academic-paper-writing` |
| 支持 `.agents/skills` 的工具 | `python3 install.py --target generic` | `~/.agents/skills/academic-paper-writing` |
| 自定义/项目目录 | `python3 install.py --dest /path/to/project/.agents/skills` | 指定目录下的 `academic-paper-writing/` |

可先在命令末尾加 `--dry-run` 查看目标位置。安装后建议打开独立新会话测试。Codex 可显式用 `$academic-paper-writing`，Claude Code 可显式用 `/academic-paper-writing`。AI 对一般论文任务自主推荐本技能时，必须先询问是否调用，不能直接套用规则。

不运行安装器时，将 `SKILL.md`、`agents/`、`references/`、`scripts/`、`assets/` 一起复制到宿主的 `skills/academic-paper-writing/`。不要只复制入口，否则会缺少参考资料。

路径依据：[Claude Code 官方文档](https://code.claude.com/docs/en/skills)、[Cursor 官方文档](https://cursor.com/docs/skills)。版本、云端与管理员配置可能限制技能发现，以实际宿主配置为准。

## 普通聊天 AI：无需安装

没有 Skills 功能或本机文件访问的 AI，可以上传 `PORTABLE.md`，或粘贴其中内容。它包含入口及文字参考规则。完整 ZIP 还包含期刊表和可选脚本。

可复制给 AI：

> 请从 https://github.com/HZQ5/academic-paper-writing-skill-public 安装完整 Skill，先读 SKILL.md 的第一原则。仅补充，不改写任何已有技能；同名目录存在时停止。安装不等于同意启用，AI 自主调用前必须先问我。建议安装后另开独立聊天测试，不影响其他对话。若不支持安装，仅说明如何提供 PORTABLE.md，等我明确同意后再将规则用于当前任务。我可在自己的 Fork 或本地副本中迭代，不回写作者正式版，不把它作为统一标准。

**兼容范围：** 支持 Agent Skills 的宿主可安装；能读 Markdown 的 AI 可使用规则。不能保证所有聊天产品都支持原生安装、脚本运行或永久记忆，未逐一完成各产品端到端实测。

## 使用示例

- “按这个 Skill 修改引言，保留研究问题与变量关系，先给可替换文本，再解释依据。”
- “把文献组织成有共识、争议、机制、边界和缺口的综述；缺少全文证据的判断单独标明。”
- “逐条回应审稿意见，说明实际修改、位置和证据，不编造新增检验。”
- “只用公开包内置规则，检查这段中文的因果措辞和概念一致性，输出修订文本及待核验项。”
- “按引言五个逻辑环节检查我的草稿，不改变变量关系；没有证据的贡献不要写成已验证结论。”

## 正式版与 Fork 的边界

作者正式版是 `HZQ5/academic-paper-writing-skill-public` 的 `main` 分支。主分支冻结后不接受推送、合并、强制改写或删除；作者今后若明确决定发布新版，需先主动调整仓库保护设置。这里使用仓库分支规则，不设置覆盖整个 Fork 网络的推送规则。

其他用户请使用 GitHub 的 **Fork** 建立自己账号下的副本，或下载后在本地维护。修改与测试只针对自己的副本；不要把作者仓库设为写入目标，也不要自动将修改合并回正式版。Fork 可以独立演进，但不代表作者审定、背书或同步升级。建议或 PR 本身不会改动正式版，冻结期间也不能合并进入主分支。

作者明确允许为安装、使用及个人需求迭代而创建并修改本项目的 Fork 或本地副本；该授权不授予作者仓库写入权限，也不替代第三方期刊资料自身的权利限制。未另行授予通用开源许可证。

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 可选工具

写作规则本身不需要 Python。以下脚本需要 Python 3.10+，均为标准库：

```bash
python3 scripts/init_project.py ./my-paper --title "论文项目"
python3 scripts/audit_workbench.py ./my-paper
python3 scripts/validate_evidence.py ./evidence.jsonl
python3 scripts/lookup_journal_rank.py "Journal of Management"
python3 scripts/privacy_scan.py .
```

维护公开副本时，可运行 `python3 scripts/build_public_bundle.py` 同步生成单文件版与摘要清单，再运行 `python3 scripts/build_public_bundle.py --check` 和 `python3 -m unittest discover -s tests -v` 检查包内引用、安装隔离和生成文件一致性。这些维护检查在仓库根目录运行，不是写作前置步骤。

证据文件每行一个 JSON，字段为 `evidence_id`、`source_id`、`claim`、`locator`、`quote`、`status`、`source_genre`、`focal_status`。`status` 为 `candidate/verified/rejected/blocked`；`focal_status` 为 `focal/secondary/not-applicable/unclear`。结构校验不会替代原文核对。

## 来源、数据与维护

基于作者 HZQ5 的私有原库 `academic-paper-writing-skill`，源提交 `95568a02902de76adbee1630aac2439716ca96bd`，于 2026-10-26 制作公开副本。原库和现有本机安装保持原状。本版保留论文规则与全部原始参考/工具文件，调整私有同步指令，增加安装器和文本入口。变更见 `CHANGELOG.md`，文件摘要见 `MANIFEST.json`。

2026-11-03 的自包含修订将通用章节规则、语言校准与构造示例直接整合进公开包，替换原来指向独立语言 Skill 的调用建议；不发布私有研究材料或历史对话。若你正在查看更新分支，主分支未合并前仍是原版，请以所在分支的文件为准。

随附期刊名单是注明版本的历史快照，不代表实时排名或本项目对第三方数据的所有权。当前名单应核验官方来源。历史风格材料是可选偏好，不应覆盖当前要求或研究设计。

未另行添加通用开源许可证；公开可见与完整开源授权不同。第三方资料权利属于原权利人。实际论文、未发表结果、参与者资料、审稿原件与凭证留在用户项目中。
