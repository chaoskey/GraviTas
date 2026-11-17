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

**记号**：$\mathcal{H}$ 是复希尔伯特空间（后面称"态空间"）；$\psi,\phi\in\mathcal{H}$ 是它的矢量，$\lVert\psi\rVert$ 是范数；$E(B)$ 是 $\mathcal{H}$ 上的正交投影；$D(\hat A)$ 记 $\hat A$ 的定义域；$\mathbb{1}$ 是恒等算子。

**本卡里的 $\psi$ 只是"任意矢量"**，用来定义标量测度 $\mu_\psi(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$；**"态"是下游的概念，本卡不预设。**

### 1.1 陈述

**一句话**：自伴算子可以写成——**把一族互相垂直、合起来是恒等的投影，按取自谱的权重加起来**。
$$
\hat A=\int_{\sigma(\hat A)}\lambda\;dE(\lambda)
$$

**先把 $E$ 说清楚。** $E$ 是**投影值测度**：把每个 **Borel 集**（从开区间出发，反复做"可数次并、交、补"能得到的所有集合）$B$ 映成一个**投影** $E(B)$，并且

- **$E(\mathbb{R})=\mathbb{1}$**（全集对应整个空间）；
- **可数可加**：两两不交的 $B_1,B_2,\dots$ 满足 $E\bigl(\bigcup_nB_n\bigr)=\sum_nE(B_n)$。

**"可数可加"里的"相加"要说明**：右边的和**不是按范数收敛**，而是**强收敛**——部分和

$$
S_N=\sum_{n\le N}E(B_n)=E\Bigl(\bigcup_{n\le N}B_n\Bigr)
$$

**本身是投影**，且 $S_1\le S_2\le\cdots\le\mathbb{1}$；对每个 $\psi$，$\lVert S_N\psi\rVert^{2}=\langle\psi\lvert S_N\lvert\psi\rangle$ 单调有界，故 $\{S_N\psi\}$ 收敛。**极限就是右边。**

**（"测度"的公理只有两条：空集为零、可数可加；非负写在取值里。投影值测度把取值从"非负数"换成"投影"，于是多出一条归一化 $E(\mathbb{R})=\mathbb{1}$。）**

**为什么取值必须是投影**：谱定理本质是一个映射 $f\mapsto f(\hat A)=\int f\,dE$，它保持乘法与共轭；而 $E(B)$ 正是 $\mathbf{1}_B$ 的像。于是 $\mathbf{1}_B^{2}=\mathbf{1}_B$ 逼出 $E(B)^{2}=E(B)$（**幂等**），$\mathbf{1}_B$ 实值逼出 $E(B)$ 自伴（**对称**）——**幂等 + 自伴就是正交投影**。正交还保证勾股：$\lVert\psi\rVert^{2}=\lVert E(B)\psi\rVert^{2}+\lVert E(B^{c})\psi\rVert^{2}$，即 $p(B)+p(B^{c})=1$。**换成一般正算子或斜投影，概率就会超过 $1$ 或漏掉。**

给定 $\hat A$，这样的 $E$ 是**唯一**的。

**定理的全部内容就是两条**：

1. **投影拼回整个空间**：$\int dE(\lambda)=E(\mathbb{R})=\mathbb{1}$——互相垂直，合起来不漏；
2. **算子按权重把投影加起来**：$\hat A=\int\lambda\,dE(\lambda)$——$\lambda$ 是权重，$dE(\lambda)$ 是那一份投影。

**"拼回整个空间"有两个式子，含义不同**：

$$
\underbrace{E(\mathbb{R})=\mathbb{1}}_{\text{定义：测度归一}}
\qquad
\underbrace{E(\sigma(\hat A))=\mathbb{1}}_{\text{定理：谱之外没有分量}}
$$

**两者由 $E(\mathbb{R}\setminus\sigma(\hat A))=0$（谱即支撑，§1.2.1）连起来**：
$$
E(\sigma(\hat A))=E(\mathbb{R})-E(\mathbb{R}\setminus\sigma(\hat A))=\mathbb{1}-0=\mathbb{1}
$$

**所以两个写法都对**；但讲"合起来是整个空间"时，**后者更有信息量**——它说了谱在哪儿。

**它在解决什么问题**：算子本身是抽象对象，"$\hat A$ 是什么"很难直接回答；谱分解把它换成两样具体的东西——**一堆数**（谱上的 $\lambda$）加**一堆投影**。之后函数演算、完备性、对角化，都变成在这两样东西上做算术。

### 1.2 它还给什么（四条）

1. **函数演算**——把谱上的 $\lambda$ 换成 $f(\lambda)$：

$$
f(\hat A)=\int f(\lambda)\;dE(\lambda),
\qquad
D\bigl(f(\hat A)\bigr)=\Bigl\{\psi\;\Big|\;\int\lvert f(\lambda)\rvert^{2}\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle<\infty\Bigr\}
$$

$f$ 是**任意** Borel 函数（不必有界）。无界时用上面那个定义域——它只是"权重太大会发散，所以要挑函数"，**不是新增的物理，是收敛性的记账**。**取 $f(\lambda)=\lambda$ 就还回 $\hat A$ 自己的定义域**，不必另记一条。$f$ 有界时它是有界算子，且 $\lVert f(\hat A)\rVert=\sup_{\lambda\in\sigma(\hat A)}\lvert f(\lambda)\rvert$。


2. **谱的位置**——两条，**都能证**（证明在 §1.2.1、§1.2.2）：
   - $\sigma(\hat A)$ 是 $E$ 的**支撑**：每个邻域里 $E$ 都不为零；
   - $E(\{\lambda\})\neq0$ 的点就是**点谱**，且这时 $E(\{\lambda\})$ 正是**投影到该本征子空间**的投影。

3. **乘法律**——投影值测度的定义只要求"可数可加、且值都是投影"，而

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

**由乘法律得到范数形式**（§1.2.1、§1.2.2 都要用它）：对 Borel 函数 $g$ 与 $\psi\in D(g(\hat A))$，

$$
\lVert g(\hat A)\psi\rVert^{2}
=\int\lvert g(\lambda)\rvert^{2}\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle
\qquad(\ast)
$$

**$g$ 有界时它是定理**，四步：

$$
\lVert g(\hat A)\psi\rVert^{2}
=\langle g(\hat A)\psi\lvert g(\hat A)\psi\rangle
=\langle\psi\lvert g(\hat A)^{\dagger}g(\hat A)\lvert\psi\rangle
=\langle\psi\lvert(\lvert g\rvert^{2})(\hat A)\lvert\psi\rangle
=\int\lvert g\rvert^{2}\,d\mu_\psi
$$

（依次用：内积定义；伴随的定义 $g(\hat A)^{\dagger}=\overline{g}(\hat A)$；上面这条乘法律；§1.2 第 1 条的二次型形式。）

**$g$ 无界时按截断取极限**：取 $g_n=g\,\mathbf{1}_{\{\lvert g\rvert\le n\}}$（有界），则 $g_n(\hat A)\psi\to g(\hat A)\psi$，而 $\lvert g_n\rvert^{2}\nearrow\lvert g\rvert^{2}$，由单调收敛右边趋于 $\int\lvert g\rvert^{2}d\mu_\psi$。

**这顺便解释了定义域**：$\psi\in D(g(\hat A))$ 当且仅当 $(\ast)$ 的右边有限——**不是额外限制，而是"作用完仍留在 $\mathcal{H}$ 里"的等价说法**。

4. **一个"对角化"模型**——谱简单时，$\hat A$ **酉等价于"乘以 $\lambda$"**。

**先用有限维看懂这件事。** 取 $\hat A=\mathrm{diag}(2,3)$，本征向量 $e_1,e_2$，并取一个"两个方向都有分量"的向量 $\psi=e_1+e_2$。对任意函数 $f$：

$$
f(\hat A)\psi=f(2)\,e_1+f(3)\,e_2
$$

**这个向量携带的全部信息，就是一对数 $\bigl(f(2),f(3)\bigr)$。** 于是定义

$$
U:\quad f(2)\,e_1+f(3)\,e_2\ \longmapsto\ \bigl(f(2),\,f(3)\bigr)
$$

**这就是"换到本征基"：$U$ 输出的是各本征方向上的系数。** 验证一下 $\hat A$ 在换基后干什么：

$$
\hat A\bigl(f(\hat A)\psi\bigr)=2f(2)\,e_1+3f(3)\,e_2
\ \longmapsto\ \bigl(2f(2),\,3f(3)\bigr)
$$

**换基之后，$\hat A$ 的作用就是"第 $i$ 个分量乘以 $a_i$"**——对角阵。**这就是"乘以 $\lambda$"在离散情形的样子。**

**无限维只改两处**：本征值从有限个变成连续的谱；"第 $i$ 个分量"变成"$\lambda$ 处的函数值 $f(\lambda)$"。

| 有限维 | 无限维 |
|---|---|
| $\sum_i\lvert f(a_i)\rvert^{2}$ | $\int\lvert f(\lambda)\rvert^{2}\,d\mu_\psi(\lambda)$ |
| 对角阵 | 乘以 $\lambda$ |

**下面把这件事写成证明。**

**① 换基怎么定义。** 取**循环矢量** $\psi$（使 $\{f(\hat A)\psi\}$ 稠密），令

$$
U\bigl(f(\hat A)\psi\bigr)=f
$$

**$U$ 干的事：把一个向量翻译成它在"本征基"上的系数函数。**

**② 良定义。** 若两个 $f$ 给出同一个向量，即 $f(\hat A)\psi=0$，由下面的等距性得 $\int\lvert f\rvert^{2}d\mu_\psi=0$，故 $f=0$ 几乎处处——**一个向量只对应一个函数**。

**③ $U$ 是酉。** 由 $(\ast)$ 式，

$$
\lVert f(\hat A)\psi\rVert^{2}=\int\lvert f(\lambda)\rvert^{2}\,d\mu_\psi(\lambda)
$$

**保长度；再加上稠密，就延拓成酉算子。**

**④ 换基之后 $\hat A$ 变成乘法。** 取 $g(\hat A)\psi$，其中 $g$ 有界且 $\lambda g$ 有界（保证 $\hat A$ 作用得上）。由乘法律：

$$
\hat A\bigl(g(\hat A)\psi\bigr)=(\lambda g)(\hat A)\psi
$$

两边用 $U$ 翻译：

$$
U\bigl(\hat A\,g(\hat A)\psi\bigr)=\lambda\,g(\lambda)=M_\lambda\bigl(U(g(\hat A)\psi)\bigr)
$$

**这里为什么冒出个 $g$**：$U$ 只对 $f(\hat A)\psi$ 这类向量好算，所以只能拿这类向量来试；**$g$ 就是"拿哪个向量试"的编号**。对每个 $g$ 都成立，就是对这类向量的每一个都成立。

**⑤ 从"这类向量"到"所有向量"。** 这类向量稠密（构成 $M_\lambda$ 的**核心**），而 $M_\lambda$ 与 $U\hat A U^{-1}$ **都是自伴算子**；两个自伴算子在一个核心上相等，就**处处相等**。

**结论**：对 $\psi\in D(\hat A)$，

$$
\bigl(U\hat A\psi\bigr)(\lambda)=\lambda\,(U\psi)(\lambda)
\qquad\text{即}\qquad
U\hat A\,U^{-1}=M_\lambda
$$

**这就是"酉等价"**：换一组基之后，$\hat A$ 只做**乘法**——输入函数在 $\lambda$ 处的值，只决定输出在 $\lambda$ 处的值，**各点互不混合**。

**为什么需要"谱简单"。** 要让 $U$ 翻译出所有向量，就需要那个 $\psi$ 在**每个本征方向都有分量**。**若某个本征值有二重以上的重数，一个 $\psi$ 覆盖不了**，只能每个本征空间各取一个，最后得到直和：

$$
\hat A\ \cong\ \bigoplus_iM_\lambda
\qquad\text{在}\quad\bigoplus_iL^{2}\bigl(\sigma(\hat A),\mu_i\bigr)\ \text{上}
$$

**地位**：它是谱定理的推论，**但多一个前提**——存在循环矢量（谱简单）。**直和版**不需要这个前提，仍是纯推论；**"一次换基就够"才是简单谱带来的细化**。

**为什么这条有用**：在这个模型里，D01 的其余结论都变成"函数上的算术"——$f(\hat A)$ 是乘以 $f(\lambda)$，$E(B)$ 是乘以指示函数 $\mathbf{1}_B$，$\int dE=\mathbb{1}$ 是"乘以 $1$ 是恒等"。**"让 $\hat q$ 对角"这句话的严格含义，就是这个。**

### 1.2.1 为什么"谱 = 支撑"

**先把"支撑"说清**。它的**原始定义**是
$$
\operatorname{supp}E\equiv\mathbb{R}\setminus\bigcup\bigl\{U\ \text{开}:\ E(U)=0\bigr\}
$$

即"所有测度为零的开集的并"的补集。**等价刻画**是我们实际要用的：

$$
\lambda\in\operatorname{supp}E
\iff
\text{对 }\lambda\text{ 的每个邻域 }U,\ E(U)\neq0
$$

**这里的 $0$ 指零算子，不是数 $0$**：$E(U)\neq0$ 的意思是 $E(U)$ 不是零投影，即它的值域非平凡。**邻域可换成 $(\lambda-\varepsilon,\lambda+\varepsilon)$**，验算时更方便。

**为什么这个并是良好定义的**：$\mathbb{R}$ 是第二可数的，任一开集都是**有理端点开区间**的可数并。所以上面那个并只需取可数个基元素，**由可数可加仍是零测集**，其补集是闭集。

**要证两个方向。**

**（1）不在支撑里 ⇒ 不在谱里。** 若 $\lambda_0$ 有邻域 $U$ 使 $E(U)=0$，则测度全落在 $U^{c}$ 上；而 $\lambda_0\notin U^{c}$（$U$ 开），故存在 $\delta>0$ 使

$$
\lvert\lambda-\lambda_0\rvert\ge\delta
\qquad(\lambda\in U^{c})
$$

由 §1.2 的 **$(\ast)$ 式**（取 $g(\lambda)=\lambda-\lambda_0$；$\psi\in D(\hat A)$ 正是它的定义域）：

$$
\lVert(\hat A-\lambda_0)\psi\rVert^{2}
=\int\lvert\lambda-\lambda_0\rvert^{2}\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle
\ \ge\ \delta^{2}\lVert\psi\rVert^{2}
$$

**有下界 $\delta$ ⇒ 可逆、且逆有界**（逆是 $\int\frac{1}{\lambda-\lambda_0}dE$，范数 $\le1/\delta$）。所以 $\lambda_0\notin\sigma(\hat A)$。

**（2）在支撑里 ⇒ 在谱里。** 取 $B_n=(\lambda_0-\frac{1}{n},\lambda_0+\frac{1}{n})$，则 $E(B_n)\neq0$；取单位向量 $\psi_n\in E(B_n)\mathcal{H}$。对 $\psi_n$，测度全落在 $B_n$ 上，故

$$
\lVert(\hat A-\lambda_0)\psi_n\rVert^{2}
=\int_{B_n}\lvert\lambda-\lambda_0\rvert^{2}\,d\langle\psi_n\lvert E\lvert\psi_n\rangle
\ \le\ \frac{1}{n^{2}}
$$

**于是 $(\hat A-\lambda_0)\psi_n\to0$ 而 $\lVert\psi_n\rVert=1$。** 若存在有界逆 $R$，则

$$
1=\lVert\psi_n\rVert\le\lVert R\rVert\,\lVert(\hat A-\lambda_0)\psi_n\rVert\le\frac{\lVert R\rVert}{n}\to0
$$

矛盾。所以 $\lambda_0\in\sigma(\hat A)$。

**合起来**：$\sigma(\hat A)=\operatorname{supp}E$。

**一句话**：**算子在哪儿"坏"，测度就在哪儿有质量。**

### 1.2.2 为什么"原子 = 本征值"

**要证的其实是等式**
$$
\operatorname{ran}E(\{\lambda\})=\ker(\hat A-\lambda)
$$

**左边是投影的值域，右边是本征子空间。** 两个方向各一条。

**方向一：$P\equiv E(\{\lambda\})\neq0$ ⇒ $\lambda$ 是本征值。** 取 $\psi\in\operatorname{ran}P$，$\psi\neq0$。对 $\psi$，测度全落在 $\{\lambda\}$ 上（因为 $(𝟙-P)\psi=0$），故

$$
\hat A\psi=\int\lambda'\,dE(\lambda')\psi=\lambda\psi
$$

**值域里的非零向量全是本征向量。**

**方向二：本征向量必被 $P$ 保留。** 若 $\hat A\psi=\lambda\psi$，则 $(\hat A-\lambda)\psi=0$。用 §1.2 的 **$(\ast)$ 式**（取 $g(\lambda')=\lambda'-\lambda$）：

$$
0=\lVert(\hat A-\lambda)\psi\rVert^{2}
=\int(\lambda'-\lambda)^{2}\,d\langle\psi\lvert E\lvert\psi\rangle
$$

**被积函数非负、积分零，故测度只落在 $\{\lambda\}$ 上**：$\langle\psi\lvert E(\{\lambda\})\lvert\psi\rangle=\lVert\psi\rVert^{2}$。由勾股（$E$ 与 $𝟙-E$ 正交）：

$$
\lVert(\mathbb{1}-E(\{\lambda\}))\psi\rVert^{2}
=\lVert\psi\rVert^{2}-\lVert E(\{\lambda\})\psi\rVert^{2}=0
$$

所以 $E(\{\lambda\})\psi=\psi$。

**两个方向合起来**：$\operatorname{ran}E(\{\lambda\})=\ker(\hat A-\lambda)$。而 $E(\{\lambda\})$ 是**正交**投影，故它就是**投影到该本征子空间**的投影。

**一句话**：**测度在某一点上的整块质量，就是一个本征子空间。**

### 1.3 它不给什么（三条，最要紧）

1. **连续谱时不给本征矢。** 对连续谱的每个单点，$E(\{q\})=0$，于是**不存在** $\psi\in\mathcal{H}$ 满足 $\hat A\psi=q\psi$。谱定理给的是"一族投影"，不是"一族向量"。
2. **不告诉你谱是什么。** 定理对**任何**自伴算子都成立，所以它对"$\hat q$ 的谱是 $\mathbb{R}$ 还是格点"一无所知。谱由你选的算子与边界条件决定。
3. **不固定归一化。** 广义本征矢的归一化系数是约定（相位与整体相位都属于这一类）。

---

## 2. Gelfand–Maurin（核空间谱定理）

### 2.1 问题：我们要"矢"，谱定理只给"投影"

谱定理说得清楚：自伴算子给一族**投影** $E(B)$。但物理上天天写的是 $\lvert q\rangle$——一个**矢**。

**它不在 $\mathcal{H}$ 里**：连续谱时 $E(\{q\})=0$（§1.3 第 1 条），所以**没有**平方可积的 $\psi$ 满足 $\hat q\psi=q\psi$。

**但 $\lvert q\rangle$ 不是错，是它住在别处。** 要给它一个合法的住处，就得把空间扩大。

### 2.2 需要什么：三层空间

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

### 2.3 陈述

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

### 2.4 它给什么

- $\lvert q\rangle$ **本身**：$[\hat q,f(\hat q)]$ 与 $\hat q$ 的谱分解都能写出来，靠的就是它；
- **本征矢族的存在性**——本卡只负责"存在"这一步；它如何特化成具体算子的本征方程、归一化如何定，都是下游的事；
- **狄拉克记号的下限**——$\langle q\lvert\psi\rangle=\psi(q)$ 是**求值泛函**，不是 $L^{2}$ 内积。

**具体画面**（"为什么必须扩大空间"的最短说明）：取 $\hat q$ 为 $L^{2}(\mathbb{R})$ 上"乘以 $q$"。则 $\lvert q\rangle$ 就是求值泛函 $\psi\mapsto\psi(q)$。它在 $L^{2}$ 上**不连续**（函数可在一点很高而范数很小），但在 Schwartz 空间 $\mathcal{S}$ 上连续——所以它住在 $\mathcal{S}^{\times}$ 里，不在 $\mathcal{H}$ 里。

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
- [ ] 说明 Gelfand–Maurin 的两条结论分别给“存在性”与“完备性”，以及为什么完备性只对 $\Phi$ 成立
