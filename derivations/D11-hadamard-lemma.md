# D11 · Hadamard 引理：$e^{A}Be^{-A}$ 的对易子展开

> 建档 2026-11-06 · 上游：无；默认：D06
> 下游：[D12](D12-two-term-truncation.md)、[D14](D14-three-bch-forms.md)、[D16](D16-translation.md)
> 原为 [N004 §2](../notes/N004-hadamard-lemma.md)，2026-11-06 移入网格以便引用。

---

## 0. 命题

$$
e^{A}Be^{-A}
=\sum_{n=0}^{\infty}\frac{1}{n!}\,\mathrm{ad}_A^{\,n}B
$$

写开：

$$
e^{A}Be^{-A}
=B+[A,B]+\frac{1}{2!}\bigl[A,[A,B]\bigr]
+\frac{1}{3!}\Bigl[A,\bigl[A,[A,B]\bigr]\Bigr]+\cdots
$$

其中 $\mathrm{ad}_A X\equiv[A,X]$。等价的一句话写法：

$$
\mathrm{Ad}\bigl(e^{A}\bigr)=e^{\mathrm{ad}_A}
$$

**适用条件**：

1. $e^{\pm A}$ 有定义——$A$ 有界时处处成立；$A$ 无界时在解析向量子空间上成立（函数演算的定义见 [D06](D06-functional-calculus.md)）；
2. 级数收敛——有界 $A$ 时对任意 $B$ 收敛；无界时逐例讨论；
3. 这是**恒等式**，不是近似：等号处处成立，没有截断误差。

**它在讲什么**：共轭的无穷小生成元是对易子。

---

## 1. 证明：三步

### 1.1 第一步：求导，得到一个方程

定义

$$
F(t)\equiv e^{tA}\,B\,e^{-tA}
$$

对 $t$ 求导。两项各求一次，且 $A$ 与 $e^{tA}$ 对易（$Ae^{tA}=e^{tA}A$）：

$$
\frac{dF}{dt}
=A\,e^{tA}Be^{-tA}-e^{tA}B\,A\,e^{-tA}
=e^{tA}\bigl(AB-BA\bigr)e^{-tA}
=e^{tA}[A,B]\,e^{-tA}
$$

再用一次 $A$ 与 $e^{\pm tA}$ 对易，把结果写成对易子：

$$
\frac{dF}{dt}=\bigl[A,\ e^{tA}Be^{-tA}\bigr]=[A,F(t)]
$$

即

$$
\boxed{\ \frac{dF}{dt}=\mathrm{ad}_A F(t)\ },\qquad F(0)=B
$$

**这一步的实质**：求导被翻译成"作用一个线性算子"。原本要算无穷多个嵌套对易子，现在只要求解一个常系数线性方程。

### 1.2 第二步：解方程

方程 $\dot F=LF$，$L=\mathrm{ad}_A$。用积分因子：

$$
G(t)\equiv e^{-t\,\mathrm{ad}_A}F(t)
$$

$$
\frac{dG}{dt}
=-e^{-t\,\mathrm{ad}_A}\,\mathrm{ad}_A F+e^{-t\,\mathrm{ad}_A}\,\dot F
=-e^{-t\,\mathrm{ad}_A}\mathrm{ad}_A F+e^{-t\,\mathrm{ad}_A}\mathrm{ad}_A F=0
$$

所以 $G$ 是常数，$G(t)=G(0)=F(0)=B$。因此

$$
F(t)=e^{t\,\mathrm{ad}_A}B
$$

### 1.3 第三步：展开，取 $t=1$

按指数函数的定义展开 $e^{t\,\mathrm{ad}_A}$：

$$
F(t)=\sum_{n=0}^{\infty}\frac{t^{n}}{n!}\,\mathrm{ad}_A^{\,n}B
$$

取 $t=1$，得 §0 的结论。

**注意这一步没有引入新技巧**：只是把 $e^{tL}$ 按定义展开。级数是否收敛由 $L$ 的谱决定，物理上只在"两边都良定义"的范围内使用。

---

## 2. 一致性检验

| 检验 | 结果 |
|---|---|
| $t=0$ 退化为恒等 | 左为 $B$，右为 $\mathrm{ad}_A^{0}B=B$，成立 |
| $[A,B]=0$ | 级数只剩 $B$，两边都等于 $B$，成立 |
| 与 [D12](D12-two-term-truncation.md) 相容 | $[A,B]=c$ 是数时 $\mathrm{ad}_A^{2}B=0$，级数两项，与 D12 一致 |
| 与 [D16](D16-translation.md) 相容 | 取 $A=ia\hat p$、$B=\hat q$，得 $e^{ia\hat p}\hat qe^{-ia\hat p}=\hat q+a$，即平移 |
| 与 [D13](D13-commutator-phase.md)、[D14](D14-three-bch-forms.md) 相容 | 由本式可推出 $e^{A}e^{B}=e^{c}e^{B}e^{A}$ 与三条 BCH 闭式 |
| 自同构性质 | $\mathrm{ad}_A$ 满足 Leibniz，故 $e^{\mathrm{ad}_A}$ 是代数自同构，与"共轭是自同构"一致 |
| 例：平移 | $A=ia\hat p$、$B=\hat q$，级数在前两项截断，结果 $\hat q+a$ ✅ |

---

## 3. 备注与边界

1. **别把它当近似。** 这是恒等式；级数"停"与"不停"取决于 $\mathrm{ad}_A$ 是否幂零（见 [D12](D12-two-term-truncation.md)），与精度无关。
2. **系数是 $1/n!$。** 来自指数函数的泰勒展开，不是组合数。$[A,[A,B]]$ 前面的系数是 $1/2$，不是 $1$。
3. **无界情形。** $A$ 无界时 $e^{tA}$ 只在稠密子空间上有定义，$\frac{d}{dt}$ 与共轭的写法都要配定义域条件。结构不变，但"处处成立"要改成"在公共定义域上成立"。
4. **推导只用了两样东西**：$A$ 与 $e^{tA}$ 对易；$\mathrm{ad}_A$ 是线性算子。没有用到 $A$、$B$ 的任何特殊性质——这正是它普遍适用的原因。

---

## 4. 自检

- [ ] 不看本文，写出定义 $F(t)$ 到 $\dot F=\mathrm{ad}_AF$ 的三行推导
- [ ] 说明积分因子 $G=e^{-\mathrm{ad}_A t}F$ 为什么能把方程解出来
- [ ] 指出级数截断的条件，并说明它与"$A$、$B$ 是否对易"的关系
- [ ] 用本式推出 D12（两项截断）
- [ ] 说明为什么这是恒等式而不是近似
