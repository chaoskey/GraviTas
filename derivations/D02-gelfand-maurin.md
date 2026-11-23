# D02 · 核空间谱定理（Gelfand–Maurin）

> 建档 2026-11-18 · 类型：**引用卡**——Gelfand–Maurin 是外部数学，本卡只引用、不证明；本卡的任务是把它翻译进 Dirac 记号，并与 [D01](D01-spectral-theorem.md) 的投影值测度接上头
> 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)
> 下游：[D03](D03-born-rule.md)、[D04](D04-position-eigen-equation.md)、[D06](D06-functional-calculus.md)、[D07](D07-trace.md)、[D09](D09-diagonal-criterion.md)、[D10](D10-product-kernel.md)、[D17](D17-translation.md)、[D18](D18-qp-overlap.md)、[D19](D19-p-completeness.md)、[D20](D20-momentum-representation.md)、[D22](D22-path-integral-representation.md)、[D23](D23-trace-is-loop.md)、[D27](D27-energy-basis.md)
> 它补的是谱定理缺的那一半：**给"一族投影"，不给"一族矢"**。

---

**记号**：$\Phi\subset\mathcal{H}\subset\Phi^{\times}$ 是 Gelfand 三重空间（§1）；$F_{\lambda,k}\in\Phi^{\times}$ 是广义本征矢，$k$ 跑重数指标；$\mu$ 是谱上的**标量谱测度**；$E$、$dE$ 沿用 [D01](D01-spectral-theorem.md) 的投影值测度。对偶括号 $\langle F,\phi\rangle$ 对 $F$ 反线性；Dirac 记号里 $\langle\lambda,k\lvert\psi\rangle:=\overline{\langle\psi\lvert\lambda,k\rangle}$——同一泛函的两副身份，不是两个对象。

---

## 0. 问题：我们要"矢"，谱定理只给"投影"

谱定理说得清楚：自伴算子给一族**投影** $E(B)$。这在标准 Hilbert 空间 $\mathcal{H}$ 里是完备的（冯·诺依曼谱测度理论）。

但物理上天天写的 $\lvert q\rangle$——一个**矢**——**不在 $\mathcal{H}$ 里**：连续谱时 $E(\{q\})=\mathbb{0}$（[D01](D01-spectral-theorem.md) §3），所以**没有**平方可积的 $\psi$ 满足 $\hat q\psi=q\psi$。

**为什么不能从 D01 直接推出。** D01 给的是**抽象**的投影值测度 $E$；它不保证 $E$ 有密度 $\lvert F_\lambda\rangle\langle F_\lambda\rvert$，更不保证有本征矢——连续谱时 $\mathcal{H}$ 里根本没有。**这两样都要另外的定理，不是换积分符号能换出来的。**

**$\lvert q\rangle$ 不算错，只是它住在别处。** 出路是把空间扩大，让它有个合法的住处。

---

## 1. Gelfand 三重空间（装备希尔伯特空间）

$$
\Phi\;\subset\;\mathcal{H}\;\subset\;\Phi^{\times}\tag{1}
$$

也叫**装备希尔伯特空间**（rigged Hilbert space），或 **Gelfand 三重空间**。

| 层 | 是什么 | 角色 |
|---|---|---|
| $\Phi$ | 核空间（典型：Schwartz 函数 $\mathcal{S}(\mathbb{R})$） | **测试探针**：好到"取值"有意义 |
| $\mathcal{H}$ | 可分复 Hilbert 空间 | **态**：平方可积 |
| $\Phi^{\times}$ | $\Phi$ 的**共轭对偶**：$\Phi$ 上全体连续反线性泛函（典型：缓增分布 $\mathcal{S}^{\times}$） | **广义对象**：$\lvert q\rangle$ 住这 |

两层嵌入都是**连续且稠密**的：$\Phi$ 稠密嵌进 $\mathcal{H}$，$\mathcal{H}$ 又稠密嵌进 $\Phi^{\times}$。

**三层各管一件事，缺一不可。**

**为什么需要最里层 $\Phi$**：对一般的 $L^{2}$ 函数，"在 $q$ 点取值"**不连续**（改掉一个点的值，态不变）。必须挑一个好函数空间 $\Phi$，在它上面取值才有意义。

**为什么需要最外层 $\Phi^{\times}$**：即便有了 $\Phi$，取值 $\phi\mapsto\phi(q)$ 也只是 $\Phi$ 上的**连续线性泛函**，**不是 $\Phi$ 里的元素**——它没有对应的"函数"，只对应一个"泛函"。所以 $\lvert q\rangle$ 住在 $\Phi^{\times}$，不在 $\Phi$ 里，更不在 $\mathcal{H}$ 里。

**为什么需要中间层 $\mathcal{H}$**：因为**三件事只在 Hilbert 空间里有定义**：

1. **内积与概率**：$\lvert\langle\phi\lvert\psi\rangle\rvert^{2}$ 要它；
2. **自伴与谱**：$\hat A$ 的自伴性、谱定理都要求**完备**的内积空间——$\Phi$ 按 $L^{2}$ 范数**不完备**（取一列 $\mathcal{S}$ 函数，其 $L^{2}$ 极限可以不再光滑，极限跑出 $\Phi$），$\Phi^{\times}$ 则根本没有内积；
3. **$\Phi^{\times}$ 的"对偶"身份**：$\mathcal{H}\subset\Phi^{\times}$ 的嵌入靠 Riesz 表示（$\psi\mapsto\langle\psi\lvert\cdot\rangle$）——**没有 $\mathcal{H}$，$\Phi^{\times}$ 只是抽象对偶，与物理无关**。

**"核空间"是外部概念**，本卡不定义它，只用它两条性质：（i）能**连续稠密**地嵌进 $\mathcal{H}$；（ii）使谱测度**可数化**——所以本征矢系能被"积出来"。**一般 Fréchet 空间不够**：这条定理对 $\Phi$ 的选择是敏感的。

**一句话记住三层**：$\Phi$ 让"取值"**连续**，$\Phi^{\times}$ 给"取值"一个**住处**，$\mathcal{H}$ 让"概率、自伴、谱"**有定义**——$\lvert q\rangle$ 不是"存在但奇怪"，而是**"取值"这个动作的严格化身**。

---

## 2. 核空间谱定理

**一句话表述**：只要算子不太野、且把好函数**连续地**映回好函数，就存在一族广义本征矢——它们①是本征矢，②够用（**$\Phi$ 里的元素都能展开**）。

**它不只是"存在广义本征函数"。** 它说的是：在合适的核空间框架下，自伴算子的整套谱理论都可以由对偶空间里的广义本征矢来实现——**这才是它的数学内容**。

**条件**（五条）：

1. $\mathcal{H}$ 是可分复 Hilbert 空间；
2. $\Phi$ 是**稠密**嵌进 $\mathcal{H}$ 的**核空间**；
3. $\hat A$ 是 $\mathcal{H}$ 上的**自伴**算子；
4. $\hat A$ **保持 $\Phi$ 不变**，即 $\hat A\Phi\subseteq\Phi$——**稳定不变性**；
5. $\hat A$ 限制在 $\Phi$ 上是**连续**线性算子，即 $\hat A\big\rvert_{\Phi}:\Phi\to\Phi$ 连续——**连续性**。

### 2.1 结论一：本征方程

对 $\sigma(\hat A)$ 上的**几乎所有** $\lambda$，存在**非零**的广义本征矢 $F_{\lambda,k}\in\Phi^{\times}$（$k$ 跑重数指标），使

$$
\hat AF_{\lambda,k}=\lambda F_{\lambda,k}\tag{2}
$$

**（2）是对偶空间里的等式**：$\hat A$ 在 $\Phi^{\times}$ 上的作用是"转置"，$\langle\hat AF,\phi\rangle=\langle F,\hat A\phi\rangle$。它在 $\Phi$ 上的等价写法是

$$
F_{\lambda,k}(\hat A\phi)=\lambda\,F_{\lambda,k}(\phi),\qquad \forall\phi\in\Phi\tag{3}
$$

**两者的关系是"定义"，不是"定理"**：用 $\Phi$ 上的数（3）来定义 $\Phi^{\times}$ 里的等式（2）——**两个式子说的是同一件事**。**这一步为什么需要条件 4、5**：$\hat A\phi$ 得留在 $\Phi$ 里，右边的括号才有意义。

### 2.2 结论二：完备性（内积表示）

存在**标量谱测度** $\mu$，使对**任意** $\phi,\psi\in\Phi$，

$$
\langle\phi\lvert\psi\rangle
=\int_{\sigma(\hat A)}\sum_k F_{\lambda,k}(\phi)\,\overline{F_{\lambda,k}(\psi)}\;d\mu(\lambda)
\tag{4}
$$

**"任意"的范围要说清**：上式只对 $\Phi$ 里的元素成立。**对 $\mathcal{H}$ 中的一般态，这个积分不一定收敛**——要延拓是另一回事。**这就是为什么 $\Phi$ 必须"好"。**

---

## 3. 翻译成 Dirac 记号

**对应关系**：

$$
F_{\lambda,k}\equiv\lvert\lambda,k\rangle,
\qquad
F_{\lambda,k}(\phi)\equiv\langle\phi\lvert\lambda,k\rangle
$$

于是（2）（3）（4）分别写成

$$
\exists\,\lvert\lambda,k\rangle\in\Phi^{\times}:\quad
\hat A\lvert\lambda,k\rangle=\lambda\lvert\lambda,k\rangle\tag{2*}
$$

$$
\langle\hat A\phi\lvert\lambda,k\rangle=\lambda\langle\phi\lvert\lambda,k\rangle,
\qquad\forall\phi\in\Phi\tag{3*}
$$

$$
\langle\phi\lvert\psi\rangle
=\int_{\sigma(\hat A)}\sum_k\langle\phi\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle\;d\mu(\lambda)
\tag{4*}
$$

**$\lvert\lambda,k\rangle$ 与 $\langle\lambda,k\rvert$ 是同一个元素**：$\Phi^{\times}$ 按"$\Phi$ 上的连续反线性泛函"定义，所以它的元素**既是矢量**（可加、可被 $\hat A$ 转置作用），**又是泛函**（可在 $\phi\in\Phi$ 上取值）。两副身份之间只有一条翻译公式，就是记号栏里那条——**（4\*）里没有共轭，是因为共轭已经吃进 $\langle\lambda,k\lvert\psi\rangle$ 的定义里了**。

**$\langle\lambda,k\rvert$ 只能吃 $\Phi$ 里的东西**，不能吃 $\Phi^{\times}$ 里的——所以 $\langle\lambda,k\lvert\lambda',k'\rangle$ 严格说**没有定义**，它只是 $\delta_{kk'}\delta(\lambda-\lambda')$ 的简写（见 §6 第 3 条）。

**两个等价形式**（弱拓扑意义下）：

$$
\begin{aligned}
&\lvert\psi\rangle=\int_{\sigma(\hat A)}\sum_k\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle\;d\mu(\lambda)
&&\text{态展开}\\
\Longleftrightarrow\quad
&\mathbb{1}=\int_{\sigma(\hat A)}\sum_k\lvert\lambda,k\rangle\langle\lambda,k\rvert\;d\mu(\lambda)
&&\text{完备性}
\end{aligned}\tag{5}
$$

**"完备性"这个名称是准确的**：$\mathbb{1}$ 被拆成一族外积的积分，说明这族矢量"铺满"了空间——**但（5）只在 $\Phi$ 上取二次型时是有数的等式**，理由同在（4）后面。

---

## 4. 接头：$E(B)$ 与 $dE$ 的密度

D01 给的是**算子级**的 $E$，本卡给的是**标量级**的 $\mu$。两者怎么对上，是这一节要回答的。

### 4.1 指示函数：$\mathbf{1}_B(\hat A)=E(B)$

取指示函数 $\mathbf{1}_B$（只取 $0$、$1$，有界）：

$$
\mathbf{1}_B(\lambda)=
\begin{cases}
1, & \lambda\in B\\
0, & \lambda\notin B
\end{cases}\tag{6}
$$

由 [D01](D01-spectral-theorem.md) §1 的函数演算、§2 的 $E(\sigma(\hat A))=E(\mathbb{R})$、§4 的乘法规则：

$$
\mathbf{1}_B(\hat A)
=\int_{\sigma(\hat A)}\mathbf{1}_B\,dE
=E\bigl(\sigma(\hat A)\cap B\bigr)
=E(\sigma(\hat A))\,E(B)
=\mathbb{1}\,E(B)
=E(B)\tag{7}
$$

### 4.2 为什么不能写成算子等式

若把 $E(B)$ 作用到广义本征矢上、写 $E(B)\lvert\lambda,k\rangle=\mathbf{1}_B(\lambda)\lvert\lambda,k\rangle$，就需要 $E(B)$ 把 $\Phi$ 映进 $\Phi$。

**这一般不成立。** 取 $\hat A=\hat q$、$\Phi=\mathcal{S}(\mathbb{R})$，则 $E(B)$ 就是乘以 $\mathbf{1}_B$：

$$
\bigl(E(B)\phi\bigr)(q)=\mathbf{1}_B(q)\,\phi(q)
$$

它在 $\partial B$ 上跳变，已经不是 Schwartz 函数。**"保 $\Phi$"这条性质对函数演算不封闭**：$\hat A$ 保 $\Phi$，多项式 $p(\hat A)$ 保 $\Phi$，但跳变函数 $\mathbf{1}_B$ 不保。所以 $E(B)$ 在 $\Phi^{\times}$ 上没有作用，下面只能走弱形式。

### 4.3 关键一步：把 $E(B)\phi$ 换成 $\Phi$ 里的元素

（3）只交代 $\hat A$ 自己对 $F_{\lambda,k}$ 的作用。要把函数演算搬过来，需要它的一条光滑版：

$$
\langle g(\hat A)\psi\lvert\lambda,k\rangle=g(\lambda)\,\langle\psi\lvert\lambda,k\rangle,
\qquad \forall\psi\in\Phi,\ \ g\in C_c^{\infty}(\mathbb{R};\mathbb{R})\tag{8}
$$

**（8）是光滑函数演算与广义本征态的相容性条件。** （3）只对**多项式** $p(\hat A)$ 归纳给出同样的式子；推广到一般光滑 $g$ 要另作声明。**它对 $\hat A=\hat q,\hat p$ 配 $\Phi=\mathcal{S}(\mathbb{R})$ 可以直接验算**：$g(\hat q)$ 是乘以 $g(q)$，$g(\hat p)$ 是卷积，两者都保 $\mathcal{S}$，（8）逐点成立。**一般 $\hat A$ 上没有这条**，所以 §4.4 的推导**以（8）单独成立为前提**——这是本卡在定理条件之外唯一多要的东西。

### 4.4 推导：用一列好函数逼近

**先对区间 $B$ 取逼近列**：此时必存在实值 $g_n\in C_c^{\infty}(\mathbb{R})$，满足 $0\le g_n\le1$ 且 $g_n\to\mathbf{1}_B$ 逐点（指示函数只有两个跳变点，用光滑截断平滑即可）。**一般 Borel 集不必另造逼近列**：右端的 $\Lambda_B$ 与左端的 $B\mapsto\langle\phi\lvert E(B)\psi\rangle$ 都是有限测度，两者在所有区间上相等，就由测度唯一性自动推广到所有 Borel 集。

对区间 $B$：由（8），$g_n(\hat A)\phi$、$g_n(\hat A)\psi$ 都留在 $\Phi$ 里，于是（4）可以作用在 $(g_m(\hat A)\phi,\,g_n(\hat A)\psi)$ 上：

$$
\begin{align}
\langle\phi\lvert E(B)\psi\rangle
&=\langle E(B)\phi\lvert E(B)\psi\rangle
&&\text{投影的等幂与自伴}\\
&=\lim_{m,n\to\infty}\langle g_m(\hat A)\phi\lvert g_n(\hat A)\psi\rangle
&& g_n(\hat A)\to E(B)\ \text{强收敛}\\
&=\lim_{m,n\to\infty}\int_{\sigma(\hat A)}g_m(\lambda)\,g_n(\lambda)\sum_k\langle\phi\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle\;d\mu(\lambda)
&&\text{由（4）与（8）}\\
&=\int_B\sum_k\langle\phi\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle\;d\mu(\lambda)
&&\text{控制收敛：}g_mg_n\to\mathbf{1}_B,\ \lvert g_mg_n\rvert\le1
\end{align}
$$

**这一步的要害**：不是把（4）直接用在 $E(B)\phi$ 上（那要 $E(B)\Phi\subseteq\Phi$），而是先把 $E(B)\phi$ 换成 $\Phi$ 里的 $g_m(\hat A)\phi$，用完（4）再取极限。

### 4.5 剥离测试探针，得密度

上式对**任意** $\phi,\psi\in\Phi$ 成立，所以先只拿到弱等式。记右端为 $\Lambda_B(\phi,\psi)$：它在 $k$ 上用柯西–施瓦茨、再用（4）（分别取 $\phi$、$\psi$ 自身），满足

$$
\lvert\Lambda_B(\phi,\psi)\rvert
\le\int\sum_k\lvert\langle\phi\lvert\lambda,k\rangle\rvert\,\lvert\langle\lambda,k\lvert\psi\rangle\rvert\;d\mu
\le\lVert\phi\rVert\,\lVert\psi\rVert
$$

于是由 Riesz 表示，存在**有界算子** $T_B$（$\lVert T_B\rVert\le1$）使 $\langle\phi\lvert T_B\psi\rangle=\Lambda_B(\phi,\psi)$。它与 $E(B)$ 在 $\Phi\times\Phi$ 上相同，而 $\Phi$ 在 $\mathcal{H}$ 中稠密——**两个有界算子在一个稠密子集上相等，就相等**：

$$
E(B)=\int_B\sum_k\lvert\lambda,k\rangle\langle\lambda,k\rvert\;d\mu(\lambda)\tag{9}
$$

对 $B$ 取微元，得**算子值测度对 $\mu$ 的密度**（Radon–Nikodym）：

$$
dE(\lambda)=\sum_k\lvert\lambda,k\rangle\langle\lambda,k\rvert\,d\mu(\lambda)\tag{10}
$$

**（9）（10）都是弱等式**：两边要夹在 $\langle\phi\lvert\,\cdot\,\lvert\psi\rangle$ 里才是数。

**无简并时**（$k$ 只剩一项）退成 $dE=\lvert\lambda\rangle\langle\lambda\rvert\,d\mu$；再用 $\mu\to\rho\mu$、$\lvert\lambda\rangle\to\lvert\lambda\rangle/\sqrt{\rho}$ 的自由度把 $\mu$ 吸收成 $\mu_{\psi_0}$（$\psi_0$ 是循环矢量，即 [D01](D01-spectral-theorem.md) §5 的"谱简单"），就得到 D01 的对角化模型。**"无简并 + 谱简单"是把本卡接回 D01 的条件**；有重数时只能保留（10）的求和形式。

---

## 5. 它给什么

- $\lvert q\rangle$ **本身**：$[\hat q,f(\hat q)]$ 与 $\hat q$ 的谱分解都能写出来，靠的就是它；
- **本征矢族的存在性**——本卡只负责"存在"这一步；它如何特化成具体算子的本征方程、归一化如何定，都是下游的事；
- **狄拉克记号的下限**——$\langle q\lvert\psi\rangle=\psi(q)$ 是**求值泛函**，不是 $L^{2}$ 内积。

**具体画面**（"为什么必须扩大空间"的最短说明）：取 $\hat q$ 为 $L^{2}(\mathbb{R})$ 上"乘以 $q$"。则 $\lvert q\rangle$ 就是求值泛函 $\psi\mapsto\psi(q)$。它在 $L^{2}$ 上**不连续**（函数可在一点很高而范数很小），但在 Schwartz 空间 $\mathcal{S}$ 上连续——所以它住在 $\mathcal{S}^{\times}$ 里，不在 $\mathcal{H}$ 里。

---

## 6. 边界

1. **非自伴算子全都没有。** 谱定理要求自伴；非自伴只有"谱"这个较弱的对象，没有投影值测度，也没有广义本征矢系。这是整套量子力学要求可观测量自伴的**数学**理由，而不只是习惯。
2. **核性不可省。** 换成一般的稠密子空间，Gelfand–Maurin 可能失效。所以"随便找个稠密子空间就能定义 $\lvert q\rangle$"是错的。
3. **归一化依赖谱测度的密度。** 若 $d\mu=\rho(q)\,dq$，则 $\langle q\lvert q'\rangle=\delta(q-q')/\rho(q)$。平直空间 $\rho=1$，弯曲空间 $\rho=\sqrt{g}$——**这是弯曲空间里测度因子的数学出处**。
4. **重数大于 1 时要加标签。** （10）里的 $\sum_k$ 就是为此准备的：一个 $F_\lambda$ 覆盖不了重数，必须按本征子空间逐项相加，归一化变成 $\delta_{kk'}$。物理上就是自旋、味道、超选扇区。
5. **这张卡不做证明。** 本仓库不重推泛函分析；能推的是"给定这些定理，物理结论如何落地"。**引用与证明的界限要一直守住**。

---

## 7. 自检

- [ ] 用一句话说清谱定理与 Gelfand–Maurin 各负责什么
- [ ] 说出定理的两条结论（本征方程、完备性），以及每条各管什么
- [ ] 解释为什么连续谱时"Hilbert 空间里没有本征矢"
- [ ] 用"求值泛函"说明 $\lvert q\rangle$ 为什么不在 $\mathcal{H}$ 里
- [ ] 说明（4）为什么只对 $\Phi$ 成立
- [ ] 说明为什么 $E(B)\Phi\subseteq\Phi$ 不成立，并给出 $\hat q$ 的反例
- [ ] 说明（8）为什么不能由（3）推出（只对多项式成立）
- [ ] 用 $g_n(\hat A)$ 逼近把（9）的每一步推一遍，并说出"剥离"为什么需要 $\Phi$ 稠密
- [ ] 说明核空间条件为什么不可省，以及 $\mu$ 为什么不必是 Lebesgue
