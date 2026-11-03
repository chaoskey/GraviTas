---
id: P10
title: 引力与量子叠加：量子引力是否可被实验区分
cluster: 时空的量子性质
difficulty: 2
status: open
prereq: [量子力学, 半经典引力, 退相干理论]
updated: 2026-11-03
---

# P10 · 引力与量子叠加

> **一句话**：引力场本身能否处于量子叠加？一个质量的叠加态，会不会通过引力
> 与另一个质量产生纠缠？

## 1. 问题是什么

半经典引力假设引力是经典的，由量子物质的**期望值**源：

$$
G_{\mu\nu} = 8\pi G \langle T_{\mu\nu} \rangle
$$

这个方程在概念上很别扭（"期望值"不是可观测量），而且早就有论证指出它不自洽
（Eppley–Hannah 1977；Page–Geilker 1981 的实验性讨论）。

替代方案有两个极端：
- **引力是量子的**：引力子存在，引力场可以叠加、可以纠缠；
- **引力是经典的但会诱导坍缩**：Diósi–Penrose 模型，叠加态在引力能差足够大时自发坍缩。

两者给出**不同的可观测后果**，这就是这个问题的价值。

## 2. 为什么它是入口

因为它是**唯一一个可以在桌面实验室里做**的量子引力问题。

BMV 提议（Bose et al. 2017；Marletto–Vedral 2017）的逻辑极其干净：

> 两个质量各自处于两个位置的叠加。如果引力是量子的，它们会通过交换引力子而**纠缠**。
> 如果引力是经典的，它只能传递**经典信息**，不能产生纠缠。
> 因此：**测到纠缠 ⇒ 引力是量子的。**

这是一个"见证"（witness），不需要建普朗克能标的对撞机。

## 3. 时间线

| 年 | 事件 |
|---|---|
| 1957 | Feynman：Chapel Hill 会议，提出"引力是否需要量子化" |
| 1977 | Eppley–Hannah：半经典引力的不自洽性论证 |
| 1981 | Page–Geilker：实验性讨论 |
| 1987 | Diósi：引力诱导坍缩模型 |
| 1996 | Penrose：引力导致波函数坍缩 |
| 2011 | Zych et al.：引力时间膨胀对量子干涉可见度的影响 |
| 2014 | Moreva et al.：从纠缠中"造出"时间（实验） |
| 2017 | Bose et al.；Marletto–Vedral：BMV 方案 |
| 2020 | Marshman et al.：桌面检验线性化引力的量子性 |
| 2021–25 | 悬浮光力学：$10^{-14}\,\mathrm{kg}$ 量级的叠加态逼近 BMV 参数 |

## 4. 当代状态（2025）

**实验尚未实现**。BMV 需要的参数大致是：
质量 ${\sim}10^{-14}\,\mathrm{kg}$，空间分离 ${\sim}10^{2}\,\mu\mathrm{m}$，相干时间 ${\sim}1\,\mathrm{s}$，真空 ${\sim}10^{-10}\,\mathrm{mbar}$。

悬浮光力学（levitated optomechanics）在 2020 年代进展最快，
但"宏观叠加 + 长相干时间 + 低噪声"三者仍然不能同时满足。

**理论上的争论**：
- 如果引力是经典的，那它如何与量子场论共存？("classical-quantum" 混合动力学是否自洽？)
- 引力诱导的纠缠是否**必然**意味着引力子的存在？有没有 loophole？
- Diósi–Penrose 模型是否已被现有实验排除？(部分参数空间已被排除，但没有完全)

## 5. 核心概念与公式

**半经典方程**

$$
G_{\mu\nu} = 8\pi G \langle T_{\mu\nu} \rangle
$$

**BMV 的纠缠条件**：两个质量 $m$、间距 $d$、相干时间 $\tau$，

$$
\tau \gtrsim \frac{\hbar d}{G m^{2}}
$$

代入 $m = 10^{-14}\,\mathrm{kg}$、$d = 250\,\mu\mathrm{m}$，得到 $\tau \sim 1\,\mathrm{s}$ 量级。

**Diósi–Penrose 坍缩时间**

$$
\tau_{\mathrm{DP}} \sim \frac{\hbar}{E_{G}}, \qquad E_{G} \sim \frac{G m^{2}}{R}
$$

对 $m = 10^{-14}\,\mathrm{kg}$、$R = 10^{-6}\,\mathrm{m}$，$\tau_{\mathrm{DP}}$ 远大于实验时间——这也是为什么它还没被排除。

**引力退相干**（Blencowe 2013）：时空涨落导致相干性按 $\exp(-t/\tau)$ 衰减，
$\tau$ 依赖质量与分离，是 BMV 实验的"背景噪声"。

## 6. 必读文献

| 年 | 文献 | 为什么读 |
|---|---|---|
| 1957 | Feynman, *Quantum mechanics and gravitation*（Chapel Hill 会议录） | 问题的第一次提出 |
| 1977 | Eppley–Hannah, *The necessity of quantizing the gravitational field*, Found. Phys. 7, 51 | 不自洽性论证 |
| 1996 | Penrose, *On gravity's role in quantum state reduction*, GRG 28, 581 | DP 模型 |
| 2013 | Blencowe, *Effective field theory approach to gravitationally induced decoherence*, PRL 111, 021302 | 退相干估计 |
| 2017 | Bose et al., *Spin entanglement witness for quantum gravity*, PRL 119, 240401 | BMV |
| 2017 | Marletto–Vedral, *Gravitationally induced entanglement…*, PRL 118, 220401 | BMV 的另一版本 |
| 2020 | Marshman et al., *Locality and entanglement in table-top testing…*, PRD 101, 083019 | 桌面方案的系统化 |

## 7. 进入路径

**第 1 步（1 周）· 半经典引力的不自洽**
读 Eppley–Hannah 或 Page–Geilker 的论证。目标：说清为什么"期望值源"会出问题。

**第 2 步（2 周）· BMV 的相位**
自己推一遍：两个叠加态通过牛顿引力相互作用，积累的相位差是多少？
什么条件下这个相位差大到可以测出纠缠？

**第 3 步（2 周）· 退相干背景**
估算 Blencowe 退相干与 DP 坍缩的速率，比较它们与 BMV 信号的大小。

## 8. 自检问题

1. 为什么"经典引力"不能产生纠缠？这个论证有没有漏洞？
2. BMV 的"见证"是**充分**条件还是**必要**条件？
3. 如果引力是经典的，量子场论会出什么问题？
4. Diósi–Penrose 模型与标准量子力学的区别，在哪里可以被实验看到？
5. 桌面实验成功后，我们是否就"量子化了引力"？

## 9. 我的笔记

- （待填）
