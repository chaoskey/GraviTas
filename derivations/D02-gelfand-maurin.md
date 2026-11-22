# D02 · 核空间谱定理（Gelfand–Maurin）

> 建档 2026-11-18 · 类型：**引用卡**——Gelfand–Maurin 是外部数学，本卡只引用、不证明；本卡的任务是把它翻译进 Dirac 记号，并与 [D01](D01-spectral-theorem.md) 的投影值测度接上头
> 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)
> 下游：[D04](D04-position-eigen-equation.md)、[D05](D05-normalization-convention.md)、[D06](D06-functional-calculus.md)、[D07](D07-trace.md)、[D09](D09-diagonal-criterion.md)、[D10](D10-product-kernel.md)、[D17](D17-translation.md)、[D18](D18-qp-overlap.md)、[D19](D19-p-completeness.md)、[D20](D20-momentum-representation.md)、[D22](D22-path-integral-representation.md)、[D23](D23-trace-is-loop.md)、[D27](D27-energy-basis.md)
> 它补的是谱定理缺的那一半：**给"一族投影"，不给"一族矢"**。

---

**记号**：$\Phi\subset\mathcal{H}\subset\Phi^{\times}$ 是 Gelfand 三重空间（§1）；$F_{\lambda,k}\in\Phi^{\times}$ 是广义本征矢，$k$ 跑重数指标；$\mu$ 是谱上的**标量谱测度**；$E$、$dE$ 沿用 [D01](D01-spectral-theorem.md) 的投影值测度。$\langle F,\phi\rangle$ 记 $\Phi^{\times}\times\Phi$ 上的对偶括号：**对 $F$ 反线性、对 $\phi$ 线性**。

---

## 0. 问题：我们要"矢"，谱定理只给"投影"

谱定理说得清楚：自伴算子给一族**投影** $E(B)$。但物理上天天写的是 $\lvert q\rangle$——一个**矢**。

**它不在 $\mathcal{H}$ 里**：连续谱时 $E(\{q\})=\mathbb{0}$（[D01](D01-spectral-theorem.md) §3），所以**没有**平方可积的 $\psi$ 满足 $\hat q\psi=q\psi$。

**为什么不能从 D01 直接推出。** D01 给的是**抽象**的投影值测度 $E$；它不保证 $E$ 有密度 $\lvert F_\lambda\rangle\langle F_\lambda\rvert$，更不保证有本征矢——连续谱时 $\mathcal{H}$ 里根本没有。**这两样都要另外的定理，不是换积分符号能换出来的。**

**$\lvert q\rangle$ 不算错，只是它住在别处。** 出路是把空间扩大，让它有个合法的住处——这就是下面这一层。

---

## 1. Gelfand 三重空间（装备希尔伯特空间）

$$
\Phi\;\subset\;\mathcal{H}\;\subset\;\Phi^{\times}
$$

也叫**装备希尔伯特空间**（rigged Hilbert space），或**Gelfand 三重空间**。

| 层 | 是什么 | 角色 |
|---|---|---|
| $\Phi$ | 核空间（典型：Schwartz 函数 $\mathcal{S}(\mathbb{R})$） | **测试探针**：好到"取值"有意义 |
| $\mathcal{H}$ | 真正的 Hilbert 空间 | **态**：平方可积 |
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

存在一族**非零**的 $F_{\lambda,k}\in\Phi^{\times}$（$k$ 跑重数指标），使每个 $\lambda\in\sigma(\hat A)$（$\mu$-**几乎处处**）都满足

$$
\hat A F_{\lambda,k}=\lambda F_{\lambda,k}\tag{2}
$$

**"几乎处处"是对 $\mu$ 说的**：$\mu$ 就是下面结论二里那个标量谱测度。**测度为零的那些点上定理不作承诺**——而下面每一个积分都在零测集上取值为零，所以承诺的范围与用到的范围正好一样。

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

**（4）是压缩写法。** 定理的完备性对**每个 Borel 集** $B$ 都成立（定理原文是对连续紧支撑函数说的，取 $f=\mathbf{1}_B$、由单调类延拓即得）：

$$
\langle\phi\lvert E(B)\psi\rangle
=\int_{\sigma(\hat A)}\mathbf{1}_B(\lambda)\sum_k F_{\lambda,k}(\phi)\,\overline{F_{\lambda,k}(\psi)}\;d\mu(\lambda)
\tag{4'}
$$

**取 $B=\sigma(\hat A)$（此时 $E(B)=\mathbb{1}$、$\mathbf{1}_B\equiv1$）就还回（4）**——**两者是同一句话，不是两条定理**。**§4 用的就是 $B$ 那一次**：只写（4）那一次不够，它只给出"总质量" $\langle\phi\lvert\psi\rangle$，**含不下"局部"的信息**，而那正是 $E(B)$ 要的东西。

---

## 3. 翻译成 Dirac 记号

**对应关系**：

$$
F_{\lambda,k}\equiv\lvert\lambda,k\rangle,
\qquad
F_{\lambda,k}(\phi)\equiv\langle\phi\lvert\lambda,k\rangle
$$

### 3.1 $\lvert\lambda,k\rangle$ 与 $\langle\lambda,k\rvert$ 是同一个元素

$\Phi^{\times}$ 是按"$\Phi$ 上的连续反线性泛函"**定义**出来的，所以它的元素**既是矢量**（可加、可被 $\hat A$ 转置作用），**又是泛函**（可在 $\phi\in\Phi$ 上取值）。$\lvert\lambda,k\rangle$ 是把它当矢量写，$\langle\lambda,k\rvert$ 是把它当泛函写——**不是两个空间里的两个矢**。

**两副身份之间只有一条翻译公式**：

$$
\langle\lambda,k\lvert\psi\rangle=\overline{\langle\psi\lvert\lambda,k\rangle}
=\overline{F_{\lambda,k}(\psi)},\qquad \psi\in\Phi
$$

**（4）里的共轭就是这条**：$F(\phi)\,\overline{F(\psi)}$ 换成 Dirac 记号，正好是 $\langle\phi\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle$。

**$\langle\lambda,k\rvert$ 只能吃 $\Phi$ 里的东西**，不能吃 $\Phi^{\times}$ 里的——所以 $\langle\lambda,k\lvert\lambda',k'\rangle$ 严格说**没有定义**，它只是 $\delta_{kk'}\delta(\lambda-\lambda')$ 的简写（见 §7 第 3 条）。

### 3.2 三个式子的 Dirac 形式

$$
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

### 3.3 两个等价形式

在弱拓扑意义下，（4）还可写成"态展开"与"完备性"两种样子：

$$
\begin{aligned}
& \lvert\psi\rangle=\int_{\sigma(\hat A)}\sum_k\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle\;d\mu(\lambda)
&&\text{态展开}\\
\Longleftrightarrow\quad
& \mathbb{1}=\int_{\sigma(\hat A)}\sum_k\lvert\lambda,k\rangle\langle\lambda,k\rvert\;d\mu(\lambda)
&&\text{完备性}
\end{aligned}\tag{5}
$$

**"完备性"这个名称是准确的**：$\mathbb{1}$ 被拆成一族外积的积分，说明这族矢量"铺满"了空间——**但（5）只在 $\Phi$ 上取二次型时是有数的等式**，理由同在（4）后面。

**（4′）写成 Dirac 记号**就是

$$
\langle\phi\lvert E(B)\psi\rangle
=\int_{\sigma(\hat A)}\mathbf{1}_B(\lambda)\sum_k\langle\phi\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle\;d\mu(\lambda)
$$

**§4 就从它出发。**

---

## 4. 接头：$E(B)$ 与 $dE$ 的密度

D01 给的是**算子级**的 $E$，D02 给的是**标量级**的 $\mu$。两者怎么对上，是这一节要回答的。

### 4.1 第一步：$\mathbf{1}_B(\hat A)=E(B)$

取指示函数 $\mathbf{1}_B$（只取 $0$、$1$，有界）：

$$
\mathbf{1}_B(\lambda)=
\begin{cases}
1, & \lambda\in B\\
0, & \lambda\notin B
\end{cases}
$$

由 [D01](D01-spectral-theorem.md) §1 的函数演算、§2 的 $E(\sigma(\hat A))=E(\mathbb{R})$、§4 的乘法规则：

$$
\mathbf{1}_B(\hat A)
=\int_{\sigma(\hat A)}\mathbf{1}_B\,dE
=E\bigl(\sigma(\hat A)\cap B\bigr)
=E(\sigma(\hat A))\,E(B)
=\mathbb{1}\,E(B)
=E(B)
$$

**这是后面每一步的入口**：$E(B)$ 就是 $\mathbf{1}_B$ 这个函数在 $\hat A$ 上的取值。

### 4.2 第二步：代进（4′）的 Dirac 形式

$$
\langle\phi\lvert E(B)\psi\rangle
=\int_{B}\sum_k\langle\phi\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle\;d\mu(\lambda)
$$

**右边的积分只在 $B$ 上**，因为 $\mathbf{1}_B$ 在 $B$ 外为零。

### 4.3 第三步：剥离测试探针

右边对每个固定的 $B$ 是 $\phi,\psi$ 上的**有界**二次型（因为 $\lvert\mathbf{1}_B\rvert\le1$，其模不超过 $\lVert\phi\rVert\lVert\psi\rVert$）。于是：

- 由 Riesz 表示，存在**有界算子** $T_B$，使 $\langle\phi\lvert T_B\psi\rangle$ 等于右边；
- $T_B$ 与 $E(B)$ 在 $\Phi\times\Phi$ 上一致，而 $\Phi$ 在 $\mathcal{H}$ 中稠密——**两个有界算子在一个稠密子集上相等，就相等**。

$$
\boxed{\;E(B)=\int_{B}\sum_k\lvert\lambda,k\rangle\langle\lambda,k\rvert\;d\mu(\lambda)\;}
$$

### 4.4 第四步：写成密度

对 $B$ 取微元，得**算子值测度对 $\mu$ 的密度**：

$$
dE(\lambda)=\sum_k\lvert\lambda,k\rangle\langle\lambda,k\rvert\,d\mu(\lambda)\tag{8}
$$

**（8）是弱等式，不是算子等式**：两边都要夹在 $\langle\phi\lvert\,\cdot\,\lvert\psi\rangle$ 里才是数。等价地说，对每个 $\phi,\psi\in\Phi$，测度 $\langle\phi\lvert E(\cdot)\lvert\psi\rangle$ 关于 $\mu$ **绝对连续**，Radon–Nikodym 导数正是 $\sum_k\langle\phi\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle$。

---

## 5. 无简并时回到单矢形式

**若每个本征值都只有一重**（无简并），$k$ 只剩一项，（8）变成

$$
dE(\lambda)=\lvert\lambda\rangle\langle\lambda\rvert\,d\mu(\lambda),
\qquad
E(B)=\int_{B}\lvert\lambda\rangle\langle\lambda\rvert\;d\mu(\lambda)
$$

**这就是 D01 §5 对角化模型里的那个 $\hat A$**：在那里 $\mathcal{H}\cong L^{2}\bigl(\sigma(\hat A),d\mu_{\psi_0}\bigr)$，$E(B)$ 是乘以 $\mathbf{1}_B$，$\lvert\lambda\rangle$ 是"$\lambda$ 点"的 $\delta$-归一化基。

**$\mu$ 可以取成 $\mu_{\psi_0}$**（$\psi_0$ 是循环矢量，即 D01 §5 的"谱简单"）：$\mu$ 本身不唯一——$\mu\to\rho\,\mu$、同时 $\lvert\lambda\rangle\to\lvert\lambda\rangle/\sqrt{\rho}$（$\rho>0$），（8）不变；用这个自由度把密度 $\lvert\langle\lambda\lvert\psi_0\rangle\rvert^{2}$ 吸收掉，就得到 $\mu=\mu_{\psi_0}$。

**所以"无简并 + 谱简单"是把 D02 接回 D01 的条件**；有重数时只能保留（8）的求和形式。

---

## 6. 它给什么

- $\lvert q\rangle$ **本身**：$[\hat q,f(\hat q)]$ 与 $\hat q$ 的谱分解都能写出来，靠的就是它；
- **本征矢族的存在性**——本卡只负责"存在"这一步；它如何特化成具体算子的本征方程、归一化如何定，都是下游的事；
- **狄拉克记号的下限**——$\langle q\lvert\psi\rangle=\psi(q)$ 是**求值泛函**，不是 $L^{2}$ 内积。

**具体画面**（"为什么必须扩大空间"的最短说明）：取 $\hat q$ 为 $L^{2}(\mathbb{R})$ 上"乘以 $q$"。则 $\lvert q\rangle$ 就是求值泛函 $\psi\mapsto\psi(q)$。它在 $L^{2}$ 上**不连续**（函数可在一点很高而范数很小），但在 Schwartz 空间 $\mathcal{S}$ 上连续——所以它住在 $\mathcal{S}^{\times}$ 里，不在 $\mathcal{H}$ 里。

---

## 7. 边界

1. **非自伴算子全都没有。** 谱定理要求自伴；非自伴只有"谱"这个较弱的对象，没有投影值测度，也没有广义本征矢系。这是整套量子力学要求可观测量自伴的**数学**理由，而不只是习惯。
2. **核性不可省。** 换成一般的稠密子空间，Gelfand–Maurin 可能失效。所以"随便找个稠密子空间就能定义 $\lvert q\rangle$"是错的。
3. **归一化依赖谱测度密度。** 若 $d\mu=\rho(q)\,dq$，则 $\langle q\lvert q'\rangle=\delta(q-q')/\rho(q)$。平直空间 $\rho=1$，弯曲空间 $\rho=\sqrt{g}$——**这是弯曲空间里测度因子的数学出处**。
4. **重数大于 1 时要加标签。** （8）里的 $\sum_k$ 就是为此准备的：一个 $F_\lambda$ 覆盖不了重数，必须按本征子空间逐项相加，归一化变成 $\delta_{kk'}$。物理上就是自旋、味道、超选扇区。
5. **这张卡不做证明。** 本仓库不重推泛函分析；能推的是"给定这些定理，物理结论如何落地"。**引用与证明的界限要一直守住**。

---

## 8. 自检

- [ ] 用一句话说清谱定理与 Gelfand–Maurin 各负责什么
- [ ] 说出定理的两条结论（本征方程、完备性），以及每条各管什么；再说清 $g$ 版为什么不是第三条
- [ ] 解释为什么连续谱时"Hilbert 空间里没有本征矢"
- [ ] 用"求值泛函"说明 $\lvert q\rangle$ 为什么不在 $\mathcal{H}$ 里
- [ ] 说明（4）为什么只对 $\Phi$ 成立
- [ ] 说清 $\lvert\lambda,k\rangle$ 与 $\langle\lambda,k\rvert$ 是同一个元素，以及唯一的翻译公式
- [ ] 从（4）的 $B$ 版推出（8），并说清"剥离"为什么需要 $\Phi$ 稠密
- [ ] 说明核空间条件为什么不可省
