# N001 · Hawking 温度的三种推导与交叉检验

> 写于 2026-11-03 · 关联：[P01](../problems/P01-black-hole-information.md)
> 目标：不查任何资料，独立推出 $T_{\mathrm{H}} = \frac{1}{8\pi G M}$，并用三条独立路径互证。

---

## 0. 结论

$$
T_{\mathrm{H}} = \frac{\hbar c^{3}}{8\pi G M k_{\mathrm{B}}}
$$

自然单位制（$G = c = \hbar = k_{\mathrm{B}} = 1$）：

$$
T_{\mathrm{H}} = \frac{1}{8\pi M}, \qquad \kappa = \frac{1}{4M}, \qquad T_{\mathrm{H}} = \frac{\kappa}{2\pi}
$$

熵：

$$
S_{\mathrm{BH}} = \frac{A}{4G} = 4\pi M^{2}
$$

---

## 1. 设定

Schwarzschild 度规（$G = c = 1$）：

$$
ds^{2} = -f(r)\,dt^{2} + f(r)^{-1} dr^{2} + r^{2} d\Omega^{2}, \qquad f(r) = 1 - \frac{2M}{r}
$$

视界在 $r_{\mathrm{h}} = 2M$。表面重力定义为视界附近静止观测者的固有加速度（红移到无穷远）：

$$
\kappa = \frac{1}{2} f'(r_{\mathrm{h}})
$$

代入 $f'(r) = \frac{2M}{r^{2}}$，得

$$
\kappa = \frac{M}{(2M)^{2}} = \frac{1}{4M}
$$

---

## 2. 方法 A：欧氏周期法

### 2.1 延拓到欧氏号差

令 $t = -i\tau$：

$$
ds_{E}^{2} = f\,d\tau^{2} + f^{-1} dr^{2} + r^{2} d\Omega^{2}
$$

### 2.2 视界附近展开

令 $r = 2M + \tilde{\rho}$，则

$$
f(r) \approx f'(2M)\,\tilde{\rho} = \frac{\tilde{\rho}}{2M}
$$

于是

$$
ds_{E}^{2} \approx \frac{\tilde{\rho}}{2M} d\tau^{2} + \frac{2M}{\tilde{\rho}} d\tilde{\rho}^{2} + (2M)^{2} d\Omega^{2}
$$

### 2.3 换成固有径向坐标

令 $\rho^{2} = 8M\tilde{\rho}$，即 $\tilde{\rho} = \frac{\rho^{2}}{8M}$，$d\tilde{\rho} = \frac{\rho\,d\rho}{4M}$。代入：

$$
\frac{2M}{\tilde{\rho}} d\tilde{\rho}^{2} = \frac{2M \cdot 8M}{\rho^{2}} \cdot \frac{\rho^{2} d\rho^{2}}{16M^{2}} = d\rho^{2}
$$

$$
\frac{\tilde{\rho}}{2M} d\tau^{2} = \frac{\rho^{2}}{16M^{2}} d\tau^{2}
$$

得到

$$
ds_{E}^{2} \approx d\rho^{2} + \rho^{2} \left(\frac{d\tau}{4M}\right)^{2} + (2M)^{2} d\Omega^{2}
$$

### 2.4 消去锥奇点

这是 $(\rho, \theta)$ 平面上的极坐标，其中 $\theta = \frac{\tau}{4M}$。
$\rho = 0$ 处没有锥奇点的条件是 $\theta$ 的周期为 $2\pi$，即

$$
\tau \sim \tau + 8\pi M
$$

### 2.5 读温度

欧氏时间周期 $\beta = 1/T$，所以

$$
\beta = 8\pi M \quad \Rightarrow \quad T = \frac{1}{8\pi M}
$$

恢复量纲：

$$
T_{\mathrm{H}} = \frac{\hbar c^{3}}{8\pi G M k_{\mathrm{B}}}
$$

**关键点**：$\beta$ 不是"坐标 $t$ 的周期"这种约定，而是**几何要求**——
否则 $\rho = 0$ 处会出现一个真实的锥形奇点（曲率在那里是 $\delta$ 函数）。

---

## 3. 方法 B：表面重力 + Unruh

视界附近的度规近似为 Rindler 形式：

$$
ds^{2} \approx -\kappa^{2} x^{2} dt^{2} + dx^{2} + d\mathbf{x}_{\perp}^{2}
$$

一个在视界外静止的观测者，其固有加速度为 $a = \kappa$。
Unruh 效应给出，加速观测者看到的真空温度为

$$
T_{U} = \frac{a}{2\pi} = \frac{\kappa}{2\pi}
$$

而无穷远观测者看到的温度因红移因子 $\sqrt{-g_{tt}}$ 修正，恰好得到同一个 $\frac{\kappa}{2\pi}$。

$$
T_{\mathrm{H}} = \frac{\kappa}{2\pi} = \frac{1}{8\pi M}
$$

与方法 A 完全一致。

---

## 4. 方法 C：欧氏作用量与热力学

在 $\beta = 8\pi M$ 时，欧氏 Schwarzschild 几何是一个光滑的"雪茄"。
其欧氏作用量（仅边界项贡献，因为 $R = 0$）为

$$
I_{E} = \frac{\beta M}{2} = 4\pi M^{2}
$$

配分函数 $Z = e^{-I_{E}}$，于是

$$
S = \beta M - I_{E} = 8\pi M^{2} - 4\pi M^{2} = 4\pi M^{2}
$$

而 $A = 4\pi(2M)^{2} = 16\pi M^{2}$，所以

$$
S = \frac{A}{4}
$$

这与 Bekenstein–Hawking 公式一致——**热力学自洽性检验通过**。

---

## 5. 一致性检验（这一步比推导更重要）

| 检验 | 结果 |
|---|---|
| Smarr 公式 $M = 2TS$ | $2 \cdot \frac{1}{8\pi M} \cdot 4\pi M^{2} = M$ ✓ |
| 第一定律 $dM = T\,dS$ | $dS = 8\pi M\,dM$，$T\,dS = dM$ ✓ |
| 量纲 | $T \sim \hbar c^{3}/(G M k_{\mathrm{B}})$，是温度 ✓ |
| 经典极限 $M \to \infty$ | $T \to 0$，黑洞变冷 ✓ |
| 与 Unruh 的连续性 | $\kappa \to a$，$T \to \frac{a}{2\pi}$ ✓ |

---

## 6. 我一开始错在哪（留档）

1. **把 $\kappa$ 当成"视界处的加速度"**。实际上无穷远观测者测到的加速度要乘红移因子，
   $\kappa$ 的定义正是"红移到无穷远后的加速度"。
2. **用 $t$ 的周期而不是 $\tau$ 的周期**。欧氏化之后，$t$ 已经变成 $\tau$，周期的几何意义完全不同。
3. **以为锥奇点只是坐标问题**。$\rho = 0$ 处的锥奇点对应曲率的 $\delta$ 函数，是**真实**的奇点，
   不是坐标假象。
4. **恢复量纲时漏掉 $\hbar$**。经典黑洞没有温度，$T \propto \hbar$ 是量子效应的标志。

---

## 7. 延伸

- 如果 $f(r)$ 有多个视界（Kerr、dS），欧氏化会在每个视界处出现锥奇点，
  只有**一个** $\beta$ 能同时消去所有锥奇点——这解释了为什么多视界时空的量子态是混合态。
- 对 dS：$T = \frac{H}{2\pi}$，$S = \frac{3\pi}{G\Lambda}$（见 [P07](../problems/P07-cosmological-constant.md)）。
- 对偶视角：AdS/CFT 中，$T_{\mathrm{H}}$ 对应边界 CFT 的温度，Page 曲线从这里开始
  （见 [P01](../problems/P01-black-hole-information.md)）。

---

## 8. 自检

- [ ] 不看笔记，写出从 $f(r)$ 到 $\beta = 8\pi M$ 的完整步骤
- [ ] 解释为什么 $\tau$ 的周期是几何量，而 $t$ 的周期不是
- [ ] 用方法 C 重算 $S$，确认是 $\frac{A}{4}$
- [ ] 说明 $T \propto 1/M$ 的物理含义（黑洞越蒸发越热）
