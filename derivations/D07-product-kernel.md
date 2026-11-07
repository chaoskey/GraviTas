# D07 · 乘积的核：插入完备性

> 建档 2026-11-07 · 上游：[D01](D01-spectral-theorem.md)
> 下游：[D17](D17-path-integral-representation.md)
> 原为 [N003 §3.3](../notes/N003-basis-and-operator-relations.md)，2026-11-07 移入网格。

---

## 0. 命题

$$
\langle q'\lvert\hat A\hat B\lvert q''\rangle
=\int dq\;\langle q'\lvert\hat A\lvert q\rangle\,\langle q\lvert\hat B\lvert q''\rangle
$$

**它在讲什么**：两个算子相乘的核，等于"中间插一个完备集再积分"。物理语言就是**在中间放一张快照**。

---

## 1. 证明（一行）

$$
\hat A\hat B=\hat A\cdot\mathbb{1}\cdot\hat B
=\hat A\left(\int dq\,\lvert q\rangle\langle q\rvert\right)\hat B
$$

取 $\langle q'\lvert\cdots\lvert q''\rangle$ 即得。

---

## 2. 为什么它是路径积分的引擎

把 $\hat A\hat B$ 换成 $\hat A_1\hat A_2\cdots\hat A_N$，逐次插入，得 $N-1$ 重积分：

$$
\langle q_f\lvert\hat A_1\cdots\hat A_N\lvert q_i\rangle
=\int\prod_{k=1}^{N-1}dq_k\;\prod_{k=0}^{N-1}\langle q_{k+1}\lvert\hat A_{k+1}\lvert q_k\rangle
$$

**每插入一次，就多一个"中途位置"**。取 $N\to\infty$，这些中途位置连成一条路径——这正是 [D17](D17-path-integral-representation.md) §1.1 的全部内容。

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| $\hat A=\hat B=\mathbb{1}$ | 右边 $\int dq\,\delta(q'-q)\delta(q-q'')=\delta(q'-q'')$ ✅ |
| $\hat A=\lvert q_1\rangle\langle q_1\rvert$ | 右边塌缩为 $\langle q'\lvert q_1\rangle\langle q_1\lvert\hat B\lvert q''\rangle$，与直接计算一致 ✅ |
| 与 [D17](D17-path-integral-representation.md) §1.1 对照 | 同一式子，只是那里取 $\hat A_k=e^{-\varepsilon H}$ ✅ |
| 与 [D01](D01-spectral-theorem.md) 一致 | 完备性 $\int dq\lvert q\rangle\langle q\rvert=\mathbb{1}$ 是它的 resolution of identity ✅ |

---

## 4. 边界

1. **连续谱时核是分布**，这个积分要在分布意义下理解；收敛性取决于 $\hat A,\hat B$ 的性质（例如两者都有界时无问题）。
2. **它不处理"同一时刻"的算子排序问题**：$\hat A\hat B$ 与 $\hat B\hat A$ 的核不同，插值的位置决定谁在左。
3. **有限维时是平凡的矩阵乘法**（$\sum_k A_{ik}B_{kj}$）；连续谱只是把求和变成积分。

---

## 5. 自检

- [ ] 用一行写出证明，并说明插的是什么
- [ ] 把二重乘积推广到 $N$ 重，并说出积分的重数
- [ ] 说明为什么它"就是"路径积分的切片构造
- [ ] 举例说明 $\hat A\hat B$ 与 $\hat B\hat A$ 的核不同
