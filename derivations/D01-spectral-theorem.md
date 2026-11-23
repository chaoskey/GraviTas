# D01 · 谱定理：自伴算子的谱分解

> 建档 2026-11-07 · 类型：**引用卡**——谱定理是外部数学，本卡只引用、不证明；本卡的任务是由它**推出五条推论**
> 上游：[D00](D00-commutator-axiom.md)
> 下游：[D02](D02-gelfand-maurin.md)、[D03](D03-born-rule.md)、[D04](D04-position-eigen-equation.md)、[D06](D06-functional-calculus.md)、[D07](D07-trace.md)、[D08](D08-commutator-p-fq.md)、[D09](D09-diagonal-criterion.md)、[D10](D10-product-kernel.md)、[D18](D18-qp-overlap.md)、[D20](D20-momentum-representation.md)、[D22](D22-path-integral-representation.md)、[D23](D23-trace-is-loop.md)、[D26](D26-uncertainty.md)
> 五条推论：**函数演算**、**谱即支撑**、**投影非零的独点即点谱**、**乘法规则**、**算子对角化**。

---

**记号**：$\mathcal{H}$ 是复希尔伯特空间（后面称"态空间"）；$\psi,\phi\in\mathcal{H}$ 是它的矢量，$\lVert\psi\rVert$ 是范数。$E(B)$ 是 $\mathcal{H}$ 上的正交投影；$D(\hat A)$ 记算子 $\hat A$ 的**定义域**；$\mathbb{1}$ 是恒等算子；$\mathbb{0}$ 是零算子。

**本卡里的 $\psi$ 只是"任意矢量"**，用来定义标量测度 $\mu_\psi(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$；**"态"是下游的概念，本卡不预设。**

---

## 0. 自伴算子的谱分解（谱定理）

**自伴算子** $\hat A$ 可以被拆成一族互相垂直的**投影**、按谱上的数**加权求和/积分**起来（$\lambda\in\sigma(\hat A)$）；并且给定 $\hat A$，这族投影是**唯一**的。而这族互相垂直的**投影**合起来是**整个空间**：

$$
\hat A=\int_{\sigma(\hat A)}\lambda\;dE(\lambda),
\qquad
\int_{\sigma(\hat A)}dE(\lambda)=E(\sigma(\hat A))=E(\mathbb{R})=\mathbb{1}
$$

**有限维时这是求和，无限维时这是积分；连续谱时那些投影不是"本征投影"。**

其中 $E$ 是把每个 **Borel 集**（从开区间出发，反复做"可数次并、交、补"能得到的所有集合）$B$ 映射到**投影（算子）** $E(B)$ 的**测度**——也就是说，$E$ 是一个取值为**投影（算子）**的**测度**，或称**投影（算子）值测度**。作为测度，它还必须满足两条**测度公理**：

1. $E(\varnothing)=\mathbb{0}$；
2. **可数可加**：两两不交的 $B_n$ 满足 $E\bigl(\bigcup_nB_n\bigr)=\sum_nE(B_n)$，和按**强收敛**理解。

**务必分清三个概念**：$B$ 是 **Borel 集**；$E(B)$ 是**投影（算子）**；$E$ 是**投影（算子）值测度**。

为后续方便，再定义 $\psi$ 下的**标量测度**

$$
\mu_\psi(B)=\langle\psi\lvert E(B)\lvert\psi\rangle
$$

此外，一般而言 $\sigma(\hat A)\neq\mathbb{R}$，但 $E(\sigma(\hat A))=E(\mathbb{R})$ 依然成立——这可以证明，见 §2。

**它在解决什么问题**：算子本身是抽象对象，"$\hat A$ 是什么"很难直接回答；谱分解把它换成两样具体的东西——**一堆数**（谱上的 $\lambda$）加**一堆投影**（$dE(\lambda)$）。之后函数演算、完备性、对角化，都变成在这两样东西上做算术。

---

## 1. 推论一：函数演算的分解

把谱上的 $\lambda$ 换成 $f(\lambda)$（$f$ 无界时必须结合定义域理解），立刻得到**函数演算**：

$$
f(\hat A)=\int f(\lambda)\;dE(\lambda),
\qquad
D\bigl(f(\hat A)\bigr)=\Bigl\{\psi\;\Big|\;\int\lvert f(\lambda)\rvert^{2}\,d\mu_\psi(\lambda)<\infty\Bigr\}
$$

$f$ 是**任意** Borel 函数（不必有界）。无界时用上面那个定义域——它只是"权重太大会发散，所以要挑函数"，**不是新增的物理，是收敛性的记账**。**取 $f(\lambda)=\lambda$ 就还回 $\hat A$ 自己的定义域**。$f$ 有界时它是有界算子；**$f$ 在谱上连续**时

$$
\lVert f(\hat A)\rVert=\sup_{\lambda\in\sigma(\hat A)}\lvert f(\lambda)\rvert
$$

**一般的有界 Borel $f$ 要把 $\sup$ 换成 $E$ 的本质上确界**：$\lVert f(\hat A)\rVert=\inf\{c\ge0:E(\{\lvert f\rvert>c\})=\mathbb{0}\}$——否则会把零测集上的值也算进范数（如 $f=\mathbf{1}_{\{0\}}$、$E(\{0\})=\mathbb{0}$ 时范数为 $0$，而谱上的点态上确界是 $1$）。

**由此立刻得到范数形式**（§2、§3 都要用）：对 Borel 函数 $g$ 与 $\psi\in D(g(\hat A))$，
$$
\lVert g(\hat A)\psi\rVert^{2}
=\int\lvert g(\lambda)\rvert^{2}\,d\mu_\psi(\lambda)
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

（依次用：内积定义；伴随的定义 $g(\hat A)^{\dagger}=\overline{g}(\hat A)$；乘法规则（见 §4）；本条的函数演算。）

**$g$ 无界时按截断取极限**：取 $g_n=g\,\mathbf{1}_{\{\lvert g\rvert\le n\}}$（有界），则 $g_n(\hat A)\psi\to g(\hat A)\psi$，而 $\lvert g_n\rvert^{2}\nearrow\lvert g\rvert^{2}$，由单调收敛右边趋于 $\int\lvert g\rvert^{2}d\mu_\psi$。

**这顺便解释了定义域**：$\psi\in D(g(\hat A))$ 当且仅当 $(\ast)$ 的右边有限——**不是额外限制，而是"作用完仍留在 $\mathcal{H}$ 里"的等价说法**。

---

## 2. 推论二：谱即支撑

**要证**：

$$
\sigma(\hat A)=\operatorname{supp}E
$$

**先把"支撑"说清**。它的**原始定义**是

$$
\operatorname{supp}E\equiv\mathbb{R}\setminus\bigcup\bigl\{U\ \text{开}:\ E(U)=\mathbb{0}\bigr\}
$$

即"所有测度为零的开集的并"的补集。**等价刻画**是我们实际要用的：

$$
\lambda\in\operatorname{supp}E
\iff
\text{对 }\lambda\text{ 的每个邻域 }U,\ E(U)\neq\mathbb{0}
$$

**这里的 $\mathbb{0}$ 指零算子，不是数 $0$**：$E(U)\neq\mathbb{0}$ 的意思是 $E(U)$ 不是零投影，即它的值域非平凡。**邻域可换成 $(\lambda-\varepsilon,\lambda+\varepsilon)$**，验算时更方便。

**为什么这个并是良好定义的**：$\mathbb{R}$ 是第二可数的，任一开集都是**有理端点开区间**的可数并。所以上面那个并只需取可数个基元素，**由可数可加仍是零测集**，其补集是闭集。

**要证两个方向。**

**（1）不在支撑里 ⇒ 不在谱里。** 若 $\lambda_0$ 有邻域 $U$ 使 $E(U)=\mathbb{0}$，则非零测度全落在 $U^{c}$ 上；而 $\lambda_0\notin U^{c}$（$U$ 开），故存在 $\delta>0$ 使

$$
\lvert\lambda-\lambda_0\rvert\ge\delta
\qquad(\lambda\in U^{c})
$$

由 §1 的 $(\ast)$ 式（取 $g(\lambda)=\lambda-\lambda_0$；$\psi\in D(\hat A)$ 正是它的定义域）：

$$
\lVert(\hat A-\lambda_0\mathbb{1})\psi\rVert^{2}
=\int(\lambda-\lambda_0)^{2}\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle
\ \ge\ \delta^{2}\lVert\psi\rVert^{2}
$$

这说明 $\lVert(\hat A-\lambda_0\mathbb{1})\psi\rVert/\lVert\psi\rVert$ 有下界 $\delta$，进而 $\hat A-\lambda_0\mathbb{1}$ **可逆、且逆有界**（逆是 $\int\frac{1}{\lambda-\lambda_0}dE(\lambda)$，范数 $\le1/\delta$）。所以 $\lambda_0\notin\sigma(\hat A)$。

**（2）在支撑里 ⇒ 在谱里。** 取 $B_n=(\lambda_0-\frac{1}{n},\lambda_0+\frac{1}{n})$，则 $E(B_n)\neq\mathbb{0}$；取单位向量 $\psi_n\in E(B_n)\mathcal{H}$。对 $\psi_n$，测度全落在 $B_n$ 上，故

$$
\lVert(\hat A-\lambda_0\mathbb{1})\psi_n\rVert^{2}
=\int_{B_n}(\lambda-\lambda_0)^{2}\,d\langle\psi_n\lvert E(\lambda)\lvert\psi_n\rangle
\ \le\ \frac{1}{n^{2}}
$$

于是 $(\hat A-\lambda_0\mathbb{1})\psi_n\to0$ 而 $\lVert\psi_n\rVert=1$。若存在有界逆 $R$，则

$$
1=\lVert\psi_n\rVert\le\lVert R\rVert\,\lVert(\hat A-\lambda_0\mathbb{1})\psi_n\rVert\le\frac{\lVert R\rVert}{n}\to0
$$

矛盾。所以 $\lambda_0\in\sigma(\hat A)$。

**合起来**：$\sigma(\hat A)=\operatorname{supp}E$。【证毕】

**顺带得到 $E(\sigma(\hat A))=E(\mathbb{R})$**：由可数可加与谱即支撑，

$$
E(\sigma(\hat A))=E(\mathbb{R})-E\bigl(\mathbb{R}\setminus\sigma(\hat A)\bigr)
=E(\mathbb{R})-E\bigl(\mathbb{R}\setminus\operatorname{supp}E\bigr)=E(\mathbb{R})
$$

最后一步因为 $\mathbb{R}\setminus\operatorname{supp}E$ 是**零测开集之并**，其投影为零。

---

## 3. 推论三：投影非零的独点就是点谱

**要证**：$E(\{\lambda\})\neq\mathbb{0}$ 的点就是**点谱**，且 $E(\{\lambda\})$ 是投影到该本征子空间的投影。要证的其实是等式

$$
\operatorname{ran}E(\{\lambda\})=\ker(\hat A-\lambda\mathbb{1})
$$

**左边是投影的值域，右边是本征子空间。** 两个方向各一条。

**方向一：$P\equiv E(\{\lambda\})\neq0$ ⇒ $\lambda$ 是本征值。** 取 $\psi\in\operatorname{ran}P$，$\psi\neq0$。对 $\psi$，测度全落在 $\{\lambda\}$ 上（因为 $(\mathbb{1}-P)\psi=0$），故

$$
\hat A\psi=\int_{\sigma(\hat A)}\lambda'\,dE(\lambda')\psi
=\lambda\int_{\sigma(\hat A)}dE(\lambda')\psi
=\lambda\mathbb{1}\psi=\lambda\psi
$$

**值域里的非零向量全是本征向量。**

**方向二：本征向量必被 $P$ 保留。** 若 $\hat A\psi=\lambda\psi$，则 $(\hat A-\lambda\mathbb{1})\psi=0$。用 §1 的 $(\ast)$ 式（取 $g(\lambda')=\lambda'-\lambda$）：

$$
0=\lVert(\hat A-\lambda\mathbb{1})\psi\rVert^{2}
=\int(\lambda'-\lambda)^{2}\,d\langle\psi\lvert E\lvert\psi\rangle
$$

**被积函数非负、积分零，故测度只落在 $\{\lambda\}$ 上**：$\langle\psi\lvert E(\{\lambda\})\lvert\psi\rangle=\lVert\psi\rVert^{2}$。由勾股（$E$ 与 $\mathbb{1}-E$ 正交）：

$$
\lVert(\mathbb{1}-E(\{\lambda\}))\psi\rVert^{2}
=\lVert\psi\rVert^{2}-\lVert E(\{\lambda\})\psi\rVert^{2}=0
$$

所以 $E(\{\lambda\})\psi=\psi$。

**两个方向合起来**：$\operatorname{ran}E(\{\lambda\})=\ker(\hat A-\lambda\mathbb{1})$。而 $E(\{\lambda\})$ 是**正交**投影，故它就是**投影到该本征子空间**的投影。

---

## 4. 推论四：乘法规则

根据投影值测度的**可数可加**与**其值就是投影**这两条性质，推出

$$
E(B)\,E(B')=E(B\cap B')
$$

**两步可证。**

**（1）不交的两个集合，其投影必然正交。** 若 $B,B'$ 不交，则由可数可加

$$
E(B)+E(B')=E(B\cup B')
$$

左边是两个投影之和，右边仍是一个投影。于是

$$
\begin{aligned}
&(P+Q)^{2}=P+Q &&\text{投影幂等}\\
\Longrightarrow\ &P^{2}+QP+PQ+Q^{2}=P+Q &&\text{展开}\\
\Longrightarrow\ &P+QP+PQ+Q=P+Q &&\text{投影幂等}\\
\Longrightarrow\ &QP+PQ=0 &&\text{化简}\\
\Longrightarrow\ &\begin{cases}PQP+PQ=0 & \text{左乘 }P\\ QP+PQP=0 & \text{右乘 }P\end{cases} &&\\
\Longrightarrow\ &PQ=QP &&\text{两式相减}\\
\Longrightarrow\ &PQ=QP=0 &&\text{代回 }QP+PQ=0
\end{aligned}
$$

**反之**：$PQ=QP=0$ 时 $(P+Q)^{2}=P^{2}+Q^{2}=P+Q$，仍是投影。

**所以两个投影之和仍是投影，当且仅当它们正交。**

**（2）一般情形靠拆分。** 把 $B$、$B'$ 各拆成"交集 + 差集"：

$$
B=(B\cap B')\sqcup(B\setminus B'),
\qquad
B'=(B\cap B')\sqcup(B'\setminus B)
$$

代入 $E(B)E(B')$ 展开，三个交叉项都含不交的集合对，由第（1）步全为零，只剩 $E(B\cap B')^{2}=E(B\cap B')$。【证毕】

---

## 5. 推论五：算子对角化

**要证**：当**谱简单**时，$\hat A$ **酉等价于"乘以 $\lambda$"**：

$$
\bigl(U\hat A\psi\bigr)(\lambda)=\lambda\,(U\psi)(\lambda)
$$

**换句话说**：换一组基之后，$\hat A$ 只做**乘法**——输入函数在 $\lambda$ 处的值，只决定输出在 $\lambda$ 处的值，**各点互不混合**。这就是"对角"的含义。

**所谓"谱简单"**，是指存在一个**循环矢量** $\psi_0\in\mathcal{H}$，使集合

$$
\mathcal{D}_0=\bigl\{f(\hat A)\psi_0\ \big|\ f\ \text{为}\ \sigma(\hat A)\ \text{上的有界 Borel 函数}\bigr\}
$$

在 $\mathcal{H}$ 中稠密。

**下面按"谱简单"这个前提，直接构造酉算子 $U$，再验证。**

**【证明】**

**第一步：构造标量测度与 $L^{2}$ 空间。** 由 §0 的标量测度 $\mu_{\psi_0}(B)=\langle\psi_0\lvert E(B)\lvert\psi_0\rangle$，它在 $\sigma(\hat A)$ 上给出总测度 $\lVert\psi_0\rVert^{2}<\infty$ 的正 Borel 测度。由此构造

$$
L^{2}\bigl(\sigma(\hat A),d\mu_{\psi_0}\bigr)
$$

**第二步：构造 $U_0$ 并证等距。** 对 $\phi=f(\hat A)\psi_0\in\mathcal{D}_0$，定义

$$
U_0:\ f(\hat A)\psi_0\ \longmapsto\ f(\lambda)
$$

计算两态的内积（用 §1 的函数演算）：

$$
\begin{aligned}
\langle f(\hat A)\psi_0,\;g(\hat A)\psi_0\rangle_{\mathcal{H}}
&=\langle\psi_0,\;f(\hat A)^{\dagger}g(\hat A)\psi_0\rangle_{\mathcal{H}}\\
&=\langle\psi_0,\;(\overline{f}g)(\hat A)\psi_0\rangle_{\mathcal{H}}\\
&=\int_{\sigma(\hat A)}\overline{f(\lambda)}\,g(\lambda)\,d\langle\psi_0\lvert E(\lambda)\lvert\psi_0\rangle\\
&=\int_{\sigma(\hat A)}\overline{f(\lambda)}\,g(\lambda)\,d\mu_{\psi_0}(\lambda)\\
&=\langle f,g\rangle_{L^{2}(d\mu_{\psi_0})}
\end{aligned}
$$

**这证明 $U_0$ 在稠密子空间上严格保持内积与范数（是等距映射）。**

**第三步：连续延拓为酉算子 $U$。** 因为 $\mathcal{D}_0$ 在 $\mathcal{H}$ 中稠密，且有界 Borel 函数在 $L^{2}$ 中也稠密，故 $U_0$ 唯一延拓为

$$
U:\ \mathcal{H}\ \longrightarrow\ L^{2}\bigl(\sigma(\hat A),d\mu_{\psi_0}\bigr)
$$

的**酉算子**。

**第四步：验证算子变乘法。** **先取紧支撑的有界 Borel 函数 $f$**——此时 $\lambda f(\lambda)$ 也有界，$\psi=f(\hat A)\psi_0$ 与 $\hat A\psi$ 都落在 $\mathcal{D}_0$ 里，可以用"$\lambda f(\lambda)$ 对应 $\hat A f(\hat A)$"这条规则（$\operatorname{id}(\lambda)=\lambda$）：

$$
\hat A\psi=\hat A f(\hat A)\psi_0=(\operatorname{id}\cdot f)(\hat A)\psi_0
$$

经 $U$ 映射：

$$
\bigl(U\hat A\psi\bigr)(\lambda)
=U\bigl((\operatorname{id}\cdot f)(\hat A)\psi_0\bigr)(\lambda)
=\lambda f(\lambda)
=\lambda\,(U\psi)(\lambda)
$$

**再由闭性延拓到全定义域。** 这类紧支撑态在 $D(\hat A)$ 中按图范数稠密（用谱截断逼近），而 $\hat A$ 与 $M_\lambda$ 都是闭算子，故

$$
U\hat A\,U^{\dagger}=M_\lambda
\qquad
D(M_\lambda)=\bigl\{h\in L^{2}(d\mu_{\psi_0}):\ \lambda h\in L^{2}(d\mu_{\psi_0})\bigr\}
$$

（乘以 $\lambda$ 的乘法算子，定义域如右）。对投影 $E(B)$ 同理：

$$
\bigl(UE(B)\psi\bigr)(\lambda)=\mathbf{1}_B(\lambda)\,(U\psi)(\lambda)
$$

【证毕】

**为什么需要"谱简单"**：要让 $U$ 翻译出所有向量，就需要 $\psi_0$ 在**每个本征方向都有分量**。**若某个本征值有二重以上的重数，一个 $\psi_0$ 覆盖不了**，只能每个本征空间各取一个，得到直和形式：

$$
\hat A\ \cong\ \bigoplus_iM_\lambda
\qquad\text{在}\quad\bigoplus_iL^{2}\bigl(\sigma(\hat A),\mu_i\bigr)\ \text{上}
$$

**地位**：它是谱定理的推论，**但多一个前提**——存在循环矢量（谱简单）。**直和版**不需要这个前提，仍是纯推论；**"一次换基就够"才是简单谱带来的细化**。

**为什么这条有用**：在这个模型里，前四条都变成"函数上的算术"——$f(\hat A)$ 是乘以 $f(\lambda)$，$E(B)$ 是乘以指示函数 $\mathbf{1}_B$，$\int dE=\mathbb{1}$ 是"乘以 $1$ 是恒等"。**"让 $\hat q$ 对角"这句话的严格含义，就是这个。**

---

## 6. 边界

1. **连续谱时不给本征矢。** 对连续谱的每个单点，$E(\{q\})=\mathbb{0}$，于是**不存在** $\psi\in\mathcal{H}$ 满足 $\hat A\psi=q\psi$。谱定理给的是"一族投影"，不是"一族向量"——要矢，得请出核空间谱定理（下一张卡）。
2. **不告诉你谱是什么。** 定理对**任何**自伴算子都成立，所以它对"$\hat q$ 的谱是 $\mathbb{R}$ 还是格点"一无所知。谱由你选的算子与边界条件决定。
3. **不固定归一化。** 广义本征矢的归一化系数是约定，不在本卡。
4. **算子对角化需要"谱简单"。** 有重数时只能退成直和形式（§5）。

---

## 7. 自检

- [ ] 说出谱定理的两条内容，以及 $E(\mathbb{R})=\mathbb{1}$ 与 $E(\sigma(\hat A))=\mathbb{1}$ 的区别
- [ ] 说清三个对象：Borel 集 $B$、投影 $E(B)$、投影值测度 $E$
- [ ] 写出 $(\ast)$ 式，并说明它为什么让"定义域"变成"右边有限"
- [ ] 证明 $\sigma(\hat A)=\operatorname{supp}E$ 的两个方向
- [ ] 证明 $\operatorname{ran}E(\{\lambda\})=\ker(\hat A-\lambda\mathbb{1})$
- [ ] 用"两个投影之和仍是投影"推出乘法律
- [ ] 说出对角化模型里的 $U$ 是怎么构造的，以及"谱简单"在哪一步用上
