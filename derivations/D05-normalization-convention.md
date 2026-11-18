# D05 · 归一化：$\langle q\lvert q'\rangle=\delta(q-q')$

> 建档 2026-11-07 · 类型：**定理卡**——$\langle q\lvert q'\rangle$ 就是"恒等算子的核"，本卡把它写出来
> 上游：[D01](D01-spectral-theorem.md)（谱定理、求值泛函 $\langle q\lvert\psi\rangle=\psi(q)$）、[D04](D04-position-eigen-equation.md)（密度形式，权重 $w=1$）
> 下游：[D06](D06-functional-calculus.md)、[D07](D07-trace.md)、[D09](D09-diagonal-criterion.md)、[D17](D17-translation.md)、[D18](D18-qp-overlap.md)、[D19](D19-p-completeness.md)

---

## 0. 命题与地位

$$
\langle q\lvert q'\rangle=\delta(q-q')
$$

**它的全部内容是**：$\langle q\lvert q'\rangle$ 是**恒等算子在 $\lvert q\rangle$ 基下的核**，而恒等算子的核就是 $\delta$。**不是"投影性逼出来的"，也不是"选出来的"。**

| 成分 | 地位 | 在哪 |
|---|---|---|
| 核 $K_A$ 的定义 | **定义** | §1 |
| $K_{\mathbb{1}}=\delta$ | 由完备性（$w=1$）唯一确定 | §2 |
| $\lvert q\rangle$ 的尺度 | **约定** | [D04](D04-position-eigen-equation.md) §1.2 |

**唯一的一次约定在 D04**：取密度形式，等价于完备性的权重 $w=1$。**本卡承接它，不另立约定。**

---

## 1. 核是什么

**定义**：算子 $A$ 在 $\lvert q\rangle$ 基下的**核** $K_A(q,q')$，是使

$$
\langle\phi\lvert A\lvert\psi\rangle=\int\!\!\int\overline{\phi(q)}\,K_A(q,q')\,\psi(q')\,dq\,dq'
\tag{1}
$$

对**所有** $\phi,\psi$ 成立的分布。其中 $\phi(q)\equiv\langle q\lvert\phi\rangle$。

**三个例子**：

| $A$ | 核 $K_A$ | 验证 |
|---|---|---|
| $\mathbb{1}$ | $\delta(q-q')$ | (1) 退化成 $\int\overline{\phi(q)}\psi(q)\,dq$ |
| $\hat q$ | $q\,\delta(q-q')$ | 退化成 $\int q\,\overline{\phi(q)}\psi(q)\,dq$ |
| $E(B)$ | $\mathbf{1}_B(q)\,\delta(q-q')$ | 退化成 $\int_B\overline{\phi(q)}\psi(q)\,dq$ |

**关键一句**：$\langle q\lvert q'\rangle$ **就是 $K_{\mathbb{1}}$**——"基矢的内积"与"恒等算子的核"是同一个东西。

**于是要证的东西变成**：$K_{\mathbb{1}}=\delta$。

---

## 2. 由完备性定出 $K_{\mathbb{1}}=\delta$

**第一步：完备性给内积。** [D04](D04-position-eigen-equation.md) §1.4 已取定权重 $w=1$：

$$
\int dq\,\lvert q\rangle\langle q\rvert=\mathbb{1}
\ \Longrightarrow\
\langle\phi\lvert\psi\rangle=\int dq\,\langle\phi\lvert q\rangle\langle q\lvert\psi\rangle
=\int\overline{\phi(q)}\,\psi(q)\,dq
\tag{2}
$$

**第二步：按核的定义写同一个内积。** 在 (1) 中取 $A=\mathbb{1}$：

$$
\langle\phi\lvert\psi\rangle=\int\!\!\int\overline{\phi(q)}\,K_{\mathbb{1}}(q,q')\,\psi(q')\,dq\,dq'
\tag{3}
$$

**第三步：比较 (2) 与 (3)。** 两式的右边对**所有** $\phi,\psi$ 相等。而一个分布由它的全部配对唯一确定，故

$$
K_{\mathbb{1}}(q,q')=\delta(q-q')
$$

**所以**

$$
\langle q\lvert q'\rangle=K_{\mathbb{1}}(q,q')=\delta(q-q')
$$

**证毕。**

**这一步不需要任何额外假设。** $\delta$ 是恒等算子的核——这就是 $\delta$ 的定义本身。

---

## 3. 唯一的自由度：尺度

若把 $\lvert q\rangle$ 整体换成 $\lambda\lvert q\rangle$（常数），则

$$
\langle q\lvert q'\rangle\ \longrightarrow\ \lvert\lambda\rvert^{2}\,\delta(q-q')
$$

**同时**完备性的权重必须跟着换，否则 $\int\lvert q\rangle\langle q\rvert dq\neq\mathbb{1}$：

$$
w\ \longrightarrow\ \frac{w}{\lvert\lambda\rvert^{2}}
$$

**两者一起换，物理不变**：只改中间步骤的系数，不改任何可观测的预言。

**[D04](D04-position-eigen-equation.md) §1.2 已经把密度形式取定**（相当于 $w=1$），所以本卡不再有自由度：只剩 $\lvert\lambda\rvert=1$ 的相位，$\delta$ 不变。

---

## 4. 一致性检验

| 检验 | 结果 |
|---|---|
| $E$ 是投影值测度 | $K_{E(B)}=\mathbf{1}_B K_{\mathbb{1}}$，故不交的 $B,B'$ 给 $K=\mathbf{1}_B\mathbf{1}_{B'}\delta=0$ ✅ |
| $\hat q$ 的本征方程 | $K_{\hat q}=qK_{\mathbb{1}}$，即"乘以 $q$"，正是 $\hat q\lvert q\rangle=q\lvert q\rangle$ ✅ |
| 与 D04 的完备性 | $K_{\mathbb{1}}=\delta$ 与 $\int\lvert q\rangle\langle q\rvert dq=\mathbb{1}$ 是同一句话的两种写法 ✅ |

---

## 5. 边界

1. **弯曲空间**：测度带 $\rho=\sqrt{g}$，核相应变成 $\delta(q-q')/\rho(q)$——这是同一个尺度关系的写法（[D01](D01-spectral-theorem.md) §5 第 3 条）。
2. **离散谱**：$\delta(q-q')\to\delta_{nm}$，积分变求和。
3. **多分量**：本征矢要加内部指标，$\langle q,i\lvert q',j\rangle=\delta_{ij}\delta(q-q')$。
4. **它不是"物理内容"**：核只影响中间步骤的系数，所有可观测量的期望值都与尺度方案无关。
5. **动量基那一侧属下游**，本卡不涉及。

---

## 6. 自检

- [ ] 写出核的定义，并说明 $\langle q\lvert q'\rangle$ 是哪个算子的核
- [ ] 用完备性（$w=1$）证明 $K_{\mathbb{1}}=\delta$，并指出哪一步用了"核由全部配对唯一确定"
- [ ] 说明本卡为什么不需要"投影性""正性"这些论证
- [ ] 说明尺度换成 $\lambda\lvert q\rangle$ 时，为什么权重必须同时换
- [ ] 说明弯曲空间里 $\delta$ 前为什么多一个 $\rho^{-1}$
