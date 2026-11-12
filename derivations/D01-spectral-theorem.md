# D01 · 谱定理与 Gelfand–Maurin

> 建档 2026-11-06 · 类型：**引用卡**——陈述定理、说清用法与边界，**不复现证明**（证明属泛函分析，不在本仓库范围内）
> 上游：外部数学定理（本仓库不证明）
> 下游：[D02](D02-born-rule.md)、[D03](D03-position-eigen-equation.md)、[D04](D04-normalization-convention.md)、[D05](D05-functional-calculus.md)、[D06](D06-trace.md)、[D07](D07-commutator-p-fq.md)、[D08](D08-diagonal-criterion.md)、[D09](D09-product-kernel.md)、[D17](D17-qp-overlap.md)、[D18](D18-p-completeness.md)、[D19](D19-momentum-representation.md)、[D21](D21-path-integral-representation.md)、[D22](D22-trace-is-loop.md)、[D25](D25-uncertainty.md)

---

## 0. 两张定理，各一句话

| 定理 | 一句话 |
|---|---|
| **谱定理** | 自伴算子 $\iff$ 一族投影（投影值测度），算子就是"按谱参数把这些投影积起来" |
| **Gelfand–Maurin** | 在核空间条件下，这族投影可以"对角化"成**广义本征矢**——代价是本征矢搬到 Hilbert 空间外面 |

**分工**：谱定理管"算子长什么样"，Gelfand–Maurin 管"能不能写出本征基"。前者给函数演算与完备性，后者给 $\lvert q\rangle$ 本身。

---

## 1. 谱定理

### 1.1 陈述

**一句话**：自伴算子可以被拆成一族互相垂直的投影，权重是它的谱。

**这句话在解决什么问题**：算子本身是个抽象对象，"$\hat A$ 是什么"很难直接回答；谱分解把它换成两样具体的东西——**一堆数**（谱上的 $\lambda$）加**一堆投影**（$E(\lambda)$）。拆开之后，函数演算、完备性、对角化都变成在这两样东西上做算术。

**拆出来的两条性质**（这两条就是定理的全部内容）：

1. **投影能拼回整个空间**：$\int dE(\lambda)=\mathbb{1}$。投影互相垂直，合起来不漏。
2. **算子按权重把投影加起来**：$\hat A=\int\lambda\,dE(\lambda)$。$\lambda$ 是权重，$dE(\lambda)$ 是那一份投影。

**下面是可以跳过的精确陈述**（不影响理解上面两句）：

设 $\hat A$ 是 Hilbert 空间 $\mathcal{H}$ 上的自伴算子（可以无界）。则存在**唯一**的投影值测度 $E$（定义在 $\mathbb{R}$ 的 Borel 集上，支撑在谱 $\sigma(\hat A)$ 上），使

$$
\hat A=\int_{\sigma(\hat A)}\lambda\;dE(\lambda)
$$

对**任意** Borel 函数 $f$（**不必有界**）：

$$
f(\hat A)=\int f(\lambda)\;dE(\lambda),
\qquad
D\bigl(f(\hat A)\bigr)=\Bigl\{\psi\;\Big|\;\int\lvert f(\lambda)\rvert^{2}\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle<\infty\Bigr\}
$$

$f$ **有界**时它是有界算子，且 $\lVert f(\hat A)\rVert=\sup_{\lambda\in\sigma(\hat A)}\lvert f(\lambda)\rvert$。

**怎么读这两行**：

- 第一行说"$\hat A$ 是各族投影按 $\lambda$ 加权求和"；
- 第二行说"把 $\lambda$ 换成 $f(\lambda)$ 就行"。定义域那串只是"太重的权重会让和发散，所以要挑函数"——**不是新增的物理，是收敛性的记账**。**取 $f(\lambda)=\lambda$ 就还回 $\hat A$ 自己的定义域**，不必另记一条。

### 1.2 它给什么（五条）

1. **函数演算**——本卡的谱分解是它的全部依据；
2. **resolution of identity**——$\mathbb{1}=\int dE(\lambda)$，取 $f=1$ 即得；
3. **谱的信息**——$\sigma(\hat A)$ 是 $E$ 的支撑；$E(\{\lambda\})\neq0$ 的点就是点谱，且这时 $E(\{\lambda\})$ 正是**投影到该本征子空间**的投影；
4. **一个"对角化"模型**——谱简单时 $\hat A$ 酉等价于"在 $L^{2}(\mathbb{R},d\mu)$ 上乘以 $\lambda$"。**"让 $\hat q$ 对角"这句话的严格含义就是这个。**
5. **乘法律**——投影值测度的定义只要求"可数可加、且值都是投影"，而

$$
E(B)\,E(B')=E(B\cap B')
$$

是它的**推论**，不是额外假设。两步：

**（1）不交的两个集合，其投影必然正交。** 若 $B,B'$ 不交，则由可加性

$$
E(B)+E(B')=E(B\cup B')
$$

左边是两个投影之和，右边仍是一个投影。而**两个投影之和仍是投影，只有它们正交时才可能**：

$$
(P+Q)^{2}=P+Q\ \Longrightarrow\ PQ+QP=0\ \Longrightarrow\ PQ=QP=0
$$

（左乘 $P$ 与右乘 $P$ 各得一式，相减得 $PQ=QP$；再代回 $PQ+QP=0$ 即得 $PQ=0$。）

**（2）一般情形靠拆分。** 把 $B$、$B'$ 各拆成"交集 + 差集"：

$$
B=(B\cap B')\sqcup(B\setminus B'),
\qquad
B'=(B\cap B')\sqcup(B'\setminus B)
$$

代入 $E(B)E(B')$ 展开，四个交叉项都含不交的集合对，全为零，只剩 $E(B\cap B')^{2}=E(B\cap B')$。

**所以这条不需要假设**；谱定理保证这样的 $E$ 存在且唯一。

**它说的其实是**：**集合取交，对应算子复合**——指示函数的 $\mathbf{1}_B\cdot\mathbf{1}_{B'}=\mathbf{1}_{B\cap B'}$ 的算子版。

### 1.3 它不给什么（三条，最要紧）

1. **连续谱时不给本征矢。** 对连续谱的每个单点，$E(\{q\})=0$，于是**不存在** $\psi\in\mathcal{H}$ 满足 $\hat A\psi=q\psi$。谱定理给的是"一族投影"，不是"一族向量"。
2. **不告诉你谱是什么。** 定理对**任何**自伴算子都成立，所以它对"$\hat q$ 的谱是 $\mathbb{R}$ 还是格点"一无所知。谱由你选的算子与边界条件决定。
3. **不固定归一化。** 广义本征矢的归一化系数是约定（相位与整体相位都属于这一类）。

---

## 2. Gelfand–Maurin（核空间谱定理）

### 2.1 需要的结构：rigged Hilbert space

**一句话**：谱定理给了"一族投影"，没给"一族矢"；要写出 $\lvert q\rangle$，必须把它搬到 Hilbert 空间外面去。

**卡在哪**：连续谱时 $E(\{q\})=0$（§1.3 第 1 条），所以**没有**平方可积的 $\psi$ 满足 $\hat q\psi=q\psi$。可物理上我们天天写 $\lvert q\rangle$——这不是错，是它**住在别的空间里**。

**三层结构**：

$$
\Phi\;\subset\;\mathcal{H}\;\subset\;\Phi^{\times}
$$

| 层 | 是什么 | 在做什么 |
|---|---|---|
| $\Phi$ | 核空间（典型：Schwartz 函数 $\mathcal{S}(\mathbb{R})$） | **测试探针**：好到"取值"有意义 |
| $\mathcal{H}$ | 真正的 Hilbert 空间 | **态**：平方可积 |
| $\Phi^{\times}$ | $\Phi$ 上的连续线性泛函（缓增分布） | **广义对象**：$\lvert q\rangle$ 住这 |

**为什么中间那层不能省**：$\lvert q\rangle$ 干的事是"在 $q$ 点取值"。对 $L^{2}$ 函数这没有意义（改掉一个点的值，态不变）；对 $\Phi$ 里的好函数才有意义。

**为什么最外层不能省**：取值这个操作在 $\mathcal{H}$ 上**不连续**——函数可以在一点很高、范数却很小。所以它不是 $\mathcal{H}$ 里的矢量，而是 $\Phi$ 上的泛函。

**一句话记住三层**：$\lvert q\rangle$ 不是"存在但奇怪"，而是**"取值"这个动作的严格化身**——取值的对象必须是好函数，取出的值才有意义；而"取值"在 $\mathcal{H}$ 上不连续，所以它只能住在 $\Phi^{\times}$。

两层嵌入都连续且稠密。"核"这个条件是关键：它保证谱测度能被"数出来"、本征矢系能被"积出来"。**一般 Fréchet 空间不够**——这条定理对 $\Phi$ 的选择是敏感的。

### 2.2 陈述

**一句话**：只要算子不太野、把好函数还是映射到好函数里，就存在一族广义本征矢——它们①是本征矢，②够用（能展开任何态）。

**两个条件各管什么**：

| 条件 | 管什么 |
|---|---|
| $\hat A\Phi\subset\Phi$ | 让"本征方程"有意义（作用完还留在能谈的范围内） |
| $\Phi$ 是核空间 | 让"展开"这一步真能做成（不是形式上的） |

**精确陈述**：

设 $\hat A$ 自伴，$\Phi$ 核空间、连续稠密嵌入，且 $\hat A\Phi\subset\Phi$（$\hat A$ 在 $\Phi$ 上连续）。则存在谱测度 $\mu$ 与一族广义本征矢 $F_\lambda\in\Phi^{\times}$，使

$$
\hat A F_\lambda=\lambda F_\lambda
$$

且这族**完备**：对任意 $\phi,\psi\in\Phi$，

$$
\langle\phi\lvert\psi\rangle=\int\langle\phi\lvert F_\lambda\rangle\,\langle F_\lambda\lvert\psi\rangle\;d\mu(\lambda)
$$

写成算子的样子：

$$
\mathbb{1}=\int\lvert F_\lambda\rangle\langle F_\lambda\rvert\;d\mu(\lambda)
$$

### 2.3 它给什么

- $\lvert q\rangle$ **本身**：$[\hat q,f(\hat q)]$ 与 $\hat q$ 的谱分解都能写出来，靠的就是它；
- **本征矢族的存在性**——本卡只负责“存在”这一步；它如何特化成具体算子的本征方程、归一化如何定，都是下游的事；
- 狄拉克记号的下限——$\langle q\lvert\psi\rangle=\psi(q)$ 是**求值泛函**，不是 $L^{2}$ 内积。

**具体画面**（这也是"为什么必须扩大空间"的最短说明）：取 $\hat q$ 为 $L^{2}(\mathbb{R})$ 上"乘以 $q$"。则 $\lvert q\rangle$ 就是求值泛函 $\psi\mapsto\psi(q)$。这个泛函在 $L^{2}$ 上**不连续**（函数可在一点很高而范数很小），但在 Schwartz 空间 $\mathcal{S}$ 上连续——所以它住在 $\mathcal{S}^{\times}$ 里，不在 $\mathcal{H}$ 里。

---

## 3. 在本网格里的位置

依赖关系见 [网格](README.md) 的“输入”列，此处不重复。

**这就是网格最底下的那层**。它之上的一切都用它，它自己则不被本仓库证明。

---

## 4. 一致性检验

| 检验 | 结果 |
|---|---|
| 乘法算子（$\hat q$ 乘以 $q$） | 谱为 $\mathbb{R}$，$E(B)$ 为"乘以 $B$ 的特征函数"，广义本征矢为 $\delta(q'-q)$（即求值泛函，$q'$ 为自变量）✅ |

---

## 5. 边界

1. **非自伴算子全都没有。** 谱定理要求自伴；非自伴只有"谱"这个较弱的对象，没有 PVM，也没有广义本征矢系。这是整套量子力学要求可观测量自伴的**数学**理由，而不只是习惯。
2. **核性不可省。** 换成一般的稠密子空间，Gelfand–Maurin 可能失效。所以"随便找个稠密子空间就能定义 $\lvert q\rangle$"是错的。
3. **归一化依赖谱测度密度。** 若 $d\mu=\rho(q)\,dq$，则 $\langle q\lvert q'\rangle=\delta(q-q')/\rho(q)$。平直空间 $\rho=1$，弯曲空间 $\rho=\sqrt{g}$——**这是弯曲空间里测度因子的数学出处**。
4. **重数大于 1 时要加标签。** 本征矢写成 $F_{\lambda,i}$，完备性多一个 $\sum_i$，归一化变成 $\delta_{ij}$。物理上就是自旋、味道、超选扇区。
5. **这张卡不做证明。** 本仓库不重推泛函分析；能推的是“给定这些定理，物理结论如何落地”。**引用与证明的界限要一直守住**。

---

## 6. 自检

- [ ] 用一句话说清谱定理与 Gelfand–Maurin 各负责什么
- [ ] 解释为什么连续谱时"Hilbert 空间里没有本征矢"
- [ ] 用"求值泛函"说明 $\lvert q\rangle$ 为什么不在 $\mathcal{H}$ 里
- [ ] 说明核空间条件为什么不可省
- [ ] 举一个本网格里"引用谱定理"而非"证明"的具体位置
- [ ] 说明 §2.2 的两条定理分别给“存在性”与“完备性”
