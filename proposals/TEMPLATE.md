# AI4S 任务提案 / AI4S Task Proposal: 请填写标题 / Enter title


## 0. 提案元数据 / Proposal metadata

一级学科必须使用根目录 `README.md` 的 taxonomy 中规定的英文 slug。二级学科仅工程科学任务需要填写，且必须使用该 taxonomy 规定的工程二级学科 slug；其他任务请留空。细分领域必须填写，但可使用自由文本。若任务无法合理归类，请在提交前联系项目负责人，不要自行创建新的一级或二级学科类别。
The primary domain must use an exact English slug from the taxonomy in the root `README.md`. The secondary discipline is required only for Engineering Sciences tasks and must use an engineering-discipline slug from that taxonomy; leave it blank for all other tasks. The research area is required but may be entered as free text. If the task does not reasonably fit the taxonomy, contact the project lead before submission rather than creating a new primary or secondary category.

- 提案 ID / Proposal ID: `AI4S-2026-domain-task-slug`
- 一级学科 / Primary domain: `replace-domain`
- 二级学科（仅工程科学必填）/ Secondary discipline (required only for Engineering Sciences):
- 细分领域（自由填写）/ Research area (free text):
- 任务类型 / Task type: `workflow_automation` 或 / or `frontier_research`

## 1. 贡献人基本信息 / Contributor information

- 姓名 / Name:
- 邮箱 / Email:
- 机构 / Affiliation:
- 研究领域 / Research area:
- 个人学术主页（可选）/ Academic profile (optional):
- 代表性论文 / Representative papers: 请列出与本人研究方向或本任务相关的代表性论文（正式发表论文或预印本均可），并为每篇论文提供可直接访问的链接。 / List representative papers relevant to your research area or this task. Publications and preprints are both acceptable; provide a direct link for every paper.

## 2. 任务类型与理由 / Task type and rationale

请选择且仅选择以下一种任务类型，并说明理由：
Select exactly one of the following task types and explain your rationale:

- **科学工作流自动化 / Scientific workflow automation (`workflow_automation`)**：自动完成现实科研中已有的、目标与正确性标准相对明确的工作流。任务重点是可靠地执行科研过程并产出可验证的结果，不要求对领域当前前沿形成新的突破。 / Automating an established real-world scientific workflow whose objective and correctness criteria are reasonably well defined. The emphasis is on reliable execution and verifiable outputs, not on producing a new advance beyond the field's frontier.
- **前沿问题攻关 / Frontier research (`frontier_research`)**：面向尚未解决或尚未达到目标水平的前沿科研问题。任务成功意味着相对当前 SOTA 取得可验证的实质进展，而不仅是复现或执行既有流程。 / Tackling a frontier scientific problem that remains unsolved or has not reached the desired level. Success requires verifiable, meaningful progress beyond the current SOTA, rather than merely reproducing or executing an established workflow.

请在此用自然语言回答。 / Please answer here in prose.

## 3. 任务描述与价值 / Task description and value

**任务描述与目标 / Task description and objective**
请说明要解决的科学问题或科研任务、提供给 agent 的主要输入，以及成功完成任务时应得到的结果。
Describe the scientific problem or research task, the main inputs available to the agent, and the result expected from a successful solution.

请在此用自然语言回答。
Please answer here in prose.

**任务的科学或应用价值 / Scientific or application value**
请说明该任务为何值得解决，以及成功解决后可能产生的科学价值、应用价值。
Explain why this task is worth solving and the scientific value, application value, or both that a successful solution could create.

请在此用自然语言回答。
Please answer here in prose.

**前沿问题突破的领域内意义与当前 SOTA（仅前沿问题攻关任务）/ Domain significance of a frontier advance and current SOTA (frontier-research tasks only)**
若任务类型为 `frontier_research`，请说明预期突破对本领域的意义、截至提案提交时的当前 SOTA，以及什么可验证的结果可被视为相对 SOTA 的实质进展；请附关键论文、基准或其他一手来源的直接链接，并注明信息日期。若任务类型为 `workflow_automation`，请填写“不适用 / Not applicable”。
For a `frontier_research` task, explain why the intended advance matters to the field, identify the current SOTA as of the proposal date, and state what verifiable result would constitute meaningful progress beyond it. Include direct links to key papers, benchmarks, or other primary sources and give the as-of date. For a `workflow_automation` task, write “不适用 / Not applicable.”

请在此用自然语言回答。
Please answer here in prose.

## 4. 科研工作流 / Research workflow

请简单描述 agent 将执行的工作流，包括可见输入、主要研究阶段与关键决策，以及允许采用的合理方法。描述应足以让领域专家判断任务是否真实、完整且可执行。
Describe the expected workflow the agent will perform, including agent-visible inputs, major research stages and consequential decisions, and reasonable approaches. The description should let a domain expert judge whether the task is realistic, complete, and executable.

请在此回答。 / Please answer here.

## 5. 数据及来源 / Data and provenance

如任务使用数据，请说明数据内容和来源、获取方式及许可条件。如无外部数据，请明确说明。
If the task uses data, describe its contents, source, version, and licensing conditions. If no external data is needed, say so explicitly.

请在此用自然语言回答。 / Please answer here in prose.

## 6. 计算环境 / Computational environment

请描述完成任务所需的代码库、软件，及CPU、内存、存储或 GPU 等计算资源、网络或外部服务依赖，以及合理的运行时间预算。注：请优先使用代码库，如实在需要，再使用依赖图形界面的交互软件。
Describe the software and key versions, compute resources such as CPU, memory, storage, or GPU, network or external-service dependencies, and a reasonable runtime budget. Note: Please prioritize using code-based tools. Only use GUI-based interactive software when absolutely necessary.

请在此用自然语言回答。 / Please answer here in prose.

## 7. 评价标准 / Evaluation criteria

请说明如何判定任务成功，包括可程序化计算的指标或基于 LLM rubric 的判分规则。评价方案应允许科学上正确的替代解通过，同时拒绝空洞、取巧或明显错误的提交。
Explain how success will be determined, including programmatically computed metrics or a binary LLM grading rubric. The evaluation should accept scientifically valid alternative solutions while rejecting empty, shortcut, or clearly incorrect submissions.

请在此用自然语言回答。 / Please answer here in prose.

## 8. 难度评估 / Difficulty assessment

请说明完成任务所需的专家背景，预估一名合格人类专家独立完成任务所需的实际工作时间，同时预测当前前沿模型的表现。
Describe the expertise required, estimate the actual working time a qualified human expert would need to complete the task independently and briefly justify that estimate, and predict how current frontier models would perform.

请在此用自然语言回答。 / Please answer here in prose.
