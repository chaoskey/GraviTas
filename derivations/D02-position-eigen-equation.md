# D02 · 位置本征方程：$\hat q\lvert q\rangle=q\lvert q\rangle$

> 建档 2026-11-07 · 上游：[D01](D01-spectral-theorem.md)（谱分解与 $\hat q$ 的简单谱）
> 下游：[D06](D06-diagonal-criterion.md)、[D13](D13-translation.md)
> 本卡把"本征方程"从前提变成结论，并顺手交代**正交归一从哪来**。

---

## 0. 命题

$$
\hat q\,\lvert q\rangle=q\,\lvert q\rangle,
\qquad
\langle q\lvert q'\rangle=\delta(q-q')
$$

**它在讲什么**：$\lvert q\rangle$ 是 $\hat q$ 的本征矢，本征值 $q$ 是实数。

**本卡的定位要说清**：它**不是**从零证明"存在这样的矢"，而是证明——**给定 [D01](D01-spectral-theorem.md) 的谱分解与"简单谱"识别，本征方程一行得出，正交归一是投影测度性质推出来的**。非循环的存在性来源仍是 [D01](D01-spectral-theorem.md) §2.2 的 Gelfand–Maurin。

---

## 1. 证明

### 1.1 第一步：谱分解

由 [D01](D01-spectral-theorem.md) §1.1，自伴的 $\hat q$ 对应唯一的投影值测度 $E$：

$$
\hat q=\int_{\sigma(\hat q)}q\;dE(q)
$$

### 1.2 第二步：把测度写成密度

谱**简单且绝对连续**时（[D01](D01-spectral-theorem.md) §2.4 的条件），$E$ 对 Lebesgue 测度有密度：

$$
dE(q)=dq\,\lvert q\rangle\langle q\rvert
$$

**这一步是"识别"，不是"推导"**：它把"$\lvert q\rangle$ 是本征矢族"作为识别的内容写进来——所以本卡证明的是**自洽性**，存在性靠 D01。

于是

$$
\hat q=\int q\,dq\,\lvert q\rangle\langle q\rvert
\qquad\text{（哑变量改名为 $q'$ 得 } \hat q=\int q'\,dq'\,\lvert q'\rangle\langle q'\rvert\text{）}
$$

### 1.3 第三步：作用在本征矢上

$$
\hat q\lvert q\rangle
=\int q'\,dq'\;\lvert q'\rangle\;\langle q'\lvert q\rangle
\overset{(*)}=
\int q'\,dq'\;\lvert q'\rangle\;\delta(q'-q)
=q\,\lvert q\rangle
$$

其中 $(*)$ 用下一节的结论：$\langle q'\lvert q\rangle=\delta(q'-q)$。

**证毕。**

### 1.4 正交归一从哪来（不是假设）

$E$ 是**投影值**测度，故对不交的 $B,B'$

$$
E(B)E(B')=E(B\cap B')=0
$$

代入密度形式：

$$
0=\int_B\!\!\int_{B'}\langle q\lvert q'\rangle\,\lvert q\rangle\langle q'\rvert\,dq\,dq'
$$

这要求 $\langle q\lvert q'\rangle$ 的支撑只在 $q=q'$，即正比于 $\delta(q-q')$；系数取 $1$ 是 [D01](D01-spectral-theorem.md) §2.4 的归一化选择。

**所以正交归一是"投影性 + 密度识别"的推论，不是独立假设。** 这一条以前散落在各处、没人负责，本卡把它收下。

---

## 2. 为什么必须写成"本征方程"而不是"直接说 $\hat q$ 对角"

两种说法等价，但**用途不同**：

| 说法 | 用在 |
|---|---|
| $\hat q=\int q\,dq\lvert q\rangle\langle q\rvert$ | 算子的谱分解（[D04](D04-functional-calculus.md) 的函数演算） |
| $\hat q\lvert q\rangle=q\lvert q\rangle$ | 作用在**单个矢**上（[D06](D06-diagonal-criterion.md) 的对易子论证、[D13](D13-translation.md) 的平移） |

**本征方程是把"对角"从算子层面降到矢量层面的那句话。** [D06](D06-diagonal-criterion.md) 的整条推导都靠它。

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| 谱为实数 | $\hat q$ 自伴 $\Rightarrow$ 本征值 $q\in\mathbb{R}$，与 [D01](D01-spectral-theorem.md) §1.1 一致 ✅ |
| 与 [D01](D01-spectral-theorem.md) §2.2 相容 | Gelfand–Maurin 的 $\hat A F_\lambda=\lambda F_\lambda$ 取 $\hat A=\hat q$ 即本卡命题 ✅ |
| 与 [D06](D06-diagonal-criterion.md) 相容 | 那里用 $\langle q'\lvert\hat q=q'\langle q'\rvert$（需自伴）与本卡右矢版本配对 ✅ |
| 与 [D15](D15-p-completeness.md) 对称 | 那边对 $\hat p$ 做同一件事，只是权重带 $2\pi$ ✅ |

---

## 4. 边界

1. **"简单谱"是前提。** 重数大于 1 时 $E$ 的密度不是 $\lvert q\rangle\langle q\rvert$，而要写成 $\sum_i\lvert q,i\rangle\langle q,i\rvert$，本征方程要加指标。
2. **绝对连续是前提。** 纯点谱时没有密度，$\delta$ 要换成 $\delta_{qq'}$，求和代替积分（[D01](D01-spectral-theorem.md) §4 第 3 条的离散特例）。
3. **$\lvert q\rangle$ 不在 $\mathcal{H}$ 内。** 本征方程是 $\Phi^{\times}$ 意义下的等式（[D01](D01-spectral-theorem.md) §2.3）。
4. **不能拿本卡去"证明"Gelfand–Maurin。** 本卡的起点（密度识别）已经预设了那个家族存在；循环的方向是 D01 → 本卡，不是反过来。

---

## 5. 自检

- [ ] 从 $\hat q=\int q\,dE$ 出发，写出本征方程的三步
- [ ] 说明 $dE=dq\lvert q\rangle\langle q\rvert$ 是"识别"而非"推导"，以及它的非循环来源
- [ ] 用投影性 $E(B)E(B')=0$ 推出正交归一的支撑
- [ ] 说明重数大于 1 时本卡哪一步失效
- [ ] 对比本卡与 [D15](D15-p-completeness.md)：为什么 $\hat p$ 那边要多一个 $2\pi$
