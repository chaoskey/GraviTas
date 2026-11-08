> [!IMPORTANT]
> **这是一个「人 × AI」协作项目。**
> 人类提出问题、做判断、承担结论；AI 负责检索、起草、校对与仓库维护。
> 所有物理结论都必须能追溯到可核对的推导或文献——**AI 的输出不是证据**，
> 它只提供候选答案与反例；错误由人类发现，并在 `log/` 里留下记录。

# GraviTas

> **GRAVITAS**，拉丁语：严肃、庄重、有分量。
> 它与 **Gravity**（引力）同源；这里故意把 **T** 大写，让它同时指 **T = Time**——
> 量子引力研究的，正是 **Space + Time + Quantum** 三者的交汇。

这个仓库不是一堆笔记，而是一台**问题牵引机**：
先把自己扔到一个尚未解决的问题面前，再让这个问题反过来决定你该学什么、该算什么、该读到哪一层为止。

---

## 三条原则

**1. 问题优先于章节。**
不从《某某教材》第 1 章读到第 12 章，而是从 `problems/` 里挑一个问题，倒推它需要哪些工具。
教科书是字典，不是路线。

**2. 推导优先于阅读。**
读过 ≠ 会。每个问题档案都带有"自检问题"和"进入路径"，路径的每一步都以**能在纸上独立重算**为完成标准。
看不懂的公式，抄一遍不算；改一个假设、再算一遍让别人看不出错误，才算。

**3. 输出优先于输入。**
每个问题必须产出一份**能讲给别人听**的东西：一份推导笔记，或一次 20 分钟的讲解。
仓库里的 `notes/` 和 `log/` 就是为此存在的——写不出，就是没懂。

---

## 五条主线

量子引力不是"一个"问题，而是围绕同一处裂缝的一圈问题。本仓库把它们归成五条主线：

| 主线 | 核心张力 | 问题档案 |
|---|---|---|
| **A · 信息与全息** | 黑洞蒸发是否破坏量子力学？时空是否是量子信息的编码？ | [P01](problems/P01-black-hole-information.md) · [P02](problems/P02-holography.md) · [P03](problems/P03-emergent-spacetime.md) |
| **B · 引力的紫外完备** | 引力在普朗克尺度上到底是什么理论？ | [P04](problems/P04-string-theory.md) · [P05](problems/P05-loop-quantum-gravity.md) · [P06](problems/P06-uv-completion-landscape.md) |
| **C · 时空的量子性质** | 时空本身是否有量子自由度？经典时空从何而来？ | [P09](problems/P09-singularities.md) · [P10](problems/P10-gravity-quantum-superposition.md) · [P11](problems/P11-problem-of-time.md) |
| **D · 宇宙学** | 宇宙的初条件、暗能量与量子引力如何互相约束？ | [P07](problems/P07-cosmological-constant.md) · [P08](problems/P08-cosmic-origins.md) |
| **E · 检验** | 量子引力有没有可做的实验/观测？ | [P12](problems/P12-phenomenology.md) |

> 主线之间不是并列的：A 是当前**进展最快**的一条，B 是**历史最久**的一条，C 是**最容易被忽视**的一条，D 是**唯一有观测**的一条，E 决定这一切是否还算物理学。

---

## 仓库结构

```
GraviTas/
├── README.md                  # 你在读的东西：项目宣言与导航
├── AGENTS.md                  # 给 AI 代理的维护契约（人类可跳过）
├── ROADMAP.md                 # 分阶段路线、时间预算、通关标准（gate）
├── problems/                  # 核心：每个前沿问题一个档案
│   ├── README.md              #   索引表 + 依赖图 + 推荐顺序
│   └── P01…P12.md             #   12 个问题
├── docs/
│   ├── method.md              # 怎么学：问题驱动的具体操作手册
│   └── prerequisites.md       # 前置知识地图：最小可用版本
├── reading/
│   └── bibliography.md        # 分主题文献：教材、综述、里程碑论文
├── notes/                     # 推导笔记（N001 推导范例 · N002 补丁讲义 · N003 表象速查 · N004 Hadamard 引理 · N005 算子地基读本）
├── derivations/               # 推导网格：一命题一卡，稳定编号（D01 起）
├── log/                       # 研究日志：每周做了什么、卡在哪
├── templates/                 # 问题档案 / 笔记 / 日志的模板
└── scripts/
    └── check_repo.py          # 仓库自检：元数据、链接、索引一致性
```

---

## 怎么用（第一次打开就做这三件事）

1. 读 [ROADMAP.md](ROADMAP.md)，确认自己现在处在哪个阶段、下一个 gate 是什么。
2. 读 [docs/method.md](docs/method.md)，照着里面的"两周一个循环"跑一轮。
3. 打开 [problems/P02-holography.md](problems/P02-holography.md)——这是全仓库最好的入口，
   因为它同时是**可计算**的、**有标准答案**的、**通向所有其他问题**的。

## 当前状态

| 项 | 状态 |
|---|---|
| 问题档案 | 12 个已建档（P01–P12） |
| 阶段 | 阶段 0（地基）未开始 |
| 下一个 gate | G1：独立推导 Bekenstein–Hawking 熵与 Hawking 温度 |
| 最近更新 | 2026-11-05 |

## 约定

- 每个问题档案头部有 YAML front-matter：`id / title / cluster / difficulty(1–5) / status / prereq / updated`。
- 状态词表：`open`（未解决）、`candidate`（有强候选答案）、`contested`（多个方案竞争）、`settled`（已解决，可当背景）。
- 笔记编号 `N###`，日志按日期 `YYYY-MM-DD.md`。
- AI 代理协作规则见 [AGENTS.md](AGENTS.md)；提交前跑一次 `python3 scripts/check_repo.py`。

## 许可证

[MIT](LICENSE) © 2026 chaoskey
