# D18 · 迹即闭合路径：$\mathrm{Tr}\,e^{-\beta H}=\oint\mathcal{D}q\,e^{-S_E}$

> 建档 2026-11-06 · 上游：[D17](D17-path-integral-representation.md)；默认：D01
> 下游：无卡片依赖（结论只被笔记引用）
> 原为 [N002 §2.4](../notes/N002-finite-temperature-path-integral.md)，2026-11-06 移入网格。

---

## 0. 命题

$$
Z(\beta)\equiv\mathrm{Tr}\,e^{-\beta H}
=\oint_{q(0)=q(\beta)}\mathcal{D}q\;e^{-S_E[q]}
$$

**适用条件**：

1. 已有单条路径的表示：$\langle q_f\lvert e^{-\beta H}\lvert q_i\rangle=\int_{q(0)=q_i}^{q(\beta)=q_f}\mathcal{D}q\,e^{-S_E}$（输入，本卡片不证）；
2. $e^{-\beta H}$ 是迹类（低温柔和；严格时需 $H$ 有下界 + 高温截断）；
3. 欧氏作用量 $S_E[q]=\int_0^\beta d\tau\left[\frac{m}{2}\dot q^{2}+V(q)\right]$。

**它在讲什么**：**迹 = 把两端焊起来**。配分函数不是"从某点出发走一段"，而是"绕一圈回来"——而这一圈的长度就是 $\beta$。

---

## 1. 证明

### 1.1 第一步：迹是"对角元之和"

$$
Z(\beta)=\mathrm{Tr}\,e^{-\beta H}=\int dq\;\langle q\lvert e^{-\beta H}\lvert q\rangle
$$

**这里最容易错**：$\mathrm{Tr}$ 不是 $\langle 0\lvert\cdots\lvert 0\rangle$，而是对**所有** $q$ 求和（对本征态求和的连续版本）。

### 1.2 第二步：代入单条路径

由输入（[N002 §2.1](../notes/N002-finite-temperature-path-integral.md)）：

$$
\langle q_f\lvert e^{-\beta H}\lvert q_i\rangle
=\int_{q(0)=q_i}^{q(\beta)=q_f}\mathcal{D}q\;e^{-S_E[q]}
$$

取 $q_i=q_f=q$：

$$
\langle q\lvert e^{-\beta H}\lvert q\rangle
=\int_{q(0)=q}^{q(\beta)=q}\mathcal{D}q\;e^{-S_E[q]}
$$

### 1.3 第三步：对端点积分，即"焊起来"

$$
Z(\beta)=\int dq\int_{q(0)=q}^{q(\beta)=q}\mathcal{D}q\;e^{-S_E[q]}
$$

外层 $\int dq$ 遍历所有起点。把两种积分合并成一种写法：

$$
Z(\beta)=\oint_{q(0)=q(\beta)}\mathcal{D}q\;e^{-S_E[q]}
$$

即：**对所有闭合路径求和，起点可以是任何点**。

**证毕。**

---

## 2. 一致性检验

| 检验 | 结果 |
|---|---|
| 与能级求和一致 | 在 $H\lvert n\rangle=E_n\lvert n\rangle$ 的基下，$\mathrm{Tr}\,e^{-\beta H}=\sum_n e^{-\beta E_n}$，两种算法应给出同一数 |
| 自由粒子（[N002 §4.1](../notes/N002-finite-temperature-path-integral.md)） | 核为 $\left(m/2\pi\beta\right)^{1/2}$，端点重合后对 $q$ 积分给 $Z=L\left(m/2\pi\beta\right)^{1/2}$ ✅ |
| 量纲 | $\beta$ 是长度（欧氏时间），$S_E$ 无量纲（$\hbar=1$），$Z$ 无量纲 ✅ |
| $\beta\to0$ | 环缩成一点，$Z\to$ 态密度（高温展开）✅ |
| 与 §2.5 的对照 | "边界条件 $q(0)=q(\beta)$，不固定" ✅ |

---

## 3. 备注与边界

1. **"闭合"不是新加的假设，是取迹的自动结果。** 两个端点原本可以不同；取迹要求 $q_i=q_f$，再对 $q$ 积分——**焊死端点这一步就是"$Z$ 是一个环"的全部内容**。
2. **那个 $\int dq$ 是环路积分的零模。** 环路可以整体平移而不改作用量（对平移不变的 $V$），这个平移方向正是端点积分释放出来的。这就是谐振子环路积分里"$n=0$ 零模要单独处理"的来源（[N002 §4.2](../notes/N002-finite-temperature-path-integral.md)）。
3. **它是一个"结构性"结论，不是数值结论。** 它不告诉你 $Z$ 等于多少，只告诉你 $Z$ 长什么样。数值要靠高斯积分（自由场）或微扰/格点（相互作用）。
4. **玻色/费米的周期与反周期由此而来。** 迹给出周期边界 $q(0)=q(\beta)$；若把 $q$ 换成费米场，取迹会带上 $(-1)^{F}$，给出反周期——这是 [N002 §5](../notes/N002-finite-temperature-path-integral.md) 里 $\omega_n=(2n+1)\pi T$ 的出处。
5. **无限体积时发散。** 自由粒子的 $Z$ 带一个体积因子 $L$；取 $L\to\infty$ 时 $Z$ 发散，物理量要看比值（自由能密度）。

---

## 4. 自检

- [ ] 不看本文，写出 $\mathrm{Tr}$ 的定义并说明它为什么有 $\int dq$
- [ ] 说明"端点焊死"与"对端点积分"各自对应哪一步
- [ ] 用自由粒子的结果验证量纲与 $L$ 因子
- [ ] 解释为什么端点积分对应零模
- [ ] 说明费米场的反周期从哪里来
