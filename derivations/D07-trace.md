# D07 · 迹：$\mathrm{Tr}\,\hat A=\int dq\,\langle q\lvert\hat A\lvert q\rangle$

> 建档 2026-11-08 · 上游：[D01](D01-spectral-theorem.md)（完备性）、[D03](D03-position-eigen-equation.md)（位置基）、[D04](D04-normalization-convention.md)
> 下游：[D22](D22-trace-is-loop.md)、[D23](D23-density-matrix.md)、[D26](D26-energy-basis.md)
> 本卡补的是"迹"这个对象的定义与基无关性——[D22](D22-trace-is-loop.md) 一直在用它，却没人交代过。

---

## 0. 命题

对**任意**一组正交完备基：

$$
\mathrm{Tr}\,\hat A=\sum_n\langle n\lvert\hat A\lvert n\rangle
$$

特别地，取位置基：

$$
\mathrm{Tr}\,\hat A=\int dq\,\langle q\lvert\hat A\lvert q\rangle
$$

**它在讲什么**：迹是"对角元之和"，而且**与选哪组基无关**——这个"无关"不是假设，是下面两行证明的结论。

**说明**：动量基下的写法 $\int\frac{dp}{2\pi}\langle p\lvert\hat A\lvert p\rangle$ 也是对的，但那要用动量基的完备性（属下游）；本卡不需要它。

---

## 1. 证明：基无关

设 $\{\lvert n\rangle\}$ 与 $\{\lvert m\rangle\}$ 是**任意两组**正交完备基。用两次完备性：

$$
\sum_n\langle n\lvert\hat A\lvert n\rangle
=\sum_n\sum_m\langle n\lvert m\rangle\,\langle m\lvert\hat A\lvert n\rangle
$$

再把 $\langle n\lvert m\rangle=\overline{\langle m\lvert n\rangle}$ 挪到右边，重新配对：

$$
=\sum_m\sum_n\langle m\lvert\hat A\lvert n\rangle\,\langle n\lvert m\rangle
=\sum_m\Bigl\langle m\Bigl\lvert\hat A\Bigl(\sum_n\lvert n\rangle\langle n\rvert\Bigr)\Bigr\lvert m\Bigr\rangle
=\sum_m\langle m\lvert\hat A\lvert m\rangle
$$

**两边相等。** 因为 $\{\lvert n\rangle\}$ 与 $\{\lvert m\rangle\}$ 是任意选的，所以迹与基无关。**证毕。**

（只用到两件事：两组完备性 $\sum\lvert\cdot\rangle\langle\cdot\rvert=\mathbb{1}$，来自 [D01](D01-spectral-theorem.md)；以及求和的绝对收敛，见 §4。）

**取位置基**就是把 $\{\lvert n\rangle\}$ 换成 $\{\lvert q\rangle\}$、求和换成积分：

$$
\mathrm{Tr}\,\hat A=\int dq\,\langle q\lvert\hat A\lvert q\rangle
$$

这一步用到 [D03](D03-position-eigen-equation.md) 的本征基与 [D04](D04-normalization-convention.md) 的归一化，但它**不影响基无关性本身**——那是 §1 已经证过的。

---

## 2. 四条性质

| 性质 | 内容 |
|---|---|
| 线性 | $\mathrm{Tr}(\alpha A+\beta B)=\alpha\mathrm{Tr}A+\beta\mathrm{Tr}B$ |
| **循环** | $\mathrm{Tr}(\hat A\hat B)=\mathrm{Tr}(\hat B\hat A)$ —— 由核展开即得 |
| 正定 | $\hat A\ge0\Rightarrow\mathrm{Tr}\hat A\ge0$（对角元非负） |
| 相似不变 | $\mathrm{Tr}(U\hat AU^{\dagger})=\mathrm{Tr}\hat A$，所以基无关 |

**循环性是下游“把两端焊起来”那一步的前提**：$e^{-\beta H}$ 的迹不依赖你把切点放在哪。

---

## 3. 与谱分解的关系

设 $\hat A=\int\lambda\,dE(\lambda)$，定义**谱测度的迹**

$$
\mu_A(B)\equiv\mathrm{Tr}\,E(B)
$$

则对任意可积的 $f$：

$$
\mathrm{Tr}\,f(\hat A)=\int f(\lambda)\,d\mu_A(\lambda)
$$

**$\mu_A(\mathbb{R})=\mathrm{Tr}\,\mathbb{1}$ 是"态空间的维数"**（连续谱时为发散，这也是为什么 $Z$ 必须靠 $e^{-\beta H}$ 收敛）。

---

## 4. 边界

1. **无界算子可能不可迹。** $\mathrm{Tr}\,\mathbb{1}$ 无穷；但 $e^{-\beta\hat H}$ 对 $\beta>0$ 通常可迹——这正是下游能把它写成可迹表达式的原因。
2. **连续谱时"迹"是形式的。** $\int dq\langle q\lvert A\lvert q\rangle$ 对一般 $A$ 发散；只有衰减足够快的算符（如 $e^{-\beta H}$）给出有限值。
3. **它不依赖归一化约定的具体取值**，但依赖"完备性写成 $\int dq\lvert q\rangle\langle q\rvert$"这一形式（[D03](D03-position-eigen-equation.md)）。若换成带权重的写法，$\int dq$ 前要补同样的权重。

---

## 5. 自检

- [ ] 用动量完备性证明迹与基无关，并说出用了哪两条公式
- [ ] 说明为什么 $\mathrm{Tr}(AB)=\mathrm{Tr}(BA)$ 对下游很关键
- [ ] 写出 $\mathrm{Tr}\,f(\hat A)$ 的谱表示
- [ ] 解释 $\mathrm{Tr}\,\mathbb{1}$ 为什么发散、而 $\mathrm{Tr}\,e^{-\beta H}$ 不一定
