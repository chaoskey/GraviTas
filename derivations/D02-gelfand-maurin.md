# D02 · 核空间谱定理（Gelfand–Maurin）

> 建档 2026-11-18 · 类型：**引用卡**——Gelfand–Maurin 是外部数学，本卡只引用、不证明；由它推出四条推论
> 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)
> 下游：（由网格反查生成）
> 它补的是谱定理缺的那一半：**给"一族投影"，不给"一族矢"**。

---

## 0. 问题：我们要"矢"，谱定理只给"投影"

谱定理说得清楚：自伴算子给一族**投影** $E(B)$。但物理上天天写的是 $\lvert q\rangle$——一个**矢**。

**它不在 $\mathcal{H}$ 里**：连续谱时 $E(\{q\})=\mathbb{0}$（[D01](D01-spectral-theorem.md) §3），所以**没有**平方可积的 $\psi$ 满足 $\hat q\psi=q\psi$。

**为什么不能从 D01 直接推出。** D01 给的是**抽象**的投影值测度 $E$；它不保证 $E$ 有密度 $\lvert F_\lambda\rangle\langle F_\lambda\rvert$，更不保证有本征矢——连续谱时 $\mathcal{H}$ 里根本没有。**这两样都要另外的定理，不是换积分符号能换出来的。**

**出路**：把空间扩大，让"矢"住在更大的空间里。

---

## 1. 三层空间

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

**"核空间"是外部概念**，本卡不定义它，只用它两条性质：（i）能**连续稠密**地嵌进 $\mathcal{H}$；（ii）使谱测度**可数化**——所以本征矢系能被"积出来"。**一般 Fréchet 空间不够**：这条定理对 $\Phi$ 的选择是敏感的。

**两层嵌入怎么嵌**：$\Phi\subset\mathcal{H}$ 是包含；$\mathcal{H}\subset\Phi^{\times}$ 是"用内积造泛函"——$\psi\mapsto\langle\psi\lvert\cdot\rangle$。

**一句话记住三层**：$\lvert q\rangle$ 不是"存在但奇怪"，而是**"取值"这个动作的严格化身**。

---

## 2. 定理（核空间谱定理）

**条件**（三条）：

| 条件 | 管什么 |
|---|---|
| $\hat A$ 自伴 | 谱是实的、谱测度存在 |
| $\Phi$ 是核空间，连续稠密地嵌进 $\mathcal{H}$ | 让"展开"真能做成，不是形式上的 |
| $\hat A$ **连续地**映 $\Phi$ 到 $\Phi$ | 让"本征方程"有意义：作用完还留在能谈的范围内 |

**结论**（两条）：

**（i）本征方程。** 存在一族 $F_{\lambda,i}\in\Phi^{\times}$，使

$$
\hat A F_{\lambda,i}=\lambda F_{\lambda,i}
$$

（$\hat A$ 在 $\Phi^{\times}$ 上按对偶作用：$\langle\hat A F_{\lambda,i},\phi\rangle=\langle F_{\lambda,i},\hat A\phi\rangle$——**这正是要求 $\hat A$ 把 $\Phi$ 映进 $\Phi$ 的原因**。）

**（ii）谱分解。** 存在**标量测度** $\mu$，使对**任意有界 Borel 函数 $g$**，

$$
g(\hat A)=\int g(\lambda)\,P(\lambda)\;d\mu(\lambda),
\qquad
P(\lambda)=\sum_i\lvert F_{\lambda,i}\rangle\langle F_{\lambda,i}\rvert
$$

**定理的全部内容就是这两条**：一支矢（本征方程），一把尺（谱分解）。

---

## 3. 推论

**四条推论都只取定理的 (ii)，各取一个 $g$；边界感在于：换 $g$ 就换结论，不混用。**

### 3.1 推论一：完备性（取 $g\equiv1$）

$$
\mathbb{1}=\int P(\lambda)\;d\mu(\lambda)
$$

**"对谁成立"要说清**：上式是 $\Phi$ 上的二次型——对**任意 $\phi,\psi\in\Phi$**，

$$
\langle\phi\lvert\psi\rangle=\int\sum_i\langle\phi\lvert F_{\lambda,i}\rangle\,\langle F_{\lambda,i}\lvert\psi\rangle\;d\mu(\lambda)
$$

**对 $\mathcal{H}$ 中的一般态，这个积分不一定收敛**——要延拓是另一回事。**这就是为什么 $\Phi$ 必须"好"。**

### 3.2 推论二：谱测度有密度（取 $g=\mathbf{1}_B$）

$\mathbf{1}_B$ 是 Borel 集 $B$ 的**指示函数**：

$$
\mathbf{1}_B(\lambda)=
\begin{cases}
1, & \lambda\in B\\
0, & \lambda\notin B
\end{cases}
$$

**它只取 $0$、$1$ 两个值，所以有界**——(ii) 对它有定义，不需要额外的定义域条件。

**左边**：由 [D01](D01-spectral-theorem.md) §1，$\mathbf{1}_B(\hat A)=E(B)$。于是

$$
E(B)=\int_B P(\lambda)\;d\mu(\lambda)
$$

**这就是 D01 的抽象投影 $E$ 与 D02 的密度 $P\,d\mu$ 的接头**。

### 3.3 推论三：与 D01 的标量测度 $\mu_\psi$ 的关系（对 3.2 取期望）

$$
\mu_\psi(B)=\langle\psi\lvert E(B)\lvert\psi\rangle=\int_B\langle\psi\lvert P(\lambda)\lvert\psi\rangle\,d\mu(\lambda)
$$

**所以** $\mu_\psi\ll\mu$，**密度就是 $\langle\psi\lvert P(\lambda)\lvert\psi\rangle$**。反过来，取一组正交基 $\{\psi_n\}$ 并令 $\mu=\sum_n2^{-n}\mu_{\psi_n}$，它就能"罩住"所有 $\mu_\psi$。

**$\mu$ 不唯一**：$\mu\to\rho\,\mu$、同时 $P\to P/\rho$（$\rho>0$），$E$ 不变。**而 $\mu_\psi$ 由 $E$ 与 $\psi$ 唯一决定**，没有这个自由度。

### 3.4 推论四：无简并时回到单矢形式（对 3.2 取 $i$ 只有一项）

**若每个本征值都只有一重**（无简并），则 $P(\lambda)$ 只剩一项：

$$
P(\lambda)=\lvert F_\lambda\rangle\langle F_\lambda\rvert
\qquad\Longrightarrow\qquad
E(B)=\int_B\lvert F_\lambda\rangle\langle F_\lambda\rvert\;d\mu(\lambda)
$$

**并且这时可以取 $\mu=\mu_{\psi_0}$**（$\psi_0$ 为循环矢量）——这正是 [D01](D01-spectral-theorem.md) §5 里 $U:\mathcal{H}\to L^{2}(\sigma,d\mu_{\psi_0})$ 用的那个测度。

**所以"无简并"是把 D02 接回 D01 对角化模型的条件**；有重数时只能保留 $P(\lambda)$ 的求和形式。

---

## 4. 它给什么

- $\lvert q\rangle$ **本身**：$[\hat q,f(\hat q)]$ 与 $\hat q$ 的谱分解都能写出来，靠的就是它；
- **本征矢族的存在性**——本卡只负责"存在"这一步；它如何特化成具体算子的本征方程、归一化如何定，都是下游的事；
- **狄拉克记号的下限**——$\langle q\lvert\psi\rangle=\psi(q)$ 是**求值泛函**，不是 $L^{2}$ 内积。

**具体画面**（"为什么必须扩大空间"的最短说明）：取 $\hat q$ 为 $L^{2}(\mathbb{R})$ 上"乘以 $q$"。则 $\lvert q\rangle$ 就是求值泛函 $\psi\mapsto\psi(q)$。它在 $L^{2}$ 上**不连续**（函数可在一点很高而范数很小），但在 Schwartz 空间 $\mathcal{S}$ 上连续——所以它住在 $\mathcal{S}^{\times}$ 里，不在 $\mathcal{H}$ 里。

---

## 5. 边界

1. **非自伴算子全都没有。** 谱定理要求自伴；非自伴只有"谱"这个较弱的对象，没有投影值测度，也没有广义本征矢系。这是整套量子力学要求可观测量自伴的**数学**理由，而不只是习惯。
2. **核性不可省。** 换成一般的稠密子空间，Gelfand–Maurin 可能失效。所以"随便找个稠密子空间就能定义 $\lvert q\rangle$"是错的。
3. **归一化依赖谱测度密度。** 若 $d\mu=\rho(q)\,dq$，则 $\langle q\lvert q'\rangle=\delta(q-q')/\rho(q)$。平直空间 $\rho=1$，弯曲空间 $\rho=\sqrt{g}$——**这是弯曲空间里测度因子的数学出处**。
4. **重数大于 1 时要加标签。** 定理里的 $P(\lambda)=\sum_i\lvert F_{\lambda,i}\rangle\langle F_{\lambda,i}\rvert$ 就是为此准备的：一个 $F_\lambda$ 覆盖不了重数，必须按本征子空间逐项相加，归一化变成 $\delta_{ij}$。物理上就是自旋、味道、超选扇区。
5. **这张卡不做证明。** 本仓库不重推泛函分析；能推的是"给定这些定理，物理结论如何落地"。**引用与证明的界限要一直守住**。

---

## 6. 自检

- [ ] 用一句话说清谱定理与 Gelfand–Maurin 各负责什么
- [ ] 说出定理的两条结论，以及每条各管什么
- [ ] 解释为什么连续谱时"Hilbert 空间里没有本征矢"
- [ ] 用"求值泛函"说明 $\lvert q\rangle$ 为什么不在 $\mathcal{H}$ 里
- [ ] 说明核空间条件为什么不可省
- [ ] 从 (ii) 推出 3.1、3.2、3.3、3.4 四条，并说清每一步用了 (i) 还是 (ii)
