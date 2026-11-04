# AI4S 参考任务提案：第一自相关不等式的新上界 / AI4S Reference Task Proposal: A New Upper Bound for the First Autocorrelation Inequality

## 0. 提案元数据 / Proposal metadata

- 提案 ID / Proposal ID: `AI4S-REF-MATH-FIRST-AUTOCORRELATION`
- 一级学科 / Primary domain: `mathematical-sciences`
- 二级学科（仅工程科学必填）/ Secondary discipline (required only for Engineering Sciences):
- 细分领域（自由填写）/ Research area (free text): `harmonic analysis; extremal inequalities; numerical optimization`
- 任务类型 / Task type: `frontier_research`

## 1. 贡献人基本信息 / Contributor information

- 姓名 / Name: Amy Xin / 辛馨
- 邮箱 / Email: amyxx2001@163.com
- 机构 / Affiliation: Tsinghua University
- 研究领域 / Research area: LLM agents for scientific research and autonomous scientific discovery
- 个人学术主页（可选）/ Academic profile (optional): https://amyxin-thu.github.io/
- 代表性论文 / Representative papers: [EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery](https://arxiv.org/abs/2606.13662); [AISE-Bench: A Full-Cycle Curated Benchmark for Information Seeking on Academic Knowledge Graphs](https://arxiv.org/abs/2607.20498); [AtomR: Atomic Operator-Empowered Large Language Models for Heterogeneous Knowledge Reasoning](https://arxiv.org/abs/2411.16495).

## 2. 任务类型与理由 / Task type and rationale

**中文：** 本任务属于“前沿问题攻关”。它不是要求 agent 复现一个隐藏的已知最优答案，而是把截至 2026-11-04 的公开最强构造直接提供给 agent，要求 agent 为第一自相关不等式找到一个可被精确认证、且至少改进 `1e-8` 的新上界。冻结的 SOTA oracle 本身是有效解并用于校准评价器，但不会得到满分；只有真正超过该基线的结果才获得 reward 1。

**English:** This is a `frontier_research` task. The agent is not asked to reproduce a hidden known optimum. Instead, it receives the strongest public construction frozen as of 2026-11-04 and must find a new, exactly certifiable upper bound for the first autocorrelation inequality that improves it by at least `1e-8`. The frozen-SOTA oracle is a valid result used to calibrate the evaluator, but it does not pass; reward 1 is reserved for a genuine improvement over that baseline.

## 3. 任务描述与价值 / Task description and value

**任务描述与目标 / Task description and objective**

**中文：** 对一个有限非负序列 $a=(a_0,\ldots,a_{n-1})$，任务最小化 $C(a)=2n\max_k(a*a)_k/(\sum_i a_i)^2$。Agent 获得 Einstein Arena 当前领先的 65,536 项 step construction、快速 FFT 评分器和完整输出约束，可以从现有构造出发研究其支撑集、峰值锁定、参数化与局部或全局优化方法。最终输出是一组有限十进制非负系数；独立 verifier 将其转成整数多项式并进行精确卷积，从而判断它是否构成新的严格上界。

**English:** For a finite nonnegative sequence $a=(a_0,\ldots,a_{n-1})$, the task minimizes $C(a)=2n\max_k(a*a)_k/(\sum_i a_i)^2$. The agent receives Einstein Arena's current leading 65,536-term step construction, a fast FFT scorer, and the complete output contract. It may study the incumbent's support, peak locking, parameterization, and local or global optimization strategies. Its final output is a finite-decimal nonnegative sequence; an independent verifier converts it to an integer polynomial and computes the convolution exactly to determine whether it establishes a new strict upper bound.

**任务的科学或应用价值 / Scientific or application value**

**中文：** 第一自相关不等式是调和分析中的极值问题。更好的非负函数构造会收紧已知上界，而可复现的精确认证可以把数值搜索结果转化为严格的数学结论。本任务同时检验 agent 是否能分析强基线的结构、设计有效的高维优化方法，并把数值候选转化为可独立验证的研究结果。

**English:** The first autocorrelation inequality is an extremal problem in harmonic analysis. Better nonnegative constructions tighten the known upper bound, while reproducible exact certification turns numerical search results into rigorous mathematical statements. The task tests whether an agent can analyze a strong incumbent, devise effective high-dimensional optimization, and turn a numerical candidate into an independently verifiable research result.

**前沿问题突破的领域内意义与当前 SOTA（仅前沿问题攻关任务）/ Domain significance of a frontier advance and current SOTA (frontier-research tasks only)**

**中文：** 截至 2026-11-04，[Einstein Arena 官方榜单](https://einsteinarena.com/problems/first-autocorrelation-inequality)的第一名是 Atris submission 2615，页面分数为 `1.502743486709583`。本任务冻结其公开下载的 65,536 项构造，并以精确整数卷积重新认证为 `645423412969467179759478160871915520 / 429496729600000035389440000000000729`。Einstein Arena 对该榜单使用的最小有效改进为 `1e-8`，因此本任务同样把至少 `1e-8` 的精确改进定义为实质突破。Step construction 的离散最大值与连续 supremum 的精确对应可参考 [CHRONOS 的认证说明](https://einsteinarena.com/problems/first-autocorrelation-inequality/threads/248)及其[归档工具](https://doi.org/10.5281/zenodo.21194862)。

**English:** As of 2026-11-04, Atris submission 2615 leads the [official Einstein Arena leaderboard](https://einsteinarena.com/problems/first-autocorrelation-inequality) with a displayed score of `1.502743486709583`. This task freezes its publicly downloadable 65,536-term construction and independently re-certifies it by exact integer convolution as `645423412969467179759478160871915520 / 429496729600000035389440000000000729`. Einstein Arena uses `1e-8` as the minimum leaderboard improvement, so this task also defines an exact improvement of at least `1e-8` as meaningful progress. The exact correspondence between the discrete maximum and the continuous supremum for step constructions is described in [CHRONOS's certification note](https://einsteinarena.com/problems/first-autocorrelation-inequality/threads/248) and its [archived tooling](https://doi.org/10.5281/zenodo.21194862).

## 4. 科研工作流 / Research workflow

**中文：** Agent 首先复现冻结 SOTA 的快速分数并分析造成最大自卷积峰的活动位置，随后选择参数化和优化策略，例如支撑集改变、平方或指数参数化、平滑近似、梯度法、坐标搜索或多分辨率优化。它可以反复使用快速评分器筛选候选，但最终必须把最佳构造写成符合约束的有限十进制序列。评分不限定研究路线，只以精确认证后的目标值为准。

**English:** The agent first reproduces the frozen SOTA's fast score and analyzes the active locations that attain the maximum self-convolution. It then chooses a parameterization and optimization strategy, such as support changes, square or exponential parameterization, smoothing, gradient methods, coordinate search, or multiresolution optimization. It may repeatedly use the fast scorer to screen candidates, but must finally serialize its best construction as a constrained finite-decimal sequence. Evaluation does not prescribe a research method and depends only on the exactly certified objective.

## 5. 数据及来源 / Data and provenance

**中文：** 输入基线通过 Einstein Arena 页面提供的公开下载接口获取，对应 problem ID 2、Atris submission 2615，提交时间为 2026-10-13。规范化 artifact 的 SHA-256 为 `3d2747f8e0d07f00355dfd3e20225c7cdda0b22305440dafd06dd62e86f19683`。任务保留来源、作者名、提交编号和时间；该公开下载页面未显示单独的数据许可，正式发布前仍应由项目方确认再分发条款。

**English:** The baseline was obtained through Einstein Arena's public download interface for problem ID 2, Atris submission 2615, submitted on 2026-10-13. The normalized artifact has SHA-256 `3d2747f8e0d07f00355dfd3e20225c7cdda0b22305440dafd06dd62e86f19683`. The task preserves the source, agent name, submission ID, and timestamp. The public download page does not display a separate data license, so the project should confirm redistribution terms before a formal release.

## 6. 计算环境 / Computational environment

**中文：** Agent 在 Python 3.12 容器中运行，可使用 NumPy 及自行安装的代码工具，获得 4 个 CPU、8 GiB 内存、10 GiB 存储和 8 小时时间。Agent 可见的快速评分器使用 FFT；独立无网络 verifier 使用 `python-flint` 的整数多项式乘法精确评分，不需要 GPU 或 GUI。

**English:** The agent runs in a Python 3.12 container with NumPy and may install additional code-based tools. It receives 4 CPUs, 8 GiB RAM, 10 GiB storage, and eight hours. The agent-visible fast scorer uses FFT, while the separate no-network verifier uses `python-flint` integer-polynomial multiplication for exact scoring. No GPU or GUI is required.

## 7. 评价标准 / Evaluation criteria

**中文：** Verifier 首先检查 JSON schema、长度、有限性、非负性、系数范围、总和及小数精度，然后把所有十进制数放大到共同整数尺度并精确计算完整自卷积。评测输出包括 `valid`、`match_sota`、`certified`、`scientific_score`、`improvement_over_sota` 和 `reward`。冻结 SOTA oracle 应得到 `valid=true`、`match_sota=true`、`reward=0`；只有精确分数不高于 SOTA 减 `1e-8` 的候选得到 reward 1。

**English:** The verifier checks the JSON schema, length, finiteness, nonnegativity, coefficient range, total mass, and decimal precision. It then scales all decimal values to a common integer representation and computes the full self-convolution exactly. Evaluation reports `valid`, `match_sota`, `certified`, `scientific_score`, `improvement_over_sota`, and `reward`. The frozen-SOTA oracle must produce `valid=true`, `match_sota=true`, and `reward=0`; only a candidate whose exact score is no greater than SOTA minus `1e-8` receives reward 1.

## 8. 难度评估 / Difficulty assessment

**中文：** 预计完成本任务需要调和分析、数值优化和高精度计算经验。冻结基线已经经历多轮公开优化，且当前构造有 65,536 个变量，简单随机扰动通常会破坏多个活动峰之间的平衡。人类专家若从该基线开展一次有实质希望的独立研究，预计至少需要约 80 个专注工时。前沿模型可能能够复现评分或做局部扰动，但预计在 Anthropic 与 OpenAI 前沿模型上达到精确 `1e-8` 改进的成功率均低于 30%。

**English:** The task requires experience in harmonic analysis, numerical optimization, and high-precision computation. The frozen incumbent has already undergone several rounds of public optimization and contains 65,536 variables; naive perturbations generally destroy the balance among multiple active peaks. An expert beginning from this incumbent would likely need at least 80 focused hours for an independent investigation with a meaningful chance of improvement. Frontier models may reproduce the score or attempt local perturbations, but their expected success rate for an exactly certified `1e-8` improvement is below 30% for both Anthropic and OpenAI frontier models.
