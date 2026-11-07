# D17 · 路径积分表示：$\langle q_f\lvert e^{-\beta H}\lvert q_i\rangle=\int\mathcal{D}q\,e^{-S_E}$

> 建档 2026-11-06 · 上游：[D00](D00-commutator-axiom.md)、[D14](D14-qp-overlap.md)、[D07](D07-product-kernel.md)、[D15](D15-p-completeness.md)；默认：D01
> 下游：[D18](D18-trace-is-loop.md)
> 原为 [N002 §2.1–2.3](../notes/N002-finite-temperature-path-integral.md)，2026-11-06 移入网格。

---

## 0. 命题

$$
\langle q_f\lvert e^{-\beta H}\lvert q_i\rangle
=\int_{q(0)=q_i}^{q(\beta)=q_f}\mathcal{D}q\;e^{-S_E[q]}
$$

其中

$$
S_E[q]=\int_0^\beta d\tau\left[\frac{m}{2}\dot q^{2}+V(q)\right]
$$

**适用条件**：

1. $H=\dfrac{\hat p^{2}}{2m}+V(\hat q)$——动能是 $p$ 的二次型，位能只依赖坐标；
2. 极限 $N\to\infty$、$\varepsilon=\beta/N\to0$ 存在（自由情形精确，一般情形形式成立）；
3. 测度 $\mathcal{D}q$ **自带**归一化因子 $\prod_k\left(m/2\pi\varepsilon\right)^{1/2}$（见 §1.4，最易漏）；
4. 端点条件 $q(0)=q_i$、$q(\beta)=q_f$——**不是零，也不是周期**；周期是 [D18](D18-trace-is-loop.md) 取迹之后的事。

**它在讲什么**：把一个算子的矩阵元换成"对全部历史的加权求和"，权是 $e^{-S_E}$。这是整条路线的地基——没有它，[D18](D18-trace-is-loop.md)、欧氏化、黑洞温度都无处落地。

---

## 1. 证明

### 1.1 第一步：切片

$$
e^{-\beta H}=\left(e^{-\varepsilon H}\right)^{N},
\qquad
\varepsilon=\frac{\beta}{N}
$$

在每两片之间插入位置完备性 $\int dq_k\lvert q_k\rangle\langle q_k\rvert=\mathbb{1}$ 共 $N-1$ 次：

$$
\langle q_f\lvert e^{-\beta H}\lvert q_i\rangle
=\int\prod_{k=1}^{N-1}dq_k\;\prod_{k=0}^{N-1}\langle q_{k+1}\lvert e^{-\varepsilon H}\lvert q_k\rangle
$$

其中 $q_0=q_i$、$q_N=q_f$。

### 1.2 第二步：单片矩阵元

用 Trotter 分裂（误差 $\mathcal{O}(\varepsilon^{2})$）：

$$
e^{-\varepsilon H}=e^{-\varepsilon V(\hat q)}\,e^{-\varepsilon\hat p^{2}/2m}\left(1+\mathcal{O}(\varepsilon^{2})\right)
$$

$e^{-\varepsilon V}$ 在 $q$ 基下对角，给出 $e^{-\varepsilon V(q')}\delta(q'-q'')$。动能部分插入动量完备性 $\int\frac{dp}{2\pi}\lvert p\rangle\langle p\rvert=\mathbb{1}$，并用 [D14](D14-qp-overlap.md) 的 $\langle q\lvert p\rangle=e^{ipq}$：

$$
\langle q'\lvert e^{-\varepsilon H}\lvert q\rangle
=\int\frac{dp}{2\pi}\,e^{ip(q'-q)}\,e^{-\varepsilon\left[p^{2}/2m+V(q)\right]}
$$

对 $p$ 做高斯积分（$\int e^{-ap^{2}+bp}dp=\sqrt{\pi/a}\,e^{b^{2}/4a}$，取 $a=\varepsilon/2m$、$b=i(q'-q)$）：

$$
\langle q'\lvert e^{-\varepsilon H}\lvert q\rangle
=\left(\frac{m}{2\pi\varepsilon}\right)^{1/2}
\exp\left[-\frac{m(q'-q)^{2}}{2\varepsilon}-\varepsilon V(q)\right]
$$

**这就是短时核。** 注意那个 $\frac{m(q'-q)^{2}}{2\varepsilon}$：它来自对 $p$ 的积分，也就是来自 $[\hat q,\hat p]=i$。若二者对易，$p$ 积分直接给 $\delta(q'-q)$，就没有"路径"可走。

### 1.3 第三步：拼回去，取连续极限

$N$ 个因子相乘，指数上是

$$
-\sum_{k=0}^{N-1}\left[\frac{m(q_{k+1}-q_k)^{2}}{2\varepsilon}+\varepsilon V(q_k)\right]
$$

当 $\varepsilon\to0$：$(q_{k+1}-q_k)/\varepsilon\to\dot q$，$\varepsilon\sum_k\to\int_0^\beta d\tau$，于是

$$
-\sum_k[\cdots]\;\longrightarrow\;-\int_0^\beta d\tau\left[\frac{m}{2}\dot q^{2}+V(q)\right]=-S_E[q]
$$

### 1.4 第四步：测度

连同每片各带一个的 $(m/2\pi\varepsilon)^{1/2}$，记

$$
\mathcal{D}q\equiv\lim_{N\to\infty}\prod_{k=0}^{N-1}\left(\frac{m}{2\pi\varepsilon}\right)^{1/2}\prod_{k=1}^{N-1}dq_k
$$

**漏掉归一化必错**，而且错得不显眼：自由粒子的结果是 $\beta^{-1/2}$，指数正是由"每片一个 $(m/\varepsilon)^{1/2}$、共 $N$ 片"定出来的。

**证毕。**

---

## 2. 一致性检验

| 检验 | 结果 |
|---|---|
| 自由粒子（$V=0$） | 核为 $(m/2\pi\beta)^{1/2}e^{-m(q_f-q_i)^{2}/2\beta}$，与直接解热方程一致 ✅ |
| 合成律 | $\int dq'\,K(q_f,q';\beta_2)K(q',q_i;\beta_1)=K(q_f,q_i;\beta_1+\beta_2)$，正是切片构造的自洽性 ✅ |
| $\beta\to0$ | 宽度 $\sqrt{\beta/m}\to0$，核趋于 $\delta(q_f-q_i)$ ✅ |
| 与能级展开一致 | $K=\sum_n e^{-\beta E_n}\psi_n(q_f)\psi_n^{*}(q_i)$，取迹即 [D18](D18-trace-is-loop.md) ✅ |
| 测度检查 | 保留 $\prod(m/\varepsilon)^{1/2}$ 才得到正确的 $\beta^{-1/2}$；丢弃则量纲都不对 ✅ |

---

## 3. 备注与边界

1. **这不是恒等式，是极限。** 每片都是 $\mathcal{O}(\varepsilon^{2})$ 近似，乘 $N=\beta/\varepsilon$ 片后累计 $\mathcal{O}(\varepsilon)$，$\varepsilon\to0$ 才消失。
2. **测度不是 $\prod dq_k$。** 它自带归一化。这是路径积分"形式化"的根源，也是 $\zeta$ 正规化与热核展开的入口。
3. **Trotter 分裂的排序无关性依赖"动能是 $p$ 的二次型、位能只依赖 $q$"。** 一旦动能含 $q$（弯曲空间 $g^{ij}(q)p_ip_j$），中点序与端点序的差别会留下有限修正——弯曲空间路径积分里那个测度项就是这么来的。本卡片在平直空间，故可任取。
4. **端点不固定为 $0$。** 常见错误是写 $q(0)=q(\beta)=0$；正确是 $q(0)=q_i$、$q(\beta)=q_f$，两端自由。
5. **它只管"从 $q_i$ 走到 $q_f$"的一条路径。** 取迹（把两端焊死）是 [D18](D18-trace-is-loop.md) 的事，不是本卡片的一部分。

---

## 4. 自检

- [ ] 不看本文，写出切片三步：$e^{-\varepsilon H}$ 的分裂、单片核、乘积取极限
- [ ] 说明 $(q_{k+1}-q_k)^{2}/\varepsilon$ 从哪来，以及它为什么是 $[\hat q,\hat p]=i$ 的影子
- [ ] 复现短时核的高斯积分，检查归一化因子
- [ ] 用自由粒子的已知结果检验 $\beta^{-1/2}$ 的幂次
- [ ] 说明为什么测度不能写成 $\prod dq_k$
- [ ] 说明端点条件为什么不是零
