# 学术论文写作 Skill · 通用公开版

## 第一原则：仅作补充，由用户决定是否采用

**安装不等于启用；不得改写现有 Skill，不得干扰其他对话；AI 自主调用前必须询问用户。** 这一限制优先于本包内的写作规则、历史偏好和所有示例。

- 不修改、覆盖、删除或替换已有技能；同名安装立即停止。组合调用仅在当前任务中协作，不改写其他 Skill 的文件、全局指令或共享记忆。
- 可单独调用，也可经用户同意与其他 Skill 配合。用户明确点名即为当前任务授权；AI 自主选择时必须先询问，收到明确同意后才应用。普通论文请求和安装行为不构成调用同意。
- **建议安装后在新建的独立聊天中，用副本或示例先测试。** 不自动影响其他聊天的学术写作；在一个对话中的授权不能传递到另一个对话。
- **建议按自己的需求自由修改、删减、停用和迭代升级。** 本包提供参考方法，不是统一学术标准，也不要求其他技能或用户迁就本包。

完整约束是 `SKILL.md` 正文的首个章节。Codex 元数据设为 `allow_implicit_invocation: false`；其他宿主须遵守先询问的文本规则。这些文件不能保证每一种 AI 产品都在技术上强制执行权限或隔离，宿主实际支持情况仍需测试。

用于中英文学术论文、学位论文、文献综述、理论论证与审稿修订。保留研究边界，组织论证链，核查引文与证据，提供可直接替换的修订文本。

**公开地址：** https://github.com/HZQ5/academic-paper-writing-skill-public

采用 [Agent Skills](https://agentskills.io/specification) 的 `SKILL.md + references/ + scripts/ + assets/` 结构。不依赖作者的私有仓库、API 密钥或其他 Skill。这是写作规则与辅助工具，不是模型权重；安装不会训练模型。

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

> 请从 https://github.com/HZQ5/academic-paper-writing-skill-public 安装完整 Skill，先读 SKILL.md 的第一原则。仅补充，不改写任何已有技能；同名目录存在时停止。安装不等于同意启用，AI 自主调用前必须先问我。建议安装后另开独立聊天测试，不影响其他对话。若不支持安装，仅说明如何提供 PORTABLE.md，等我明确同意后再将规则用于当前任务。我可按需自由修改和迭代，不把它作为统一标准。

**兼容范围：** 支持 Agent Skills 的宿主可安装；能读 Markdown 的 AI 可使用规则。不能保证所有聊天产品都支持原生安装、脚本运行或永久记忆，未逐一完成各产品端到端实测。

## 使用示例

- “按这个 Skill 修改引言，保留研究问题与变量关系，先给可替换文本，再解释依据。”
- “把文献组织成有共识、争议、机制、边界和缺口的综述；缺少全文证据的判断单独标明。”
- “逐条回应审稿意见，说明实际修改、位置和证据，不编造新增检验。”

## 可选工具

写作规则本身不需要 Python。以下脚本需要 Python 3.10+，均为标准库：

```bash
python3 scripts/init_project.py ./my-paper --title "论文项目"
python3 scripts/audit_workbench.py ./my-paper
python3 scripts/validate_evidence.py ./evidence.jsonl
python3 scripts/lookup_journal_rank.py "Journal of Management"
python3 scripts/privacy_scan.py .
```

证据文件每行一个 JSON，字段为 `evidence_id`、`source_id`、`claim`、`locator`、`quote`、`status`、`source_genre`、`focal_status`。`status` 为 `candidate/verified/rejected/blocked`；`focal_status` 为 `focal/secondary/not-applicable/unclear`。结构校验不会替代原文核对。

## 来源、数据与维护

基于作者 HZQ5 的私有原库 `academic-paper-writing-skill`，源提交 `95568a02902de76adbee1630aac2439716ca96bd`，于 2026-10-26 制作公开副本。原库和现有本机安装保持原状。本版保留论文规则与全部原始参考/工具文件，调整私有同步指令，增加安装器和文本入口。变更见 `CHANGELOG.md`，文件摘要见 `MANIFEST.json`。

随附期刊名单是注明版本的历史快照，不代表实时排名或本项目对第三方数据的所有权。当前名单应核验官方来源。历史风格材料是可选偏好，不应覆盖当前要求或研究设计。

未另行添加通用开源许可证；公开可见与完整开源授权不同。第三方资料权利属于原权利人。实际论文、未发表结果、参与者资料、审稿原件与凭证留在用户项目中。
