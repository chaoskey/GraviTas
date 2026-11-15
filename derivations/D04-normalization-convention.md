# D04 · 归一化：$\langle q\lvert q'\rangle=\delta(q-q')$

> 建档 2026-11-07 · 类型：**定理卡**——承接 [D03](D03-position-eigen-equation.md) 的尺度选择，证明它的后果；**本卡不另立约定**
> 上游：[D01](D01-spectral-theorem.md)（谱定理）、[D03](D03-position-eigen-equation.md)（密度形式与 $w=1$）
> 下游：[D05](D05-functional-calculus.md)、[D06](D06-trace.md)、[D08](D08-diagonal-criterion.md)、[D16](D16-translation.md)、[D17](D17-qp-overlap.md)、[D18](D18-p-completeness.md)

---

## 0. 命题与地位

$$
\langle q\lvert q'\rangle=\delta(q-q')
$$

**本卡证明它，不是规定它。** 两半，各自有来源：

| 成分 | 地位 | 在哪证 |
|---|---|---|
| 为什么是 $\delta$（不是别的函数） | **被迫** | §1（投影性 + 正性） |
| $\delta$ 前的系数为什么是 $1$ | **配定**（不是自选） | §2（$w\,c=1$，D03 取 $w=1$） |

**唯一的一次约定在 [D03](D03-position-eigen-equation.md) §1.2**：取密度形式 $E(B)=\int_B dq\lvert q\rangle\langle q\rvert$，等价于完备性的权重 $w=1$。**本卡承接它，不另立约定。**

**这意味着什么**：不要把整条当成"约定"一笔勾销——形式有来源；也不要以为系数能随便取——它与 $w$ 互为倒数。

---

## 1. 为什么形式是 $\delta$（被迫）

### 1.1 不交的集合给正交投影

$E$ 是投影值测度（[D01](D01-spectral-theorem.md) §1.2 第 3 条）。对不交的 Borel 集 $B,B'$：

$$
E(B)\,E(B')=0
$$

### 1.2 写成核，读出支撑

由 [D03](D03-position-eigen-equation.md) §1.2 的密度形式 $E(B)=\int_B dq\lvert q\rangle\langle q\rvert$，对 $\phi,\psi\in\Phi$：

$$
0=\langle\phi\lvert E(B)E(B')\lvert\psi\rangle
=\int_B\!\!\int_{B'}\langle\phi\lvert q\rangle\,\langle q\lvert q'\rangle\,\langle q'\lvert\psi\rangle\,dq\,dq'
$$

**对所有不交的 $B,B'$ 都成立**，故 $\langle q\lvert q'\rangle$ 的支撑只能落在对角线 $q=q'$ 上。

### 1.3 对角线上的分布

支撑在对角线上的分布必可写成

$$
\langle q\lvert q'\rangle=c(q)\,\delta(q-q')+\sum_{k\ge1}g_k(q)\,\partial_q^{k}\delta(q-q')
$$

**（标准分布论事实，属外部数学，不依赖任何卡片。）**

### 1.4 正性排除导数项

$E(B)$ 是投影，故二次型非负。取 $B=(a,b)$、核为 $\partial_q\delta(q-q')$：

$$
\int_a^b\overline{\phi(q)}\,\partial_q\phi(q)\,dq
=-\frac12\bigl(\lvert\phi(b)\rvert^{2}-\lvert\phi(a)\rvert^{2}\bigr)
$$

**取 $\lvert\phi(b)\rvert>\lvert\phi(a)\rvert$ 它就为负**，与正性矛盾。所以所有 $g_k=0$，只剩

$$
\langle q\lvert q'\rangle=c(q)\,\delta(q-q')
$$

---

## 2. 为什么系数是 $1$

### 2.1 前提

| 前提 | 内容 | 出处 |
|---|---|---|
| (A) | $\int dq\,\lvert q\rangle\langle q\rvert=\mathbb{1}$（权重 $w=1$） | [D03](D03-position-eigen-equation.md) §1.4 |
| (B) | $\langle q\lvert q'\rangle=c(q)\delta(q-q')$ | §1.4 |
| (C) | $\lvert q\rangle\in\Phi^{\times}$，内积在 $\Phi$ 上取值 | [D01](D01-spectral-theorem.md) §2.3 |

**（B）里的 $c$ 就是要证的东西。**

### 2.2 五步

**第 1 步：把完备性夹进内积。** 对 $\phi,\psi\in\Phi$：

$$
\langle\phi\lvert\psi\rangle=\langle\phi\lvert\mathbb{1}\lvert\psi\rangle
=\int dq\,\langle\phi\lvert q\rangle\langle q\lvert\psi\rangle
\tag{1}
$$

（夹取是谱积分的二次型写法；[D01](D01-spectral-theorem.md) §1.2 第 1 条）

**第 2 步：取广义本征矢上的版本。** 在 (1) 中取 $\phi\to\lvert q'\rangle$、$\psi\to\lvert q''\rangle$（由 (C)）：

$$
\langle q'\lvert q''\rangle=\int dq\,\langle q'\lvert q\rangle\langle q\lvert q''\rangle
\tag{2}
$$

**没有新假设**：这只是 (1) 的分布写法。

**第 3 步：代入 (B)。**

$$
\langle q'\lvert q\rangle=c(q')\,\delta(q'-q),
\qquad
\langle q\lvert q''\rangle=c(q)\,\delta(q-q'')
$$

代进 (2) 右边，并用 $\int dq\,\delta(q'-q)\delta(q-q'')=\delta(q'-q'')$：

$$
\int dq\,c(q')\,c(q)\,\delta(q'-q)\,\delta(q-q'')
=c(q')^{2}\,\delta(q'-q'')
\tag{3}
$$

**第 4 步：两边比较。** (2) 的左边由 (B) 是 $c(q')\delta(q'-q'')$：

$$
c(q')\,\delta(q'-q'')=c(q')^{2}\,\delta(q'-q'')
\quad\Longrightarrow\quad
c(q')=1
\tag{4}
$$

**第 5 步：排除 $c=0$。** 若 $c\equiv0$，则 (2) 给 $\langle q'\lvert q''\rangle=0$，于是 (1) 给 $\mathbb{1}=0$——与 (A) 矛盾。

**所以 $c\equiv1$。**

---

## 3. 一般权重：$w\,c=1$

上面的证明没有用到 $w=1$ 的特殊性。若完备性带权重

$$
\int dq\,w(q)\,\lvert q\rangle\langle q\rvert=\mathbb{1}
$$

则 (1) 变成 $\langle\phi\lvert\psi\rangle=\int dq\,w(q)\langle\phi\lvert q\rangle\langle q\lvert\psi\rangle$，(3) 变成 $w(q')c(q')^{2}\delta$，(4) 换成

$$
w(q')\,c(q')=1
$$

**这就是"配对"的全部内容**：$w$ 与 $c$ 互为倒数，**只差一个自由度——那个自由度是尺度，已在 [D03](D03-position-eigen-equation.md) §1.2 定为 $w=1$。**

**本仓库的取法**：$w=1$，故 $c=1$。

---

## 4. 边界

1. **弯曲空间**：$\langle q\lvert q'\rangle=\delta(q-q')/\rho(q)$，$\rho=\sqrt{g}$——这是弯曲空间里测度因子的数学出处（[D01](D01-spectral-theorem.md) §5 第 3 条）。
2. **离散谱**：$\delta(q-q')\to\delta_{nm}$，积分变求和。
3. **多分量**：本征矢要加内部指标，$\langle q,i\lvert q',j\rangle=\delta_{ij}\delta(q-q')$。
4. **它不是"物理内容"**：归一化只影响中间步骤的系数，所有可观测量的期望值都与尺度方案无关。
5. **动量基那一侧属下游**，本卡不涉及。

---

## 5. 自检

- [ ] 说清"形式被迫、系数配定"分别依据什么
- [ ] 说明本卡为什么不是"约定卡"：约定的那一步在哪张卡
- [ ] 写出 $w\,c=1$ 的推导，并说明 $c=0$ 为什么被排除
- [ ] 说明正性如何排除 $\delta$ 的导数项
- [ ] 说明弯曲空间里 $\delta$ 前为什么多一个 $\rho^{-1}$
