# D05 · 函数演算与位置表象下的积分核

> 建档 2026-11-06 · 类型：**定义 + 定理 + 判据**——三组命题共用一套符号：函数演算、位置表象的核、对角与乘积
> 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)（§1 谱分解定义与范数公式、§4 投影乘法律）、[D02](D02-gelfand-maurin.md)（§3 完备性、§4 外积密度）、[D04](D04-position-eigen-equation.md)（§2 尺度选择、§3 谱分解与完备性、§4 $\delta$ 归一）
> 下游：[D06](D06-exponential-map-and-bch.md)、[D08](D08-commutator-p-fq.md)、[D09](D09-weyl-phase.md)、[D11](D11-translation.md)、[D12](D12-qp-overlap.md)、[D15](D15-hamiltonian.md)、[D16](D16-path-integral-representation.md)、[D21](D21-energy-basis.md)

---

## 0. 命题

本卡把三组彼此咬合的结论放在一处：**函数演算给出"算子怎么被函数作用"，核给出"这个算子在位置表象里长什么样"，对角判据与乘积核给出"这个表格的代数"**。

| 组 | 内容 | 逻辑地位 |
|---|---|---|
| 甲 | $f(\hat A)$ 的两种定义（幂级数、谱分解）＋ 一种特化（本征基展开） | **定义**（特化不是独立定义） |
| 甲 | 两种定义在解析函数上一致 | **定理**（§1.4） |
| 甲 | $\sigma\bigl(f(\hat A)\bigr)=f\bigl(\sigma(\hat A)\bigr)$ | **定理**（§2.2） |
| 乙 | 核 $K_A(q,q')\equiv\langle q\lvert\hat A\lvert q'\rangle$ 与它的双线性配对 | **定义**（§3.1） |
| 丙 | $\bigl[\hat q,f(\hat q)\bigr]=\mathbb{0}\Rightarrow K_{f(\hat q)}(q',q'')=f(q')\delta(q'-q'')$ | **判据**（§4） |
| 丙 | $K_{AB}(q',q'')=\int K_A(q',q)K_B(q,q'')\,dq$ | **定理**（§5.1） |

**它在讲什么**：量子力学里的"算子"有两副面孔——抽象的谱积分，和位置表象里的双变量分布。本卡证明这两副面孔是同一件事，并给出**在位置表象里做算子代数**的两条规则（对角判据、乘积核）。下游所有"插入完备性"的计算，用的都是这两条。

**适用条件**：$\hat A$ 自伴（甲组全部）；$\hat q$ 的本征矢已按 [D04](D04-position-eigen-equation.md) §2 选定 $d\mu=dq$（乙、丙组）。

---

## 1. 函数演算：两种定义、一种特化、一条定理

**先给结论**，免得把四件事混成一类：

| 写法 | 逻辑地位 | 依赖 | 覆盖范围 |
|---|---|---|---|
| 1.1 幂级数 | **定义**（独立） | 只要算子的乘与加 | 解析函数 |
| 1.2 谱分解 | **定义（典范）** | [D01](D01-spectral-theorem.md) 谱定理 | Borel 函数 |
| 1.3 本征基展开 | **特化**，不是独立定义 | [D01](D01-spectral-theorem.md)、[D04](D04-position-eigen-equation.md) | 简单谱 + 密度为 $1$ |
| 1.4 两者一致 | **定理** | 1.1、1.2 | 交集（解析函数） |

### 1.1 幂级数（解析函数）

$$
f(\hat A)\equiv\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}\,\hat A^{n}\tag{1}
$$

**这是一个定义**——不需要谱定理，只需要算子能相乘相加、级数能收敛。这是它与 1.2 并列的唯一理由。

- $\hat A$ **有界**时，只要 $\lVert\hat A\rVert<R$（$R$ 为收敛半径），级数按算子范数绝对收敛；
- $\hat A$ **无界**时，级数只是形式记号，严格定义要靠解析向量上的强收敛延拓。

**局限**：只覆盖解析函数。$1/x$、$\sqrt{x}$、$\ln x$、$e^{-1/x^{2}}$ 都不在其中。

### 1.2 谱分解（最一般）

**定义、定义域与范数公式全在 [D01](D01-spectral-theorem.md) §1**，此处只借用：

$$
f(\hat A)\equiv\int_{\sigma(\hat A)}f(\lambda)\;dE(\lambda)\tag{2}
$$

与 1.1 的差别只有两条：需要先有谱定理（$E$ 由 $\hat A$ 唯一确定），所以是"典范"的那个；但它覆盖**全部** Borel 函数。

### 1.3 本征基展开（谱简单时）

这是 [D04](D04-position-eigen-equation.md) §3 的谱分解在一般简单谱上的写法：

$$
f(\hat A)=\int da\;f(a)\,\lvert a\rangle\langle a\rvert\tag{3}
$$

**它不是独立的定义**，是 (2) 把 $dE$ 换成 $\lvert a\rangle\langle a\rvert da$ 的特化。"密度为 $1$"是一次尺度选择（[D04](D04-position-eigen-equation.md) §2），换成 $\rho\,da$ 则展开同乘 $1/\rho$。

### 1.4 两者为什么一致（这是一条定理）

**要证**：对解析 $f$（收敛半径 $R>\lVert\hat A\rVert$），(1) 与 (2) 给出同一个算子。

**第一步：矩性质 ⇒ 多项式逐项相等。**

谱分解定义只直接给出 $n=1$（即 $\hat A=\int\lambda\,dE$）；$n\ge2$ 要靠**函数版乘法律**

$$
\Bigl(\int f\,dE\Bigr)\Bigl(\int g\,dE\Bigr)=\int fg\,dE
$$

它分三层成立，每层只靠一样东西：

| 层 | 靠什么 |
|---|---|
| 指示函数 $f=\mathbf{1}_B$ | [D01](D01-spectral-theorem.md) §4 的 $E(B)E(B')=E(B\cap B')$ |
| 简单函数 | 积分的线性 |
| 一般 $f,g$ | 有界一致逼近 ＋ 保范（[D01](D01-spectral-theorem.md) §1 的范数形式） |

取 $f=g=\mathrm{id}$ 重复 $n$ 次，得**矩性质**

$$
\int\lambda^{n}\,dE(\lambda)=\hat A^{n}
$$

**它在说什么**：乘方只作用在**权重** $\lambda$ 上，不作用在**投影** $E$ 上。于是对多项式 $p$，$\int p\,dE=p(\hat A)$——**这一步不需要任何极限论证**。

**第二步：把"逐项相等"抬到"极限相等"。**

关键是**保范**：$\lVert\int g\,dE\rVert=\sup_{\sigma(\hat A)}\lvert g\rvert$（[D01](D01-spectral-theorem.md) §1）。它保证 $g_N\to g$ 在谱上一致收敛时，$\int g_N\,dE\to\int g\,dE$ 按范数收敛。

- **谱侧**：$\sigma(\hat A)\subseteq[-\lVert\hat A\rVert,\lVert\hat A\rVert]$，而 $R>\lVert\hat A\rVert$，故 $\sup_{\sigma}\lvert f-p_N\rvert\to0$；由保范，$\int p_N\,dE\to\int f\,dE$。
- **代数侧**：同一条件 $\lVert\hat A\rVert<R$ 保证 $\sum c_n\hat A^{n}$ 按范数收敛，其部分和正是 $p_N(\hat A)$。

部分和恒等（第一步），两边都收敛（第二步），故极限相同。**证毕。**

**一句话**：多项式上逐项相等 ＋ 有界函数演算保范 $\Rightarrow$ 极限上相等。**两条缺一不可**：没有保范，一致收敛传不过去；没有逐项相等，起点就断了。

**边界**：这套论证用算子范数与谱上的 $\sup$，直接结论只对**有界** $\hat A$ 成立；无界时一致性要在解析向量上逐点成立。

---

## 2. 运算性质与谱映射定理

### 2.1 一条已证、一条直接得到

| 性质 | 内容 | 为什么"直接" |
|---|---|---|
| 同态 | $(fg)(\hat A)=f(\hat A)\,g(\hat A)$ | 就是 §1.4 第一步的函数版乘法律 |
| 与自变量对易 | $[f(\hat A),\hat A]=\mathbb{0}$ | 两者用同一族投影 $E$，投影互相交换 |

**注意同态只对同一个算子的函数成立**——$f(\hat A)g(\hat B)\neq g(\hat B)f(\hat A)$，除非 $\hat A,\hat B$ 对易。

### 2.2 谱映射定理

**命题**：$f$ 连续时，

$$
\sigma\bigl(f(\hat A)\bigr)=f\bigl(\sigma(\hat A)\bigr)\tag{4}
$$

**包含"$\subseteq$"**：设 $\lambda_0\notin f(\sigma(\hat A))$，则 $g(\lambda)\equiv1/\bigl(f(\lambda)-\lambda_0\bigr)$ 在 $\sigma(\hat A)$ 上有界（连续函数在紧集上），由 §1.2 与 [D01](D01-spectral-theorem.md) §1 的范数公式，$g(\hat A)$ 有界，且

$$
g(\hat A)\,\bigl(f(\hat A)-\lambda_0\mathbb{1}\bigr)=\mathbb{1}
$$

故 $\lambda_0\mathbb{1}-f(\hat A)$ 有有界逆，$\lambda_0\notin\sigma(f(\hat A))$。

**包含"$\supseteq$"**：设 $\lambda_0=f(\lambda_1)$，$\lambda_1\in\sigma(\hat A)$。取一列 $\lambda_n\to\lambda_1$，则 $f(\lambda_n)\to\lambda_0$；若 $\lambda_0$ 在预解集中，用连续性可把 $\bigl(f(\hat A)-\lambda_0\bigr)^{-1}$ 搬到 $\bigl(\hat A-\lambda_1\bigr)^{-1}$ 上，与 $\lambda_1\in\sigma(\hat A)$ 矛盾。**证毕。**

### 2.3 两条判据：由谱映射直接读出

| 判据 | 内容 |
|---|---|
| 自伴 | $f(\hat A)$ 自伴 $\iff$ $f$ 在 $\sigma(\hat A)$ 上取实值 |
| 酉 | $f(\hat A)$ 酉 $\iff$ $\lvert f\rvert=1$ 在 $\sigma(\hat A)$ 上 |

**这两条不是新定理**：代进 (4) 就得到。最有用的推论是：$\hat A$ 自伴 $\Rightarrow$ 对任意实数 $\alpha$，$e^{i\alpha\hat A}$ 是酉算子——**这是一切酉变换的发动机**。

---

## 3. 位置表象下的积分核

### 3.1 定义：连续谱下的"矩阵元表格"

离散正交归一基下，算子 $\hat A$ 的全部信息装在二指标表格 $A_{mn}=\langle m\lvert\hat A\lvert n\rangle$ 里。到连续的位置基 $\{\lvert q\rangle\}$，离散指标变成连续实变量，表格升级为双变量分布——**积分核**：

$$
K_A(q,q')\equiv\langle q\lvert\hat A\lvert q'\rangle\tag{5}
$$

严格地说，$K_A$ 是使

$$
\langle\phi\lvert\hat A\lvert\psi\rangle=\iint_{\mathbb{R}^{2}}\overline{\phi(q)}\,K_A(q,q')\,\psi(q')\,dq\,dq'\tag{6}
$$

对**任意** $\phi,\psi\in\Phi=\mathcal{S}(\mathbb{R})$ 都成立的分布（在左右各插入一次 [D04](D04-position-eigen-equation.md) §3 的完备性即得）。由 (6) 同时读出算子作用在波函数上的积分变换：

$$
(\hat A\psi)(q)=\langle q\lvert\hat A\lvert\psi\rangle=\int_{\mathbb{R}}K_A(q,q')\,\psi(q')\,dq'\tag{7}
$$

**给定 $\hat A$，核唯一**——(6) 对全体测试函数成立，而分布由它在全体探针上的配对值唯一决定。

### 3.2 三个基本例子

| $\hat A$ | 核 $K_A$ | 代入 (6) 后 |
|---|---|---|
| $\mathbb{1}$ | $\delta(q-q')$ | 退化成 $\int\overline{\phi(q)}\psi(q)\,dq$ |
| $\hat q$ | $q\,\delta(q-q')$ | 退化成 $\int q\,\overline{\phi(q)}\psi(q)\,dq$ |
| $E(B)$ | $\mathbf{1}_B(q)\,\delta(q-q')$ | 退化成 $\int_B\overline{\phi(q)}\psi(q)\,dq$ |

**三行靠同一件事**：$\delta$ 把 $q'$ 钉在 $q$ 上，于是 $q'$ 处的算子像变成 $q$ 处的标量。**第一行还说明**：$\langle q\lvert q'\rangle$ 不是内积，而是**恒等算子的核** $K_{\mathbb{1}}$；它在 (7) 中必须是 $\delta$，因为只有 $\delta$ 能把波函数原封不动地还回来。

### 3.3 共同规律：都是局部乘法算子

$\mathbb{1}$、$\hat q$、$E(B)$ 都不把不同位置 $q\neq q'$ 的波函数混在一起，所以核都正比于 $\delta(q-q')$。这不是巧合，下一节把它写成判据。

**核随基矢尺度变，物理不变**：若 $\lvert q\rangle\to\lambda\lvert q\rangle$，则核整体乘 $\lvert\lambda\rvert^{2}$，同时完备性权重按 [D04](D04-position-eigen-equation.md) §2 反向改。两者一起换，所有可观测量不变——核只影响中间步骤的系数，不是物理内容。

---

## 4. 对角判据

**命题**：对任意只含 $\hat q$ 的算子 $f(\hat q)$，

$$
\bigl[\hat q,f(\hat q)\bigr]=\mathbb{0}\tag{8}
$$

且它在位置表象下的核必然对角：

$$
K_{f(\hat q)}(q',q'')=\langle q'\lvert f(\hat q)\lvert q''\rangle=f(q')\,\delta(q'-q'')\tag{9}
$$

**它在讲什么**：与 $\hat q$ 对易 $\iff$ 在 $q$ 基下对角；对角算子的核必然是"一个函数乘以 $\delta$"。

**(8) 的方向**：由 §2.1 的同态与"与自变量对易"，$f(\hat q)$ 与 $\hat q$ 对易是**已证的**。下面两条路线把反向的约束——核长什么样——逼出来。

### 4.1 路线一：由位置基展开直接读出

由 [D04](D04-position-eigen-equation.md) §3 的谱分解 $f(\hat q)=\int f(q)\lvert q\rangle\langle q\rvert\,dq$，左右夹上 $\langle q'\lvert$ 与 $\lvert q''\rangle$，并用 [D04](D04-position-eigen-equation.md) §4 的 $\langle q'\lvert q\rangle=\delta(q'-q)$：

$$
\langle q'\lvert f(\hat q)\lvert q''\rangle
=\int f(q)\,\delta(q'-q)\,\delta(q-q'')\,dq
=f(q')\,\delta(q'-q'')
$$

### 4.2 路线二：由对易子逼出 $\delta$ 核

**不假定 $f(\hat q)$ 已写成积分展开**，只用 (8)。对任意 $q',q''$：

$$
\begin{aligned}
0&=\bigl\langle q'\bigr\lvert\bigl[\hat q,f(\hat q)\bigr]\bigl\lvert q''\bigr\rangle\\
&=\bigl(\langle q'\lvert\hat q\bigr)f(\hat q)\lvert q''\rangle-\langle q'\lvert f(\hat q)\bigl(\hat q\lvert q''\rangle\bigr)\\
&=q'\langle q'\lvert f(\hat q)\lvert q''\rangle-q''\langle q'\lvert f(\hat q)\lvert q''\rangle\\
&=(q'-q'')\,\langle q'\lvert f(\hat q)\lvert q''\rangle
\end{aligned}
$$

**第 3 行两项的来源并不对称**：右项取出 $q''$ 直接用了 [D04](D04-position-eigen-equation.md) §1 的右矢本征方程；左项能取出实数 $q'$，**依赖 $\hat q$ 自伴**（[D00](D00-commutator-axiom.md) §0）——取伴随并用谱值 $q'\in\mathbb{R}$，才得到左矢版本 $\langle q'\lvert\hat q=q'\langle q'\lvert$。这一步不能省。

记 $T(q',q'')\equiv\langle q'\lvert f(\hat q)\lvert q''\rangle$，(9) 之前的分布方程为

$$
(q'-q'')\,T(q',q'')=0\tag{10}
$$

- $q'\neq q''$ 时可除以非零实数，得 $T=0$——**对角线之外处处为零**；
- $q'=q''$ 时系数为零，方程不加限制——支撑集中在对角线上。

**为什么只能是 $\delta$，不能是 $\delta'$**：$x\,\delta(x)=0$ 符合 (10)；而分部积分给出 $x\,\delta'(x)=-\delta(x)\neq0$，违反 (10)。所以对角线上只能放 $\delta$ 本身。

于是 $T=c(q')\delta(q'-q'')$；再把 $f(\hat q)\lvert q''\rangle=f(q'')\lvert q''\rangle$ 左乘 $\langle q'\lvert$，得 $c(q')=f(q')$。**证毕。**

**为什么这条路更根本**：它把"对角"归因于**对易**，而不是"$f$ 长什么样"。所以对不可微、不可展开的 $f$ 也成立。

### 4.3 两条推论

**推论一：$f(q')$ 与 $f(q'')$ 可互换。** 因为它们后面乘着 $\delta(q'-q'')$，在支撑集 $q'=q''$ 上两者作为分布**精确相等**，不存在任何近似。

**推论二：作用在波函数上就是乘法。** 把 (9) 代入 (7)：

$$
\bigl(f(\hat q)\psi\bigr)(q)=\int f(q)\,\delta(q-q')\,\psi(q')\,dq'=f(q)\,\psi(q)\tag{11}
$$

这把 [D04](D04-position-eigen-equation.md) §5 的 $(\hat q\psi)(q)=q\psi(q)$ 推广到 $\hat q$ 的任意函数——例如势能 $V(\hat q)$ 或它的指数 $e^{-\varepsilon V(\hat q)}$。

---

## 5. 算子乘积的积分核

### 5.1 合成公式

$K_A$、$K_B$ 已知，$\hat A\hat B$ 的核怎么算？在两者之间插入 [D04](D04-position-eigen-equation.md) §3 的完备性：

$$
\hat A\hat B=\hat A\Bigl(\int\lvert q\rangle\langle q\rvert\,dq\Bigr)\hat B
$$

两边左乘 $\langle q'\lvert$、右乘 $\lvert q''\rangle$：

$$
K_{AB}(q',q'')=\langle q'\lvert\hat A\hat B\lvert q''\rangle
=\int_{\mathbb{R}}\langle q'\lvert\hat A\lvert q\rangle\,\langle q\lvert\hat B\lvert q''\rangle\,dq
=\int_{\mathbb{R}}K_A(q',q)\,K_B(q,q'')\,dq\tag{12}
$$

**它就是离散矩阵乘法 $\sum_k A_{ik}B_{kj}$ 的连续版本**：求和指标 $k$ 换成连续中间位置 $q$。**顺序不可颠倒**——$\hat A\hat B$ 与 $\hat B\hat A$ 的核一般不同。

**自洽性**：取 $\hat A=f(\hat q)$、$\hat B=g(\hat q)$，代入 (9)：

$$
\int f(q')\,\delta(q'-q)\,g(q)\,\delta(q-q'')\,dq=f(q')g(q')\,\delta(q'-q'')=K_{(fg)(\hat q)}(q',q'')
$$

恰好还原 §2.1 的同态乘法律。

### 5.2 推广到 $N$ 重乘积

把 (12) 的插入重复 $N-1$ 次（记 $q_0\equiv q_i$、$q_N\equiv q_f$）：

$$
\langle q_f\lvert\hat A_N\hat A_{N-1}\cdots\hat A_1\lvert q_i\rangle
=\int_{\mathbb{R}^{N-1}}\Bigl(\prod_{k=1}^{N-1}dq_k\Bigr)\prod_{k=0}^{N-1}\langle q_{k+1}\lvert\hat A_{k+1}\lvert q_k\rangle\tag{13}
$$

**每插入一次就多一个"中途位置快照"**：整体的核拆成每一小步的核的乘积，再对所有中间位置积分。取 $N\to\infty$，这些中途位置连成一条路径——这是下游"切片"构造的全部代数内容。

---

## 6. 一致性检验

| 检验 | 结果 |
|---|---|
| $f(\lambda)=1,\ \lambda,\ \lambda^{n}$ | 三个定义都给 $\mathbb{1}$、$\hat A$、$\hat A^{n}$ ✅ |
| $f(\lambda)=e^{i\lambda}$，$\hat A$ 自伴 | $\lvert e^{i\lambda}\rvert=1$，故 $e^{i\hat A}$ 酉 ✅ |
| $f(\lambda)=1$ 的核 | $K_{\mathbb{1}}=\delta(q'-q'')$，与 §3.2 第一行一致 ✅ |
| $f=\hat q$ 的核 | $q'\delta(q'-q'')$，与 §3.2 第二行一致 ✅ |
| $f$ 取复值 | 核 $f(q')\delta(q'-q'')$ 仍是分布但不再实——与 §2.3 的自伴判据一致 ✅ |
| $A=B=\mathbb{1}$ 代入 (12) | 右端 $\int\delta(q'-q)\delta(q-q'')dq=\delta(q'-q'')$ ✅ |
| 不解析的 $f$（如阶跃） | 路线二仍成立；路线一与 §1.2 要求 Borel 可测 ✅ |

---

## 7. 备注与边界

1. **自伴是前提。** 非自伴算子没有谱定理，只能用 Dunford 演算，且只对谱点附近解析的函数有定义。**这一条决定了整套量子力学为什么要求可观测量自伴。**
2. **幂级数定义不能推得太远。** $1/\hat A$、$\sqrt{\hat A}$、$\ln\hat A$ 都要走谱分解；用幂级数硬写会发散或给出错误结果。
3. **$f'(\hat A)$ 是对函数求导**，不是"对算子求导"。
4. **同态只对同一个算子的函数成立。** 两套函数演算要合并，必须先证 $\hat A,\hat B$ 对易。
5. **核依赖基矢尺度**：$\lvert q\rangle\to\lambda\lvert q\rangle$ 时核乘 $\lvert\lambda\rvert^{2}$，权重反向改——它是中间系数，不是物理内容。
6. **弯曲空间核带 $1/\rho$**：若 $d\mu=\rho(q)dq$，则 $K_{\mathbb{1}}=\delta(q-q')/\rho(q)$，其余例子同乘该因子（[D04](D04-position-eigen-equation.md) §2、§7）。
7. **离散谱与多分量**：纯点谱时 $\delta(q-q')\to\delta_{nn'}$、积分变求和；有内部自由度时 $\langle q,i\lvert q',j\rangle=\delta_{ij}\delta(q-q')$。
8. **连续谱时 (6) 与 (12) 是分布等式**，要在分布意义下读；收敛性取决于算子的性质（两者有界时无问题）。
9. **不能反过来用**：核对角不意味着算子是 $\hat q$ 的函数（同一表象下不会，换表象时要注意）。
10. **动量基那一侧**属下游：核的定义对任何连续基都成立，但换到 $p$ 基要用 $\langle q\lvert p\rangle=e^{ipq}$。

---

## 8. 自检

- [ ] 说出哪两个是定义、哪个只是特化，各需要什么前提
- [ ] 复述一致性的两步：多项式逐项相等、保范性把极限抬上去
- [ ] 用谱映射证明 $\hat A$ 自伴 $\Rightarrow$ $e^{i\alpha\hat A}$ 酉
- [ ] 写出核的定义 (5)(6)，并说明 $\langle q\lvert q'\rangle$ 是哪个算子的核
- [ ] 用对易子论证写出 (9)，并说明为什么不需要 $f$ 解析
- [ ] 说明为什么对角线上只能放 $\delta$、不能放 $\delta'$
- [ ] 用一行导出 (12)，并说明它"就是"矩阵乘法
- [ ] 说明 $[\hat q,f(\hat q)]=0$ 与 $[\hat p,f(\hat q)]=-if'$ 为什么不矛盾
