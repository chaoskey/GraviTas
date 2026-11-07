# D14 · 动量基的完备性：$\int\frac{dp}{2\pi}\lvert p\rangle\langle p\rvert=\mathbb{1}$

> 建档 2026-11-07 · 上游：[D01](D01-spectral-theorem.md)（位置基的完备性）、[D13](D13-qp-overlap.md)（$\langle q\lvert p\rangle=e^{ipq}$）
> 下游：[D15](D15-momentum-representation.md)、[D16](D16-path-integral-representation.md)
> 本卡补的是"换基"这一步：它**不是新假设**，是从位置基推出来的。

---

## 0. 命题

$$
\int\frac{dp}{2\pi}\;\lvert p\rangle\langle p\rvert=\mathbb{1}
$$

**它在讲什么**：动量本征态也构成一组完备基，权重是 $\frac{dp}{2\pi}$，不是 $dp$。

**关键区分**（本卡存在的理由）：

| 式子 | 来源 | 性质 |
|---|---|---|
| $\int dq\,\lvert q\rangle\langle q\rvert=\mathbb{1}$ | [D01](D01-spectral-theorem.md) §1.2 的 resolution of identity | **定理**（谱定理直接给） |
| $\int\frac{dp}{2\pi}\lvert p\rangle\langle p\rvert=\mathbb{1}$ | 上一行 + $\langle q\lvert p\rangle=e^{ipq}$ | **推论**（本卡证明） |

**所以 $\frac{dp}{2\pi}$ 这个系数不必死记，它由"换基要保持恒等算子"唯一确定。**

---

## 1. 证明（三行）

### 1.1 第一步：把待证对象化成核

由 [D01](D01-spectral-theorem.md) 的 $\{\lvert q\rangle\}$ 完备，算子由它的核唯一确定。对任意 $q',q''$：

$$
\Bigl\langle q'\bigr\lvert\Bigl(\int\frac{dp}{2\pi}\lvert p\rangle\langle p\rvert\Bigr)\bigr\lvert q''\Bigr\rangle
=\int\frac{dp}{2\pi}\,\langle q'\lvert p\rangle\,\langle p\lvert q''\rangle
$$

### 1.2 第二步：代入重叠

由 [D13](D13-qp-overlap.md)，$\langle q\lvert p\rangle=e^{ipq}$，故 $\langle p\lvert q''\rangle=\overline{e^{ipq''}}=e^{-ipq''}$：

$$
=\int\frac{dp}{2\pi}\,e^{ip(q'-q'')}
$$

### 1.3 第三步：$\delta$ 的傅里叶表示

$$
\int\frac{dp}{2\pi}\,e^{ipx}=\delta(x)
\quad\Longrightarrow\quad
=\delta(q'-q'')=\langle q'\lvert q''\rangle
$$

**两个算子的核处处相同**，而 $\{\lvert q\rangle\}$ 完备 $\Rightarrow$ 两个算子相等：

$$
\int\frac{dp}{2\pi}\lvert p\rangle\langle p\rvert=\mathbb{1}
$$

**证毕。**

---

## 2. 为什么 $2\pi$ 必须在那

把系数换掉，看结果：

| 写法 | 积分给出 | 是否等于 $\mathbb{1}$ |
|---|---|---|
| $\int\frac{dp}{2\pi}$ | $\delta(q'-q'')$ | ✅ |
| $\int dp$ | $2\pi\,\delta(q'-q'')$ | ❌ 等于 $2\pi\mathbb{1}$ |
| $\int\frac{dp}{\sqrt{2\pi}}$ | $\frac{1}{\sqrt{2\pi}}\delta(q'-q'')$ | ❌ 差一个因子 |

**只有 $\frac{dp}{2\pi}$ 给出恒等算子。** 所以它不是"配平出来"的，而是被 $\delta$ 的傅里叶表示**唯一钉死**的。

这与 [D01](D01-spectral-theorem.md) §2.4 的 $w\,c=1$ 是同一件事的两面：$\langle p\lvert p'\rangle=2\pi\delta$ 给出 $c=2\pi$，于是完备性权重只能是 $w=\frac{1}{2\pi}$。

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| 作用在平面波上 | $\int\frac{dp'}{2\pi}\lvert p'\rangle\langle p'\lvert p\rangle=\lvert p\rangle$，与 $\int\frac{dp'}{2\pi}2\pi\delta(p'-p)=1$ 一致 ✅ |
| 与 [D13](D13-qp-overlap.md) §1.5 相容 | 那里由 $\int dq\lvert q\rangle\langle q\rvert$ 反推 $\lvert c(p)\rvert=1$；本卡是同一恒等式的另一侧 ✅ |
| 与 [D15](D15-momentum-representation.md) 相容 | 那里插入 $\int\frac{dp}{2\pi}\lvert p\rangle\langle p\rvert$ 得 $\hat p=-i\partial_q$，系数与本卡一致 ✅ |
| 与 [D16](D16-path-integral-representation.md) 相容 | 短时核的动量积分正是用本卡的权重 ✅ |

---

## 4. 边界

1. **需要 $\lvert p\rangle$ 存在。** 与 $\lvert q\rangle$ 同理，来自 [D01](D01-spectral-theorem.md) 的 Gelfand–Maurin，不在 $\mathcal{H}$ 内。
2. **$2\pi$ 的位置是约定，但"总要有系数"不是。** 若改用对称归一 $\langle q\lvert p\rangle=e^{ipq}/\sqrt{2\pi}$，则 $\langle p\lvert p'\rangle=\delta(p-p')$、完备性变成 $\int dp\lvert p\rangle\langle p\rvert=\mathbb{1}$——$2\pi$ 搬家了，但 $wc=1$ 不变。
3. **多自由度时按维数乘。** $n$ 维时权重是 $\frac{d^{n}p}{(2\pi)^{n}}$；这是傅里叶变换约定在每维各带一个 $2\pi$ 的直接结果，不是新规则。
4. **这不是"另一条公设"。** 换基只是用不同基底展开同一个恒等算子，不存在"两套完备性"需要各自假设。

---

## 5. 自检

- [ ] 用"算核"的方式写出证明，并说明为什么核相同就能断定算子相同
- [ ] 说明 $2\pi$ 为什么必须在积分测度里，而不在 $\lvert p\rangle$ 的定义里
- [ ] 把 $\int dp$ 的写法代进去，算出它等于 $2\pi\mathbb{1}$ 而不是 $\mathbb{1}$
- [ ] 用 $w\,c=1$ 把本卡与 [D01](D01-spectral-theorem.md) §2.4 对上
- [ ] 说明换成对称归一时 $2\pi$ 去哪了
