# D03 · 位置本征方程：$\hat q\lvert q\rangle=q\lvert q\rangle$

> 建档 2026-11-07 · 上游：[D01](D01-spectral-theorem.md)
> 下游：[D04](D04-normalization-convention.md)、[D05](D05-functional-calculus.md)、[D06](D06-trace.md)、[D08](D08-diagonal-criterion.md)、[D16](D16-translation.md)
> 本卡只做"取 $\hat A=\hat q$"这一步，读出本征方程与谱分解；**本卡会取定一个密度形式**（§1.2，那是选择不是推论），**正交归一的系数属下游**。

---

## 0. 命题

$$
\hat q\,\lvert q\rangle=q\,\lvert q\rangle,
\qquad
\mathbb{1}=\int\lvert q\rangle\langle q\rvert\;dq
\qquad
\hat q=\int q\,dq\,\lvert q\rangle\langle q\rvert
$$

**它在讲什么**：$\lvert q\rangle$ 是 $\hat q$ 的本征矢；把本征矢"填回"谱定理，就得到 $\hat q$ 的谱分解。

**本卡不做什么**：不讨论归一化（属下游），不重复第 1 张卡里那条定理的证明。本卡只把它的两条定理**各取一次** $\hat A=\hat q$，再把结果对起来。

---

## 1. 证明

### 1.1 第一步：Gelfand–Maurin 直接给本征方程与完备性

[D01](D01-spectral-theorem.md) §2.3：存在谱测度 $\mu$ 与广义本征矢 $F_\lambda\in\Phi^{\times}$，使

$$
\hat A F_\lambda=\lambda F_\lambda,
\qquad
\mathbb{1}=\int\lvert F_\lambda\rangle\langle F_\lambda\rvert\,d\mu(\lambda)
$$

取 $\hat A=\hat q$、$F_\lambda=\lvert q\rangle$、$\lambda=q$：

$$
\hat q\lvert q\rangle=q\lvert q\rangle,
\qquad
\mathbb{1}=\int\lvert q\rangle\langle q\rvert\,d\mu(q)
$$

**本征方程在这里是一行**——它不是推出来的，是定理的直接特化。**存在性的全部来源就是这一步。**

### 1.2 第二步：定密度形式（本卡的**选择**）

定理只给 $d\mu$。要写出"$\hat q$ 按 $\lvert q\rangle$ 展开"的具体样子，还要**选定谱测度的密度**。本卡取

$$
E(B)=\int_B dq\,\lvert q\rangle\langle q\rvert
\qquad\bigl(\text{即 } dE(q)=dq\,\lvert q\rangle\langle q\rvert\bigr)
$$

**这是一次选择，不是定理的推论。** 它等价于固定 $\lvert q\rangle$ 的尺度：把 $\lvert q\rangle$ 乘常数、把 $dq$ 除以同一因子，整条式子不变。

**这一步同时把 $\mu$ 定成了 Lebesgue**：同一个 $\mathbb{1}$ 分解成同一种密度，两边的权重只能重合。所以

$$
d\mu(q)=dq
$$

**至于 $\langle q\lvert q'\rangle$ 的系数**——那是"投影"这一条要求的，属下游（归一化那一卡）；本卡只用"每一点的分量是 $\lvert q\rangle\langle q\rvert$"。

### 1.3 第三步：代入谱定理

[D01](D01-spectral-theorem.md) §1.1 的谱定理给

$$
\hat q=\int q\,dE(q)
$$

把 §1.2 的密度形式代进 $dE$ 的位置：

$$
\hat q=\int q\,dE(q)=\int q\,dq\,\lvert q\rangle\langle q\rvert
$$

**这一步是"代入"，不是"对照"**：谱定理告诉你 $dE$ 在哪里，§1.2 告诉你 $dE$ 是什么。

### 1.4 第四步：完备性的同一个写法

由 §1.2 的密度形式与 $\int dE=\mathbb{1}$（[D01](D01-spectral-theorem.md) §1.1）：

$$
\mathbb{1}=\int\lvert q\rangle\langle q\rvert\,dq
$$

这与 §1.1 的 $\mathbb{1}=\int\lvert q\rangle\langle q\rvert\,d\mu$ 是**同一个选择的两种写法**（§1.2 已把 $\mu$ 定成 $dq$）。**它们不互相推出，只是同一件事换了记号。**

**证毕。**

---

## 2. 为什么值得单列（本征方程 vs 谱分解）

两种说法等价，但**用途不同**：

| 说法 | 用在 |
|---|---|
| $\hat q=\int q\,dq\lvert q\rangle\langle q\rvert$ | 算子的谱分解（函数演算要用它） |
| $\hat q\lvert q\rangle=q\lvert q\rangle$ | 作用在**单个矢**上（对角判据、平移都要用它） |

**本征方程是把“对角”从算子层面降到矢量层面的那句话。**

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| 谱为实数 | $\hat q$ 自伴 $\Rightarrow$ 本征值 $q\in\mathbb{R}$，与 [D01](D01-spectral-theorem.md) §1.1 一致 ✅ |
| 与 [D01](D01-spectral-theorem.md) §2.2 相容 | 本卡就是 $\hat A F_\lambda=\lambda F_\lambda$ 取 $\hat A=\hat q$ ✅ |
| 自洽 | §1.2 的密度形式同时给出 §1.3 的算子式与 §1.4 的完备性 ✅ |

---

## 4. 边界

1. **"简单谱"是前提。** 重数大于 1 时 $dE$ 的密度不是 $\lvert q\rangle\langle q\rvert$，而要写成 $\sum_i\lvert q,i\rangle\langle q,i\rvert$，本征方程要加指标。
2. **绝对连续是前提。** 纯点谱时没有密度，$\delta$ 要换成 $\delta_{qq'}$，求和代替积分（[D01](D01-spectral-theorem.md) §5 的离散特例）。
3. **$\lvert q\rangle$ 不在 $\mathcal{H}$ 内。** 本征方程是 $\Phi^{\times}$ 意义下的等式（[D01](D01-spectral-theorem.md) §2.1）。
4. **不能拿本卡去"证明"Gelfand–Maurin。** 本卡的起点就是那条定理；循环的方向是 D01 → 本卡，不是反过来。
5. **本卡只取密度形式。** 正交归一的**系数**不在本卡——它由"投影"这一条逼出，属下游。

---

## 5. 自检

- [ ] 说明本征方程为什么是"一行"，它的存在性来自哪条定理
- [ ] 说明密度形式是一次**选择**而非推论，以及它等价于固定什么
- [ ] 说明 $\hat q$ 的表达式是"代入"而不是"对照"
- [ ] 说明重数大于 1 时哪一步失效
