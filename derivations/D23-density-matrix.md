# D23 · 密度矩阵与配分函数

> 建档 2026-11-08 · 上游：[D07](D07-trace.md)（迹）、[D20](D20-hamiltonian.md)（$\hat H$）、[D22](D22-trace-is-loop.md)（迹即闭合路径）
> 下游：[D24](D24-temperature-period.md)、[D26](D26-energy-basis.md)
> 本卡补的是"纯态之外"的那一半：热平衡与混合态。

---

## 0. 命题

$$
\rho=\frac{e^{-\beta\hat H}}{Z},
\qquad
Z=\mathrm{Tr}\,e^{-\beta\hat H},
\qquad
F=-\frac{1}{\beta}\ln Z
$$

$$
\langle\hat A\rangle=\mathrm{Tr}\bigl(\rho\,\hat A\bigr)
$$

**它在讲什么**：纯态用一个矢 $\lvert\psi\rangle$ 描述；**混合态用一个算子 $\rho$ 描述**。热平衡就是"$\rho$ 正比于 $e^{-\beta H}$"。

---

## 1. 为什么纯态不够

| 情形 | 为什么矢不够 |
|---|---|
| 热平衡 | 系统与热库纠缠，自身没有确定的波函数 |
| 统计混合 | 制备过程有经典不确定性（不知道是哪个态） |
| 子系统 | 整体是纯态，局部一般不是 |

$\rho$ 是这三件事的共同语言：**"以概率 $p_i$ 处于 $\lvert\psi_i\rangle$"** 写成

$$
\rho=\sum_i p_i\lvert\psi_i\rangle\langle\psi_i\rvert,
\qquad p_i\ge0,\quad\sum_i p_i=1
$$

**纯态是特例**：$\rho=\lvert\psi\rangle\langle\psi\rvert$。

---

## 2. 四条性质

| 性质 | 内容 |
|---|---|
| 正定 | $\rho\ge0$、$\mathrm{Tr}\rho=1$ |
| 纯态判据 | 纯 $\iff$ $\mathrm{Tr}\rho^{2}=1$；混合则 $<1$ |
| 期望值 | $\langle\hat A\rangle=\mathrm{Tr}(\rho\hat A)$——与 [D02](D02-born-rule.md) 的公式在纯态时一致 |
| 演化 | $\rho(t)=U(t)\rho(0)U(t)^{\dagger}$ |

**第三条是关键**：它把 Born 规则推广到混合态，形式从"$\langle\psi\lvert\hat A\lvert\psi\rangle$"变成"$\mathrm{Tr}(\rho\hat A)$"——**同一个东西的两种写法**（纯态时 $\rho$ 是一维投影）。

---

## 3. 配分函数与热力学

$Z$ 是所有热力学量的母函数：

| 量 | 表达式 |
|---|---|
| 自由能 | $F=-\frac{1}{\beta}\ln Z$ |
| 内能 | $E=-\partial_\beta\ln Z=\langle\hat H\rangle$ |
| 熵 | $S=\beta(E-F)=-\mathrm{Tr}(\rho\ln\rho)$ |

**这意味着什么**：只要算出 $Z$，热力学全有了。**所以 [D24](D24-temperature-period.md) 的核心任务是把 $Z$ 写成一个几何对象。**

---

## 4. 与路径积分的接口

由 [D22](D22-trace-is-loop.md)：

$$
Z=\mathrm{Tr}\,e^{-\beta\hat H}=\oint_{q(0)=q(\beta)}\mathcal{D}q\;e^{-S_E[q]}
$$

**左边是统计力学（迹），右边是几何（闭合回路）。** 本卡给出左边的物理含义（热平衡），[D24](D24-temperature-period.md) 把右边解释成温度。

---

## 5. 边界

1. **只对可区分粒子直接成立。** 全同粒子要加对称化，玻色/费米要用巨配分函数（带化学势）。
2. **$\beta\to0$ 时 $Z\to\mathrm{Tr}\,\mathbb{1}$ 发散**——这是紫外发散的雏形，场论里要重整化。
3. **热平衡假设本身是输入的**。$\rho\propto e^{-\beta H}$ 描述平衡态；非平衡要解量子主方程，不在本卡范围。
4. **它不解释"为什么平衡态长这样"**。这属于统计力学基础（各态历经、最大熵原理），不在本网格内。

---

## 6. 自检

- [ ] 写出 $\rho$、$Z$、$F$ 的定义，并说明为什么纯态不够
- [ ] 用 $\mathrm{Tr}\rho^{2}$ 判断纯态/混合态
- [ ] 说明 $\mathrm{Tr}(\rho\hat A)$ 与 Born 规则的关系
- [ ] 指出 $Z$ 为什么既是热力学的母函数、又是路径积分的入口
