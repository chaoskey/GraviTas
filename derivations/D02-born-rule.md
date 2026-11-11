# D02 · 态与测量：Born 规则

> 建档 2026-11-08 · 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)
> 下游：[D25](D25-uncertainty.md)
> 本卡补的是"数学怎么变成预言"的那一步。没有它，整个网格算不出一个可检验的数。

---

## 0. 定义、公理与推论

**态**：单位射线 $\lvert\psi\rangle$，$\langle\psi\lvert\psi\rangle=1$。

**测量**：设可观测量 $\hat A=\int\lambda\,dE(\lambda)$（[D01](D01-spectral-theorem.md) 的谱分解）。对 Borel 集 $B$，测得结果落在 $B$ 内的概率是

$$
p(B)=\langle\psi\lvert E(B)\lvert\psi\rangle
$$

**期望值**：

$$
\langle\hat A\rangle=\langle\psi\lvert\hat A\lvert\psi\rangle=\int\lambda\;d\langle\psi\lvert E(\lambda)\lvert\psi\rangle
$$

**三条的地位不同**，不要当成并列的三条公理：

| 表达式 | 地位 | 为什么 |
|---|---|---|
| 态 = 单位射线 | **定义 + 归一化约定** | 它不预言任何测量结果，只是把“态”这个词固定下来；$\langle\psi\lvert\psi\rangle=1$ 是挑代表元（§0.1） |
| $p(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$ | **公理**（本卡唯一） | 数学推不出“概率”，这一步只能选定 |
| $\langle\hat A\rangle=\langle\psi\lvert\hat A\lvert\psi\rangle$ | **定理** | 由 $\langle\hat A\rangle=\int\lambda\,dp(\lambda)$ 与谱定理 $\hat A=\int\lambda\,dE(\lambda)$ 直接得到 |

**期望值为什么是定理**：把 Born 规则代进期望值的定义，再用谱分解：

$$
\langle\hat A\rangle
=\int\lambda\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle
=\Bigl\langle\psi\Bigl\lvert\int\lambda\,dE(\lambda)\Bigr\rvert\psi\Bigr\rangle
=\langle\psi\lvert\hat A\lvert\psi\rangle
$$

**中间没有新假设。** 所以“期望值等于那个双线性形式”是**推出来的**。

**所以本卡真正的输入只有一条：Born 规则。**

**它在讲什么**：谱分解告诉你"$\hat A$ 是投影的组合"——那是**算子**，不含任何态的信息。Born 规则告诉你：**把投影夹在 $\langle\psi\lvert$ 与 $\lvert\psi\rangle$ 之间**，得到的数就是概率。

**三个对象必须分清**（这是本卡最容易含糊的地方）：

| 对象 | 类型 | 归谁 |
|---|---|---|
| $E(B)$ | **算子**（投影） | [D01](D01-spectral-theorem.md) 的谱定理 |
| $\langle\psi\lvert E(B)\lvert\psi\rangle$ | **数**（概率） | **本卡的 Born 规则** |
| $dE(\lambda)$ | **算子值**测度 | 谱定理的"密度"形式 |
| $d\langle\psi\lvert E(\lambda)\lvert\psi\rangle$ | **测度**（数） | 上一行的夹取，概率密度形式 |

**为什么这个区分要紧**：若 $E(B)$ 本身就是概率，Born 规则就是多余的。它之所以是公理，正因为"**把算子变成数**"这一步没有任何数学依据——同一个投影，可以用别的归一化双线性形式去夹，物理选了这一个。

### 0.1 态是什么

**态是射线，不是矢量。** $\lvert\psi\rangle$ 与 $c\lvert\psi\rangle$（$c\neq0$）描述**同一个态**：因为

$$
p(B)=\langle c\psi\lvert E(B)\lvert c\psi\rangle=\lvert c\rvert^{2}\langle\psi\lvert E(B)\lvert\psi\rangle
$$

乘 $c$ 只是把所有权重同时放大 $\lvert c\rvert^{2}$——**没有任何测量能察觉**。所以态是**等价类**

$$
[\psi]=\{c\lvert\psi\rangle:\ c\in\mathbb{C},\ c\neq0\}
$$

这就是“射线”：复平面上从原点出发的一条半直线。

**那为什么还要写 $\langle\psi\lvert\psi\rangle=1$**：等价类里的元素长短不一，得挑一个**代表元**。挑单位长的那个不是装饰——它正是概率归一的来源：

$$
p(\mathbb{R})=\langle\psi\lvert\mathbb{1}\lvert\psi\rangle=\langle\psi\lvert\psi\rangle
$$

**要概率总和为 $1$，就必须 $\langle\psi\lvert\psi\rangle=1$。** §2 第 ② 条用的就是这个“$1$”。

**一句话**：态是**射线**（乘非零复数不改变物理）；$\langle\psi\lvert\psi\rangle=1$ 是把这条射线的代表元挑成单位长。

---

## 1. 为什么必须当成公理

| 谱定理给什么 | Born 规则加什么 |
|---|---|
| $\hat A=\int\lambda\,dE(\lambda)$——算子的结构 | $E(B)$ 的**期望值**是 $\langle\psi\lvert E(B)\lvert\psi\rangle$ |
| 谱在 $\mathbb{R}$，本征矢完备 | 本征值是**测量读数**，夹取后的模方是**概率**（连续谱时为概率密度） |

**没有一步数学能推出 Born 规则**：给定同一个算子，你完全可以把"概率"定义成别的函数（只要归一）。之所以取模方，是因为**实验**（干涉、符合计数）支持它。

**这跟 [D00](D00-commutator-axiom.md) 的地位一样**：它是输入，不是结论。

---

## 2. 三条直接推论

**① 本征态必得本征值。** 若 $\hat A\lvert\psi\rangle=a\lvert\psi\rangle$，则

$$
E(\{a\})\lvert\psi\rangle=\lvert\psi\rangle
\quad\Longrightarrow\quad
p(\{a\})=\langle\psi\lvert E(\{a\})\lvert\psi\rangle=\langle\psi\lvert\psi\rangle=1
$$

**中间那一步不是本征方程给的，要交代清楚**：本征方程只说"$\hat A$ 作用上去等于乘 $a$"，它**没有说** $E(\{a\})$ 会保留 $\lvert\psi\rangle$。这一步来自**谱定理**——$E(\{a\})$ 正是"投影到 $a$ 的本征子空间"的那个投影。

**另一条不依赖这个识别的走法（方差论证）**：记 $\mu_\psi(B)=\langle\psi\lvert E(B)\lvert\psi\rangle$，它是概率测度。由 $\int\lambda\,d\mu_\psi=\langle\hat A\rangle=a$ 与 $\int\lambda^{2}d\mu_\psi=\langle\hat A^{2}\rangle=a^{2}$，

$$
\int(\lambda-a)^{2}\,d\mu_\psi=a^{2}-2a\cdot a+a^{2}=0
$$

**方差为零的概率测度只能是 $\delta_a$**，故 $\mu_\psi(\{a\})=1$。

**边界**：本条只对**点谱**成立。连续谱时 $E(\{q\})=0$，而 $\lvert q\rangle$ 不可归一、概率无定义——所以"本征态"在这里默认指点谱本征态。

**② 概率归一。** $E(\mathbb{R})=\mathbb{1}$（[D01](D01-spectral-theorem.md) §1.2 的 resolution of identity），故
$$
p(\mathbb{R})=\langle\psi\lvert\mathbb{1}\lvert\psi\rangle=1
$$

**③ 期望值就是双线性形式。** 对 $\hat A=\int\lambda\,dE$，按 Born 规则加权：

$$
\int\lambda\,dp(\lambda)=\int\lambda\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle=\langle\psi\lvert\hat A\lvert\psi\rangle
$$

**这三条合起来说明**：谱分解 + Born 规则 = 全部可观测量的统计。

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| 与 [D01](D01-spectral-theorem.md) §1.2 相容 | $E(\mathbb{R})=\mathbb{1}$ 给 $p=1$ ✅ |
| 简并情形 | $E(\{a\})$ 是投影而非一维时，$p$ 仍是迹式，无需改定义 ✅ |
| 与其他态的叠加 | $p$ 对 $\lvert\psi\rangle$ **非线性**（$\lvert c\psi\rangle$ 给同一 $p$）——这正是"射线"的说法 ✅ |

---

## 4. 边界

1. **它只说"概率是多少"，不说"为什么是概率"。** 测量问题（波函数何时坍缩、谁在测量）不在本卡范围内，物理上仍是开放的（[P11](../problems/P11-problem-of-time.md) 相关）。
2. **坍缩（投影假设）是额外的一条。** 只算期望值不需要它；要算"测量后再测"才需要：
   $$
   \lvert\psi\rangle\;\longrightarrow\;\frac{E(B)\lvert\psi\rangle}{\sqrt{p(B)}}
   $$
3. **连续谱时 $p$ 是"落在区间"的概率**，密度 $d p/d q$ 才可谈；单点概率为零。
4. **纯态才用本卡**。混合态（热平衡、统计混合）要换成混合态的描写（属下游）。

---

## 5. 自检

- [ ] 写出 Born 规则与期望值公式，并说明它们与谱分解的分工
- [ ] 说明为什么 Born 规则不能从谱定理推出来
- [ ] 用 $E(\mathbb{R})=\mathbb{1}$ 证明概率归一
- [ ] 说明"本征态必得本征值"用到了哪一条
- [ ] 分清三条的地位：哪条是定义、哪条是公理、哪条是定理
- [ ] 指出本卡**不**包含哪一条（坍缩、测量问题）
