# D03 · 归一化约定：$\langle q\lvert q'\rangle=\delta(q-q')$

> 建档 2026-11-07 · 类型：**约定卡**——记下"哪些是被迫的、哪些是选的"，并给出两套方案与换算
> 上游：[D01](D01-spectral-theorem.md)（谱定理）、[D02](D02-position-eigen-equation.md)（$\delta$ 的**形式**是被迫的）
> 下游：[D07](D07-diagonal-criterion.md)、[D14](D14-translation.md)、[D15](D15-qp-overlap.md)、[D16](D16-p-completeness.md)

---

## 0. 约定

$$
\langle q\lvert q'\rangle=\delta(q-q'),
\qquad
\int dq\,\lvert q\rangle\langle q\rvert=\mathbb{1}
$$

**这两条是一对，必须同时成立。** 但其中**成分不同**，必须分开说：

| 成分 | 地位 | 依据 |
|---|---|---|
| 为什么是 $\delta$（不是别的函数） | **被迫** | 投影测度的投影性（[D02](D02-position-eigen-equation.md) §1.4） |
| $\delta$ 前的系数为什么是 $1$ | **选的** | 与完备性权重配对（[D01](D01-spectral-theorem.md) §2.4 的 $w\,c=1$） |

**这意味着什么**：不要把整条当成"约定"一笔勾销——形式有来源，只有系数是自由的。反过来也不要以为系数能随便取：改一个必须改另一个。

---

## 1. 为什么必须成对改

设正交归一带系数 $c$、完备性带权重 $w$：

$$
\langle q\lvert q'\rangle=c\,\delta(q-q'),
\qquad
\int dq\,w\,\lvert q\rangle\langle q\rvert=\mathbb{1}
$$

用完备性展开 $\langle q'\lvert q''\rangle$ 得 $w\,c=1$。**所以改一个必须改另一个**，否则自相矛盾。

---

## 2. 两套常用方案

| 方案 | $\langle q\lvert q'\rangle$ | $\langle p\lvert p'\rangle$ | $\langle q\lvert p\rangle$ | 常见于 |
|---|---|---|---|---|
| **本仓库（物理常用）** | $\delta(q-q')$ | $2\pi\delta(p-p')$ | $e^{ipq}$ | 全部卡片 |
| 对称（数学常用） | $\delta(q-q')$ | $\delta(p-p')$ | $e^{ipq}/\sqrt{2\pi}$ | 泛函分析文献 |

**换算关系**：

$$
\lvert p\rangle_{\mathrm{sym}}=\frac{\lvert p\rangle}{\sqrt{2\pi}}
$$

两套方案**都对**，只是把 $2\pi$ 放在不同位置。**混用必错**：$\langle q\lvert p\rangle$ 用一套、$\langle p\lvert p'\rangle$ 用另一套，算出的中间结果会差 $\sqrt{2\pi}$ 的因子，量纲上看不出来。

**注意：$\langle p\lvert p'\rangle=2\pi\delta$ 这一行不是独立选择。** 它由 $\langle q\lvert p\rangle=e^{ipq}$ 加 $q$ 的完备性算出：

$$
\langle p\lvert p'\rangle=\int dq\,\langle p\lvert q\rangle\langle q\lvert p'\rangle
=\int dq\,e^{-ipq}\,e^{ip'q}=2\pi\,\delta(p-p')
$$

**所以换方案时，改 $\langle q\lvert p\rangle$ 是主动的，改 $\langle p\lvert p'\rangle$ 是被动的**——前者定了，后者就没得选。

---

## 3. 怎么验：两条互锁

$$
\int\frac{dp}{2\pi}\,e^{ip(q-q')}=\delta(q-q'),
\qquad
\int dq\,e^{i(p-p')q}=2\pi\,\delta(p-p')
$$

**两条必须同时成立。** 只验一条是不够的：完备性（"用不用得上"）与正交归一（"系数对不对"）是两件事，一条错了另一条可能仍然成立。

---

## 4. 边界

1. **弯曲空间**：$\langle q\lvert q'\rangle=\delta(q-q')/\rho(q)$，$\rho=\sqrt{g}$——这是路径积分里测度因子的数学出处（[D01](D01-spectral-theorem.md) §5 第 3 条）。
2. **离散谱**：$\delta(q-q')\to\delta_{nm}$，积分变求和，$2\pi$ 变盒子长度。
3. **多分量**：本征矢要加内部指标，$\langle q,i\lvert q',j\rangle=\delta_{ij}\delta(q-q')$。
4. **它不是"物理内容"**：归一化只影响中间步骤的系数，所有可观测量的期望值都与方案无关。

---

## 5. 自检

- [ ] 说清"形式被迫、系数自选"分别是哪一半，各自依据哪张卡
- [ ] 用 $w\,c=1$ 说明为什么两个式子必须成对改
- [ ] 写出两套方案的三个式子，并给出 $\lvert p\rangle$ 的换算
- [ ] 解释为什么"只验一条互锁"不够
- [ ] 说明弯曲空间里 $\delta$ 前为什么多一个 $\rho^{-1}$
