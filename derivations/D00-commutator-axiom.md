# D00 · 公理：$[\hat q,\hat p]=i$

> 建档 2026-11-07 · 类型：**公理卡**——整个网格的输入，不是推导
> 上游：无
> 下游：[D04](D04-commutator-p-fq.md)、[D05](D05-diagonal-criterion.md)、[D11](D11-weyl-phase.md)、[D12](D12-translation.md)、[D13](D13-qp-overlap.md)、[D15](D15-momentum-representation.md)、[D16](D16-path-integral-representation.md)、[D18](D18-uncertainty.md)
> 编号规则见 [derivations/README](README.md)：D00 保留给公理，D01 起按拓扑序。

---

## 0. 陈述

$$
[\hat q,\hat p]=i
$$

**指数化形式（Weyl 关系）**：对一切 $a,b\in\mathbb{R}$，

$$
e^{ia\hat p}\,e^{ib\hat q}=e^{iab}\,e^{ib\hat q}\,e^{ia\hat p}
$$

即 [D11](D11-weyl-phase.md) 的 Weyl 关系。

**两者不等价，方向不对称：**

| 方向 | 是否成立 | 条件 |
|---|---|---|
| Weyl 关系推出对易子 | 成立（形式求导） | 需 $e^{ia\hat p}$、$e^{ib\hat q}$ 在公共定义域上可微 |
| 对易子推出 Weyl 关系 | **不成立** | 需额外要求：两者**自伴**、有**公共不变稠密域**、且群**强连续** |

**为什么对易子推不出 Weyl 关系**：$[\hat q,\hat p]=i$ 只是"在某个稠密子集上成立的一个等式"，它没有规定算子是否自伴、定义域是否被算子保持。缺这些条件时，$e^{ia\hat p}$ 可能根本不存在或不是酉算子，Weyl 关系无从谈起（例：半直线上的 $\hat p=-i\partial_x$ 只是对称的，自伴扩张不唯一）。

**为什么仍用指数形式**：$\hat q,\hat p$ 无界，乘积有定义域问题；指数化后两边都是有界酉算子，处处有定义，并且把中心荷 $e^{iab}$ 显式写出来，这正是 [D02](D02-stone-von-neumann.md) 唯一性定理所需的输入。

### 0.1 从 Weyl 关系导出对易子（求导法）

**前提**：$U,V$ 强连续（Stone 定理给出生成元 $\hat p,\hat q$）；$\psi$ 取在公共不变稠密域内，保证下面每一步求导合法。

把 Weyl 关系写成"差为零"的形式：

$$
W(a,b)\equiv U(a)\,V(b)-e^{iab}\,V(b)\,U(a)=0
$$

**第一步：对 $b$ 求导。**

$$
\partial_b W
=U(a)\,\partial_b V(b)-\bigl(ia\,e^{iab}\bigr)V(b)U(a)
-e^{iab}\bigl(\partial_b V(b)\bigr)U(a)
$$

这里用到 $\partial_b e^{iab}=ia\,e^{iab}$。

**第二步：再对 $a$ 求导。**

$$
\begin{aligned}
\partial_a\partial_b W
={}&(\partial_aU)\,(\partial_bV)
-i\,e^{iab}VU+ab\,e^{iab}VU-ia\,e^{iab}V(\partial_aU)\\
&-ib\,e^{iab}(\partial_bV)U-e^{iab}(\partial_bV)(\partial_aU)
\end{aligned}
$$

**第三步：取 $a=b=0$。** 含 $a$ 或 $b$ 的项全部为零，只剩三项：
$$
0=\partial_a\partial_b W\big|_{0}
=(i\hat p)(i\hat q)-i-(i\hat q)(i\hat p)
=-\hat p\hat q-i+\hat q\hat p
=[\hat q,\hat p]-i
$$

故

$$
\boxed{\ [\hat q,\hat p]=i\ }
$$

**那个 $-i$ 从哪来**：$\partial_b e^{iab}=ia\,e^{iab}$，再对 $a$ 求导时那个 $ia$ 变成常数 $i$。**它是中心荷的残余**——若两个群对易（相因子为 $1$），这一项消失，得到 $[\hat q,\hat p]=0$。所以**非零对易子完全由相位 $e^{iab}$ 产生**，这也解释了为什么反过来推不出：对易子只记住了"有一个 $i$"，没记住"相位是 $iab$"。

**另证（更短）**：把关系写成共轭形式 $U(a)V(b)U(a)^{-1}=e^{iab}V(b)$。先对 $a$ 求导得 $[\hat p,V(b)]=b\,V(b)$，再对 $b$ 求导得 $i[\hat p,\hat q]=\mathbb{1}$。

**三点注意**：

1. **结论只在稠密子集上成立**：$[\hat q,\hat p]\psi=i\psi$（$\psi\in D$），不是全空间的算子等式；
2. **$W$ 是算子的差**，$W=0$ 指它在 $D$ 上作用为零；
3. 这只是"Weyl 推出对易子"这一方向；反向不成立，见上文的方向表。

---

## 1. 它的地位：三句话说清

| 说法 | 判断 |
|---|---|
| 它是定理吗？ | **不是。** 无法从其他东西推出（在标准框架内） |
| 它是定义吗？ | **不是。** $\hat q,\hat p$ 已经由"可观测量是自伴算子 + 谱"确定；对易子是**额外**的输入 |
| 它是什么？ | **量子化的唯一输入项。** 给定这一条，其余全被锁死（[D02](D02-stone-von-neumann.md)） |

**这意味着什么**：整个网格（D01–D18）都建立在这一行之上。删掉它，所有卡片同时失效——$e^{ia\hat p}$ 不再平移、Weyl 相位变成 1、$\langle q\lvert p\rangle$ 失去定义。

---

## 2. 它规定了什么（下游一览）

| 直接推论 | 卡片 |
|---|---|
| $[\hat p,\hat q]=-i$ 与符号约定 | 全部卡片的前提 |
| $[\hat p,\hat q^{n}]=-in\hat q^{n-1}$（归纳） | [D04](D04-commutator-p-fq.md) |
| $e^{ia\hat p}\hat qe^{-ia\hat p}=\hat q+a$ | [D08](D08-two-term-truncation.md) → [D12](D12-translation.md) |
| Weyl 相位 $e^{iab}$ | [D11](D11-weyl-phase.md) |
| $\langle q\lvert p\rangle=e^{ipq}$ | [D13](D13-qp-overlap.md) |
| 路径积分里的 $(q'-q)^{2}/\varepsilon$ | [D16](D16-path-integral-representation.md) |

**注意最后一行**：路径积分的动能项是这一条公理的影子——若二者对易，$p$ 积分给 $\delta(q'-q)$，就没有"路径"可走。

---

## 3. 它为什么不是任意的：三条等价视角

1. **泊松括号量子化**：经典 $\{q,p\}=1$，量子化把 $\{\cdot,\cdot\}$ 换成 $[\cdot,\cdot]/(i)$。这是 Dirac 的处方。
2. **Weyl 形式**：指数化后成为群关系，中心荷就是辛形式（见 [D11](D11-weyl-phase.md) §3）。
3. **表示唯一性**：给定这一条，有限自由度下表示唯一（[D02](D02-stone-von-neumann.md)）——所以"选定这条公理"等价于"选定 Schrödinger 表示"。

**三点合起来说明**：这条公理不是"随手挑的对易子"，它在三种语言里都是同一个东西。

---

## 4. 边界

1. **只对有限自由度唯一。** 无穷自由度时表示不唯一（[D02](D02-stone-von-neumann.md)），"这条公理"不再是完整描述——还要指定表示（Fock、$\theta$ 真空、热态）。
2. **无界性使裸形式不严格。** 严格表述是 Weyl 关系；裸对易子只在共同的稠密定义域上有意义。
3. **它在引力中可能不是基本的。** 若时空是涌现的（[P03](../problems/P03-emergent-spacetime.md)），或时间是涌现的（[P11](../problems/P11-problem-of-time.md)），$\hat q,\hat p$ 及其对易子都可能只是低能有效描述。**这是本仓库整条路线要问的问题，不是本卡片能回答的。**
4. **它可被修改，但要做成新理论。** $\theta$ 变形、$\kappa$-Poincaré 等非对易几何都改写这一条；改写之后 [D02](D02-stone-von-neumann.md) 通常失效，整套表示论要重建。

---

## 5. 自检

- [x] 写出裸对易子与 Weyl 关系，并说明为什么后者更严格

答：

裸对易子：

$$
[\hat q,\hat p]=i
$$

Weyl 关系：

$$
e^{ia\hat p}\,e^{ib\hat q}=e^{iab}\,e^{ib\hat q}\,e^{ia\hat p}
$$

Weyl 关系可以推出裸对易子（对 $a,b$ 各求一次导，见 §0.1）；反之不成立——由对易子推回 Weyl 关系，还要补三条：**两者自伴**、有**公共不变稠密域**、群**强连续**（Stone 定理由此给出生成元）。缺任一条，$e^{ia\hat p}$ 可能不存在或不是酉算子，Weyl 关系就无从谈起。所以后者更严格。

- [x] 说明为什么它是公理而不是定义

答：无法从其他东西推出（在标准框架内）；$\hat q,\hat p$ 已经由"可观测量是自伴算子 + 谱"确定，对易子是**额外**的输入；它是量子化的唯一输入项。

更关键的一层：若它只是**定义**，那么"任何满足这个定义的算子对"都同样合法，理论对现实就没有约束力；正因为它不可推出、只能选定，它才携带物理内容。**定义不产生信息，公理产生信息。**

- [ ] 举出至少三条由它导出的结论及其卡片编号
- [ ] 说明它在无穷自由度下为什么不再是完整描述
- [ ] 说明它在量子引力语境下可能被改写，以及改写后哪些卡片会失效
- [x] 不做任何假设，从 Weyl 关系求导导出 $[\hat q,\hat p]=i$，并指出那个 $-i$ 从哪来

答：推导见 §0.1（原为手写稿）。虚数来自相因子的**混合二阶偏导**：

$$
\partial_b e^{iab}=ia\,e^{iab},
\qquad
\partial_a\partial_b e^{iab}=i\,e^{iab}-ab\,e^{iab}
\quad\Longrightarrow\quad
\partial_a\partial_b e^{iab}\big|_{0,0}=i
$$

具体机制：$\partial_b$ 产生因子 $ia$，再对 $a$ 求导时那个 $ia$ 贡献常数 $i$。

**不能用"对同一变量求两次"来理解**：$\partial_b^{2}e^{iab}|_{0,0}=-a^{2}e^{iab}|_{0,0}=0$，那里没有 $i$。所以准确说法是"混合"二阶偏导。
