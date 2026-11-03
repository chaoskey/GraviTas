---
id: P07
title: 宇宙学常数与 de Sitter 量子引力
cluster: 宇宙学
difficulty: 3
status: open
prereq: [GR, QFT 真空能, 宇宙学, 有效场论]
updated: 2026-11-03
---

# P07 · 宇宙学常数与 de Sitter 量子引力

> **一句话**：为什么真空能对引力的贡献，比实际观测到的暗能量小了 `10^120` 倍？
> 以及：一个正的宇宙学常数，对量子引力意味着什么？

## 1. 问题是什么

量子场论给真空能一个"自然"的估计：把每个涨落模的零点能加起来，截断在普朗克尺度，

```
ρ_vac ~ M_P⁴ ~ (10¹⁹ GeV)⁴
```

观测给出

```
ρ_Λ ~ (10⁻³ eV)⁴ ~ 10⁻⁴⁷ GeV⁴
```

差了约 `10^120` 倍。这不是"算错了一点"，而是**物理学史上最坏的预言**。

更麻烦的是，这个问题的结构有三层，常被混为一谈：

1. **为什么这么小？**（精细调节）
2. **为什么不是零，而且恰好在现在这个量级？**（宇宙学巧合）
3. **为什么辐射修正不会把它推回去？**（稳定性）

## 2. 为什么它是入口

因为 `Λ > 0` 意味着我们的宇宙是 **de Sitter**，而 de Sitter 的量子引力**极其难定义**：

- 观测者只能看到有限区域（static patch），存在视界与 Gibbons–Hawking 温度；
- 没有无穷远的 S-矩阵，散射语言失效；
- 熵有限 `S = 3π/(GΛ)`，意味着量子态空间是有限维的——这与"量子场论需要无穷维希尔伯特空间"直接冲突；
- dS/CFT 要求边界理论非幺正，物理意义不明。

所以"宇宙学常数问题"不仅是调节问题，它是**我们唯一确知的正 Λ 宇宙的量子引力如何定义**的问题。

## 3. 时间线

| 年 | 事件 |
|---|---|
| 1917 | Einstein 引入 `Λ` |
| 1967 | Zel'dovich：真空能应与 `Λ` 同量级 |
| 1977 | Gibbons–Hawking：dS 视界温度与熵 |
| 1987 | Weinberg：人择上界 |
| 1989 | Unruh、Henneaux–Teitelboim：未模引力（unimodular gravity） |
| 1998 | 超新星观测：`Λ > 0`，加速膨胀 |
| 1999 | Cohen–Kaplan–Nelson：全息暗能量上界 |
| 2003 | KKLT：弦论中的 dS 真空 |
| 2014 | Kaloper–Padilla：sequestering 机制 |
| 2018 | de Sitter swampland 猜想 |
| 2019 | Trans-Planckian censorship conjecture |
| 2024–25 | DESI 数据提示暗能量可能随时间演化（`w₀w_a`） |

## 4. 当代状态（2025）

**主流态度**：承认这是一个"未被解决的问题"，而不是"已被某个方案解决"。

**几条主要思路及其代价**：

| 思路 | 核心想法 | 代价 |
|---|---|---|
| 人择 | 只有小 `Λ` 的区域才有观测者 | 放弃预言力；需要 landscape |
| 未模引力 | 把 `Λ` 从场方程中解放为积分常数 | 不解释为什么小 |
| Sequestering | 引入全局项抵消真空能 | 机制人为，紫外完备性不明 |
| 全息上界 | `ρ_Λ ≤ M_P² H²` | 只能解释量级，不能解释数值 |
| 弦论 landscape | 大量真空，人择选择 | `10^500` 个真空，无可检验性 |
| Swampland | 禁止稳定 dS | 与观测冲突（若 `Λ > 0` 且稳定） |

**新动向**：如果 DESI 的 `w ≠ −1` 信号被确认，整个问题的框架会变——`Λ` 不再是常数，而是动力学场。

## 5. 核心概念与公式

**Gibbons–Hawking 温度与熵**（dS₄）

```
T_dS = H/(2π) ,    S_dS = A/(4G) = 3π/(G Λ)
```

**有效场论估计**

```
ρ_vac = ∫^{M_P} d³k (1/2) ħω_k ~ M_P⁴
```

**全息上界**（Cohen–Kaplan–Nelson）

```
ρ_Λ ≤ M_P² H²
```

代入 `H ~ 10⁻³³ eV`，给出 `ρ_Λ ~ 10⁻⁴⁷ GeV⁴`——**量级对上了**（差几个数量级以内）。
这是少数"没有精细调节就得到正确数量级"的思路。

**de Sitter swampland 猜想**

```
|∇V| ≥ c · V/M_P     或     min(V) ≤ 0
```

如果成立，稳定的 dS 真空不存在——与我们的宇宙直接冲突。

## 6. 必读文献

| 年 | 文献 | 为什么读 |
|---|---|---|
| 1989 | Weinberg, *The cosmological constant problem*, Rev. Mod. Phys. 61, 1 | **必读**，问题的最佳表述 |
| 1977 | Gibbons–Hawking, PRD 15, 2738 | dS 热力学 |
| 1999 | Cohen–Kaplan–Nelson, *Effective field theory, black holes, and the cosmological constant*, PRL 82, 4971 | 全息上界 |
| 1989 | Unruh, *A unimodular theory of canonical quantum gravity*, PRD 40, 1048 | 未模引力 |
| 2014 | Kaloper–Padilla, *Sequestering the Standard Model vacuum energy*, PRL 112, 091304 | 机制 |
| 2018 | Obied–Ooguri–Spodyneiko–Vafa, arXiv:1806.08362 | swampland |
| 2019 | Bedroya–Vafa, *Trans-Planckian censorship*, arXiv:1909.11063 | TCC |
| 2001 | Strominger, *The dS/CFT correspondence*, hep-th/0106113 | dS 全息的第一次尝试 |

## 7. 进入路径

**第 1 步（1 周）· 把数量级算清楚**
亲手算 `M_P⁴` 与 `(10⁻³ eV)⁴` 的比值，确认是 `10^120` 而不是 `10^60`。这一步能过滤掉大量"听说"。

**第 2 步（2 周）· 读 Weinberg 1989 的前 20 页**
重点：他如何把问题拆成"真空能"与"引力耦合"两部分。

**第 3 步（2 周）· dS 热力学**
推 `T_dS = H/2π`、`S = 3π/(GΛ)`。然后回答：为什么 dS 的有限熵是"问题"而不是"特色"？

## 8. 自检问题

1. `10^120` 这个数字是怎么来的？它依赖截断吗？
2. 如果 `Λ` 是积分常数（未模引力），问题就被解决了吗？
3. 全息上界为什么能给出正确量级？它是推导还是拟合？
4. dS 的有限熵与量子场论的无穷维希尔伯特空间，矛盾在哪？
5. 如果 DESI 确认 `w ≠ −1`，swampland 猜想会更容易还是更难成立？

## 9. 我的笔记

- （待填）
