# N002 · 有限温度路径积分：从 Wick rotation 到「几何决定温度」

> 写于 2026-11-03 · 关联：[N001](N001-hawking-temperature.md)、[P01](../problems/P01-black-hole-information.md)
> 用途：三天补丁的 Day 1–2 的唯一读物。读完要能**合上书复述 §2**。
> 约定：全文公式用 LaTeX（行内 `$...$`，行间 `$$...$$`）。

---

## 0. 这份讲义是什么，不是什么

**不是** Tong 或 Laine–Vuorinen 讲义的中文翻译——那两份材料有版权，逐段翻译并公开是侵权。
这是**原创写作**：用同样的物理，走一条更短的路，只覆盖你补丁需要的东西。

覆盖三件事：

1. **Wick rotation** 是什么，为什么它不是单纯的技巧；
2. 为什么 $\mathrm{Tr}\,e^{-\beta H}$ 等于**一条闭合路径**的积分；
3. 为什么那条路径的**周长就是** $\beta = 1/T$。

读完你应该能自己做 [N001](N001-hawking-temperature.md) 的阶梯 C。

---

## 1. Wick rotation：把振荡变成衰减

### 1.1 问题

闵可夫斯基空间的路径积分是

$$
\mathcal{Z} = \int \mathcal{D}\varphi\, e^{iS[\varphi]}
$$

$e^{iS}$ 是相位，模长恒为 $1$，积分不绝对收敛。数学上它只是一个形式记号。

### 1.2 操作

令

$$
t = -i\tau
$$

其中 $\tau$ 是实数，叫**欧氏时间**。于是 $\partial_t = i\,\partial_\tau$，$dt = -i\,d\tau$。对标量场

$$
\begin{aligned}
S &= \int dt\left[\frac12(\partial_t\varphi)^2 - V(\varphi)\right] \\
  &= \int (-i\,d\tau)\left[-\frac12(\partial_\tau\varphi)^2 - V(\varphi)\right] \\
  &= i\int d\tau\left[\frac12(\partial_\tau\varphi)^2 + V(\varphi)\right]
   \equiv i\,S_E
\end{aligned}
$$

其中

$$
S_E[\varphi] = \int d\tau\left[\frac12(\partial_\tau\varphi)^2 + V(\varphi)\right]
$$

是**欧氏作用量**。于是

$$
e^{iS} = e^{-S_E}
$$

指数从虚变实，且 $S_E$ 有下界（对正常势），积分变成衰减的高斯型——这时它才**存在**。

### 1.3 这不是技巧

三个理由：

- **定义**：欧氏路径积分是构造量子场论测度的标准方式（Osterwalder–Schrader 公理）；
- **计算**：它把量子涨落变成统计力学的配分函数，于是你可以借统计物理的全部工具；
- **结构**：它把"温度"翻译成"时间的周期"，这是本文后面一切的基础。

号差也变了：$(-,+,+,+) \to (+,+,+,+)$。所以叫"欧氏"。

---

## 2. 核心：$\mathrm{Tr}\,e^{-\beta H}$ 是一条闭合路径

这一节是整个补丁的关键。**必须能自己重推。**

### 2.1 从振幅开始

$$
\langle q_f|e^{-\beta H}|q_i\rangle
= \int_{q(0)=q_i}^{q(\beta)=q_f} \mathcal{D}q\; e^{-S_E[q]},
\qquad
S_E[q] = \int_0^\beta d\tau\left[\frac{m}{2}\dot q^2 + V(q)\right]
$$

**这一步怎么来的**：把 $e^{-\beta H}$ 切成 $N$ 片、每两片之间插入完备性、对单片做高斯积分、再取 $N\to\infty$。完整推导见 [D10 · 路径积分表示](../derivations/D10-path-integral-representation.md)。

### 2.2 单片矩阵元

短时核是整条推导的引擎：

$$
\langle q'|e^{-\varepsilon H}|q\rangle
=\left(\frac{m}{2\pi\varepsilon}\right)^{1/2}
\exp\left[-\frac{m(q'-q)^2}{2\varepsilon}-\varepsilon V(q)\right]
$$

它由"Trotter 分裂 + 动量完备性 + $\langle q|p\rangle=e^{ipq}$ + 高斯积分"四步得到，见 [D10](../derivations/D10-path-integral-representation.md) §1.2。

### 2.3 拼回去

$N$ 个因子相乘，$\varepsilon\to0$ 时指数上的和收敛为 $-S_E$，测度归一化因子也一起趋于确定极限。细节见 [D10](../derivations/D10-path-integral-representation.md) §1.3–1.4。

### 2.4 取迹：闭合

$$
Z(\beta)=\mathrm{Tr}\,e^{-\beta H}
=\oint_{q(0)=q(\beta)}\mathcal{D}q\;e^{-S_E[q]}
$$

**一句话**：迹 = 把两端焊起来，再对焊点积分。所以配分函数"绕一圈回来"，这一圈的周长就是 $\beta$。

**完整证明、零模来源与费米反周期见 [D09 · 迹即闭合路径](../derivations/D09-trace-is-loop.md)。**

### 2.5 两个容易混的点

| 容易错 | 正确 |
|---|---|
| $Z = \langle 0 \vert e^{-\beta H} \vert 0\rangle$ | $Z = \sum_n \langle n \vert e^{-\beta H} \vert n\rangle$，要对**所有**态求和 |
| 边界条件固定为 $q(0)=0,\ q(\beta)=0$ | 边界条件是 $q(0)=q(\beta)$，**不固定**，还要对 $q(0)$ 积分 |

---

## 3. 温度 = 环的周长倒数

统计力学里

$$
Z(\beta) = \sum_n e^{-\beta E_n}, \qquad \beta = \frac{1}{k_B T}
$$

单位制取 $k_B = 1$，则 $\beta = 1/T$。

结合 §2.4：**欧氏时间是一个周长 $\beta$ 的圆**，于是

$$
T = \frac{1}{\beta}
$$

即：温度的倒数，就是这条圆的周长。

换句话说：

> 温度不是"系统有多热"的度量，而是"虚时间方向被紧致化得多紧"的度量。

这句话现在可能只是顺口。等你在 Schwarzschild 上算出 $\beta = 8\pi M$，它会变得具体。

---

## 4. 两个检验

### 4.1 自由粒子在盒子里

$$
\langle q|e^{-\beta H}|q'\rangle
= \left(\frac{m}{2\pi\beta}\right)^{1/2}
  \exp\left[-\frac{m(q-q')^2}{2\beta}\right]
$$

取 $q = q'$，对 $q\in[0,L]$ 积分：

$$
Z = L\left(\frac{m}{2\pi\beta}\right)^{1/2}
$$

$Z \propto \beta^{-1/2}$。$\beta$ 越小（越热），可及的态越多，$Z$ 越大。
这是第 3 节"紧致化"的图像。

### 4.2 谐振子

能级 $E_n = \omega\left(n+\tfrac12\right)$：

$$
Z = \sum_n e^{-\beta\omega(n+1/2)}
  = \frac{e^{-\beta\omega/2}}{1-e^{-\beta\omega}}
  = \frac{1}{2\sinh(\beta\omega/2)}
$$

两个极限：

- $\beta\omega \gg 1$（低温）：$Z \to e^{-\beta\omega/2}$，只剩基态；
- $\beta\omega \ll 1$（高温）：$Z \to 1/(\beta\omega)$，能级被"抹平"。

**用路径积分算同一个 $Z$**：作用量是 $\int \frac{m}{2}(\dot q^2 + \omega^2 q^2)$，
圆上的本征值是 $\left(\frac{2\pi n}{\beta}\right)^2 + \omega^2$，
行列式乘积需要对 $n$ 做 zeta 正规化，且 $n=0$ 零模要单独处理，
最后同样给出 $1/\left[2\sinh(\beta\omega/2)\right]$。

这条路技术细节多、和黑洞无关，**先跳过**。你只需要相信两件事：
能级求和给 $1/(2\sinh)$；路径积分给同一个数——这说明 §2 的等价不是空话。

---

## 5. 场论版本：Matsubara 频率

把 $\tau$ 紧致成周长 $\beta$ 的圆后，场在 $S^1\times\mathbb{R}^3$ 上。对 $\tau$ 做傅里叶展开：

$$
\varphi(\tau,\mathbf{x})
= T\sum_n \int\frac{d^3p}{(2\pi)^3}\;
  e^{i\omega_n\tau + i\mathbf{p}\cdot\mathbf{x}}\;
  \tilde\varphi_n(\mathbf{p})
$$

周期条件 $\varphi(\tau+\beta) = \varphi(\tau)$ 迫使频率离散（玻色子）：

$$
\omega_n = 2\pi n T
$$

于是"连续频率"变成"离散频率之和"——这正是有限温度场论与零温场论的全部差别。

费米子要反周期，$\varphi(\tau+\beta) = -\varphi(\tau)$，给出（费米子）

$$
\omega_n = (2n+1)\pi T
$$

这里不展开。

**记住一个图像**：有限温度 = 时间方向被卷成一个圆；$T$ 越大，圆越细。

---

## 6. 弯曲时空：几何唯一决定温度

现在把 §2–§5 搬到弯曲时空。这一步是 Hawking 温度的来源。

### 6.1 定理（陈述，不证）

若一个欧氏度规在某个"视界"处要**光滑**（没有锥奇点），那么时间方向的周期被几何
唯一确定。

近视界处，任何有 Killing 视界的度规都可以写成 Rindler 形式：

$$
ds^2 \approx d\rho^2 + \kappa^2\rho^2\,d\tau^2 + \gamma_{AB}\,dx^A dx^B
$$

其中 $\kappa$ 是表面重力。这是平面极坐标 $d\rho^2 + \rho^2 d\theta^2$，只要令 $\theta = \kappa\tau$。
平面在原点光滑的条件是 $\theta$ 的周期为 $2\pi$，所以

$$
\tau \sim \tau + \frac{2\pi}{\kappa}
\quad\Longrightarrow\quad
\beta = \frac{2\pi}{\kappa}
\quad\Longrightarrow\quad
T = \frac{\kappa}{2\pi}
$$

### 6.2 这条定理为什么"是"物理

因为它把温度变成了**几何的自洽性条件**：

> 时空不能在视界处长出一个锥尖。要不长锥尖，虚时间就必须以特定周期卷起来。
> 那个周期就是 $1/T$。

于是"黑洞有温度"不再是一个需要额外输入的事实，而是"视界附近的欧氏几何必须光滑"的推论。

### 6.3 你的任务

§6.1 说"任何有 Killing 视界的度规都能写成 Rindler 形式"。**这句话在 Schwarzschild 上
具体长什么样**，就是 [N001](N001-hawking-temperature.md) 的阶梯 C：

- 取 $f = 1 - 2M/r$，在 $r = 2M$ 附近展开；
- 换径向坐标，让度规写成 $d\rho^2 + \rho^2(\cdots)^2$；
- 读出 $(\cdots)$ 里的系数，令它对应 $2\pi$ 周期。

这一步**我不会替你算**。

---

## 7. 练习与验收

| # | 练习 | 验收标准 |
|---|---|---|
| E1 | 自由粒子在长度 $L$ 的盒子里，算 $Z(\beta)$ | 得到 $L\left(m/2\pi\beta\right)^{1/2}$，并说明 $\beta$ 的幂次为什么是这个 |
| E2 | 谐振子：从能级求和得 $1/\left[2\sinh(\beta\omega/2)\right]$ | 两个极限（$\beta\omega\gg 1$、$\beta\omega\ll 1$）都能解释 |
| E3 | **不看本文**，重推 §2.4（$\mathrm{Tr}$ = 闭合路径） | 能独立写出时间切片那三步 |
| E4 | 二维锥面 $ds^2 = dr^2 + r^2d\theta^2$，$\theta$ 周期为 $\alpha$ | 算出 deficit angle $2\pi - \alpha$，说清它对应曲率的 $\delta$ 函数 |
| E5 | Schwarzschild 近视界展开，求 $\beta$ | 得到 $\beta = 8\pi M$，且与 $\kappa = 1/(4M)$ 的路线一致 |

E3 是**唯一**一道必须过的。过不了 E3，后面全是背的。

---

## 8. 来源（读原文用）

| 材料 | 用途 |
|---|---|
| D. Tong, *Statistical Field Theory*（DAMTP 讲义，免费） | 第 1–2 章；路径积分与有限温度的完整讲法 |
| M. Laine, A. Vuorinen, *Basics of Thermal Field Theory*, arXiv:1701.01554 | 第 2 章；周期性的严格推导 |
| J. Kapusta, C. Gale, *Finite-Temperature Field Theory* | 查用，不必通读 |

再次说明：本讲义是**独立写作**，不是上述任何材料的中文版。对原文的引用只是让你
知道去哪里看更严格的版本。

---

## 9. 五句话速查

> 1. $t = -i\tau$，$e^{iS} = e^{-S_E}$。
> 2. $Z = \mathrm{Tr}\,e^{-\beta H} = \oint \mathcal{D}q\, e^{-S_E}$，路径闭合。
> 3. 闭合环的周长 $=\beta=1/T$。
> 4. 场论里：$\tau$ 紧致 $\Rightarrow$ 频率离散，$\omega_n = 2\pi n T$。
> 5. 弯曲时空里：视界处要光滑 $\Rightarrow$ 周期被 $\kappa$ 唯一确定 $\Rightarrow$ $T = \kappa/2\pi$。
