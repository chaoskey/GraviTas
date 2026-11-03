---
id: P11
title: 时间问题与量子参考系
cluster: 时空的量子性质
difficulty: 3
status: open
prereq: [正则量子化, 约束系统, 量子力学诠释]
updated: 2026-11-03
---

# P11 · 时间问题与量子参考系

> **一句话**：把引力正则量子化之后，时间变量消失了——Wheeler–DeWitt 方程
> $\hat{H}\Psi = 0$ 里根本没有 $t$。那么，"演化"是什么？

## 1. 问题是什么

广义相对论是**重参数化不变**的：时间坐标可以任意选择，物理不依赖它。
把这个对称性带到量子理论里，就得到约束

$$
\hat{H}\Psi = 0
$$

这个方程描述的是"整个宇宙的波函数"，它**不随时间演化**。这就是"时间问题"：

- 如果宇宙的量子态不演化，为什么我们看到变化？
- 如果演化是相对于某个"内部时钟"的，那这个时钟是什么？
- 为什么在低能下，时间又"回来"了？

## 2. 为什么它是入口

因为它是量子引力里**最哲学、也最技术**的问题。它逼你回答：
"时间"到底是基本的，还是涌现的？

如果时间是涌现的（像 P03 里的空间一样），那量子引力的基本方程不该含时间；
如果时间是基本的，那正则量子化就做错了——但没有更好的方案。

这个问题还与黑洞信息（P01）、宇宙学（P08）直接相连：
**宇宙波函数没有时间**，正是 Hartle–Hawking 方案的核心。

## 3. 时间线

| 年 | 事件 |
|---|---|
| 1950 | Dirac：约束系统的量子化 |
| 1967 | DeWitt：Wheeler–DeWitt 方程 |
| 1968 | Wheeler：superspace 与量子几何动力学 |
| 1983 | Page–Wootters：*Evolution without evolution* |
| 1985 | Isham–Kuchař：时间问题的分类 |
| 1991 | Rovelli：*Time in quantum gravity: an hypothesis* |
| 1992 | Kuchař：时间问题的系统综述 |
| 2002 | Rovelli：偏可观测量（partial observables） |
| 2011 | Zych et al.：引力时间膨胀影响量子干涉 |
| 2014 | Moreva et al.：用纠缠"造出"时间的实验 |
| 2018 | Giacomini–Brukner：量子参考系中的协变量子力学 |
| 2020 | Smith–Ahmadi：量子时钟观测到经典与量子时间膨胀 |

## 4. 当代状态（2025）

**没有共识**。大致有四条路线：

1. **时间不存在，只有关联**（Rovelli）：物理量是"偏可观测量"，时间只是其中一个坐标；
2. **时间从纠缠中涌现**（Page–Wootters）：时钟与系统纠缠，条件化后得到演化；
3. **时间在低能下涌现**（半经典）：WKB 近似下，$\Psi \sim e^{iS}$ 给出经典时间；
4. **量子参考系**：把"时间"看作一个量子系统，变换参考系会改变演化的定义。

**实验**：Moreva et al. (2014) 在光学系统中演示了 Page–Wootters 机制；
但这是"模拟"，不是"证明时间涌现"。

**最大的困难**：所有方案都在**重新定义**问题，而不是**解决**它。
没有方案给出可证伪的预言。

## 5. 核心概念与公式

**Wheeler–DeWitt 方程**

$$
\hat{H}\Psi[h_{ij}] = 0
$$

$\hat{H}$ 是 Hamiltonian 约束算符。注意：这不是"薛定谔方程令 $E=0$"，而是**约束**。

**Page–Wootters**

$$
(H_{C} + H_{R})\,\lvert\Psi\rangle = 0
$$

$C$ 是时钟，$R$ 是其余系统。对时钟态 $\lvert t\rangle$ 条件化：

$$
\lvert \psi_{R}(t)\rangle = \langle t \mid \Psi\rangle
$$

条件态满足一个**有效**的薛定谔方程——时间从纠缠中"长"出来。
代价：$t$ 不是基本参数，而是时钟的读数；不同时钟给出不同的"演化"。

**半经典时间**：把 $\Psi = e^{iS/\hbar}$ 代入约束，在 $\hbar \to 0$ 时得到 Hamilton–Jacobi 方程，
$S$ 的梯度定义了一个"时间"方向。

## 6. 必读文献

| 年 | 文献 | 为什么读 |
|---|---|---|
| 1967 | DeWitt, *Quantum theory of gravity I*, Phys. Rev. 160, 1113 | WdW 方程 |
| 1983 | Page–Wootters, *Evolution without evolution*, PRD 29, 2885 | 最优雅的方案 |
| 1992 | Kuchař, *Time and interpretations of quantum gravity* | 分类最清楚 |
| 2002 | Rovelli, *Partial observables*, gr-qc/0110035 | 关系时间 |
| 2014 | Moreva et al., *Time from quantum entanglement: an experimental illustration*, PRA 89, 052122 | 实验 |
| 2018 | Giacomini–Brukner, *Quantum mechanics and the covariance of physical laws…*, arXiv:1712.06840 | 量子参考系 |
| 2020 | Smith–Ahmadi, *Quantum clocks observe classical and quantum time dilation*, Nat. Commun. 11, 5360 | 引力 + 量子时钟 |
| 2012 | Anderson, *The problem of time*, arXiv:1009.2157 | 综述 |

## 7. 进入路径

**第 1 步（1 周）· 约束量子化**
先搞懂：为什么重参数化不变性会给出 $\hat{H}\Psi = 0$。用单粒子玩具模型推一遍。

**第 2 步（2 周）· Page–Wootters**
用一个两比特模型，手算条件态与有效哈密顿量。这一步会让你真正"看见"时间怎么出来。

**第 3 步（2 周）· 与宇宙学对接**
读 Hartle–Hawking 的"无时间"解释，对比 P08。问：宇宙波函数的"时间"在哪里？

## 8. 自检问题

1. 为什么 $\hat{H}\Psi = 0$ 不意味着"什么都没有发生"？
2. Page–Wootters 的条件态为什么满足幺正演化？它真的等价于时间吗？
3. "关系时间"与"内部时间"有什么区别？
4. 量子参考系的变换，会不会改变"什么是时间"这个问题的答案？
5. 如果时间涌现，为什么低能下它看起来如此"基本"？

## 9. 我的笔记

- （待填）
