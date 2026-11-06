# D00 · 公理：$[\hat q,\hat p]=i$

> 建档 2026-11-07 · 类型：**公理卡**——整个网格的输入，不是推导
> 上游：无
> 下游：[D04](D04-commutator-p-fq.md)、[D05](D05-diagonal-criterion.md)、[D11](D11-weyl-phase.md)、[D12](D12-translation.md)、[D13](D13-qp-overlap.md)、[D14](D14-momentum-representation.md)、[D15](D15-path-integral-representation.md)、[D17](D17-uncertainty.md)
> 编号规则见 [derivations/README](README.md)：D00 保留给公理，D04 起按登记顺序。

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

---

## 1. 它的地位：三句话说清

| 说法 | 判断 |
|---|---|
| 它是定理吗？ | **不是。** 无法从其他东西推出（在标准框架内） |
| 它是定义吗？ | **不是。** $\hat q,\hat p$ 已经由"可观测量是自伴算子 + 谱"确定；对易子是**额外**的输入 |
| 它是什么？ | **量子化的唯一输入项。** 给定这一条，其余全被锁死（[D02](D02-stone-von-neumann.md)） |

**这意味着什么**：整个网格（D01–D17）都建立在这一行之上。删掉它，所有卡片同时失效——$e^{ia\hat p}$ 不再平移、Weyl 相位变成 1、$\langle q\lvert p\rangle$ 失去定义。

---

## 2. 它规定了什么（下游一览）

| 直接推论 | 卡片 |
|---|---|
| $[\hat p,\hat q]=-i$ 与符号约定 | 全部卡片的前提 |
| $[\hat p,\hat q^{n}]=-in\hat q^{n-1}$（归纳） | [D04](D04-commutator-p-fq.md) |
| $e^{ia\hat p}\hat qe^{-ia\hat p}=\hat q+a$ | [D08](D08-two-term-truncation.md) → [D12](D12-translation.md) |
| Weyl 相位 $e^{iab}$ | [D11](D11-weyl-phase.md) |
| $\langle q\lvert p\rangle=e^{ipq}$ | [D13](D13-qp-overlap.md) |
| 路径积分里的 $(q'-q)^{2}/\varepsilon$ | [D15](D15-path-integral-representation.md) |

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

- [ ] 写出裸对易子与 Weyl 关系，并说明为什么后者更严格
- [ ] 说明为什么它是公理而不是定义
- [ ] 举出至少三条由它导出的结论及其卡片编号
- [ ] 说明它在无穷自由度下为什么不再是完整描述
- [ ] 说明它在量子引力语境下可能被改写，以及改写后哪些卡片会失效
