# D08 · 对角判据：$[\hat q,f(\hat q)]=0$ ⇒ 核正比于 $\delta$

> 建档 2026-11-07 · 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)、[D02](D02-gelfand-maurin.md)、[D04](D04-position-eigen-equation.md)（$\langle q\lvert q'\rangle=\delta$、$f(\hat q)$ 的展开）
> 下游：[D09](D09-product-kernel.md)、[D20](D20-hamiltonian.md)
> 原为 [N003 §4.2](../notes/N003-basis-and-operator-relations.md)，2026-11-07 移入网格。
> 本卡同时是"**核**"这个语言在网格里的落脚处：$\S1$ 给出核的定义与三个基本例子，$\S2$ 用它陈述并证明判据。

---

## 0. 命题

对任意只含 $\hat q$ 的算子 $f(\hat q)$，

$$
\langle q'\lvert f(\hat q)\lvert q''\rangle=f(q')\,\delta(q'-q'')\tag{1}
$$

等价说法：

$$
\bigl[\hat q,f(\hat q)\bigr]=0\tag{2}
$$

**它在讲什么**：算子与 $\hat q$ 对易 $\iff$ 它在 $q$ 基下对角。对角算子的核必然是"一个函数乘以 $\delta$"。

---

## 1. 核：算子在 $q$ 表象下的"表格"

### 1.1 定义

**定义**：算子 $A$ 在 $\lvert q\rangle$ 基下的**核** $K_A(q,q')$，是使

$$
\langle\phi\lvert A\lvert\psi\rangle=\int\!\!\int\overline{\phi(q)}\,K_A(q,q')\,\psi(q')\,dq\,dq'\tag{3}
$$

对**所有** $\phi,\psi\in\Phi$ 成立的分布。其中 $\phi(q)\equiv\langle q\lvert\phi\rangle$。

**它是"矩阵元"的连续版本**：离散基下算子的全部信息就是矩阵 $\langle i\lvert A\lvert j\rangle$；连续基下就是这张两变量的"表" $K_A(q,q')$。**给定 $A$，核唯一**——因为 (3) 对所有配对成立，而分布由全部配对唯一确定。

### 1.2 三个基本例子

| $A$ | 核 $K_A$ | 代入 (3) 后 |
|---|---|---|
| $\mathbb{1}$ | $\delta(q-q')$ | 退化成 $\int\overline{\phi(q)}\psi(q)\,dq$ |
| $\hat q$ | $q\,\delta(q-q')$ | 退化成 $\int q\,\overline{\phi(q)}\psi(q)\,dq$ |
| $E(B)$ | $\mathbf{1}_B(q)\,\delta(q-q')$ | 退化成 $\int_B\overline{\phi(q)}\psi(q)\,dq$ |

**三行都靠同一件事**：$\delta$ 把 $q'$ 钉在 $q$ 上，于是 $q'$ 处的算子像变成 $q$ 处的标量。$\hat q$ 与 $E(B)$ 在 $q$ 表象下"已对角"，核就是对角标量乘 $\delta$。

**其中第一行就是本卡要用的那一行**：$\langle q\lvert q'\rangle$ 不是内积，而是**恒等算子的核** $K_{\mathbb{1}}$；它的值 $\delta(q-q')$ 已由 [D04](D04-position-eigen-equation.md) §4 给出（选定 $d\mu=dq$ 后完备性在对偶意义下的表现）。

### 1.3 核随基矢尺度变，物理不变

若把 $\lvert q\rangle$ 整体乘 $\lambda$，则 $\langle q\lvert q'\rangle\to\lvert\lambda\rvert^{2}\delta$，即核整体乘 $\lvert\lambda\rvert^{2}$；同时完备性权重必须变成 $w/\lvert\lambda\rvert^{2}$（[D04](D04-position-eigen-equation.md) §2 的同步缩放）。**两者一起换，所有可观测量不变**——核只影响中间步骤的系数，不是物理内容。

---

## 2. 证明（两条路，第二条更根本）

### 2.1 路线一：谱分解

由 [D04](D04-position-eigen-equation.md) §3 的（9）与 [D01](D01-spectral-theorem.md) 的函数演算：

$$
f(\hat q)=\int dq\,f(q)\,\lvert q\rangle\langle q\rvert
$$

核直接读出：$\langle q'\lvert f(\hat q)\lvert q''\rangle=\int dq\,f(q)\delta(q'-q)\delta(q-q'')=f(q')\delta(q'-q'')$。

### 2.2 路线二：对易子论证

**不需要 $f$ 能展开，只需要"$f$ 是 $\hat q$ 的函数"这一件事。**

对任意 $q',q''$：

$$
\begin{aligned}
0&=\bigl\langle q'\bigr\lvert\bigl[\hat q,f(\hat q)\bigr]\bigl\lvert q''\bigr\rangle \\
&=\bigl\langle q'\bigr\lvert\hat q\,f(\hat q)\bigl\lvert q''\bigr\rangle
-\bigl\langle q'\bigr\lvert f(\hat q)\,\hat q\bigl\lvert q''\bigr\rangle \\
&=q'\bigl\langle q'\bigr\lvert f(\hat q)\bigl\lvert q''\bigr\rangle
-q''\bigl\langle q'\bigr\lvert f(\hat q)\bigl\lvert q''\bigr\rangle \\
&=(q'-q'')\,\langle q'\lvert f(\hat q)\lvert q''\rangle
\end{aligned}
$$

**第 3 行第一个等号依赖 $\hat q$ 自伴**：本征方程只给右矢 $\hat q\lvert q'\rangle=q'\lvert q'\rangle$；取伴随并用 $\hat q^{\dagger}=\hat q$，才得到左矢版本 $\langle q'\rvert\hat q=q'\langle q'\rvert$。而第二个等号（取出 $q''$）直接来自右矢本征方程——**两边的来源并不对称**，这一步不能省。

由 $(q'-q'')\,T=0$（记 $T\equiv\langle q'\lvert f(\hat q)\lvert q''\rangle$）：

- 若 $q'\ne q''$，则 $T=0$——**对角线之外一律为零**；
- 若 $q'=q''$，方程不约束 $T$——**对角线上可以"无限大"**。

所以 $T$ 只能集中在 $q'=q''$ 上，形如

$$
T=c(q')\,\delta(q'-q'')
$$

**为什么是 $\delta$，而不是它的导数**：把 $(q'-q'')$ 乘回去验算——$\delta$ 给出 $0$（符合要求），而 $\delta'$ 给出 $-\delta$（不符合）。所以对角线上只能放 $\delta$ 本身，不能放它的导数。

系数由"作用在态上"定：$f(\hat q)\lvert q''\rangle=f(q'')\lvert q''\rangle$，故 $c=f$。用核的语言写，就是

$$
K_{f(\hat q)}(q',q'')=f(q')\,\delta(q'-q'')\tag{4}
$$

**为什么这条路更根本**：它把"对角"这件事归因于**对易**，而不是归因于"$f$ 长什么样"。所以对不可微、不可展开的函数也成立。

---

## 3. 它用在哪

1. **$e^{-\varepsilon V(\hat q)}$ 在 $q$ 基下对角**——这是下游"位能那块直接提出去"的前提；
2. **解释一个常见困惑**：为什么 $V(q)$ 与 $V(q')$ 在 $\langle q'\lvert e^{-\varepsilon V(\hat q)}\lvert q''\rangle$ 里可以随便换？因为 $\delta$ 的支撑上 $q'=q''$，两者**精确**相等。差 $\mathcal{O}(\varepsilon^{3/2})$ 的说法只出现在"$\delta$ 被 $p$ 积分抹成高斯之后"——那时两点不再重合。
3. **判据可推广**：任何"与某算子对易"的算子，在该算子的表象下都对角。

---

## 4. 一致性检验

| 检验 | 结果 |
|---|---|
| $f=1$ | 核 $=K_{\mathbb{1}}=\delta(q'-q'')$，与 §1.2 第一行一致 ✅ |
| $f=\hat q$ | 核 $=q'\delta(q'-q'')$，与 §1.2 第二行一致 ✅ |
| 与 [D07](D07-commutator-p-fq.md) 对照 | $[\hat p,f(\hat q)]\neq0$（等于 $-if'$），$[\hat q,f(\hat q)]=0$——**方向不同，结论相反** ✅ |
| 不解析的 $f$（如阶跃） | 路线二仍成立，路线一需谱分解 ✅ |

---

## 5. 边界

1. **需要 $\lvert q\rangle$ 存在**（[D02](D02-gelfand-maurin.md)）。
2. **对 $f$ 无需解析**，只需 Borel 可测（走路线一）；路线二连可测都不需要，只需"是 $\hat q$ 的函数"。
3. **不能反过来用**：核对角不意味着算子是 $\hat q$ 的函数（同一表象下不会，但换表象时要注意）。
4. **核依赖基矢的尺度**：$\lvert q\rangle\to\lambda\lvert q\rangle$ 时核乘 $\lvert\lambda\rvert^{2}$，同时权重按 [D04](D04-position-eigen-equation.md) §2 反向改——**它是中间系数，不是物理内容**。
5. **弯曲空间核带 $1/\rho$**：若 $d\mu=\rho(q)\,dq$，则 $K_{\mathbb{1}}=\delta(q-q')/\rho(q)$，其余例子同乘该因子（[D04](D04-position-eigen-equation.md) §6 第 3 条）。
6. **离散谱与多分量**：纯点谱时 $\delta(q-q')\to\delta_{nn'}$、积分变求和；有内部自由度时 $\langle q,i\lvert q',j\rangle=\delta_{ij}\delta(q-q')$。
7. **动量基那一侧**：核的定义对任何连续基都成立，但换到 $p$ 基要用 $\langle q\lvert p\rangle=e^{ipq}$，属下游。

---

## 6. 自检

- [ ] 写出核的定义 (3)，并说明 $\langle q\lvert q'\rangle$ 是哪个算子的核
- [ ] 用对易子论证写出核的形式 (4)，并说明为什么不需要 $f$ 解析
- [ ] 说明 $[\hat q,f(\hat q)]=0$ 与 $[\hat p,f(\hat q)]=-if'$ 为什么不矛盾
- [ ] 说明为什么对角线上只能放 $\delta$、不能放 $\delta'$
- [ ] 说明核随基矢尺度怎么变、为什么物理量不受影响
- [ ] 用它解释 $V(q)$ 与 $V(q')$ 何时可以互换
