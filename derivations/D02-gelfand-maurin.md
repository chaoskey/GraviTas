# D02 · 核空间谱定理（Gelfand–Maurin）

> 建档 2026-11-18 · 类型：**引用卡**——Gelfand–Maurin 是外部数学，本卡只引用、不证明
> 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)
> 下游：[D04](D04-position-eigen-equation.md)、[D05](D05-normalization-convention.md)、[D06](D06-functional-calculus.md)、[D07](D07-trace.md)、[D09](D09-diagonal-criterion.md)、[D10](D10-product-kernel.md)、[D17](D17-translation.md)、[D18](D18-qp-overlap.md)、[D19](D19-p-completeness.md)、[D20](D20-momentum-representation.md)、[D22](D22-path-integral-representation.md)、[D23](D23-trace-is-loop.md)、[D27](D27-energy-basis.md)
> 它补的是谱定理缺的那一半：**给"一族投影"，不给"一族矢"**。

---

## 0. 问题：我们要"矢"，谱定理只给"投影"

谱定理说得清楚：自伴算子给一族**投影** $E(B)$。但物理上天天写的是 $\lvert q\rangle$——一个**矢**。

**它不在 $\mathcal{H}$ 里**：连续谱时 $E(\{q\})=\mathbb{0}$（[D01](D01-spectral-theorem.md) §3），所以**没有**平方可积的 $\psi$ 满足 $\hat q\psi=q\psi$。

**但 $\lvert q\rangle$ 不是错，是它住在别处。** 要给它一个合法的住处，就得把空间扩大。

---

## 1. 需要什么：三层空间

$$
\Phi\;\subset\;\mathcal{H}\;\subset\;\Phi^{\times}
$$

| 层 | 是什么 | 角色 |
|---|---|---|
| $\Phi$ | 核空间（典型：Schwartz 函数 $\mathcal{S}(\mathbb{R})$） | **测试探针**：好到"取值"有意义 |
| $\mathcal{H}$ | 真正的 Hilbert 空间 | **态**：平方可积 |
| $\Phi^{\times}$ | $\Phi$ 上的连续线性泛函（缓增分布） | **广义对象**：$\lvert q\rangle$ 住这 |

**为什么中间那层不能省**：$\lvert q\rangle$ 干的事是"在 $q$ 点取值"。对 $L^{2}$ 函数这没有意义（改掉一个点的值，态不变）；对 $\Phi$ 里的好函数才有意义。

**为什么最外层不能省**：取值这个操作在 $\mathcal{H}$ 上**不连续**——函数可以在一点很高、范数却很小。所以它不是 $\mathcal{H}$ 里的矢量，而是 $\Phi$ 上的泛函。

**两层嵌入都连续且稠密。** "核"这个条件是关键：它保证谱测度能被"数出来"、本征矢系能被"积出来"。**一般 Fréchet 空间不够**——这条定理对 $\Phi$ 的选择是敏感的。

**一句话记住三层**：$\lvert q\rangle$ 不是"存在但奇怪"，而是**"取值"这个动作的严格化身**。

---

## 2. 陈述

**条件**（三条）：

| 条件 | 管什么 |
|---|---|
| $\hat A$ 自伴 | 谱是实的、谱测度存在 |
| $\Phi$ 是核空间，连续稠密地嵌进 $\mathcal{H}$ | 让"展开"真能做成，不是形式上的 |
| $\hat A$ **连续地**映 $\Phi$ 到 $\Phi$ | 让"本征方程"有意义：作用完还留在能谈的范围内 |

**一句话**：只要算子不太野、且把好函数**连续地**映回好函数，就存在一族广义本征矢——它们①是本征矢，②够用（**$\Phi$ 里的元素都能展开**）。

**结论一：本征方程。** 存在族 $F_\lambda\in\Phi^{\times}$，使

$$
\hat A F_\lambda=\lambda F_\lambda
$$

（$\hat A$ 在 $\Phi^{\times}$ 上按对偶作用：$\langle\hat A F_\lambda,\phi\rangle=\langle F_\lambda,\hat A\phi\rangle$——**这正是要求 $\hat A$ 把 $\Phi$ 映进 $\Phi$ 的原因**。）

**结论二：完备性。** 存在谱测度 $\mu$，使对**任意 $\phi,\psi\in\Phi$**，

$$
\langle\phi\lvert\psi\rangle=\int\langle\phi\lvert F_\lambda\rangle\,\langle F_\lambda\lvert\psi\rangle\;d\mu(\lambda)
\qquad\Longleftrightarrow\qquad
\mathbb{1}=\int\lvert F_\lambda\rangle\langle F_\lambda\rvert\;d\mu(\lambda)
$$

**"任意"的范围要说清**：上式只对 $\Phi$ 里的元素成立。**对 $\mathcal{H}$ 中的一般态，这个积分不一定收敛**——要延拓是另一回事。**这就是为什么 $\Phi$ 必须"好"。**

---

## 3. 它给什么

- $\lvert q\rangle$ **本身**：$[\hat q,f(\hat q)]$ 与 $\hat q$ 的谱分解都能写出来，靠的就是它；
- **本征矢族的存在性**——本卡只负责"存在"这一步；它如何特化成具体算子的本征方程、归一化如何定，都是下游的事；
- **狄拉克记号的下限**——$\langle q\lvert\psi\rangle=\psi(q)$ 是**求值泛函**，不是 $L^{2}$ 内积。

**具体画面**（"为什么必须扩大空间"的最短说明）：取 $\hat q$ 为 $L^{2}(\mathbb{R})$ 上"乘以 $q$"。则 $\lvert q\rangle$ 就是求值泛函 $\psi\mapsto\psi(q)$。它在 $L^{2}$ 上**不连续**（函数可在一点很高而范数很小），但在 Schwartz 空间 $\mathcal{S}$ 上连续——所以它住在 $\mathcal{S}^{\times}$ 里，不在 $\mathcal{H}$ 里。

---

## 4. 边界

1. **非自伴算子全都没有。** 谱定理要求自伴；非自伴只有"谱"这个较弱的对象，没有投影值测度，也没有广义本征矢系。这是整套量子力学要求可观测量自伴的**数学**理由，而不只是习惯。
2. **核性不可省。** 换成一般的稠密子空间，Gelfand–Maurin 可能失效。所以"随便找个稠密子空间就能定义 $\lvert q\rangle$"是错的。
3. **归一化依赖谱测度密度。** 若 $d\mu=\rho(q)\,dq$，则 $\langle q\lvert q'\rangle=\delta(q-q')/\rho(q)$。平直空间 $\rho=1$，弯曲空间 $\rho=\sqrt{g}$——**这是弯曲空间里测度因子的数学出处**。
4. **重数大于 1 时要加标签。** 本征矢写成 $F_{\lambda,i}$，完备性多一个 $\sum_i$，归一化变成 $\delta_{ij}$。物理上就是自旋、味道、超选扇区。
5. **这张卡不做证明。** 本仓库不重推泛函分析；能推的是"给定这些定理，物理结论如何落地"。**引用与证明的界限要一直守住**。

---

## 5. 自检

- [ ] 用一句话说清谱定理与 Gelfand–Maurin 各负责什么
- [ ] 解释为什么连续谱时"Hilbert 空间里没有本征矢"
- [ ] 用"求值泛函"说明 $\lvert q\rangle$ 为什么不在 $\mathcal{H}$ 里
- [ ] 说明核空间条件为什么不可省
- [ ] 说明两条结论分别给"存在性"与"完备性"，以及为什么完备性只对 $\Phi$ 成立
