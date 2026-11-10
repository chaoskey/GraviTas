# D04 · 归一化约定：$\langle q\lvert q'\rangle=\delta(q-q')$

> 建档 2026-11-07 · 类型：**约定卡**——记下"哪些是被迫的、哪些是选的"
> 上游：[D01](D01-spectral-theorem.md)（谱定理）、[D03](D03-position-eigen-equation.md)（$\delta$ 的**形式**是被迫的）
> 下游：[D07](D07-trace.md)、[D09](D09-diagonal-criterion.md)、[D16](D16-translation.md)、[D17](D17-qp-overlap.md)、[D18](D18-p-completeness.md)

---

## 0. 约定

$$
\langle q\lvert q'\rangle=\delta(q-q')
$$

**本卡只定这一条。** 完备性 $\int dq\lvert q\rangle\langle q\rvert=\mathbb{1}$ **不在本卡**——它是 [D03](D03-position-eigen-equation.md) §1.2 的结论，本卡不重复。

**但这两条必须配对**，成分也不同：

| 成分 | 地位 | 依据 |
|---|---|---|
| 为什么是 $\delta$（不是别的函数） | **被迫** | 投影测度的投影性（见 §0.1） |
| $\delta$ 前的系数为什么是 $1$ | **选的** | 与 [D03](D03-position-eigen-equation.md) 的完备性权重配对（§1） |

**这意味着什么**：不要把整条当成"约定"一笔勾销——形式有来源，只有系数是自由的。反过来也不要以为系数能随便取：它必须与完备性的权重配合。

### 0.1 为什么形式是 $\delta$（不是别的函数）

$E$ 是**投影值**测度，故对不交的 Borel 集 $B,B'$：

$$
E(B)\,E(B')=0
$$

由 [D03](D03-position-eigen-equation.md) §1.3 的密度形式 $E(B)=\int_B dq\,\lvert q\rangle\langle q\rvert$：

$$
0=\int_B\!\!\int_{B'}\langle q\lvert q'\rangle\,\lvert q\rangle\langle q'\rvert\,dq\,dq'
$$

要让这个式子在**所有**不交的 $B,B'$ 上都为零，$\langle q\lvert q'\rangle$ 的支撑只能落在对角线 $q=q'$ 上，即正比于 $\delta(q-q')$。

**所以"是 $\delta$"不是假设，是投影性的直接后果**——本卡 §0 表格第一行说的"被迫"就是指这件事。剩下的自由只有 $\delta$ 前的系数，那是下一节的内容。

---

## 1. 为什么必须与 D03 的完备性配对

[D03](D03-position-eigen-equation.md) §1.2 已把完备性写成

$$
\int dq\,\lvert q\rangle\langle q\rvert=\mathbb{1}
\qquad(\text{即权重 }w=1)
$$

一般地，若完备性带权重 $w$：

$$
\int dq\,w\,\lvert q\rangle\langle q\rvert=\mathbb{1}
$$

而正交归一带系数 $c$，则用完备性展开 $\langle q'\lvert q''\rangle$：

$$
\langle q'\lvert q''\rangle
=\int dq\,w\,\langle q'\lvert q\rangle\langle q\lvert q''\rangle
=w\,c^{2}\,\delta(q'-q'')
=c\,\delta(q'-q'')
\quad\Longrightarrow\quad
w\,c=1
$$

**D03 取了 $w=1$，于是 $c=1$ 被逼定**；若改 $w$，$c$ 必须跟着改。**所以 D04 的"系数为 1"不是独立的约定，是 D03 那个选择的后果。**

---

## 2. 本仓库的取法

本仓库取**系数 $c=1$**：

$$
\langle q\lvert q'\rangle=\delta(q-q')
$$

**与 D03 的权重配对**：D03 已把完备性写成权重 $w=1$，由 $w\,c=1$ 即得 $c=1$。**两个数必须一起看**：改 $w$ 就必须改 $c$，否则自相矛盾。

**动量基那一侧的对应取法属下游**，本卡不涉及——它由另一条路线单独定，不必在这里预期。

---

## 4. 边界

1. **弯曲空间**：$\langle q\lvert q'\rangle=\delta(q-q')/\rho(q)$，$\rho=\sqrt{g}$——这是弯曲空间里测度因子的数学出处（[D01](D01-spectral-theorem.md) §5 第 3 条）。
2. **离散谱**：$\delta(q-q')\to\delta_{nm}$，积分变求和，$2\pi$ 变盒子长度。
3. **多分量**：本征矢要加内部指标，$\langle q,i\lvert q',j\rangle=\delta_{ij}\delta(q-q')$。
4. **它不是"物理内容"**：归一化只影响中间步骤的系数，所有可观测量的期望值都与方案无关。

---

## 5. 自检

- [ ] 说清"形式被迫、系数自选"分别是哪一半，各自依据哪张卡
- [ ] 用 $w\,c=1$ 说明为什么正交归一的系数必须与 D03 的完备性权重配对
- [ ] 说明为什么本卡只定 $q$ 基的系数，动量基那一侧属下游
- [ ] 说明弯曲空间里 $\delta$ 前为什么多一个 $\rho^{-1}$
