# D14 · 平移：$e^{ia\hat p}\lvert q\rangle=\lvert q-a\rangle$

> 建档 2026-11-06 · 上游：[D00](D00-commutator-axiom.md)、[D02](D02-position-eigen-equation.md)、[D03](D03-normalization-convention.md)、[D10](D10-two-term-truncation.md)；默认：D05
> 下游：[D15](D15-qp-overlap.md)
> 原为 [N004 §6.1](../notes/N004-hadamard-lemma.md)，2026-11-06 移入网格。

---

## 0. 命题

$$
e^{ia\hat p}\,\lvert q\rangle=\lvert q-a\rangle,
\qquad a\in\mathbb{R}
$$

三种等价说法，写清楚免得符号混：

| 形式 | 表达式 |
|---|---|
| 态 | $e^{ia\hat p}\lvert q\rangle=\lvert q-a\rangle$ |
| 左矢 | $\langle q\lvert\,e^{-ia\hat p}=\langle q-a\lvert$ |
| 波函数 | $\langle x\lvert e^{ia\hat p}\lvert\psi\rangle=\psi(x+a)$ |

**适用条件**：

1. $\hat q$ 的谱**简单**（重数为 $1$，[D01](D01-spectral-theorem.md) 的术语），否则 $e^{ia\hat p}\lvert q\rangle$ 只能定到"同本征值的某个线性组合"；
2. 相位约定：本征矢的相位取到使系数为 $1$（见 §1.3）；
3. 归一化为 $\langle q\lvert q'\rangle=\delta(q-q')$。

**它在讲什么**：$\hat p$ 是 $q$ 方向平移的生成元。**注意方向**：态标签往下移 $a$，而波函数的自变量往上移 $a$——两者不矛盾，因为 $\langle x\lvert q\rangle=\delta(x-q)$。

---

## 1. 证明

### 1.1 先把共轭关系拿到

取 $A=ia\hat p$、$B=\hat q$，由公理：

$$
[A,B]=ia[\hat p,\hat q]=ia\cdot(-i)=a
$$

$a$ 是数，于是由 [D10](D10-two-term-truncation.md)（两项截断）：

$$
e^{ia\hat p}\,\hat q\,e^{-ia\hat p}=\hat q+[A,B]=\hat q+a
$$

右乘 $e^{ia\hat p}$：

$$
e^{ia\hat p}\,\hat q=(\hat q+a)\,e^{ia\hat p}
$$

### 1.2 作用到本征矢上

两边作用在 $\lvert q\rangle$ 上，用 $\hat q\lvert q\rangle=q\lvert q\rangle$：

$$
q\,e^{ia\hat p}\lvert q\rangle
=\bigl(\hat q+a\bigr)e^{ia\hat p}\lvert q\rangle
$$

把左边的数移过去：

$$
\hat q\bigl(e^{ia\hat p}\lvert q\rangle\bigr)
=(q-a)\bigl(e^{ia\hat p}\lvert q\rangle\bigr)
$$

所以 $e^{ia\hat p}\lvert q\rangle$ 仍是 $\hat q$ 的本征矢，本征值变成 $q-a$。

### 1.3 定系数

由条件 1（重数为 $1$），本征空间是一维，故

$$
e^{ia\hat p}\lvert q\rangle=c(a,q)\,\lvert q-a\rangle
$$

由 $e^{ia\hat p}$ 是酉算子，$\lvert c\rvert=1$（用 $\delta$ 归一化：两边内积都等于 $\delta$）。于是

$$
e^{ia\hat p}\lvert q\rangle=e^{i\theta(a,q)}\,\lvert q-a\rangle
$$

**相位可以规范掉。** 重新定义基矢 $\lvert q\rangle\to e^{i\chi(q)}\lvert q\rangle$，则

$$
\theta(a,q)\ \longrightarrow\ \theta(a,q)+\chi(q)-\chi(q-a)
$$

群律 $e^{i(a+b)\hat p}=e^{ia\hat p}e^{ib\hat p}$ 给余圈条件，保证这个差分方程可解，所以可取 $\theta=0$。于是

$$
e^{ia\hat p}\,\lvert q\rangle=\lvert q-a\rangle
$$

**证毕。**

---

## 2. 一致性检验

| 检验 | 结果 |
|---|---|
| $a=0$ | 两边都是 $\lvert q\rangle$ ✅ |
| 群律 | $e^{i(a+b)\hat p}=e^{ia\hat p}e^{ib\hat p}$：两次平移分别把 $q$ 移到 $q-a$、$q-a-b$，合起来是 $e^{i(a+b)\hat p}\lvert q\rangle=\lvert q-a-b\rangle$ ✅ |
| 波函数形式 | $\langle x\lvert e^{ia\hat p}\lvert q\rangle=\delta(x-q+a)$；而 $\langle x\lvert q-a\rangle=\delta(x-q+a)$ ✅ |
| 与 $e^{a\partial_x}$ 对照 | $\hat p=-i\partial_x$ 时 $e^{ia\hat p}=e^{a\partial_x}$，作用为 $\psi(x)\to\psi(x+a)$，与表中第三行一致 ✅ |
| 谱不变 | 共轭保持谱，$\hat q$ 与 $\hat q+a$ 的谱都是 $\mathbb{R}$ ✅ |

---

## 3. 备注与边界

1. **方向最容易错。** 记法：$e^{ia\hat p}$ 把"位置标签"推向小的一侧（$q-a$），把"波函数自变量"推向大的一侧（$x+a$）。两者差一个负号，来源是 $\langle x\lvert q\rangle=\delta(x-q)$。
2. **重数为 $1$ 是前提。** 若 $\hat q$ 有内部指标（自旋、超选扇区），$e^{ia\hat p}$ 可以混合同一本征值的不同指标，结论要改成 $\sum_j S_{ij}(a)\lvert q-a,j\rangle$。
3. **相位不是定理的一部分。** $\lvert c\rvert=1$ 是定理，$c=1$ 是约定。丢掉这句话，换一套基就会"证出"矛盾。
4. **它支撑 D15。** $\langle q\lvert p\rangle=e^{ipq}$ 的推导要用 $\lvert q\rangle=e^{-iq\hat p}\lvert 0\rangle$，那正是本卡片取 $a=-q$。

---

## 4. 自检

- [ ] 不看本文，从对易子出发写出共轭关系 $e^{ia\hat p}\hat qe^{-ia\hat p}=\hat q+a$
- [ ] 说明为什么 $e^{ia\hat p}\lvert q\rangle$ 一定是 $\lvert q-a\rangle$ 的倍数，而不是别的
- [ ] 说清"重数为 $1$"这一条如果松掉，结论会变成什么
- [ ] 分别写出态形式与波函数形式，并解释两个 $a$ 的符号为何相反
- [ ] 用群律验证两次平移可以复合
