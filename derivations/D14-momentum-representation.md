# D14 · $\hat p$ 在 $q$ 表象下是 $-i\partial_q$

> 建档 2026-11-07 · 上游：[D00](D00-commutator-axiom.md)、[D13](D13-qp-overlap.md)；默认：D01
> 下游：无卡片依赖（结论只被笔记引用）
> 原为 [N003 §3.1–3.2](../notes/N003-basis-and-operator-relations.md)，2026-11-07 移入网格。

---

## 0. 命题

$$
\langle q\lvert\hat p\lvert\psi\rangle=-i\,\frac{d}{dq}\psi(q)
$$

等价地，$\hat p$ 的核是

$$
\langle q'\lvert\hat p\lvert q''\rangle=-i\,\partial_{q'}\,\delta(q'-q'')
$$

**它在讲什么**：动量在位置表象里就是"求导"。**但它不是定义，是推论**——定义只有 [D00](D00-commutator-axiom.md) 的对易关系与 $\hat q$ 的谱。

---

## 1. 证明

由 [D13](D13-qp-overlap.md)，$\langle q\lvert p\rangle=e^{ipq}$；由 [D01](D01-spectral-theorem.md)，$\int\frac{dp}{2\pi}\lvert p\rangle\langle p\rvert=\mathbb{1}$。于是

$$
\langle q\lvert\hat p\lvert\psi\rangle
=\int\frac{dp}{2\pi}\;\langle q\lvert p\rangle\,p\,\langle p\lvert\psi\rangle
=\int\frac{dp}{2\pi}\,e^{ipq}\,p\,\tilde\psi(p)
$$

另一方面，把 $\psi(q)=\int\frac{dp}{2\pi}e^{ipq}\tilde\psi(p)$ 求导：

$$
-i\,\frac{d}{dq}\psi(q)
=-i\int\frac{dp}{2\pi}(ip)\,e^{ipq}\,\tilde\psi(p)
=\int\frac{dp}{2\pi}\,p\,e^{ipq}\,\tilde\psi(p)
$$

两式相等，**证毕**。

---

## 2. 核的形式

把 $\langle q'\lvert\hat p\lvert\psi\rangle$ 写成积分：

$$
\int dq''\,\langle q'\lvert\hat p\lvert q''\rangle\,\psi(q'')
=-i\psi'(q')
$$

对照 $\int dq''\bigl[-i\partial_{q'}\delta(q'-q'')\bigr]\psi(q'')=-i\psi'(q')$，即得

$$
\langle q'\lvert\hat p\lvert q''\rangle=-i\partial_{q'}\delta(q'-q'')
$$

**模式**：对角项带 $\delta$（如 $\hat q$ 的核），非对角项带 $\delta$ 的**导数**。这个模式在所有表象里重复。

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| 平面波 | $-i\partial_q e^{ipq}=p\,e^{ipq}$，正是 $\hat p$ 的本征函数 ✅ |
| 平移 | $e^{ia\hat p}=e^{a\partial_q}$，作用为 $\psi(q)\to\psi(q+a)$，与 [D12](D12-translation.md) 一致 ✅ |
| 对易子 | $[\hat p,\hat q]=-i\partial_q(q\psi)-q(-i\partial_q\psi)=-i$ ✅ |
| 与 [D04](D04-commutator-p-fq.md) 一致 | $-i\partial_q(f\psi)-f(-i\partial_q\psi)=-if'\psi$，正是 D04 的结论 ✅ |
| $p$ 表象对称形式 | $\langle p\lvert\hat q\lvert\psi\rangle=i\partial_p\tilde\psi(p)$，符号相反（互换 $q\leftrightarrow p$ 所致）✅ |

---

## 4. 边界

1. **它是"表示"，不是"定义"。** 换成 $p$ 表象，$\hat p$ 就是"乘以 $p$"；换到相空间，又是另一个样子。定义只有 [D00](D00-commutator-axiom.md)。
2. **依赖两个前提**：$\langle q\lvert p\rangle=e^{ipq}$（[D13](D13-qp-overlap.md)，需 S–vN 与谱定理）与完备性（[D01](D01-spectral-theorem.md)）。缺一个，推导不成立。
3. **无界性**：$\hat p$ 无界，求导只在稠密定义域（绝对连续且导数平方可积的函数）上有意义。
4. **符号约定**：若取 $\hat p=+i\partial_q$（即 $[\hat q,\hat p]=-i$），符号全反。判据仍是 [D12](D12-translation.md) 的平移方向。

---

## 5. 自检

- [ ] 不看本文，从 $\langle q\lvert p\rangle=e^{ipq}$ 推出 $\hat p=-i\partial_q$
- [ ] 写出 $\hat p$ 的核，并说明"$\delta$ 的导数"从哪来
- [ ] 用平面波与平移两种方式检验
- [ ] 说明为什么这是推论而不是定义
