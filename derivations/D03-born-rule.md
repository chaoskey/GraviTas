# D03 · 态与测量：Born 规则

> 建档 2026-11-08 · 类型：推导卡（含一条**公理**）——本卡唯一的新输入是 Born 规则，其余全部是定理
> 上游：[D00](D00-commutator-axiom.md)（接口约定）、[D01](D01-spectral-theorem.md)（谱定理、函数演算）、[D02](D02-gelfand-maurin.md)（广义本征态、$E(B)$ 的密度）
> 下游：[D04](D04-position-eigen-equation.md)、[D20](D20-uncertainty.md)
> 本卡补的是"数学怎么变成预言"的那一步。没有它，整个网格算不出一个可检验的数。

---

## 0. 态：先写成一个候选矢量

先把态写成一个矢量 $\lvert\psi\rangle$，并取它为单位长：

$$
\langle\psi\lvert\psi\rangle=1\tag{1}
$$

**这不是最终答案。** §2 会说明：真正的态是**射线**，单位矢量只是这条射线挑出来的**代表元**。

**为什么不在这里先说"射线"**：因为"为什么乘非零复数不改变物理"与"为什么必须单位长"，**都是 Born 规则的后果**。先给一个候选描述，等公理到位再收紧——否则就是先下结论、后补理由。

---

## 1. Born 规则【公理】

**可观测量**：由 [D00](D00-commutator-axiom.md) 的接口约定，可观测量对应自伴算子；由 [D01](D01-spectral-theorem.md) 的谱定理，它唯一对应一族投影值测度 $E$：

$$
\hat A=\int_{\sigma(\hat A)}\lambda\;dE(\lambda)\tag{2}
$$

**Born 规则**：态为 $\lvert\psi\rangle$ 时，对 $\hat A$ 的测量读数落在 Borel 集 $B$ 内的概率是

$$
p(B)=\langle\psi\lvert E(B)\lvert\psi\rangle\tag{3}
$$

**这就是 [D01](D01-spectral-theorem.md) 里那个标量谱测度 $\mu_\psi(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$。** 在 D01 中它只是为书写函数演算定义域而引入的**数学记号**；直到这里它才拿到物理含义——**它是测量读数的概率分布**。

**四个对象必须分清**（本卡最容易含糊的地方）：

| 对象 | 数学类型 | 归谁 |
|---|---|---|
| $E(B)$ | **算子**（正交投影） | [D01](D01-spectral-theorem.md) 的谱定理 |
| $p(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$ | **非负实数**（概率） | **本卡的 Born 规则** |
| $dE(\lambda)$ | **算子值**测度微元 | 谱定理的"密度"形式 |
| $dp(\lambda)=d\langle\psi\lvert E(\lambda)\lvert\psi\rangle$ | **标量**测度微元 | 上一行的夹取，概率密度形式 |

**为什么这个区分要紧**：若 $E(B)$ 本身就是概率，Born 规则就是多余的。它之所以是公理，正因为"**把算子变成数**"这一步没有任何纯数学依据——同一个投影，可以用别的双线性形式去夹，物理选了这一个。

**本卡三样东西，地位不同**：

| 东西 | 地位 | 在哪落实 |
|---|---|---|
| 态 | **定义**（§0 给了候选） | §2 收紧为射线 |
| $p(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$ | **公理**（本卡唯一） | §1 |
| $\langle\hat A\rangle=\langle\psi\lvert\hat A\lvert\psi\rangle$ | **定理** | §3 |

---

## 2. 由 Born 推出态的结构

### 2.1 乘常数不改变物理 ⇒ 态是射线

$$
p_{c\psi}(B)=\langle c\psi\lvert E(B)\lvert c\psi\rangle=\lvert c\rvert^{2}\langle\psi\lvert E(B)\lvert\psi\rangle=\lvert c\rvert^{2}p_\psi(B)\tag{4}
$$

对任何 $\hat A$、任何 $B$，乘 $c$ 只是把所有权重同时放大 $\lvert c\rvert^{2}$，任意两个互斥事件的**相对**概率 $p(B_1)/p(B_2)$ 不变——**没有任何测量能察觉**。

**所以态是等价类**

$$
[\psi]=\bigl\{c\lvert\psi\rangle:\ c\in\mathbb{C},\ c\neq0\bigr\}\tag{5}
$$

这就是"射线"：复希尔伯特空间里从原点出发、去掉原点的一条一维复子空间。

### 2.2 要当概率就必须归一 ⇒ 单位矢量是代表元

1. **非负性**由正交投影自动给出：$E(B)=E(B)^{\dagger}=E(B)^{2}$，故
   $$
   p(B)=\langle\psi\lvert E(B)^{2}\lvert\psi\rangle=\lVert E(B)\psi\rVert^{2}\ge0\tag{6}
   $$
   这一条不需要对 $\lvert\psi\rangle$ 加任何条件。
2. **归一性**要求总概率为 $1$；由 [D01](D01-spectral-theorem.md) 的 $E(\mathbb{R})=E(\sigma(\hat A))=\mathbb{1}$，
   $$
   p(\mathbb{R})=\langle\psi\lvert E(\mathbb{R})\lvert\psi\rangle=\langle\psi\lvert\mathbb{1}\lvert\psi\rangle=\langle\psi\lvert\psi\rangle=1\tag{7}
   $$

**要概率总和为 $1$，就必须 $\langle\psi\lvert\psi\rangle=1$。** 归一化不是装饰，它是 Born 规则能成立为"概率"的前提。

### 2.3 合起来

**态是射线**（乘非零复数不改变物理）；**单位矢量是它的代表元**（这样 $p$ 才是概率）。

**这两条都是 Born 的后果**——不是前提。

---

## 3. 期望值【定理】

**期望值的定义**是"对概率测度求平均"：

$$
\langle\hat A\rangle\equiv\int_{\sigma(\hat A)}\lambda\;dp(\lambda)\tag{8}
$$

对 $\psi\in D(\hat A)$，把 Born 规则与谱分解代进去：

$$
\begin{aligned}
\langle\hat A\rangle
&=\int\lambda\,dp(\lambda) &&\text{定义}\\
&=\int\lambda\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle &&\text{Born 规则}\\
&=\Bigl\langle\psi\Bigl\lvert\int\lambda\,dE(\lambda)\Bigr\rvert\psi\Bigr\rangle &&\text{谱积分定义}\\
&=\langle\psi\lvert\hat A\lvert\psi\rangle &&\text{谱定理}
\end{aligned}\tag{9}
$$

**中间没有新假设。** 所以"期望值等于那个双线性形式"是**推出来的**，不是规定的。对任意实值 Borel $f$ 与 $\psi\in D(f(\hat A))$，同法得

$$
\langle f(\hat A)\rangle=\int_{\sigma(\hat A)}f(\lambda)\,dp(\lambda)=\langle\psi\lvert f(\hat A)\lvert\psi\rangle\tag{10}
$$

---

## 4. 本征态必得本征值【定理】

**要证**：若 $\hat A\lvert\psi\rangle=a\lvert\psi\rangle$（$\lVert\psi\rVert=1$，即 $\psi$ 落在点谱上），则

$$
p(\{a\})=\langle\psi\lvert E(\{a\})\lvert\psi\rangle=1\tag{11}
$$

**[D01](D01-spectral-theorem.md) §3 已经给出一条捷径**：那里证明了 $\operatorname{ran}E(\{a\})=\ker(\hat A-a\mathbb{1})$，于是
$\hat A\psi=a\psi\Rightarrow E(\{a\})\psi=\psi\Rightarrow p(\{a\})=1$。**但下面走一条不调用它的路**，只用方差与谱积分——它把"概率测度"这一层看得更清楚，也为 §5 的推广做铺垫。

### 4.1 七步：用测度与方差

**第 0 步：$\mu_\psi$ 是概率测度。**

记 $\mu_\psi(B)=p(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$。非负见（6）；归一见（7）。

**第 1 步：算两个矩。** 只用本征方程（不用谱定理）：

$$
\langle\hat A\rangle=\langle\psi\lvert\hat A\lvert\psi\rangle=a\langle\psi\lvert\psi\rangle=a,
\qquad
\hat A^{2}\lvert\psi\rangle=a^{2}\lvert\psi\rangle\ \Longrightarrow\ \langle\hat A^{2}\rangle=a^{2}\tag{12}
$$

**第 2 步：方差为零。**

$$
\langle(\hat A-a\mathbb{1})^{2}\rangle=\langle\hat A^{2}\rangle-2a\langle\hat A\rangle+a^{2}=a^{2}-2a^{2}+a^{2}=0\tag{13}
$$

**第 3 步：把期望换成积分。** 由 [D01](D01-spectral-theorem.md) §1 的函数演算（取 $f(\lambda)=(\lambda-a)^{2}$；$\psi$ 在定义域里，因为 $(\hat A-a\mathbb{1})\psi=0$）：

$$
0=\langle(\hat A-a\mathbb{1})^{2}\rangle=\int_{\mathbb{R}}(\lambda-a)^{2}\,d\mu_\psi(\lambda)\tag{14}
$$

**这是唯一用到谱定理的一步**：把算子期望换成对概率测度的积分。

**第 4 步：非负积分为零 ⇒ 正值集合测度为零。** 令 $A=\{(\lambda-a)^{2}>0\}$。**反证**：若 $\mu_\psi(A)>0$，把 $A$ 拆成递增列

$$
A=\bigcup_{n\ge1}A_n,
\qquad
A_n=\Bigl\{(\lambda-a)^{2}>\tfrac{1}{n}\Bigr\}\tag{15}
$$

则 $\mu_\psi(A)=\lim_n\mu_\psi(A_n)$，故必有某个 $n$ 使 $\mu_\psi(A_n)>0$。于是

$$
\int(\lambda-a)^{2}\,d\mu_\psi\ \ge\ \int_{A_n}(\lambda-a)^{2}\,d\mu_\psi\ >\ \frac{1}{n}\mu_\psi(A_n)\ >\ 0\tag{16}
$$

**与（14）矛盾。** 所以 $\mu_\psi(A)=0$。

**第 5 步：$A$ 就是 $\mathbb{R}\setminus\{a\}$。** 因为 $(\lambda-a)^{2}>0\iff\lambda\neq a$，故

$$
\mu_\psi\bigl(\mathbb{R}\setminus\{a\}\bigr)=0\tag{17}
$$

**第 6 步：取补集。**

$$
\mu_\psi(\{a\})=\mu_\psi(\mathbb{R})-\mu_\psi(\mathbb{R}\setminus\{a\})=1-0=1\tag{18}
$$

**这一步用到第 0 步的归一**：没有 $\mu_\psi(\mathbb{R})=1$，只能得 $\mu_\psi(\{a\})=\mu_\psi(\mathbb{R})$。

**第 7 步：回到 Born 规则。** $p(\{a\})=\mu_\psi(\{a\})=1$。**证毕。**

**一句话的链条**：

$$
\hat A\psi=a\psi
\ \Rightarrow\
\langle(\hat A-a\mathbb{1})^{2}\rangle=0
\ \overset{\text{D01 §1}}{=}\
\int(\lambda-a)^{2}d\mu_\psi=0
\ \Rightarrow\
\mu_\psi(\mathbb{R}\setminus\{a\})=0
\ \Rightarrow\
p(\{a\})=1
$$

### 4.2 等价地：矢量也不变

上面的结论只用了**测度**。它还有一个**矢量**版本，两者等价：

$$
E(\{a\})\lvert\psi\rangle=\lvert\psi\rangle
\quad\Longleftrightarrow\quad
p(\{a\})=\langle\psi\lvert E(\{a\})\lvert\psi\rangle=1\tag{19}
$$

**正向**：若 $E(\{a\})\lvert\psi\rangle=\lvert\psi\rangle$，两边左乘 $\langle\psi\lvert$ 立得 $1$。

**反向**：记 $E=E(\{a\})$。$E$ 是投影，故 $\mathbb{1}-E$ 也是投影，且两者正交。于是**勾股定理**给出

$$
\lVert\psi\rVert^{2}=\lVert E\psi\rVert^{2}+\lVert(\mathbb{1}-E)\psi\rVert^{2}
=\langle\psi\lvert E\lvert\psi\rangle+\lVert(\mathbb{1}-E)\psi\rVert^{2}
$$

若 $\langle\psi\lvert E\lvert\psi\rangle=1=\lVert\psi\rVert^{2}$，则 $\lVert(\mathbb{1}-E)\psi\rVert^{2}=0$，即 $E\lvert\psi\rangle=\lvert\psi\rangle$。

**意义**：同一件事有两种说法——**矢量语言**与**数值语言**；两边互相推，且都不需要知道 $E(\{a\})$ 具体是哪个投影。与 [D01](D01-spectral-theorem.md) §3 的 $\operatorname{ran}E(\{a\})=\ker(\hat A-a\mathbb{1})$ 合起来看：**本征方程、单点投影不变、Born 概率为 $1$，三者在数学上完全等价。**

**边界**：本条只对**点谱**成立。连续谱时 $E(\{q\})=\mathbb{0}$，$\mathcal{H}$ 里根本没有归一化的"本征态"（[D01](D01-spectral-theorem.md) §3），单点概率也就无从谈起。连续谱怎么办，是下一节的事。

---

## 5. 与 D02 接轨：连续谱下的概率密度

[D01](D01-spectral-theorem.md) 只给宏观投影 $E(B)$；[D02](D02-gelfand-maurin.md) §4 在装备希尔伯特空间里把它拆成广义本征态的外积。把两者代进 Born 规则，"波函数模方是概率密度"就落到了实处。

由 [D02](D02-gelfand-maurin.md) §4 的（9）式，在弱意义下

$$
E(B)=\int_B\sum_k\lvert\lambda,k\rangle\langle\lambda,k\rvert\;d\mu(\lambda)
$$

对 $\psi\in\Phi$（再由稠密性延拓）代入（3）：

$$
\begin{aligned}
p(B)
&=\Bigl\langle\psi\Bigl\lvert\Bigl(\int_B\sum_k\lvert\lambda,k\rangle\langle\lambda,k\rvert\,d\mu(\lambda)\Bigr)\Bigr\rvert\psi\Bigr\rangle\\
&=\int_B\sum_k\langle\psi\lvert\lambda,k\rangle\langle\lambda,k\lvert\psi\rangle\;d\mu(\lambda)
=\int_B\sum_k\bigl\lvert\langle\lambda,k\lvert\psi\rangle\bigr\rvert^{2}\,d\mu(\lambda)
\end{aligned}\tag{20}
$$

（最后一步用 [D02](D02-gelfand-maurin.md) §3 的共轭约定 $\langle\psi\lvert\lambda,k\rangle=\overline{\langle\lambda,k\lvert\psi\rangle}$。）

对照 $p(B)=\int_Bdp(\lambda)$，得**测量概率对 D02 标量谱测度的 Radon–Nikodym 密度**：

$$
dp(\lambda)=d\mu_\psi(\lambda)=\Bigl(\sum_k\bigl\lvert\langle\lambda,k\lvert\psi\rangle\bigr\rvert^{2}\Bigr)d\mu(\lambda)\tag{21}
$$

**这就是"波函数模方等于概率密度"的出处**，三件事一次说清：

1. **$\mu_\psi\ll\mu$**：任何态的测量概率都落在主标量谱测度 $\mu$ 的支撑里，密度是 $\rho_\psi(\lambda)=\sum_k\lvert\langle\lambda,k\lvert\psi\rangle\rvert^{2}$（有简并时对重数求和）。
2. **无简并 + $d\mu=dq$ 时回到教科书**：$k$ 只剩一项、取位置谱的 $\mu$ 为 Lebesgue（密度形式 $d\mu=dq$ 是一次选择，具体定法属下游），记 $\psi(q)=\langle q\lvert\psi\rangle$，则
   $$
   p\bigl([q_1,q_2]\bigr)=\int_{q_1}^{q_2}\lvert\psi(q)\rvert^{2}\,dq,
   \qquad
   \frac{dp}{dq}=\lvert\psi(q)\rvert^{2}\tag{22}
   $$
3. **为什么单点概率为零而密度不为零**：$\mu(\{q_0\})=0$ 时积分区间缩成一点，$p(\{q_0\})=0$；而 $\lvert\langle q_0\lvert\psi\rangle\rvert^{2}$ 是被积**函数**，当然可以非零——它是密度，不是概率。

---

## 6. 总结：从纯数学到物理预言

本卡在整张地图上完成的是一次**从算子到实验预言**的转换：

1. **一条唯一公理（§1）**：$p(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$ 把 [D01](D01-spectral-theorem.md) 的抽象投影 $E(B)$ 变成实验读数的概率——这是本卡唯一的物理输入。
2. **三大严格推论（§2～§4）**：由概率的缩放不变性与归一性逼出**态的射线结构与单位代表元**；由概率期望的定义与谱积分推出**期望值夹取定理**；由方差为零推出**点谱本征态必测得本征值**（并与 [D01](D01-spectral-theorem.md) §3 的 $\operatorname{ran}E(\{a\})=\ker(\hat A-a\mathbb{1})$ 闭环）。
3. **与 D02 合龙（§5）**：把 [D02](D02-gelfand-maurin.md) §4 的外积密度代进 Born 规则，得 $dp(\lambda)=\sum_k\lvert\langle\lambda,k\lvert\psi\rangle\rvert^{2}d\mu(\lambda)$——连续谱下的"波函数模方是概率密度"就是这样落地的。

**一句话**：数学给的是投影，物理要的是概率；中间那一步就是 (3)，它不能被推出来，只能被选定。

---

## 7. 边界

1. **它只说"概率是多少"，不说"为什么是概率"。** 测量问题（波函数何时坍缩、谁在测量）不在本卡范围内，物理上仍是开放的（[P11](../problems/P11-problem-of-time.md) 相关）。
2. **坍缩（投影假设）是额外的一条。** 只算一次测量的 $p(B)$ 或 $\langle\hat A\rangle$ 不需要它；要算"测得 $B$ 后再测"才需要：
   $$
   \lvert\psi\rangle\;\longrightarrow\;\frac{E(B)\lvert\psi\rangle}{\sqrt{p(B)}}
   $$
3. **连续谱不坍缩到单点。** $E(\{q\})=\mathbb{0}$、$\lvert q\rangle$ 又不可归一，所以真实的测量只能分辨到一个区间 $B$，测后态是 $E(B)\lvert\psi\rangle/\sqrt{p(B)}\in\mathcal{H}$，不是 $\lvert q\rangle$。
4. **纯态才用本卡。** 混合态（热平衡、统计混合）要换成密度算子 $\hat\rho$，Born 规则改成 $p(B)=\operatorname{Tr}(\hat\rho E(B))$，属下游。
5. **§5 的密度形式依赖 D02 的相容性条件。** （21）不是无条件成立的——它继承了 [D02](D02-gelfand-maurin.md) §4.3 的（8）。

---

## 8. 自检

- [ ] 说出本卡唯一的公理是什么，为什么它不能由谱定理推出
- [ ] 分清四个对象：$E(B)$、$\langle\psi\lvert E(B)\lvert\psi\rangle$、$dE(\lambda)$、$d\langle\psi\lvert E(\lambda)\lvert\psi\rangle$
- [ ] 说明"态是射线"与"必须归一"各自从 Born 的哪一步来
- [ ] 导出期望值公式，并指出哪一步用了谱定理
- [ ] 用方差论证证明"本征态必得本征值"，并说明它为什么不需要 D01 §3 的点谱定理
- [ ] 说明 $E(\{a\})\lvert\psi\rangle=\lvert\psi\rangle$ 与 $p(\{a\})=1$ 为什么等价
- [ ] 从 D02 的（9）导出（21），并说明 $\mu_\psi\ll\mu$ 的密度是什么
- [ ] 解释连续谱为什么"单点概率为零、密度不为零"
- [ ] 指出本卡**不**包含哪一条（坍缩、测量问题），以及纯态的限制
