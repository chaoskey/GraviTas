---
id: P08
title: 宇宙的起源与初始条件
cluster: 宇宙学
difficulty: 3
status: open
prereq: [FRW 宇宙学, 暴胀, 路径积分, 奇点定理]
updated: 2026-11-03
---

# P08 · 宇宙的起源与初始条件

> **一句话**：大爆炸奇点是不是经典引力的自败之处？量子引力能否给出一个
> "没有奇点"的宇宙初条件？

## 1. 问题是什么

彭罗斯–霍金奇点定理（1965–70）证明：在很一般的条件下，经典时空必然测地不完备。
这不是"我们还没算清楚"，而是**广义相对论在该处失效的数学证明**。

于是问题变成：在奇点附近，量子引力给出什么？三条互不相同的路：

1. **回避**：量子效应抹平奇点，宇宙从一个反弹态开始（LQC、火劫）；
2. **无边界**：宇宙的"起点"不是奇点，而是一个没有边界的欧氏几何（Hartle–Hawking）；
3. **无初条件**：宇宙一直存在（永恒暴胀、循环模型），"起源"问题被消解。

## 2. 为什么它是入口

因为这是**唯一有可能被观测的量子引力问题**。CMB 的功率谱、张量模、非高斯性，
都携带着"暴胀之前"的痕迹——如果那些痕迹没有被暴胀抹掉的话。

更尖锐的是 **trans-Planckian 问题**：暴胀把今天的可观测量，追溯到普朗克尺度的模式。
如果量子引力修改了高能色散关系，CMB 上就会留下可计算的偏离。

## 3. 时间线

| 年 | 事件 |
|---|---|
| 1965 | Penrose：奇点定理 |
| 1970 | Hawking–Penrose：宇宙学奇点定理 |
| 1980 | Starobinsky：$R^2$ 暴胀 |
| 1981 | Guth：旧暴胀；1982 Linde：新暴胀 / 混沌暴胀 |
| 1981 | Mukhanov–Chibisov：暴胀扰动的量子起源 |
| 1983 | Hartle–Hawking：无边界波函数 |
| 1982 | Vilenkin：从"无"隧穿 |
| 1990s | COBE 确认 $n_s \approx 1$ 的近标度不变谱 |
| 2001 | Martin–Brandenberger：trans-Planckian 问题系统化 |
| 2006 | Ashtekar–Pawlowski–Singh：LQC 反弹 |
| 2002 | Steinhardt–Turok：火劫模型 |
| 2018 | Planck：$n_s = 0.9649 \pm 0.0042$，$r < 0.036$ |
| 2020s | 永恒暴胀的测度问题、swampland 对暴胀的约束、LiteBIRD 计划 |

## 4. 当代状态（2025）

**观测已经把参数空间压得很窄**：$n_s$ 略微红倾、$r$ 很小。
这排除了大量大场暴胀模型，也让"$r$ 是不是恰好落在可探测边缘"成为关键问题。

**理论上的三个死结**：
- **测度问题**：永恒暴胀产生无穷多个"口袋宇宙"，概率无法良定义。这是概念性的，不是技术性的。
- **初条件问题**：暴胀本身需要特殊的初始条件（Bunch–Davies 真空），"暴胀解决初条件"这个说法是循环的。
- **trans-Planckian 问题**：可观测量对普朗克尺度物理的敏感性，可能让暴胀的预言失去意义。

## 5. 核心概念与公式

**慢滚参数**（$M_{\mathrm{P}}^2 = \frac{1}{8\pi G}$）

$$
\varepsilon = \frac{M_{\mathrm{P}}^2}{2}\left(\frac{V'}{V}\right)^2, \qquad \eta = M_{\mathrm{P}}^2\,\frac{V''}{V}
$$

**可观测量**

$$
n_s - 1 = -6\varepsilon + 2\eta, \qquad r = 16\varepsilon
$$

观测：$n_s \approx 0.965$，$r < 0.036$ $\Rightarrow$ $\varepsilon \lesssim 0.002$，$\eta \approx -0.02$。

**无边界波函数**（Hartle–Hawking）

$$
\Psi[h_{ij}] = \int \mathcal{D}g\; e^{-S_E[g]}
$$

对 $S^3$ 边界上的 $h_{ij}$，对所有内部无边界紧致欧氏几何求和。
结果：$\Psi \sim \exp\left[\frac{1}{12\pi G\Lambda}\right]$（在薄壁近似下）。

**LQC 反弹**：$H^2 = \frac{8\pi G}{3}\rho\left(1 - \frac{\rho}{\rho_c}\right)$，$\rho_c \sim \rho_{\mathrm{Planck}}$。

## 6. 必读文献

| 年 | 文献 | 为什么读 |
|---|---|---|
| 1965 | Penrose, *Gravitational collapse and space-time singularities*, PRL 14, 57 | 奇点定理原文 |
| 1983 | Hartle–Hawking, *Wave function of the universe*, PRD 28, 2960 | 无边界 |
| 1982 | Vilenkin, *Creation of universes from nothing*, PLB 117, 25 | 隧穿 |
| 1981 | Guth, *Inflationary universe*, PRD 23, 347 | 暴胀起点 |
| 1982 | Linde, *A new inflationary universe scenario*, PLB 108, 389 | 慢滚 |
| 2001 | Martin–Brandenberger, *The trans-Planckian problem…*, PRD 63, 123501 | 关键难题 |
| 2006 | Ashtekar–Pawlowski–Singh, *Quantum nature of the big bang*, PRL 96, 141301 | LQC |
| 2011 | Guth–Kaiser–Nomura 等，永恒暴胀综述 | 测度问题 |

## 7. 进入路径

**第 1 步（2 周）· 奇点定理**
只读 Penrose 1965 的陈述与证明思路。目标：说清"测地不完备"为什么是"理论失效"而非"物理奇点"。

**第 2 步（3 周）· 暴胀的最小版本**
单场慢滚：推 $n_s - 1 = -6\varepsilon + 2\eta$、$r = 16\varepsilon$。然后用 Planck 数据反推 $V$ 的形状。

**第 3 步（3 周）· 两条量子引力路线**
对比 Hartle–Hawking 与 LQC 反弹：它们对"奇点"的处理方式有何本质区别？哪一个更可检验？

## 8. 自检问题

1. 奇点定理的假设有哪些？量子效应可能违背哪一条？
2. 暴胀真的解决了初始条件问题吗？还是把它推到了更早？
3. Hartle–Hawking 波函数为什么"没有时间"？这与 P11 有什么联系？
4. trans-Planckian 问题是一个技术问题，还是一个原则性问题？
5. 如果 $r$ 被 LiteBIRD 测到，能排除哪些量子引力方案？

## 9. 我的笔记

- （待填）
