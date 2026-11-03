---
id: P04
title: 弦论作为引力的紫外完备
cluster: 紫外完备
difficulty: 5
status: contested
prereq: [QFT, 共形场论, 超对称, 紧致化]
updated: 2026-11-03
---

# P04 · 弦论作为引力的紫外完备

> **一句话**：普朗克尺度上的引力，是否由一维延展体（弦）而非点粒子描述？
> 如果是，它是否**唯一**自洽的选择？

## 1. 问题是什么

点粒子量子场论在紫外失败，因为引力耦合常数有负质量量纲（`[G] = −2`），
圈图发散无法被有限个反项吸收。弦论用一个根本性的动作回避这件事：

- 基本对象不是点，而是一维的弦，其特征尺度是 `ℓ_s = √α'`；
- 弦的振动谱里**自动**包含无质量自旋 2 态——引力子；
- 延展性提供了天然的紫外截断：高能过程被"抹平"，散射振幅指数衰减。

于是引力不再是"额外加上去的"，而是弦谱的**必然成员**。

## 2. 为什么它是入口

三个别的方案给不出的东西：

1. **微观计数**。Strominger–Vafa (1996) 用 D-brane 的态计数，精确复现了 5 维极端黑洞的 Bekenstein–Hawking 熵。
   这是量子引力史上第一次"数出来正好对上"。
2. **一个可定义的对偶**。AdS/CFT 出自弦论，并且给了 P01、P03 全部技术工具。
3. **自洽性约束极强**。反常抵消把维数锁死在 10（超弦）/ 26（玻色弦）；没有自由参数可调。这既是优点也是缺点。

## 3. 时间线

| 年 | 事件 |
|---|---|
| 1968–74 | Veneziano 振幅 → 弦模型；引力子作为闭弦态被发现 |
| 1984 | Green–Schwarz：反常抵消，第一次超弦革命 |
| 1985 | Heterotic 弦；Calabi–Yau 紧致化 |
| 1995 | Polchinski：D-brane；第二次超弦革命 |
| 1995 | Witten：M 理论，五种弦统一 |
| 1996 | Strominger–Vafa：黑洞熵的微观计数 |
| 1997 | Maldacena：AdS/CFT |
| 2003 | KKLT：dS 真空的构造 |
| 2003 | Susskind：landscape（`10^500` 个真空） |
| 2005– | Swampland 纲领：哪些低能理论**不能**来自量子引力 |
| 2018– | dS 猜想与"string theory 没有 dS 真空"的争论 |
| 2020–25 | 天球全息、物种尺度（species scale）、 asymptotic Hagedorn |

## 4. 当代状态（2025）

**已经做到的**：
- 唯一一个能对黑洞熵做**精确微观计数**的框架；
- 唯一一个给出**非微扰对偶**定义的框架（AdS/CFT）；
- 对低能有效理论施加了真实的约束（swampland），并已影响到宇宙学模型构建。

**没有做到的**：
- **零**个直接实验证据。所有"预言"要么在普朗克尺度，要么是超对称伙伴（LHC 未发现）。
- 真空选择问题（landscape）没有解决；`10^500` 个真空意味着理论几乎没有预言力。
- 我们的宇宙（dS，正宇宙学常数）是否在弦论景观中存在，仍有争议。
- 微扰弦论之外的非微扰定义，除 AdS/CFT 外仍不清楚。

**一句话判断**：它是目前**最完整**的候选，但不是**被验证**的候选。学它的理由不是"它一定对"，而是"它是唯一能算的"。

## 5. 核心概念与公式

**弦的谱**（开弦，超弦）

```
M² = (N − a)/α' ,   a = 0（超弦）,  a = 1（玻色弦）
```

`N` 是振动数算符。`N = 0` 给出无质量态（规范玻色子）；闭弦的 `N = 0` 态包含引力子。

**弦张力**

```
T_s = 1/(2π α')
```

**临界维数**：Weyl 反常要求 `D = 26`（玻色）、`D = 10`（超弦）。

**五种超弦 + M 理论**

```
IIA ── T ── IIB
 │            │
 S            S
 │            │
HE ── T ── HO ── S ── I
        ↘   ↙
        M 理论（11 维）
```

**Strominger–Vafa 计数**

```
S_micro = 2π √(Q₁ Q₅ n)  =  A/(4G₅) = S_BH
```

## 6. 必读文献

| 年 | 文献 | 为什么读 |
|---|---|---|
| 1998 | Polchinski, *String Theory* Vol. 1 & 2 | 标准教材；第 1 卷前 5 章是核心 |
| 2009 | Tong, *String Theory*（DAMTP 讲义） | 最快建立全局图景 |
| 1995 | Polchinski, *Dirichlet branes and Ramond–Ramond charges*, PRL 75, 4724 | D-brane 的原始论文 |
| 1996 | Strominger–Vafa, *Microscopic origin of the Bekenstein–Hawking entropy*, PLB 379, 99 | 必读，历史性 |
| 2003 | KKLT, *De Sitter vacua in string theory*, hep-th/0301240 | dS 构造 |
| 2003 | Susskind, *The anthropic landscape of string theory*, hep-th/0302219 | landscape |
| 2018 | Obied–Ooguri–Spodyneiko–Vafa, arXiv:1806.08362 | de Sitter 猜想 |
| 2019 | Blumenhagen–Lüst–Theisen, *Basic Concepts of String Theory* | 系统但可读 |

## 7. 进入路径

**第 1 步（3 周）· 世界面**
只学玻色弦：Polyakov 作用量、Weyl 反常、临界维数。目标：能解释为什么 `D=26`。

**第 2 步（3 周）· 谱与 D-brane**
算开弦谱，找到无质量矢量；理解 T-对偶；知道 D-brane 是什么、为什么它携带 RR 荷。

**第 3 步（4 周）· 黑洞计数**
读 Strominger–Vafa。不要求会所有细节，但要能说清：`Q₁, Q₅, n` 分别是什么，为什么熵是这三者的组合。

## 8. 自检问题

1. 为什么弦论能"软化"紫外？用世界面或顶点算子论证。
2. 五种超弦是如何统一的？T 对偶与 S 对偶各交换什么？
3. Strominger–Vafa 计数依赖了哪些假设？为什么它被认为是强证据？
4. Landscape 问题的本质是什么？它是理论的失败还是我们对理论的误用？
5. 如果 LHC 到 2035 年仍未发现超对称粒子，弦论会被证伪吗？

## 9. 我的笔记

- （待填）
