# AI4S 任务提案：结构感知的透明导体筛选 / AI4S Task Proposal: Structure-Aware Transparent-Conductor Screening

## 0. 提案元数据 / Proposal metadata

- 提案 ID / Proposal ID: `AI4S-2026-CHEM-TRANSPARENT-CONDUCTOR-SCREENING`
- 一级学科 / Primary domain: `chemical-materials-sciences`
- 二级学科（仅工程科学必填）/ Secondary discipline (required only for Engineering Sciences):
- 细分领域（自由填写）/ Research area (free text): `computational materials science; crystal-structure machine learning; uncertainty-aware screening`
- 任务类型 / Task type: `workflow_automation`

## 1. 贡献人基本信息 / Contributor information

- 姓名 / Name: Amy Xin / 辛馨
- 邮箱 / Email: amyxx2001@163.com
- 机构 / Affiliation: Tsinghua University
- 研究领域 / Research area: LLM agents for scientific research and autonomous scientific discovery
- 个人学术主页（可选）/ Academic profile (optional): https://amyxin-thu.github.io/
- 代表性论文 / Representative papers: [EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery](https://arxiv.org/abs/2606.13662); [AISE-Bench: A Full-Cycle Curated Benchmark for Information Seeking on Academic Knowledge Graphs](https://arxiv.org/abs/2607.20498); [AtomR: Atomic Operator-Empowered Large Language Models for Heterogeneous Knowledge Reasoning](https://arxiv.org/abs/2411.16495).

## 2. 任务类型与理由 / Task type and rationale

**中文：** 本任务属于科研工作流自动化。它改编自 MLE-Bench 中的 `nomad2018-predict-transparent-conductors`，复现计算材料筛选中的既有流程：从晶胞组成、晶格参数和原子坐标构造物理合理且对平移、旋转和原子排列不敏感的结构表示；建立并验证形成能与带隙的联合代理模型；校准预测区间；最后对候选透明导体排序。成功标准由固定隐藏标签和预先登记的数值门槛决定，不要求提出超越领域 SOTA 的新模型。

**English:** This is a `workflow_automation` task adapted from MLE-Bench's `nomad2018-predict-transparent-conductors`. It instantiates an established computational-materials screening workflow: derive physically meaningful, translation-, rotation-, and atom-order-insensitive representations from composition, lattice parameters, and atomic coordinates; fit and validate joint surrogate models for formation energy and band gap; calibrate prediction intervals; and rank candidate transparent conductors. Success is determined by frozen hidden labels and preregistered numerical gates, not by advancing the scientific state of the art.

## 3. 任务描述与价值 / Task description and value

**任务描述与目标 / Task description and objective**

**中文：** Agent 获得一组 `(Al_x Ga_y In_z)_{2N}O_{3N}` 候选材料。每个训练样本包含成分、空间群、晶格向量长度与夹角、原子数、`geometry.xyz` 原子坐标，以及 DFT 计算得到的每原子形成能和带隙；隐藏候选仅提供结构输入。Agent 必须完成数据审计、晶体结构特征化、组感知交叉验证、双目标回归、误差分析和不确定性校准，并生成所有隐藏材料的两项目标预测与 80% 预测区间，以及按“高带隙、低形成能”效用排序的候选清单。最终交付为 `/app/submission.csv` 和 `/app/shortlist.csv`；不限定算法，可使用成分描述符、径向/配位描述符、核方法、树模型、图模型或合理集成。

**English:** The agent receives candidate `(Al_x Ga_y In_z)_{2N}O_{3N}` materials. Each training record includes composition, space group, lattice lengths and angles, atom count, `geometry.xyz` coordinates, and DFT formation energy per atom and band gap; hidden candidates expose only structural inputs. The agent must audit the data, featurize crystal structures, perform group-aware cross-validation, fit two-target regressors, analyze errors, calibrate uncertainty, and produce predictions with central 80% intervals for every hidden material plus a shortlist ranked for high band gap and low formation energy. The required artifacts are `/app/submission.csv` and `/app/shortlist.csv`. Methods are unrestricted and may use compositional, radial, or coordination descriptors, kernels, tree ensembles, graph models, or scientifically reasonable ensembles.

**任务的科学或应用价值 / Scientific or application value**

**中文：** 透明导体同时需要光学透明性与电学适用性，候选的形成稳定性和带隙通常通过昂贵 DFT 计算获得。可靠的结构—性质代理模型可以优先安排后续计算或实验，从而降低材料搜索成本。与只优化单个 Kaggle 分数相比，本任务还要求子群泛化、预测区间和候选排序，更接近研究人员实际决定“下一批计算哪些结构”的工作流。

**English:** Transparent conductors must combine optical transparency with useful electrical behavior, while candidate stability and band gaps are normally assessed through costly DFT calculations. Reliable structure-property surrogates can prioritize subsequent computation or experiment and reduce search cost. Beyond optimizing one leaderboard score, this task requires subgroup generalization, uncertainty intervals, and candidate ranking, which better reflects the practical decision of which structures to compute next.

**前沿问题突破的领域内意义与当前 SOTA（仅前沿问题攻关任务）/ Domain significance of a frontier advance and current SOTA (frontier-research tasks only)**

不适用 / Not applicable. 本任务是既有材料信息学筛选流程的自动化，不以突破当前 SOTA 为成功条件。 / This task automates an established materials-informatics screening workflow and does not require an advance beyond current SOTA.

## 4. 科研工作流 / Research workflow

**中文：** Agent 首先检查成分和化学计量约束、晶格几何、坐标单位、重复结构和目标分布，避免 ID 泄漏与不合理随机切分。随后从 CSV 与 XYZ 共同构造结构不变量，例如元素比例、晶胞体积与密度、周期边界下的成对距离统计、近邻配位和元素对局部环境；按成分族与空间群设计交叉验证，分别诊断形成能和带隙误差。Agent 再选择目标变换、模型和集成方式，并利用折外残差校准 80% 区间。最后对隐藏候选预测，按公开效用函数排序，进行有限性、非负性、区间嵌套和 ID 完整性检查后写出两个规定文件。

**English:** The agent first audits composition and stoichiometry constraints, lattice geometry, coordinate units, duplicate structures, and target distributions while avoiding ID leakage and misleading random validation. It then combines CSV and XYZ inputs into structural invariants such as elemental fractions, cell volume and density, periodic pair-distance statistics, neighbor coordination, and element-pair environments. Cross-validation is grouped by composition family and space group, with separate formation-energy and band-gap diagnostics. The agent chooses target transformations, models, and ensembles, then calibrates central 80% intervals from out-of-fold residuals. Finally, it predicts hidden candidates, ranks them with the published utility, checks finiteness, nonnegativity, nested intervals, and ID completeness, and writes the two required files.

## 5. 数据及来源 / Data and provenance

**中文：** 科学数据来自 Kaggle/NOMAD 的 [Nomad2018 Predicting Transparent Conductors](https://www.kaggle.com/c/nomad2018-predict-transparent-conductors) 竞赛，包含约 3,000 个 Al-Ga-In 氧化物的表格属性和 XYZ 晶体坐标。本任务以 OpenAI [MLE-Bench](https://github.com/openai/mle-bench/tree/507f92e1138bb6e40dac5c6ee7a6758e6424bf97/mlebench/competitions/nomad2018-predict-transparent-conductors) 固定版本的准备逻辑、描述和评分器为上游依据，但会重新生成不公开的组感知划分，并保留原始样本内容校验和、上游提交与引用信息。MLE-Bench 代码按其仓库许可证使用；原始竞赛数据受 Kaggle 竞赛条款和 NOMAD 数据条款约束。完整任务实现 PR 之前必须由项目方确认可再分发范围；若不能随仓库分发，则只能使用项目方批准的私有 artifact 交付机制，不能擅自重新发布数据。

**English:** The scientific data originate from Kaggle/NOMAD's [Nomad2018 Predicting Transparent Conductors](https://www.kaggle.com/c/nomad2018-predict-transparent-conductors) competition and contain tabular properties and XYZ crystal coordinates for roughly 3,000 Al-Ga-In oxides. The task uses the pinned OpenAI [MLE-Bench](https://github.com/openai/mle-bench/tree/507f92e1138bb6e40dac5c6ee7a6758e6424bf97/mlebench/competitions/nomad2018-predict-transparent-conductors) preparation logic, description, and grader as its upstream basis, but will generate a new undisclosed group-aware split and retain source checksums, revision, and citations. MLE-Bench code is used under its repository license; the original competition data remain subject to Kaggle competition terms and NOMAD data terms. Before a complete implementation PR, the project must confirm redistribution rights. If repository redistribution is not permitted, only a project-approved private-artifact delivery mechanism may be used; the data will not be republished unilaterally.

## 6. 计算环境 / Computational environment

**中文：** 任务在无 GPU 的 Python 3.12 容器中运行，建议 4 CPU、8 GiB 内存、10 GiB 存储和 8 小时时限。环境预装固定版本的 NumPy、SciPy、pandas、scikit-learn、XGBoost 及晶体结构解析所需的轻量库；允许 agent 使用已提供的代码工具，但不需要 GUI。为避免从公开竞赛训练集反查隐藏标签，agent 运行期禁用互联网。独立 verifier 同样无网络，只读取 agent artifacts 和隐藏标签。

**English:** The task runs in a CPU-only Python 3.12 container with 4 CPUs, 8 GiB RAM, 10 GiB storage, and an eight-hour limit. The environment provides pinned versions of NumPy, SciPy, pandas, scikit-learn, XGBoost, and lightweight crystal-structure parsing tools. Code-based tooling is allowed and no GUI is needed. Agent-time internet is disabled to prevent lookup of hidden labels from the public competition training set. The independent verifier is also offline and reads only agent artifacts and hidden labels.

## 7. 评价标准 / Evaluation criteria

**中文：** `submission.csv` 必须依次包含 `id`、`formation_energy_ev_natom`、`formation_lower`、`formation_upper`、`bandgap_energy_ev`、`bandgap_lower`、`bandgap_upper`；`shortlist.csv` 必须依次包含 `rank`、`id`、`predicted_utility`，并按 rank 1–30 排列。Verifier 首先严格检查 schema、ID 集合与顺序、唯一性、数值有限性、预测非负性、区间端点顺序，以及 shortlist 是否恰含 30 个不同隐藏 ID。它在 `log1p` 空间计算形成能与带隙 RMSLE，并要求两列平均 RMSLE 不高于 `0.060`，且任一单列 RMSLE 不高于 `0.075`。为防止模型只拟合主成分区域，隐藏集按主导阳离子和空间群稀有度形成固定子群，每个至少含 15 个样本的子群平均 RMSLE 必须不高于 `0.085`。每个目标的中央 80% 区间经验覆盖率必须在 `[0.70, 0.90]`，同时其平均 `log1p` 宽度不得超过由训练集无条件 80% 区间宽度的 `0.85` 倍。公开效用定义为隐藏集中标准化后的 `z(log1p(bandgap)) - z(log1p(formation_energy))`；`shortlist.csv` 相对该真实效用排序的 NDCG@30 必须至少为 `0.80`。所有门槛同时通过才得到二元 reward `1`。指标只判断输出结果，允许任何科学上合理的替代方法；空文件、均值常数、仅复制 sample submission、过宽不确定区间、遗漏 XYZ 信息导致的弱模型以及伪造 shortlist 都会失败。正式实现时 oracle 必须在固定隐藏数据上稳定通过五次，nop 必须为零分；阈值若经 oracle 实测不可达，必须回到 proposal 审核而不能在任务实现中静默放宽。

**English:** `submission.csv` must contain, in order, `id`, `formation_energy_ev_natom`, `formation_lower`, `formation_upper`, `bandgap_energy_ev`, `bandgap_lower`, and `bandgap_upper`. `shortlist.csv` must contain, in order, `rank`, `id`, and `predicted_utility`, with ranks 1–30. The verifier first enforces both schemas, exact ID set and order, uniqueness, finite values, nonnegative predictions, ordered interval endpoints, and a shortlist containing exactly 30 distinct hidden IDs. It computes formation-energy and band-gap RMSLE in `log1p` space and requires mean column-wise RMSLE at most `0.060`, with neither target above `0.075`. To prevent fitting only the dominant composition region, the hidden set has frozen subgroups based on dominant cation and space-group rarity; every subgroup with at least 15 samples must have mean RMSLE at most `0.085`. For each target, central 80% intervals must attain empirical coverage in `[0.70, 0.90]`, while mean `log1p` width must not exceed `0.85` times the unconditional training-set 80% width. The published screening utility is `z(log1p(bandgap)) - z(log1p(formation_energy))`, standardized on the hidden set; the shortlist ordering must attain NDCG@30 of at least `0.80` against this true utility. All gates must pass for binary reward `1`. Only outcomes are graded and any scientifically valid method may pass. Empty files, constant means, copied sample submissions, vacuously wide intervals, weak models that ignore XYZ structure, and fabricated shortlists fail. The implemented oracle must pass the frozen instance five times and nop must score zero. If oracle experiments show a threshold is infeasible, the proposal must return for review rather than silently weakening it during implementation.

## 8. 难度评估 / Difficulty assessment

**中文：** 任务需要计算材料学、晶体结构表示、监督回归、组感知验证和不确定性校准的综合经验。合格研究者预计需要 30–45 个专注工时，用于解析周期晶体、验证描述符不变量、建立无泄漏划分、调试两个性质的不同误差模式、集成模型并校准区间与排序。MLE-Bench 原始榜单 879 个记录分数中，`0.060` 已接近前几个百分点，而本任务还增加子群、校准和排序联合门槛。前沿模型容易只在表格列上训练通用树模型、使用随机切分高估泛化、错误处理周期边界，或用过宽区间通过覆盖率；预计 Anthropic 和 OpenAI 前沿模型端到端一次通过率均低于 30%。

**English:** The task requires combined expertise in computational materials science, crystal representations, supervised regression, group-aware validation, and uncertainty calibration. A qualified researcher would likely need 30–45 focused hours to parse periodic crystals, validate descriptor invariance, construct leakage-resistant splits, debug different error modes for the two properties, ensemble models, and calibrate intervals and ranking. Among 879 recorded scores on the original MLE-Bench leaderboard, `0.060` is near the top few percent, while this task adds simultaneous subgroup, calibration, and ranking gates. Frontier models are likely to fit a generic tree model only to tabular columns, overestimate performance under random splits, mishandle periodic boundaries, or use vacuously wide intervals. The expected end-to-end first-attempt success rate is below 30% for both Anthropic and OpenAI frontier models.
