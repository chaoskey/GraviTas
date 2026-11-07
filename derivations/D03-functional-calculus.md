# D03 · 函数演算：$f(\hat A)$ 到底是什么意思

> 建档 2026-11-06 · 上游：[D01](D01-spectral-theorem.md)
> 下游：[D04](D04-commutator-p-fq.md)、[D07](D07-hadamard-lemma.md)、[D09](D09-commutator-phase.md)、[D10](D10-three-bch-forms.md)、[D11](D11-weyl-phase.md)、[D12](D12-translation.md)、[D13](D13-qp-overlap.md)
> 原散见于 [N003 §4.1](../notes/N003-basis-and-operator-relations.md) 与各卡片的"条件"里，2026-11-06 汇总成卡。

---

## 0. 命题

设 $\hat A$ 是**自伴**算子。则 $f(\hat A)$ 有下面三种定义方式，它们在"能同时使用"的范围内**一致**：

| 定义方式 | 适用的 $f$ | 用在哪 |
|---|---|---|
| 幂级数 | 解析函数 | [D07](D07-hadamard-lemma.md) 的 $e^{tA}$、[D09](D09-commutator-phase.md) 的 $e^{B}$ |
| 谱分解 | Borel 可测函数（最一般） | 一般 $f$，包括不可微的 |
| 本征基展开 | 谱简单时的连续函数 | [D04](D04-commutator-p-fq.md)、[D13](D13-qp-overlap.md) |

**它在讲什么**："把函数作用在算子上"不是符号游戏，而是一个**有唯一答案**的操作——但先决条件是 $\hat A$ 自伴。非自伴的算子没有这套东西。

---

## 1. 三种定义

### 1.1 幂级数（解析函数）

$$
f(\hat A)\equiv\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}\,\hat A^{n}
$$

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

其中 $f$ 是 $\sigma(\hat A)$ 上的有界 Borel 函数；$f$ 无界时，定义域收窄为

$$
D\bigl(f(\hat A)\bigr)=\Bigl\{\psi\;\Big|\;\int\lvert f(\lambda)\rvert^{2}\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle<\infty\Bigr\}
$$

**这是唯一覆盖全部"可测函数"的定义**，也是 D03 的**谱定理依赖**所在——谱定理是外部定理，不在此网格内。

### 1.3 本征基展开（谱简单时）

若 $\hat A$ 的谱简单、绝对连续，且已有 $\delta$ 归一化的广义本征矢 $\lvert a\rangle$（[D13](D13-qp-overlap.md) 的兄弟情形），则

$$
f(\hat A)=\int da\;f(a)\,\lvert a\rangle\langle a\rvert
$$

**这就是 [D04](D04-commutator-p-fq.md) 与 [N003 §4.1](../notes/N003-basis-and-operator-relations.md) 一直用的形式。** 它是 1.2 的"谱简单"特例：$dE(\lambda)$ 写成 $\lvert\lambda\rangle\langle\lambda\rvert\,d\lambda$。

**注意**：这个写法隐含条件"-归一化密度为 1"，即谱测度对 Lebesgue 测度的密度为 $1$。弯曲空间里密度是 $\sqrt{g}$，$dE$ 与 $\lvert a\rangle\langle a\rvert\,da$ 之间会差一个因子（见 [D12](D12-translation.md) 的同期讨论与 [D17](D17-trace-is-loop.md) §3 的测度问题）。

### 1.4 三者为何一致

**多项式上**：三者显然一致（$f(\lambda)=\lambda^{n}$ 时都给出 $\hat A^{n}$）。

**解析函数上**：由谱定理的**有界函数演算是连续同态**，且 $\hat A^{n}$ 与 $\int\lambda^{n}dE$ 一致，故对收敛的幂级数逐项取极限即得一致。这一步用到了"谱映射定理"（见 §2）。

**这说明什么**：幂级数定义不是"另一个定义"，而是谱分解定义在解析函数上的**简化版**。真正的定义是 1.2，1.1 与 1.3 是它的可计算形式。

---

## 2. 必须记住的六条性质

| 性质 | 内容 |
|---|---|
| 同态 | $(fg)(\hat A)=f(\hat A)\,g(\hat A)$（对同一算子的函数） |
| 与自变量对易 | $[f(\hat A),\hat A]=0$ |
| 谱映射定理 | $\sigma\bigl(f(\hat A)\bigr)=f\bigl(\sigma(\hat A)\bigr)$（$f$ 连续） |
| 自伴判据 | $f(\hat A)$ 自伴 $\iff$ $f$ 在谱上取实值 |
| 酉判据 | $f(\hat A)$ 酉 $\iff$ $\lvert f\rvert=1$ 在谱上 |
| 有界性 | $\lVert f(\hat A)\rVert=\sup_{\lambda\in\sigma(\hat A)}\lvert f(\lambda)\rvert$ |

**谱映射定理是最有用的一条**：它把"算子是否有界/自伴/酉"变成"函数在谱上是否有界/实/模 1"。例如 $\hat A$ 自伴 $\Rightarrow$ $e^{i\hat A}$ 是酉算子，用的就是这条。

**注意同态只对同一个算子的函数成立**：$f(\hat A)g(\hat B)\neq g(\hat B)f(\hat A)$，除非 $\hat A,\hat B$ 对易。

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| $f(\lambda)=1$ | 三个定义都给 $\mathbb{1}$ ✅ |
| $f(\lambda)=\lambda$ | 三个定义都给 $\hat A$ ✅ |
| $f(\lambda)=\lambda^{n}$ | 都给 $\hat A^{n}$ ✅ |
| $f(\lambda)=e^{i\lambda}$，$\hat A$ 自伴 | $\lvert e^{i\lambda}\rvert=1$，故 $e^{i\hat A}$ 酉 ✅ |
| $f(\lambda)=e^{-\beta\lambda}$，$\hat A$ 有下界 | $f$ 有界，$\lVert e^{-\beta\hat A}\rVert\le1$ ✅ |
| 与 [D07](D07-hadamard-lemma.md) 相容 | $e^{tA}$ 是整函数，幂级数定义收敛半径无穷 ✅ |

---

## 4. 备注与边界

1. **自伴是前提。** 非自伴算子（如 Jordan 块）没有谱定理，只能用 Dunford 演算，且只对"谱点附近解析"的函数有定义。**这一条决定了整套量子力学为什么要求可观测量自伴。**
2. **幂级数定义不能推得太远。** $1/\hat A$、$\sqrt{\hat A}$、$\ln\hat A$ 都要走谱分解；用幂级数硬写会发散或给出错误结果。
3. **$f'(\hat A)$ 是对函数求导。** 常见混淆：$\frac{d}{d\hat A}f(\hat A)$ 这种写法不是"对算子求导"，而是"先对函数求导、再作函数演算"（[D04](D04-commutator-p-fq.md) §4 讨论过这个措辞）。
4. **"同一个算子的函数"这个限制很紧。** $f(\hat A)+g(\hat B)$ 没有简单规则；两套函数演算要合并，必须先证明 $\hat A,\hat B$ 对易。
5. **无界时定义域要说清。** $e^{tA}$ 对无界 $A$ 在解析向量上有定义，但"处处成立"不成立。这是 [D07](D07-hadamard-lemma.md) §3 第 3 条的来源。

---

## 5. 自检

- [ ] 写出函数演算的三种定义，并说明它们各自的适用范围
- [ ] 说明为什么"多项式上三者一致"能推出"解析函数上三者一致"
- [ ] 用谱映射定理证明：$\hat A$ 自伴 $\Rightarrow$ $e^{i\hat A}$ 酉
- [ ] 举一个不能用幂级数定义的函数，并说明该走哪条定义
- [ ] 解释 $\lVert f(\hat A)\rVert=\sup\lvert f\rvert$ 是从哪来的
- [ ] 说明为什么非自伴算子没有这套演算
