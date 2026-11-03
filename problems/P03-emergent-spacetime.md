---
id: P03
title: 时空从纠缠中涌现
cluster: 信息与全息
difficulty: 4
status: open
prereq: [AdS/CFT, 纠缠熵, 张量网络, 量子纠错]
updated: 2026-11-03
---

# P03 · 时空从纠缠中涌现

> **一句话**：时空的几何——距离、连通性、曲率——是不是量子纠缠结构的宏观投影？

## 1. 问题是什么

全息原理说体是边界的编码。那么**编码的规则**是什么？如果两个边界区域纠缠得多，体里的对应区域是"更近"还是"更连通"？

Van Raamsdonk (2010) 给出了最震撼的答案：把 CFT 真空的两个半区之间的纠缠**逐渐减小**，
对偶的体几何会从"两个边界由虫洞相连"逐渐**断开**，最后变成两个独立的、无连接的时空。

也就是说：**几何的连通性 = 纠缠**。切断纠缠，时空就分裂。

## 2. 为什么它是入口

如果成立，它回答了一个比"如何量子化引力"更根本的问题：
**为什么会有时空？** 引力不再是"一种场"，而是纠缠结构的粗粒化描述。

这条思路（"It from Qubit"）在过去十五年里产出了量子引力最具体的进展：
张量网络、量子纠错码、复杂度=体积，全部从这里长出来。也是 P01 的岛屿公式能够被接受的概念背景。

## 3. 时间线

| 年 | 事件 |
|---|---|
| 1995 | Jacobson：Einstein 方程是热力学的状态方程 |
| 2006 | Ryu–Takayanagi：纠缠熵 = 面积 |
| 2009 | Swingle：MERA 是 AdS 的离散版 |
| 2010 | Van Raamsdonk：切断纠缠 → 时空断开 |
| 2013 | Maldacena–Susskind：ER=EPR |
| 2013 | Faulkner et al.：纠缠的第一定律 → 线性化 Einstein 方程 |
| 2014 | Almheiri–Dong–Harlow：体局域性 = 量子纠错 |
| 2015 | Pastawski–Yoshida–Harlow–Preskill：HaPPY 码 |
| 2015 | Jacobson：纠缠平衡 → 完整 Einstein 方程 |
| 2016 | Gao–Jafferis–Wall：可穿越虫洞（ER=EPR 的可操作版本） |
| 2016 | Susskind / Brown et al.：复杂度 = 体积 / 作用量 |
| 2017–25 | 从"纠缠→几何"到"代数→几何"（von Neumann 代数、模哈密顿量） |

## 4. 当代状态（2025）

**强证据**：
- 线性化 Einstein 方程可以从"纠缠的第一定律"推出（Faulkner et al. 2013）；
- HaPPY 码精确复现了全息的核心性质：体局域算符 = 边界逻辑算符，且受纠缠楔保护；
- 在 AdS₃/CFT₂ 中，"纠缠 → 几何" 的映射在很多情形下被显式构造出来。

**未解决**：
- 这只是**线性化**的推导。完整的非线性 Einstein 方程能否从纠缠原理推出，仍未知。
- 我们只有"给定边界 CFT，体几何是什么"的**算法**（算 RT 面），没有**原理**。
- 时间维度能否也涌现出来？现在所有构造都是"空间从纠缠涌现"，时间是外加的。
- 非 AdS 情形（dS、平直）几乎没有进展。

## 5. 核心概念与公式

**MERA ↔ 离散 AdS**：张量网络的一层对应 AdS 的一个径向切片，
网络的"深度"对应体的径向坐标 `z`（红外 → 紫外）。

**ER=EPR**：两个黑洞的纠缠 ⇔ 它们之间有虫洞。
更强的版本：任意纠缠 ⇔ 某种非局域连接。

**纠缠的第一定律**（小区域 `A`）

```
δS_A = δ⟨H_mod⟩
```

把它代入 RT 公式 `S = A/4G`，对小扰动展开，就得到**线性化 Einstein 方程**。
这是"引力 = 热力学"最干净的表述。

**复杂度 = 体积**（Susskind）

```
C ≈ V / (G R)
```

黑洞内部体积随时间的增长，对应边界态复杂度的增长——这解释了为什么黑洞内部在变大。

**HaPPY 码**：每个"完美张量"对应体中的一个区域，边界上任意足够大的区域都能重构体算符，
重构的失败模式恰好是 RT 面的形状。

## 6. 必读文献

| 年 | 文献 | 为什么读 |
|---|---|---|
| 2010 | Van Raamsdonk, *Building up spacetime with quantum entanglement*, arXiv:1005.3035 | 起点，短，必读 |
| 2013 | Maldacena–Susskind, *Cool horizons for entangled black holes*, arXiv:1306.0533 | ER=EPR |
| 2013 | Faulkner, Guica, Hartman, Myers, Van Raamsdonk, arXiv:1312.7856 | 纠缠→Einstein 方程 |
| 2014 | Almheiri–Dong–Harlow, *Bulk locality and quantum error correction*, arXiv:1411.7041 | 纠错视角 |
| 2015 | Pastawski–Yoshida–Harlow–Preskill, arXiv:1503.06237 | HaPPY 码，可动手 |
| 2015 | Jacobson, *Entanglement equilibrium and the Einstein equation*, arXiv:1505.04753 | 完整非线性版本 |
| 2016 | Gao–Jafferis–Wall, arXiv:1608.05687 | 可穿越虫洞 |
| 2016 | Cao–Carroll–Michalakis, *Space from Hilbert space*, arXiv:1606.08444 | 反向构造的尝试 |

## 7. 进入路径

**第 1 步（2 周）· 读 Van Raamsdonk**
只需理解：为什么"减少纠缠"会导致"几何断开"。画图，用 RT 公式解释。

**第 2 步（3 周）· 动手做 HaPPY 码**
用一个小的完美张量（6 腿，可由 5-qubit 码构造），手搭一个两三层的小网络，验证：边界上某个区域能否重构体算符。
这一步会让你真正理解"体局域性 = 纠错"。

**第 3 步（3 周）· 推线性化 Einstein 方程**
从 `δS = δ⟨H_mod⟩` + RT 出发，推出 `δG_{μν} = 8πG δT_{μν}`。
这是全仓库最值得亲手做一遍的推导之一。

## 8. 自检问题

1. 为什么"减少纠缠"会让时空断开？用 RT 公式说清楚。
2. ER=EPR 如果成立，对"信息能否从黑洞内部逃出"意味着什么？
3. 量子纠错码的哪个性质，恰好对应"体局域算符在边界上不可见"？
4. 复杂度=体积的猜想，解决了一个什么悖论？
5. 为什么"空间从纠缠涌现"比"时间从纠缠涌现"容易得多？

## 9. 我的笔记

- （待填）
