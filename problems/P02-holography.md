---
id: P02
title: 全息原理与 AdS/CFT
cluster: 信息与全息
difficulty: 3
status: candidate
prereq: [QFT, 超对称基础, 微分几何, CFT 基础]
updated: 2026-11-03
---

# P02 · 全息原理与 AdS/CFT

> **一句话**：一个 `d+1` 维的引力理论，是否**完全等价于**它边界上的一个 `d` 维非引力理论？

## 1. 问题是什么

全息原理说：一个区域内的全部物理信息，可以被编码在其**边界**上，每个普朗克面积约一个比特。
`d+1` 维体（bulk）里的引力，等价于 `d` 维边界上的量子场论——体里的第三个空间维度是**涌现**的。

AdS/CFT 是这句话最具体的实现：

```
IIB 型弦论 on AdS₅ × S⁵   ≡   N=4 SU(N) 超杨–米尔斯理论（4 维）
```

左边有引力，右边没有引力；左边强耦合时右边弱耦合，反之亦然。
这给了我们第一把"强耦合引力 ↔ 弱耦合场论"的双语词典。

## 2. 为什么它是入口

因为它是**唯一一个可以被计算检验**的全息实现。你可以在两边各算一个量，然后对上：

- 热力学：BTZ 黑洞熵 ↔ 2D CFT 的 Cardy 熵；
- 纠缠：RT 面面积 ↔ CFT 的纠缠熵；
- 关联函数：Witten 图 ↔ CFT 的 OPE 系数；
- 谱：AdS 中的准正规模 ↔ CFT 热态极点。

对上了，说明对偶不只是哲学。这也是为什么整个 P01 的技术进展都发生在这里。

## 3. 时间线

| 年 | 事件 |
|---|---|
| 1993 | 't Hooft：全息原理的雏形（黑洞作为比特存储） |
| 1995 | Susskind：*The world as a hologram* |
| 1997 | Maldacena：AdS/CFT 猜想（hep-th/9711200） |
| 1998 | GKP、Witten：三篇奠基论文，给出配分函数与关联函数词典 |
| 2006 | Ryu–Takayanagi：纠缠熵 = 极小面面积 |
| 2007 | Hubeny–Rangamani–Takayanagi：一般区域的 HRT 面 |
| 2013 | Faulkner–Lewkowycz–Maldacena：`1/N` 修正 |
| 2014 | Engelhardt–Wall：量子 extremal surface（QES） |
| 2016 | 纠缠楔重构（entanglement wedge reconstruction）成为共识 |
| 2019 | 岛公式与复制虫洞（P01 的技术基础） |
| 2021–25 | 天球全息（celestial holography）、dS 全息的尝试 |

## 4. 当代状态（2025）

**已经稳固的**：AdS₅/CFT₄ 在多个独立检验下成立（异常匹配、Wilson 环、数值 bootstrap、热熵）；
低维版本（AdS₃/CFT₂、AdS₂/JT）已经成为可严格计算的玩具模型。

**仍然是猜想的**：没有证明。所有检验都在"某些极限下"，没有非微扰的定义。

**最大的空白**：
- **我们的宇宙不是 AdS**。dS（正宇宙学常数）与平直时空的全息描述都还没有可用版本。
- dS/CFT（Strominger 2001）要求边界理论是非幺正的，物理意义不明。
- 天球全息把平直时空的 S-矩阵重写成天球上的 CFT 关联函数，但"体"在哪里仍不清楚。

## 5. 核心概念与公式

**参数词典**（N=4 SYM ↔ IIB on AdS₅×S⁵）

```
g_YM² = 4π g_s
R⁴ = 4π g_s N α'² = λ α'² ,   λ ≡ g_YM² N
```

- `N → ∞`：`g_s → 0`，弦论退化为经典弦（无弦圈）；
- `λ ≫ 1`：`α'/R² → 0`，弦退化为超引力（无 `α'` 修正）。

所以"经典超引力"对应"大 N、强耦合的规范理论"。

**Witten 词典**

```
Z_string[φ₀] = ⟨ exp( ∫ φ₀ O ) ⟩_CFT
```

**质量–维度关系**（标量）

```
Δ(Δ − d) = m² R²
```

**Ryu–Takayanagi**

```
S_A = Area(γ_A) / (4 G_N)
```

`γ_A` 是在边界上以 `∂A` 为边界、与 `A` 同调的**极小曲面**。

## 6. 必读文献

| 年 | 文献 | 为什么读 |
|---|---|---|
| 1997 | Maldacena, hep-th/9711200 | 原文，短而密，值得读三遍 |
| 1998 | Witten, *Anti-de Sitter space and holography*, hep-th/9802150 | 配分函数词典 |
| 1998 | Gubser–Klebanov–Polyakov, hep-th/9802109 | 关联函数与质量–维度关系 |
| 2006 | Ryu–Takayanagi, hep-th/0603001 | 纠缠熵的几何化 |
| 2014 | Engelhardt–Wall, arXiv:1408.3203 | QES，通往岛公式 |
| 2015 | Ammon–Erdmenger, *Gauge/Gravity Duality*（书） | **最佳系统教材** |
| 2018 | Hartnoll–Lucas–Sachdev, *Holographic Quantum Matter* | 应用向，凝聚态视角 |
| 2021 | 任意一篇 AdS/CFT 综述（如 Casalderrey-Solana et al.） | 查漏 |

## 7. 进入路径

**第 1 步（2 周）· 建立词典**
只读 Maldacena 原文的引言 + 第三节。回答：为什么 `N → ∞` 对应经典引力？

**第 2 步（3 周）· 算一次 RT**
在 AdS₃（Poincaré 坐标）里算单区间纠缠熵，得到

```
S = (c/3) log(ℓ/ε),   c = 3R/(2G₃)
```

并说明为什么这个结果和 2D CFT 的 Cardy 公式一致。

**第 3 步（3 周）· 热态**
把 AdS₃ 换成 BTZ 黑洞，算 `T = 1/(2π)`（适当单位），对照 CFT 的 Cardy 熵 `S = 2π√(cL₀/6)`。

## 8. 自检问题

1. 为什么 `N → ∞` 在引力侧是"经典"？`1/N` 展开对应什么？
2. RT 面为什么必须取**极小**，而不是极大或任意？
3. 纠缠楔（entanglement wedge）是什么？为什么它比 RT 面包含更多信息？
4. 如果全息原理普遍成立，我们的宇宙的"边界"在哪里？这个问题为什么难？
5. AdS/CFT 的"证明"缺的是什么？

## 9. 我的笔记

- （待填）
