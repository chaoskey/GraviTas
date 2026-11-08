# D07 · 迹：$\mathrm{Tr}\,\hat A=\int dq\,\langle q\lvert\hat A\lvert q\rangle$

> 建档 2026-11-08 · 上游：[D01](D01-spectral-theorem.md)（完备性）、[D04](D04-normalization-convention.md)
> 下游：[D22](D22-trace-is-loop.md)、[D23](D23-density-matrix.md)、[D26](D26-energy-basis.md)
> 本卡补的是"迹"这个对象的定义与基无关性——[D22](D22-trace-is-loop.md) 一直在用它，却没人交代过。

---

## 0. 命题

对一组正交完备基（任意表象）：

$$
\mathrm{Tr}\,\hat A=\sum_n\langle n\lvert\hat A\lvert n\rangle
=\int dq\,\langle q\lvert\hat A\lvert q\rangle
=\int\frac{dp}{2\pi}\,\langle p\lvert\hat A\lvert p\rangle
$$

**它在讲什么**：迹是"对角元之和"，而且**与选哪组基无关**。这个"无关"不是假设，是下面一行证明的结论。

---

## 1. 证明：基无关

用 $\lvert q\rangle$ 算，插入动量完备性 $1=\int\frac{dp}{2\pi}\lvert p\rangle\langle p\rvert$（[D18](D18-p-completeness.md)）：

$$
\int dq\,\langle q\lvert\hat A\lvert q\rangle
=\int dq\int\frac{dp}{2\pi}\,\langle q\lvert p\rangle\,\langle p\lvert\hat A\lvert q\rangle
$$

再把 $\langle p\lvert\hat A\lvert q\rangle$ 用位置完备性展开：

$$
\langle p\lvert\hat A\lvert q\rangle=\int dq'\,\langle p\lvert q'\rangle\,\langle q'\lvert\hat A\lvert q\rangle
$$

代回去，对 $q$ 积分：

$$
\int dq\;e^{ipq}e^{-ipq'}=\ 2\pi\,\delta(q-q')
\quad\Longrightarrow\quad
\int\frac{dp}{2\pi}\,\langle p\lvert\hat A\lvert p\rangle
$$

**两边相等。** 对任意两组正交完备基都成立，所以迹与基无关。

（用到的两条：$\langle q\lvert p\rangle=e^{ipq}$ 与两组完备性。这就是 [D17](D17-qp-overlap.md) 与 [D18](D18-p-completeness.md)。）

---

## 2. 四条性质

| 性质 | 内容 |
|---|---|
| 线性 | $\mathrm{Tr}(\alpha A+\beta B)=\alpha\mathrm{Tr}A+\beta\mathrm{Tr}B$ |
| **循环** | $\mathrm{Tr}(\hat A\hat B)=\mathrm{Tr}(\hat B\hat A)$ —— 由 [D10](D10-product-kernel.md) 的核展开即得 |
| 正定 | $\hat A\ge0\Rightarrow\mathrm{Tr}\hat A\ge0$（对角元非负） |
| 相似不变 | $\mathrm{Tr}(U\hat AU^{\dagger})=\mathrm{Tr}\hat A$，所以基无关 |

**循环性是 [D22](D22-trace-is-loop.md) 能"把两端焊起来"的前提**：$e^{-\beta H}$ 的迹不依赖你把切点放在哪。

---

## 3. 与谱分解的关系（[D22](D22-trace-is-loop.md) 要用）

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

1. **无界算子可能不可迹。** $\mathrm{Tr}\,\mathbb{1}$ 无穷；但 $e^{-\beta H}$ 对 $\beta>0$ 通常可迹——这正是 [D23](D23-density-matrix.md) 能定义 $Z$ 的原因。
2. **连续谱时"迹"是形式的。** $\int dq\langle q\lvert A\lvert q\rangle$ 对一般 $A$ 发散；只有衰减足够快的算符（如 $e^{-\beta H}$）给出有限值。
3. **它不依赖归一化约定的具体取值**，但依赖"完备性写成 $\int dq\lvert q\rangle\langle q\rvert$"这一形式（[D04](D04-normalization-convention.md)）。若换成带权重的写法，$\int dq$ 前要补同样的权重。

---

## 5. 自检

- [ ] 用动量完备性证明迹与基无关，并说出用了哪两条公式
- [ ] 说明为什么 $\mathrm{Tr}(AB)=\mathrm{Tr}(BA)$ 对 D22 很关键
- [ ] 写出 $\mathrm{Tr}\,f(\hat A)$ 的谱表示
- [ ] 解释 $\mathrm{Tr}\,\mathbb{1}$ 为什么发散、而 $\mathrm{Tr}\,e^{-\beta H}$ 不一定
