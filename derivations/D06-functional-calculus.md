# D06 · 函数演算：$f(\hat A)$ 到底是什么意思

> 建档 2026-11-06 · 类型：**定义 + 性质**——定义 $f(\hat A)$，并列出下游要用的运算规则；
> 其中**谱映射定理与范数公式是定理**，不是定义的复述
> 上游：[D01](D01-spectral-theorem.md)
> 下游：[D08](D08-commutator-p-fq.md)、[D11](D11-hadamard-lemma.md)、[D13](D13-commutator-phase.md)、[D14](D14-three-bch-forms.md)、[D15](D15-weyl-phase.md)、[D16](D16-translation.md)、[D17](D17-qp-overlap.md)、[D20](D20-hamiltonian.md)、[D26](D26-energy-basis.md)
> 原散见于 [N003 §4.1](../notes/N003-basis-and-operator-relations.md) 与各卡片的"条件"里，2026-11-06 汇总成卡。

---

## 0. 命题

设 $\hat A$ 是**自伴**算子。$f(\hat A)$ 有**两种独立的定义**，外加**一种特化**；两种定义在交集上的一致性是**定理**：

| 写法 | 逻辑地位 | 适用的 $f$ | 用在哪 |
|---|---|---|---|
| 幂级数 | **定义**（不需谱定理） | 解析函数 | [D11](D11-hadamard-lemma.md) 的 $e^{tA}$、[D13](D13-commutator-phase.md) 的 $e^{B}$ |
| 谱分解 | **定义**（典范，需 D01） | Borel 可测函数（最一般） | 一般 $f$，包括不可微的 |
| 本征基展开 | **特化**（不是独立定义） | 谱简单时的连续函数 | [D08](D08-commutator-p-fq.md)、[D17](D17-qp-overlap.md) |
| 两者一致 | **定理**（§1.4） | 解析函数 | 使记号 $f(\hat A)$ 不歧义 |

**它在讲什么**："把函数作用在算子上"不是符号游戏，而是一个**有唯一答案**的操作——但先决条件是 $\hat A$ 自伴。非自伴的算子没有这套东西。

---

## 1. 两种定义、一种特化

**先给结论**，免得把四件事混成一类：

| 写法 | 逻辑地位 | 依赖 | 覆盖范围 |
|---|---|---|---|
| 1.1 幂级数 | **定义**（独立） | 只要算子的乘与加 | 解析函数 |
| 1.2 谱分解 | **定义（典范）** | [D01](D01-spectral-theorem.md) 谱定理 | Borel 函数 |
| 1.3 本征基展开 | **特化**，不是独立定义 | [D01](D01-spectral-theorem.md)、[D03](D03-position-eigen-equation.md)、[D04](D04-normalization-convention.md) | 简单谱 + 密度为 $1$ |
| 1.4 两者一致 | **定理** | 1.1、1.2 | 交集（解析函数） |

**为什么 1.1 是"独立的定义"**：它只用 $\hat A$ 的乘法和加法，**完全不提谱测度**。所以它先于谱定理就成立——这是它与 1.2 并列的唯一理由。

**为什么 1.2 是"典范"**：$E$ 由 $\hat A$ 唯一确定，且覆盖**全部**可测函数；1.1 与 1.3 都是它在某个子类上的等价写法。

---

### 1.1 幂级数（解析函数）

$$
f(\hat A)\equiv\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}\,\hat A^{n}
$$

**这是一个定义**——不需要谱定理，只需要算子能相乘相加、级数能收敛。

- $\hat A$ **有界**时，只要 $\lVert\hat A\rVert<R$（$R$ 为收敛半径），级数按算子范数绝对收敛；
- $\hat A$ **无界**时，级数只是形式记号，严格定义要靠解析向量（analytic vectors）上的强收敛延拓。

**这个定义的局限**：只覆盖解析函数。$1/x$、$\sqrt{x}$、$\ln x$ 不在其中，$e^{-1/x^{2}}$ 这类非解析函数也不在。

### 1.2 谱分解（最一般）

由**谱定理**，自伴 $\hat A$ 唯一对应一个投影值测度 $E$，使

$$
\hat A=\int_{\sigma(\hat A)}\lambda\;dE(\lambda),
\qquad
f(\hat A)\equiv\int_{\sigma(\hat A)}f(\lambda)\;dE(\lambda)
$$

**这也是一个定义**，但它的前提比 1.1 重——必须先有谱定理，$E$ 才存在。

其中 $f$ 是 $\sigma(\hat A)$ 上的有界 Borel 函数；$f$ 无界时，定义域收窄为

$$
D\bigl(f(\hat A)\bigr)=\Bigl\{\psi\;\Big|\;\int\lvert f(\lambda)\rvert^{2}\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle<\infty\Bigr\}
$$

**这是唯一覆盖全部"可测函数"的定义**。

### 1.3 本征基展开（谱简单时）

若 $\hat A$ 的谱简单、绝对连续，且已有 $\delta$ 归一化的广义本征矢 $\lvert a\rangle$（[D17](D17-qp-overlap.md) 的兄弟情形），则

$$
f(\hat A)=\int da\;f(a)\,\lvert a\rangle\langle a\rvert
$$

**这不是独立的定义**，是 1.2 在"谱简单"下的特化：把 $dE(\lambda)$ 写成 $\lvert\lambda\rangle\langle\lambda\rvert\,d\lambda$。**所以它不需要自己的相容性证明**——一致性自动继承自 1.2。

**这就是 [D08](D08-commutator-p-fq.md) 与 [N003 §4.1](../notes/N003-basis-and-operator-relations.md) 一直用的形式。**

**注意**：这个写法隐含条件"归一化密度为 $1$"，即谱测度对 Lebesgue 测度的密度为 $1$。弯曲空间里密度是 $\sqrt{g}$，$dE$ 与 $\lvert a\rangle\langle a\rvert\,da$ 之间会差一个因子（见 [D16](D16-translation.md) 的同期讨论与 [D22](D22-trace-is-loop.md) §3 的测度问题）。

### 1.4 两者为什么一致（这是一条定理）

**要证的事**：对解析 $f$（收敛半径 $R>\lVert\hat A\rVert$），

$$
\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}\,\hat A^{n}
=\int f(\lambda)\,dE(\lambda)
$$

**两步。**

#### 第一步：多项式上逐项相等

这一步的全部内容是**矩性质**：

$$
\int\lambda^{n}\,dE(\lambda)=\hat A^{n}
$$

**它在说什么**：乘方只作用在**权重** $\lambda$ 上，不作用在**投影** $E$ 上。

**有限维一眼可见**。若 $\hat A=\sum_i a_i\lvert i\rangle\langle i\rvert$，则

$$
\hat A^{2}=\sum_i a_i^{2}\lvert i\rangle\langle i\rvert,
\qquad
\int\lambda^{2}\,dE=\sum_i a_i^{2}\lvert i\rangle\langle i\rvert
$$

两边相同。取 $\hat A=\mathrm{diag}(2,3)$ 手验：

$$
\int\lambda^{2}dE=4E(\{2\})+9E(\{3\})=\mathrm{diag}(4,9)=\hat A^{2}
$$

**一般情形靠投影的乘法律**：

$$
E(B)E(B')=E(B\cap B')
\quad\Longrightarrow\quad
\Bigl(\int f\,dE\Bigr)\Bigl(\int g\,dE\Bigr)=\int fg\,dE
$$

取 $f=g=\mathrm{id}$（即 $f(\lambda)=\lambda$）并重复 $n$ 次：

$$
\int\lambda^{n}dE
=\underbrace{\Bigl(\int\lambda\,dE\Bigr)\cdots\Bigl(\int\lambda\,dE\Bigr)}_{n\text{ 个}}
=\hat A^{n}
$$

第一个等号用谱定理 $\hat A=\int\lambda\,dE$，第二个用上面的乘法律。

**不循环**：这条只用到谱定理与投影性，**与幂级数定义无关**——幂级数在这段论证里根本不出场。

**有了矩性质，多项式就逐项相等**。对 $p(\lambda)=\sum_{n\le N}c_n\lambda^{n}$：

$$
\int p\,dE=\sum_{n\le N}c_n\int\lambda^{n}dE=\sum_{n\le N}c_n\hat A^{n}=p(\hat A)
$$

**多项式情形不需要任何极限论证。**

#### 第二步：把"逐项相等"抬到"极限相等"

关键是**有界函数演算是保范的**：

$$
\Bigl\lVert\int g\,dE\Bigr\rVert=\sup_{\lambda\in\sigma(\hat A)}\lvert g(\lambda)\rvert
$$

（这就是 §2.3 的范数公式。）它保证：**若 $g_N\to g$ 在谱上一致收敛，则 $\int g_N\,dE\to\int g\,dE$ 按算子范数收敛。**

现在两边的级数都满足这个条件：

- **谱侧**：$\sigma(\hat A)\subseteq[-\lVert\hat A\rVert,\lVert\hat A\rVert]$，而 $R>\lVert\hat A\rVert$，故幂级数在谱上一致收敛：$\sup_{\sigma}\lvert f-p_N\rvert\to0$。由保范性，$\int p_N\,dE\to\int f\,dE$。
- **代数侧**：同样的 $\lVert\hat A\rVert<R$ 保证 $\sum c_n\hat A^{n}$ 按算子范数收敛，而它的部分和正是 $p_N(\hat A)$。

**部分和恒等（第一步），且两边都收敛（第二步），故极限相同。证毕。**

#### 一句话概括

**多项式上逐项相等 + 有界函数演算保范 $\Rightarrow$ 极限上相等。**

**两条缺一不可**：没有"保范"，一致收敛传不过去；没有"逐项相等"，起点就断了。

**这也说明：一致性是定理，不是定义的一部分。** 两个处方各自独立成立，**恰好**在解析函数上给出同一个算子——正因为如此，记号 $f(\hat A)$ 才不歧义。

**边界**：这套论证用算子范数与谱上的 $\sup$，所以直接结论只对**有界** $\hat A$ 成立。$\hat A$ 无界时，幂级数只是形式记号，一致性要在**解析向量**上逐点成立（§1.1 的注）。

---

## 2. 六条性质：两条来自定义，两条来自谱映射，两条要证

读者容易把六条当成同等分量。**其实只有两条是真定理**。分清之后，该记的记、该查的查。

### 2.1 由定义直接得到（两条）

| 性质 | 内容 | 为什么"直接" |
|---|---|---|
| 同态 | $(fg)(\hat A)=f(\hat A)\,g(\hat A)$ | 同一个 $E$：$\int f g\,dE=\bigl(\int f\,dE\bigr)\bigl(\int g\,dE\bigr)$ |
| 与自变量对易 | $[f(\hat A),\hat A]=0$ | 两者用同一个 $E$，投影互相交换 |

**这两条不需要证**：它们是"同一族投影"的直接算术。**注意同态只对同一个算子的函数成立**——$f(\hat A)g(\hat B)\neq g(\hat B)f(\hat A)$，除非 $\hat A,\hat B$ 对易。

### 2.2 由谱映射读出（两条）

| 判据 | 内容 |
|---|---|
| 自伴 | $f(\hat A)$ 自伴 $\iff$ $f$ 在谱上取实值 |
| 酉 | $f(\hat A)$ 酉 $\iff$ $\lvert f\rvert=1$ 在谱上 |

**这两条不是新定理**：把它们代进 $\sigma(f(\hat A))=f(\sigma(\hat A))$ 就直接读出来。所以它们的分量取决于 §2.3 那条谱映射。

### 2.3 需要证明的两条

| 定理 | 内容 | 证明思路 |
|---|---|---|
| **谱映射** | $\sigma\bigl(f(\hat A)\bigr)=f\bigl(\sigma(\hat A)\bigr)$（$f$ 连续） | 若 $\lambda_0\notin f(\sigma)$，则 $1/(f-\lambda_0)$ 在谱上有界，用函数演算造出有界逆 ⇒ $\lambda_0$ 不在谱里；反向由 $f$ 的连续性 |
| **范数公式** | $\lVert f(\hat A)\rVert=\sup_{\lambda\in\sigma(\hat A)}\lvert f(\lambda)\rvert$ | C\*-恒等式；等价说法："算子多大，就是函数多大" |

**谱映射是最有用的一条**：它把"算子是否有界/自伴/酉"变成"函数在谱上是否有界/实/模 $1$"。例如 $\hat A$ 自伴 $\Rightarrow$ $e^{i\hat A}$ 是酉算子，用的就是它。

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| $f(\lambda)=1$ | 三个定义都给 $\mathbb{1}$ ✅ |
| $f(\lambda)=\lambda$ | 三个定义都给 $\hat A$ ✅ |
| $f(\lambda)=\lambda^{n}$ | 都给 $\hat A^{n}$ ✅ |
| $f(\lambda)=e^{i\lambda}$，$\hat A$ 自伴 | $\lvert e^{i\lambda}\rvert=1$，故 $e^{i\hat A}$ 酉 ✅ |
| $f(\lambda)=e^{-\beta\lambda}$，$\hat A$ 有下界 | $f$ 有界，$\lVert e^{-\beta\hat A}\rVert\le1$ ✅ |
| 与 [D11](D11-hadamard-lemma.md) 相容 | $e^{tA}$ 是整函数，幂级数定义收敛半径无穷 ✅ |

---

## 4. 备注与边界

1. **自伴是前提。** 非自伴算子（如 Jordan 块）没有谱定理，只能用 Dunford 演算，且只对"谱点附近解析"的函数有定义。**这一条决定了整套量子力学为什么要求可观测量自伴。**
2. **幂级数定义不能推得太远。** $1/\hat A$、$\sqrt{\hat A}$、$\ln\hat A$ 都要走谱分解；用幂级数硬写会发散或给出错误结果。
3. **$f'(\hat A)$ 是对函数求导。** 常见混淆：$\frac{d}{d\hat A}f(\hat A)$ 这种写法不是"对算子求导"，而是"先对函数求导、再作函数演算"（[D08](D08-commutator-p-fq.md) §4 讨论过这个措辞）。
4. **"同一个算子的函数"这个限制很紧。** $f(\hat A)+g(\hat B)$ 没有简单规则；两套函数演算要合并，必须先证明 $\hat A,\hat B$ 对易。
5. **无界时定义域要说清。** $e^{tA}$ 对无界 $A$ 在解析向量上有定义，但"处处成立"不成立。这是 [D11](D11-hadamard-lemma.md) §3 第 3 条的来源。

---

## 5. 自检

- [ ] 说出哪两个是定义、哪个只是特化，各需要什么前提
- [ ] 复述一致性的两步：多项式逐项相等、保范性把极限抬上去
- [ ] 用谱映射定理证明：$\hat A$ 自伴 $\Rightarrow$ $e^{i\hat A}$ 酉
- [ ] 把六条性质分成三组：定义直接给的两条、由谱映射读出的两条、要证的两条
- [ ] 举一个不能用幂级数定义的函数，并说明该走哪条定义
- [ ] 解释 $\lVert f(\hat A)\rVert=\sup\lvert f\rvert$ 是从哪来的
- [ ] 说明为什么非自伴算子没有这套演算
