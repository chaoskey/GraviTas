# N005 · 单粒子量子力学的算子地基

> 写于 2026-11-08 · 关联：全部 27 张推导卡片（[D00](../derivations/D00-commutator-axiom.md)–[D26](../derivations/D26-energy-basis.md)），网格见 [derivations/README](../derivations/README.md)
> 目标：把网格里的**所有结论**用白话讲一遍。**不证**——证明在卡片里，这里只讲"它在说什么""它用在哪""坑在哪"。
> 用途：读完这一页，应当能独立复述每一条结论，并知道去哪找它的证明。
> 约定：$\hbar=1$、$k_{\mathrm{B}}=1$；$[\hat q,\hat p]=i$；$q$ 既是坐标也是本征值，需要第二个位置标签时用 $q'$。

---

## 0. 全景：一句话与一张图

**一句话**：从一条对易关系出发，造出"能测的量"，最后把它算成一个"温度"。

**四层结构**：

- **公理**：D00 对易关系（附：谱与自伴的定义、接口约定）；D02 态与 Born 规则。
- **地基**：D01 谱定理 → D03 位置本征方程 → D04 归一化；另有 D02 Born 规则、D05 函数演算、D06 迹、D15 唯一性。
- **代数**：D07 对易子 → D10 Hadamard → D11 两项截断 → D12 交换相位 → D13 三条 BCH；另有 D08 对角判据、D09 乘积的核、D25 不确定关系。
- **表象**：D14 Weyl 相位 → D16 平移 → D17 平面波 → D18 动量完备性 → D19 动量表象。
- **统计**：D20 Hamiltonian → D21 路径积分 → D22 迹即闭合路径 → D23 密度矩阵与配分函数 → D26 能级展开 → D24 温度即周期倒数。

**读法**：每一节先给一句白话，再给式子，再给"卡片出处"。**卡片的编号即拓扑序**——任何一张的输入都比它自己小。

---

## 1. 输入：一条公理、一条接口、一条测量规则

### 1.1 对易关系（[D00](../derivations/D00-commutator-axiom.md)）

$$
[\hat q,\hat p]=i
$$

**白话**：位置与动量这两个量，不能同时被确定——这一条不是推出来的，是**输入**。

**它为什么是公理**：既不是定理（推不出来），也不是定义（$\hat q,\hat p$ 已由"可观测量 = 自伴算子"确定了，对易子是**额外**加的一条）。它是量子化的**唯一**输入项。

**顺带把另一条接口点名**：**可观测量对应自伴算子**。这不是推出来的，也不是定义能给的——它是量子力学与数学之间的接口（数学上只有自伴算子保证谱是实数，物理要求测量读数是实数）。**本笔记把它当定义接受。**

**它有严格版本**，叫 Weyl 关系（见 §4.1）：指数化之后两边都是有界算子，避开无界算子的定义域麻烦。**两个方向不对称**：Weyl 能推出对易子，反过来不行（除非再补"自伴 + 公共不变域 + 强连续"）。

### 1.2 态与测量：Born 规则（[D02](../derivations/D02-born-rule.md)）

**先说什么叫“态”**：态是**射线**，不是矢量——$\lvert\psi\rangle$ 与 $c\lvert\psi\rangle$ 给同一组概率（乘 $c$ 只把权重放大 $\lvert c\rvert^{2}$，没有测量能察觉）。写 $\langle\psi\lvert\psi\rangle=1$ 只是**挑代表元**：等价类里的元素长短不一，挑单位长那个。这不是装饰——$p(\mathbb{R})=\langle\psi\lvert\psi\rangle$，**要概率总和为 $1$ 就必须归一**。

**白话**：谱定理告诉你"$\hat A$ 是一堆投影拼起来的"——那是**算子**，不含态的信息；Born 规则告诉你：**把投影夹在 $\langle\psi\lvert$ 与 $\lvert\psi\rangle$ 之间**，得到的数才是概率。

三种对象要分清：$E(B)$ 是**算子**（谱定理给），$\langle\psi\lvert E(B)\lvert\psi\rangle$ 是**数**（Born 规则给），$d\langle\psi\lvert E(\lambda)\lvert\psi\rangle$ 是**测度**（夹取后的密度形式）。

**三条的地位不同**：态是**定义**（射线 + 归一化），$p(B)$ 是**公理**，期望值 $\langle\hat A\rangle=\langle\psi\lvert\hat A\lvert\psi\rangle$ 是**定理**（把 Born 代进期望值的定义、再用谱分解即得）。**本卡真正的输入只有一条。**

**别把公理说成“$E(B)$ 的期望值”**：$E(B)$ 的期望由上面的公式算出，是**定理**；Born 规则真正加的是“**这个数就是概率**”。

$$
p(B)=\langle\psi\lvert E(B)\lvert\psi\rangle,
\qquad
\langle\hat A\rangle=\langle\psi\lvert\hat A\lvert\psi\rangle
$$

**三条直接后果**：

- 若 $\lvert\psi\rangle$ 是 $\hat A$ 的本征态，则必得该本征值（概率 1）——**点谱**才成立（连续谱时 $E(\{q\})=0$）。矢量式与数值式等价：$E(\{a\})\lvert\psi\rangle=\lvert\psi\rangle \iff \langle\psi\lvert E(\{a\})\lvert\psi\rangle=1$；
- 概率归一：因为 $E(\mathbb{R})=\mathbb{1}$；
- 期望值就是那个双线性形式。

**它不管什么**：不管"为什么是概率"、不管坍缩。坍缩（测量后态变成 $E(B)\lvert\psi\rangle/\sqrt{p}$）是**额外**假设，不用它也能算期望值。

---

## 2. 地基：让算子"可算"

### 2.1 谱定理（[D01](../derivations/D01-spectral-theorem.md) §1）

**白话**：任何一个自伴算子，都能拆成一族**互相垂直的投影**，权重是它的谱。

$$
\hat A=\int_{\sigma(\hat A)}\lambda\,dE(\lambda),
\qquad
\int dE(\lambda)=E(\mathbb{R})=\mathbb{1}
$$

**两条性质就是定理的全部内容**：投影拼回整个空间；算子按权重把投影加起来。

**它还给三样东西**（下游天天用）：

- **函数演算**：$f(\hat A)=\int f(\lambda)\,dE(\lambda)$——把谱上的 $\lambda$ 换成 $f(\lambda)$；$f$ 无界时按定义域 $\int\lvert f\rvert^{2}d\langle\psi\lvert E\lvert\psi\rangle<\infty$ 理解；
- **谱的位置**：$\sigma(\hat A)$ 是 $E$ 的**支撑**（每个邻域里 $E$ 都不为零）；$E(\{\lambda\})\neq0$ 的点是**点谱**；
- **乘法律**：$E(B)E(B')=E(B\cap B')$。**它不是假设**——定义只要"可数可加 + 值是投影"，不交时两投影之和仍是投影，逼出正交，再由拆分得到交集律。

**它不给什么**（很重要）：

| 不给 | 后果 |
|---|---|
| 连续谱时不给本征矢 | $E(\{q\})=0$，所以不存在平方可积的 $\psi$ 满足 $\hat q\psi=q\psi$ |
| 不告诉你谱是什么 | 谱由你选的算子与边界条件决定 |
| 不固定归一化 | 系数是约定 |

**顺手一句**：定义域那串条件不是物理，只是"权重太大会发散，定义域要挑"——**收敛性的记账**。

### 2.2 核空间谱定理（[D01](../derivations/D01-spectral-theorem.md) §2）

**白话**：谱定理给了"一族投影"，但我们要的是"一族**矢**"（$\lvert q\rangle$）。办法是把它们请出希尔伯特空间——搬到外面去住。

**条件**：$\hat A$ 自伴；$\Phi$ 是核空间、连续稠密地嵌进 $\mathcal{H}$；且 $\hat A$ **不把好函数弄坏**，即 $\hat A\Phi\subset\Phi$。

**结论一：本征方程。** 存在一族广义本征矢 $F_\lambda\in\Phi^{\times}$，使

$$
\hat A F_\lambda=\lambda F_\lambda
$$

**结论二：完备性。** 存在谱测度 $\mu$，使对任意 $\phi,\psi\in\Phi$，

$$
\langle\phi\lvert\psi\rangle=\int\langle\phi\lvert F_\lambda\rangle\,\langle F_\lambda\lvert\psi\rangle\;d\mu(\lambda)
\qquad\Longleftrightarrow\qquad
\mathbb{1}=\int\lvert F_\lambda\rangle\langle F_\lambda\rvert\;d\mu(\lambda)
$$

**这两条就是全部结论，但有两点要看清**：

- $F_\lambda$ 住在 $\Phi^{\times}$，**不在 $\mathcal{H}$ 里**——这才是"广义"二字的全部含义；
- $\mu$ 是**谱测度**，不一定是 Lebesgue。把它选成 $dq$ 是后来的约定（[D03](../derivations/D03-position-eigen-equation.md) §1.2）。

**为什么需要三层结构**：定理里的 $F_\lambda$ 不在 $\mathcal{H}$ 里，得给它安排一个能住的地方。

$$
\Phi\;\subset\;\mathcal{H}\;\subset\;\Phi^{\times}
$$

| 层 | 是什么 | 在做什么 |
|---|---|---|
| $\Phi$ | 好函数（Schwartz 函数） | **测试探针** |
| $\mathcal{H}$ | 平方可积函数 | **态** |
| $\Phi^{\times}$ | 连续线性泛函 | **广义对象**：$\lvert q\rangle$ 住这 |

**为什么不能省中间层**：$\lvert q\rangle$ 干的是"在 $q$ 点取值"。对 $L^{2}$ 函数这没意义（改一个点，态不变）。

**为什么不能省外层**：取值在 $\mathcal{H}$ 上**不连续**（函数可以一点很高、范数很小），所以它不是矢量，是泛函。

**一句话记住三层**：$\lvert q\rangle$ 是**"取值"这个动作的严格化身**。

### 2.3 位置本征方程（[D03](../derivations/D03-position-eigen-equation.md)）

**白话**：把 2.2 的定理取 $\hat q$，就得到位置基。**位置基的"三件套"里有两条出在本卡**：

$$
\hat q\lvert q\rangle=q\lvert q\rangle,
\qquad
\mathbb{1}=\int\lvert q\rangle\langle q\rvert\,dq,
\qquad
\hat q=\int q\,dq\,\lvert q\rangle\langle q\rvert
$$

**证明只有一步**：取 $\hat A=\hat q$、$F_\lambda=\lvert q\rangle$、$\lambda=q$。

**归属**：本征方程与**完备性**（中间那条）都在本卡（D03 §1.2）；第三件"正交归一的系数"属于 [D04](../derivations/D04-normalization-convention.md)。**完备性不在 D04，别去那里找。**

**唯一的选择**：定理给的测度是 $d\mu$，写成 $dq$ 是**我们选的**（等价于固定 $\lvert q\rangle$ 的尺度）。

### 2.4 归一化（[D04](../derivations/D04-normalization-convention.md)）

$$
\langle q\lvert q'\rangle=\delta(q-q')
$$

**完备性那一半在 §2.3**（属于 D03），本节不重复。这里只管**正交归一的系数**，并说明它必须与 D03 的完备性权重配对：

| 成分 | 地位 |
|---|---|
| 为什么是 $\delta$（不是别的函数） | **被迫**：投影测度的投影性推出来的 |
| $\delta$ 前系数为什么是 1 | **选的**：与 D03 的完备性权重配对，$w\,c=1$ |

**系数与权重必须一起改**（否则 $w\,c=1$ 不成立）。两套常用方案：

| 方案 | $\langle q\lvert q'\rangle$ | $\langle p\lvert p'\rangle$ | $\langle q\lvert p\rangle$ |
|---|---|---|---|
| 本仓库 | $\delta(q-q')$ | $2\pi\delta(p-p')$ | $e^{ipq}$ |
| 对称（数学） | $\delta(q-q')$ | $\delta(p-p')$ | $e^{ipq}/\sqrt{2\pi}$ |

**混用必错**，且错得不显眼（只差 $\sqrt{2\pi}$ 的因子）。

### 2.5 函数演算（[D05](../derivations/D05-functional-calculus.md)）

**白话**：把函数作用在算子上，就是"**把谱上的 $\lambda$ 换成 $f(\lambda)$**"。
$$
f(\hat A)=\int f(\lambda)\,dE(\lambda),
\qquad
f(\hat q)=\int dq\,f(q)\,\lvert q\rangle\langle q\rvert
$$

**两种定义 + 一种特化**——**幂级数与谱分解是并列的两个定义**（前者不需要谱定理），本征基展开只是后者的特化：

1. **幂级数**（**定义**，不需要谱定理）：只对解析函数、收敛半径内有效；
   $$
   f(\hat A)\equiv\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}\,\hat A^{n}
   $$
   
2. **谱分解**（**定义**，需谱定理，最一般）：
   $$
   \hat A=\int_{\sigma(\hat A)}\lambda\;dE(\lambda),
   \qquad
   f(\hat A)\equiv\int_{\sigma(\hat A)}f(\lambda)\;dE(\lambda)
   $$
   
3. **本征基展开**（**不是独立定义**，是第 2 条的"简单谱"特化）：谱简单时的显式形式，实际计算用这个。
   $$
   f(\hat A)=\int da\;f(a)\,\lvert a\rangle\langle a\rvert
   $$
   

**两个定义为什么一致（这是定理，不是定义的复述）**：

- **第一步**：多项式上逐项相等——由矩性质 $\int\lambda^{n}dE=\hat A^{n}$（乘方只落在权重上，就是 [D01](../derivations/D01-spectral-theorem.md) §1.1 的 $f$ 公式取 $f(\lambda)=\lambda^{n}$；[D05](../derivations/D05-functional-calculus.md) §1.4 把它推广到一般函数）；
- **第二步**：有界函数演算**保范** $\lVert\int g\,dE\rVert=\sup_{\sigma}\lvert g\rvert$，故"谱上一致收敛"传到"算子范数收敛"。

**部分和恒等 + 两边都收敛 ⇒ 极限相同。** 缺"保范"传不过去，缺"逐项相等"起点就断。

**六条性质，分量不同**：

| 组 | 内容 |
|---|---|
| 定义直接给（两条） | 同态 $(fg)(\hat A)=f(\hat A)g(\hat A)$；$[f(\hat A),\hat A]=0$ |
| 由谱映射读出（两条） | $f(\hat A)$ 自伴 $\iff$ $f$ 实值；$f(\hat A)$ 酉 $\iff$ $\lvert f\rvert=1$ |
| 要证（两条） | 谱映射 $\sigma(f(\hat A))=f(\sigma(\hat A))$；范数 $\lVert f(\hat A)\rVert=\sup\lvert f\rvert$ |

**前提是 $\hat A$ 自伴**。非自伴没有谱定理，只有 Dunford 演算——**这就是量子力学要求可观测量自伴的数学理由**。

### 2.6 迹（[D06](../derivations/D06-trace.md)）

**白话**：迹就是"对角元之和"，而且**跟选哪组基无关**。

$$
\mathrm{Tr}\,\hat A=\sum_n\langle n\lvert\hat A\lvert n\rangle
=\int dq\,\langle q\lvert\hat A\lvert q\rangle
=\int\frac{dp}{2\pi}\,\langle p\lvert\hat A\lvert p\rangle
$$

**基无关是证出来的**：插入两组完备性，用 $\langle q\lvert p\rangle=e^{ipq}$ 让积分塌成 $\delta$。

**四条性质**：线性、循环 $\mathrm{Tr}(AB)=\mathrm{Tr}(BA)$、正定、相似不变。

**循环性是后面"把路径两端焊起来"的前提**——$e^{-\beta H}$ 的迹不依赖切点放在哪。

---

### 2.7 表示唯一性（[D15](../derivations/D15-stone-von-neumann.md)）

**白话**：给定 $[\hat q,\hat p]=i$，有限自由度下"位置与动量算子"**只有一套**——差一个换基。

三个词要先懂：

- **表示**：把抽象的对易关系落到具体空间与算子上；
- **不可约**：不能拆开（可约 = 几份拷贝堆在一起）；
- **酉等价**：差一个保长度的换基，物理一样。

**它意味着**：$\hat q\to q$、$\hat p\to-i\partial_q$ 不是"挑了个方便的"，是**唯一**的选择（差等价）。所以 D17 的平面波是**定理**不是约定。

**它何时失效**：无穷自由度（量子场论）——表示不唯一，Fock 只是一个选择，真空/热态/$\theta$ 真空互不等价。

## 3. 算子代数：算子的"四则运算"

### 3.1 对易子公式（[D07](../derivations/D07-commutator-p-fq.md)）

$$
\bigl[\hat p,f(\hat q)\bigr]=-i\,f'(\hat q)
$$

**白话**：$\hat p$ 作用在"$\hat q$ 的函数"上，等于求导。

**镜像版**：$[\hat q,g(\hat p)]=i\,g'(\hat p)$，符号相反——**这是最常见的错处**。

**Jacobi 恒等式**（同卡）：

$$
\bigl[A,[B,C]\bigr]+\bigl[B,[C,A]\bigr]+\bigl[C,[A,B]\bigr]=0
$$

所有推导都默认它在用；$\mathrm{ad}_A$ 能当"求导"使，靠的就是这一条。

### 3.2 对角判据（[D08](../derivations/D08-diagonal-criterion.md)）

$$
\bigl[\hat q,f(\hat q)\bigr]=0
\quad\Longrightarrow\quad
\langle q'\lvert f(\hat q)\lvert q''\rangle=f(q')\,\delta(q'-q'')
$$

**白话**：**与 $\hat q$ 对易的算子，在 $q$ 基下必然对角。**

**证明就一步**：展开对易子，两侧各用一次本征方程，得到 $(q'-q'')T=0$。于是对角线外为零、对角线上"无限大"——只能是 $\delta$。

**为什么不能是 $\delta'$**：乘回 $(q'-q'')$ 验算，$\delta$ 给 $0$（合要求），$\delta'$ 给 $-\delta$（不合）。

**用途**：$V(\hat q)$ 在 $q$ 基对角，所以路径积分里位能那块可以直接提出来。

### 3.3 乘积的核（[D09](../derivations/D09-product-kernel.md)）

$$
\langle q'\lvert\hat A\hat B\lvert q''\rangle
=\int dq\;\langle q'\lvert\hat A\lvert q\rangle\langle q\lvert\hat B\lvert q''\rangle
$$

**白话**：两个算子相乘，等于"中间插一张快照再积分"。

**为什么它是路径积分的引擎**：连乘 $N$ 次就有 $N-1$ 个中途位置，取极限就是一条路径。

### 3.4 Hadamard 引理与 BCH（[D10](../derivations/D10-hadamard-lemma.md)–[D13](../derivations/D13-three-bch-forms.md)）

**D10 · 级数展开**：

$$
e^{A}Be^{-A}=\sum_{n=0}^{\infty}\frac{1}{n!}\,\mathrm{ad}_A^{\,n}B,
\qquad
\mathrm{ad}_A X\equiv[A,X]
$$

**白话**：共轭的生成元是对易子；这是**恒等式**，不是近似。

**D11 · 两项截断**（$[A,B]=c$ 是数）：

$$
e^{A}Be^{-A}=B+c
$$

**白话**：级数"停"在第二项——因为 $\mathrm{ad}_A$ 对常数失效。

**D12 · 交换相位**：

$$
e^{A}e^{B}=e^{c}\,e^{B}e^{A}
$$

**只定比值**：$e^{A}e^{B}$ 与 $e^{B}e^{A}$ 相差 $e^{c}$。

**D13 · 三条 BCH 闭式**：

$$
e^{A}e^{B}=e^{c/2}e^{A+B},
\qquad
e^{B}e^{A}=e^{-c/2}e^{A+B},
\qquad
e^{A/2}e^{B}e^{A/2}=e^{A+B}
$$

**定绝对分配**：$c/2$ 分在两边。**D12 给不出来**——它只知道差值，不知道分法。

**这一组的分工要记牢**：D12 定**比例**，D13 定**位置**。

### 3.5 不确定关系（[D25](../derivations/D25-uncertainty.md)）

$$
\Delta q\,\Delta p\ge\frac{1}{2}
$$

**白话**：同一条波函数上，两个量的弥散不能同时很小。**与"测量会扰动"无关**——证明里没有"测量"二字。

**证明骨架**：移到均值处 → Cauchy–Schwarz → 拆成反对易子（实）与对易子（虚）→ 丢掉实部 → 得 $\lvert i/2\rvert^{2}=1/4$。

**其中 $\{A,B\}=AB+BA$ 叫反对易子**，与对易子 $[A,B]=AB-BA$ 相对。

---

## 4. 表象：同一件事的两种画法

### 4.1 Weyl 相位（[D14](../derivations/D14-weyl-phase.md)）

$$
e^{ia\hat p}\,e^{ib\hat q}=e^{iab}\,e^{ib\hat q}\,e^{ia\hat p}
$$

**白话**：两个平移群交换一次，代价是一个相位 $e^{iab}$。**这个相位就是中心荷。**

**为什么用指数形式**：$\hat q,\hat p$ 无界，"乘积相减"要交代定义域；指数化后两边都是有界酉算子，处处有定义。

### 4.2 平移（[D16](../derivations/D16-translation.md)）

$$
e^{ia\hat p}\lvert q\rangle=\lvert q-a\rangle
$$

**白话**：动量生成位置平移。

**方向陷阱**：**态标签往下移**（$q\to q-a$），**波函数自变量往上移**（$\psi(q)\to\psi(q+a)$）。两者不矛盾，差一个负号。

### 4.3 平面波（[D17](../derivations/D17-qp-overlap.md)）

$$
\langle q\lvert p\rangle=e^{ipq}
$$

**白话**：动量本征态在位置表象里就是平面波。

**它是定理不是约定**：整体相位的模由归一化逼出为 1（§1.5），相位约定取 $c=1$（§1.6）。而"存在且唯一"来自 [D15](../derivations/D15-stone-von-neumann.md)。

**顺带**：波函数与其傅里叶变换互为坐标—

$$
\tilde\psi(p)=\int dq\,e^{-ipq}\psi(q),
\qquad
\psi(q)=\int\frac{dp}{2\pi}\,e^{ipq}\tilde\psi(p)
$$

### 4.4 动量基的完备性（[D18](../derivations/D18-p-completeness.md)）

$$
\int\frac{dp}{2\pi}\,\lvert p\rangle\langle p\rvert=\mathbb{1}
$$

**白话**：动量本征态也完备，但权重是 $\frac{dp}{2\pi}$，不是 $dp$。

**它不是新假设**：由位置完备性 + $\langle q\lvert p\rangle=e^{ipq}$ 三行推出（算核 → 代重叠 → 用 $\delta$ 的傅里叶表示）。

**为什么 $2\pi$ 必须在那**：换成 $\int dp$ 会得到 $2\pi\mathbb{1}$，换成 $\frac{dp}{\sqrt{2\pi}}$ 差因子。**只有 $\frac{dp}{2\pi}$ 给恒等。**

### 4.5 动量表象（[D19](../derivations/D19-momentum-representation.md)）

$$
\langle q\lvert\hat p\lvert\psi\rangle=-i\frac{d}{dq}\psi(q),
\qquad
\langle q'\lvert\hat p\lvert q''\rangle=-i\partial_{q'}\delta(q'-q'')
$$

**白话**：动量在位置表象里就是求导。

**注意**：这是**表示**不是定义。定义只有 D00。

---

## 5. 统计形式：从算子到温度

### 5.1 Hamiltonian 与演化（[D20](../derivations/D20-hamiltonian.md)）

$$
\hat H=\frac{\hat p^{2}}{2m}+V(\hat q),
\qquad
\lvert\psi(t)\rangle=e^{-i\hat Ht}\lvert\psi(0)\rangle
$$

**白话**：动能 + 位能。**不是推出来的，是三条要求逼出来的**：平移要有生成元（动能）、位置测量要有势（位能）、概率要守恒（$\hat H$ 必须自伴）。

**关键**：只有自伴生成元给出酉演化，酉演化才保住概率。

**欧氏化**：$\beta=it$ 把"振荡" $e^{-iHt}$ 换成"衰减" $e^{-\beta H}$——这是下面全部内容的起点。

### 5.2 路径积分（[D21](../derivations/D21-path-integral-representation.md)）

$$
\langle q_f\lvert e^{-\beta\hat H}\lvert q_i\rangle
=\int_{q(0)=q_i}^{q(\beta)=q_f}\mathcal{D}q\;e^{-S_E[q]},
\qquad
S_E=\int_0^\beta d\tau\Bigl[\frac{m}{2}\dot q^{2}+V(q)\Bigr]
$$

**白话**：把时间切片，每片插一张快照，取极限就是"对所有历史加权求和"。

**三步**：切片 → 单片核（高斯积分）→ 拼接取极限。

**记住**：测度自带归一化 $\prod(m/2\pi\varepsilon)^{1/2}$，丢了就错；端点不是零，是 $q_i,q_f$。

### 5.3 迹即闭合路径（[D22](../derivations/D22-trace-is-loop.md)）

$$
Z=\mathrm{Tr}\,e^{-\beta\hat H}
=\oint_{q(0)=q(\beta)}\mathcal{D}q\;e^{-S_E[q]}
$$

**白话**：取迹就是把路径的两端**焊起来**——于是路径变成闭合的环。

**为什么能焊**：因为迹与基无关（[D06](../derivations/D06-trace.md)），可以放心在 $q$ 基下取。

### 5.4 密度矩阵与配分函数（[D23](../derivations/D23-density-matrix.md)）

$$
\rho=\frac{e^{-\beta\hat H}}{Z},
\qquad
Z=\mathrm{Tr}\,e^{-\beta\hat H},
\qquad
F=-\frac{1}{\beta}\ln Z
$$

**白话**：纯态用一个矢描述，混合态用一个算子描述。热平衡就是 $\rho\propto e^{-\beta H}$。

**为什么纯态不够**：热平衡（与热库纠缠）、统计混合、子系统——都需要 $\rho$。

**期望值**：$\langle\hat A\rangle=\mathrm{Tr}(\rho\hat A)$，是 Born 规则的混合态版本。

**$Z$ 是母函数**：$F=-\frac1\beta\ln Z$、$E=-\partial_\beta\ln Z$、$S=\beta(E-F)$。

### 5.5 能级展开（[D26](../derivations/D26-energy-basis.md)）

$$
Z=\sum_n e^{-\beta E_n},
\qquad
K(q_f,q_i;\beta)=\sum_n e^{-\beta E_n}\psi_n(q_f)\psi_n^{*}(q_i)
$$

**白话**：只要知道能谱，配分函数就是能级求和。

**由两步得到**：函数演算给 $e^{-\beta H}$ 的谱分解；迹给"对角元之和"。

**它是路径积分的检验**：两条路必须给同一个 $Z$。

**低温**：$Z\simeq e^{-\beta E_0}$（基态主导）。**高温**：$Z\to$ 态空间维数。

### 5.6 温度 = 周期的倒数（[D24](../derivations/D24-temperature-period.md)）

$$
q(\tau+\beta)=q(\tau),
\qquad
\beta=\frac{1}{T}
$$

**白话**：路径的闭合条件给出"周期"，而 $\beta$ 同时是逆温度——**温度就是一个几何长度**。

**why it matters**：这把统计力学翻译成几何。低温 = 长周期（量子结构清楚），高温 = 短周期（退化为经典）。

**这正是霍金温度的入口**：近视界欧氏时空要消掉锥奇点，只能把虚时间卷成 $\beta=2\pi/\kappa$。

---

## 6. 十条最容易错的地方

| # | 错法 | 正确 |
|---|---|---|
| 1 | 把 $[\hat q,\hat p]=i$ 当成能推出 Weyl 关系 | 反过来才行；反向要补三条 |
| 2 | 以为 Born 规则能由谱定理推出 | 它是**公理**，不能推 |
| 3 | 连续谱时找"平方可积的本征矢" | 不存在；$\lvert q\rangle$ 在 $\Phi^{\times}$ 里 |
| 4 | 把 $\langle q\lvert q'\rangle=\delta$ 整体当约定 | 形式被迫、系数自选 |
| 5 | 两套归一化混用 | 差 $\sqrt{2\pi}$，量纲上看不出 |
| 6 | 记错 $[\hat q,g(\hat p)]$ 的符号 | 与 $[\hat p,f(\hat q)]$ 相反 |
| 7 | 以为 D12 能给出 $c/2$ 的分配 | 它只给比值，绝对分配在 D13 |
| 8 | 说"不确定关系是测量扰动" | 推导里没有测量；是同一波函数上的弥散 |
| 9 | 把 $\hat p=-i\partial_q$ 当定义 | 它是**表示**，定义是对易子 |
| 10 | 路径积分里漏掉测度归一化 | 每片带 $(m/2\pi\varepsilon)^{1/2}$ |

---

## 7. 我一开始错在哪

1. **以为 Hadamard 引理是近似公式。** 总想给它找"一阶、二阶修正"。实际上它是**恒等式**，级数停不停取决于 $\mathrm{ad}_A$ 是否幂零。

2. **试图用有限维矩阵数值检验 $[A,B]=cI$。** 怎么都不对，以为是代码错。实际是**原理性不可能**：$\mathrm{tr}[A,B]=0$ 而 $\mathrm{tr}(cI)=cn$。

3. **把 Weyl 相位写成 $e^{-iab}$。** 记的是"$q$ 在前的版本"，套在"$p$ 在前"的写法上。现在知道：不要背符号，现算 $[ia\hat p,ib\hat q]=iab$。

4. **以为本征方程能一步"证明"**。$\hat q\lvert q\rangle=q\lvert q\rangle$ 看着像定义，其实是 Gelfand–Maurin 取 $\hat A=\hat q$ 的一行特化——**存在性**才是那条定理给的。

5. **以为"函数演算"只是一个定义。** 实际它定义对象之后，还要给出"这个对象必须满足什么"——谱映射与范数公式是**定理**，不是定义的复述。

---

## 8. 自检

- [ ] 不看笔记，说出一条公理、一条接口、一条测量规则各是什么，为什么它们不能互相推出
- [ ] 一句话说清谱定理与 Gelfand–Maurin 的分工
- [ ] 说明 $\langle q\lvert q'\rangle=\delta$ 里哪一半是被迫的、哪一半是选的
- [ ] 说出 S–vN 的三个前提，以及它在什么情形失效
- [ ] 默写函数演算的三种定义，并说明哪一种才是真正的定义
- [ ] 写出迹的定义，并说明它为什么与基无关
- [ ] 说出 D12 与 D13 的分工（比值 vs 绝对分配）
- [ ] 解释平移的两个方向为什么不矛盾
- [ ] 说清 $\frac{dp}{2\pi}$ 的 $2\pi$ 从哪来
- [ ] 从 $\hat H$ 出发，一步步走到 $Z=\sum_n e^{-\beta E_n}$，中间经过哪几张卡
- [ ] 说明为什么"温度是一个几何长度"
- [ ] 指出这张网络在哪里失效（至少两处）
