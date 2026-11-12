# D02 · 态与测量：Born 规则

> 建档 2026-11-08 · 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)
> 下游：[D25](D25-uncertainty.md)
> 本卡补的是"数学怎么变成预言"的那一步。没有它，整个网格算不出一个可检验的数。

---

## 0. 态：先写成一个矢量

**先把态写成一个矢量** $\lvert\psi\rangle$，并取它为单位长：
$$
\langle\psi\lvert\psi\rangle=1
$$

**这不是最终答案。** §2 会说明：真正的态是**射线**，单位矢量只是这条射线挑出来的**代表元**。

**为什么不在这里先说"射线"**：因为"为什么是射线"与"为什么必须单位长"，**都是 Born 规则的后果**。先给一个候选描述，等公理到位再收紧——否则就是先下结论、后补理由。

---

## 1. Born 规则【公理】

**可观测量**：由 [D00](D00-commutator-axiom.md) 的接口约定，可观测量对应自伴算子；由 [D01](D01-spectral-theorem.md) 的谱定理，它可以写成

$$
\hat A=\int\lambda\,dE(\lambda)
$$

**Born 规则**：对 Borel 集 $B$，测得结果落在 $B$ 内的概率是

$$
p(B)=\langle\psi\lvert E(B)\lvert\psi\rangle
$$

**三个对象必须分清**（本卡最容易含糊的地方）：

| 对象 | 类型 | 归谁 |
|---|---|---|
| $E(B)$ | **算子**（投影） | [D01](D01-spectral-theorem.md) 的谱定理 |
| $\langle\psi\lvert E(B)\lvert\psi\rangle$ | **数**（概率） | **本卡的 Born 规则** |
| $dE(\lambda)$ | **算子值**测度 | 谱定理的"密度"形式 |
| $d\langle\psi\lvert E(\lambda)\lvert\psi\rangle$ | **测度**（数） | 上一行的夹取，概率密度形式 |

**为什么这个区分要紧**：若 $E(B)$ 本身就是概率，Born 规则就是多余的。它之所以是公理，正因为"**把算子变成数**"这一步没有任何数学依据——同一个投影，可以用别的归一化双线性形式去夹，物理选了这一个。

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
p(B)=\langle c\psi\lvert E(B)\lvert c\psi\rangle=\lvert c\rvert^{2}\langle\psi\lvert E(B)\lvert\psi\rangle
$$

乘 $c$ 只是把所有权重同时放大 $\lvert c\rvert^{2}$——**没有任何测量能察觉**。

**所以态是等价类**

$$
[\psi]=\{c\lvert\psi\rangle:\ c\in\mathbb{C},\ c\neq0\}
$$

这就是"射线"：复平面上从原点出发的一条半直线。

### 2.2 要当概率就必须归一 ⇒ 单位矢量是代表元

$$
p(\mathbb{R})=\langle\psi\lvert E(\mathbb{R})\lvert\psi\rangle=\langle\psi\lvert\mathbb{1}\lvert\psi\rangle=\langle\psi\lvert\psi\rangle
$$

**要概率总和为 $1$，就必须 $\langle\psi\lvert\psi\rangle=1$。** 归一化不是装饰，它是 Born 规则能成立为"概率"的前提。

### 2.3 合起来

**态是射线**（乘非零复数不改变物理）；**单位矢量是它的代表元**（这样 $p$ 才是概率）。

**这两条都是 Born 的后果**——不是前提。

---

## 3. 期望值【定理】

**期望值的定义**是"对概率测度求平均"：

$$
\langle\hat A\rangle\equiv\int\lambda\,dp(\lambda)
$$

把 Born 规则与谱分解代进去：

$$
\begin{aligned}
\langle\hat A\rangle
&=\int\lambda\,dp(\lambda) &&\text{定义}\\
&=\int\lambda\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle &&\text{Born 规则}\\
&=\Bigl\langle\psi\Bigl\lvert\int\lambda\,dE(\lambda)\Bigr\rvert\psi\Bigr\rangle &&\text{谱积分定义}\\
&=\langle\psi\lvert\hat A\lvert\psi\rangle &&\text{谱定理}
\end{aligned}
$$

**中间没有新假设。** 所以"期望值等于那个双线性形式"是**推出来的**，不是规定的。

---

## 4. 本征态必得本征值【定理】

**要证**：若 $\hat A\lvert\psi\rangle=a\lvert\psi\rangle$，则 $p(\{a\})=1$。

下面每一步只用一个理由。

**第 0 步：$\mu_\psi$ 是概率测度。**

记 $\mu_\psi(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$。

- **非负**：$E(B)$ 是投影，$E(B)=E(B)^{2}=E(B)^{\dagger}$，故
  $$
  \mu_\psi(B)=\langle\psi\lvert E(B)^{2}\lvert\psi\rangle=\lVert E(B)\psi\rVert^{2}\ge0
  $$
- **归一**：$E(\mathbb{R})=\mathbb{1}$，故
  $$
  \mu_\psi(\mathbb{R})=\langle\psi\lvert\mathbb{1}\lvert\psi\rangle=\langle\psi\lvert\psi\rangle=1
  $$

**第 1 步：算两个矩。** 只用本征方程（不用谱定理）：

$$
\langle\hat A\rangle=\langle\psi\lvert\hat A\lvert\psi\rangle=a\langle\psi\lvert\psi\rangle=a
$$

$$
\hat A^{2}\lvert\psi\rangle=\hat A(a\lvert\psi\rangle)=a^{2}\lvert\psi\rangle
\ \Longrightarrow\
\langle\hat A^{2}\rangle=a^{2}
$$

**第 2 步：方差为零。**

$$
\langle(\hat A-a)^{2}\rangle=\langle\hat A^{2}\rangle-2a\langle\hat A\rangle+a^{2}=a^{2}-2a^{2}+a^{2}=0
$$

**第 3 步：把期望换成积分。** 由 [D01](D01-spectral-theorem.md) §1.2 第 1 条的 $f$ 公式（取 $f(\lambda)=(\lambda-a)^{2}$；$\psi$ 在定义域里，因为 $(\hat A-a)^{2}\psi=0$）：

$$
0=\langle(\hat A-a)^{2}\rangle=\int(\lambda-a)^{2}\,d\mu_\psi(\lambda)
$$

**这是唯一用到谱定理的一步**：把算子期望换成对测度的积分。

**第 4 步：非负积分为零 ⇒ 该集合测度为零。**

令 $A=\{\lambda:(\lambda-a)^{2}>0\}$。**反证**：若 $\mu_\psi(A)>0$，把 $A$ 拆成

$$
A=\bigcup_{n\ge1}A_n,
\qquad
A_n=\Bigl\{\lambda:(\lambda-a)^{2}>\frac{1}{n}\Bigr\}
$$

$A_n$ 递增，$\mu_\psi(A)=\lim_n\mu_\psi(A_n)$，故必有某个 $n$ 使 $\mu_\psi(A_n)>0$。于是

$$
\int(\lambda-a)^{2}\,d\mu_\psi\ \ge\ \int_{A_n}(\lambda-a)^{2}\,d\mu_\psi\ >\ \frac{1}{n}\mu_\psi(A_n)\ >\ 0
$$

**与积分为零矛盾。** 所以 $\mu_\psi(A)=0$。

**第 5 步：$A$ 就是 $\mathbb{R}\setminus\{a\}$。** 因为 $(\lambda-a)^{2}>0\iff\lambda\neq a$，故

$$
\mu_\psi\bigl(\mathbb{R}\setminus\{a\}\bigr)=0
$$

**第 6 步：取补集。**

$$
\mu_\psi(\{a\})=\mu_\psi(\mathbb{R})-\mu_\psi(\mathbb{R}\setminus\{a\})=1-0=1
$$

**这一步用到第 0 步的归一**：没有 $\mu_\psi(\mathbb{R})=1$，只能得 $\mu_\psi(\{a\})=\mu_\psi(\mathbb{R})$。

**第 7 步：回到 Born 规则。**

$$
p(\{a\})=\mu_\psi(\{a\})=1
$$

**证毕。**

**一句话的链条**：

$$
\hat A\psi=a\psi
\ \Rightarrow\
\langle(\hat A-a)^{2}\rangle=0
\ \overset{\text{谱定理}}{=}\
\int(\lambda-a)^{2}d\mu_\psi=0
\ \Rightarrow\
\mu_\psi(\mathbb{R}\setminus\{a\})=0
\ \Rightarrow\
\mu_\psi(\{a\})=1
\ \Rightarrow\
p(\{a\})=1
$$

### 4.1 等价地：矢量也不变

上面的结论只用了**测度**。它还有一个**矢量**版本，两者等价：

$$
E(\{a\})\lvert\psi\rangle=\lvert\psi\rangle
\quad\Longleftrightarrow\quad
\langle\psi\lvert E(\{a\})\lvert\psi\rangle=1
$$

**正向**：若 $E(\{a\})\lvert\psi\rangle=\lvert\psi\rangle$，则

$$
\langle\psi\lvert E(\{a\})\lvert\psi\rangle=\langle\psi\lvert\psi\rangle=1
$$

**反向**：记 $E=E(\{a\})$。$E$ 是投影，故 $\mathbb{1}-E$ 也是投影，且两者正交。于是**勾股定理**给出

$$
\lVert\psi\rVert^{2}=\lVert E\psi\rVert^{2}+\lVert(\mathbb{1}-E)\psi\rVert^{2}
$$

又由 $E^{2}=E$：

$$
\langle\psi\lvert E\lvert\psi\rangle=\langle\psi\lvert E^{2}\lvert\psi\rangle=\lVert E\psi\rVert^{2}
$$

若它等于 $1=\lVert\psi\rVert^{2}$，则 $\lVert(\mathbb{1}-E)\psi\rVert^{2}=0$，即 $E\lvert\psi\rangle=\lvert\psi\rangle$。

**意义**：同一件事有两种说法——**矢量语言**（左边）与**数值语言**（右边）；两边互相推，且**都不需要知道 $E(\{a\})$ 具体是哪个投影**。

**边界**：本条只对**点谱**成立。连续谱时 $E(\{q\})=0$，此时"本征态"根本不存在（[D01](D01-spectral-theorem.md) §1.3），概率也就无从谈起。

---

## 5. 一致性检验与边界

| 检验 | 结果 |
|---|---|
| 概率归一 | $E(\mathbb{R})=\mathbb{1}$ 给 $p(\mathbb{R})=1$ ✅ |
| 简并情形 | $E(\{a\})$ 是投影而非一维时，$p$ 仍是夹取式，无需改定义 ✅ |
| 射线 | $p$ 对 $\lvert c\psi\rangle$ 只变 $\lvert c\rvert^{2}$——这正是 §2 的说法 ✅ |

**边界**：

1. **它只说"概率是多少"，不说"为什么是概率"。** 测量问题（波函数何时坍缩、谁在测量）不在本卡范围内，物理上仍是开放的（[P11](../problems/P11-problem-of-time.md) 相关）。
2. **坍缩（投影假设）是额外的一条。** 只算期望值不需要它；要算"测量后再测"才需要：
   $$
   \lvert\psi\rangle\;\longrightarrow\;\frac{E(B)\lvert\psi\rangle}{\sqrt{p(B)}}
   $$
3. **连续谱时 $p$ 是"落在区间"的概率**：$E(\{q\})=0$，所以单点概率为零，只有区间才有正概率。
4. **纯态才用本卡**。混合态（热平衡、统计混合）要换成混合态的描写（属下游）。

---

## 6. 自检

- [ ] 说出本卡唯一的公理是什么，为什么它不能由谱定理推出
- [ ] 分清三个对象：$E(B)$、$\langle\psi\lvert E(B)\lvert\psi\rangle$、$d\langle\psi\lvert E(\lambda)\lvert\psi\rangle$
- [ ] 说明"态是射线"与"必须归一"各自从 Born 的哪一步来
- [ ] 导出期望值公式，并指出哪一步用了谱定理
- [ ] 用方差论证证明"本征态必得本征值"，并说明它为什么不需要"谱投影识别"
- [ ] 说明 $E(\{a\})\lvert\psi\rangle=\lvert\psi\rangle$ 与 $p(\{a\})=1$ 为什么等价
- [ ] 指出本卡**不**包含哪一条（坍缩、测量问题），以及连续谱的边界
