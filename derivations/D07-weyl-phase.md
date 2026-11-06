# D07 · Weyl 相位：$e^{ia\hat p}e^{ib\hat q}=e^{iab}e^{ib\hat q}e^{ia\hat p}$

> 建档 2026-11-06 · 上游：[D00](D00-commutator-axiom.md)、[D05](D05-commutator-phase.md)
> 下游：[D08](D08-qp-overlap.md)；[N003 §0.3](../notes/N003-basis-and-operator-relations.md)、[N004 §5](../notes/N004-hadamard-lemma.md)
> 原为 [N004 §5](../notes/N004-hadamard-lemma.md) 尾部，2026-11-06 移入网格。

---

## 0. 命题

$$
e^{ia\hat p}\,e^{ib\hat q}=e^{iab}\,e^{ib\hat q}\,e^{ia\hat p},
\qquad a,b\in\mathbb{R}
$$

**换次序就是换符号**（$q$ 在前）：

$$
e^{ia\hat q}\,e^{ib\hat p}=e^{-iab}\,e^{ib\hat p}\,e^{ia\hat q}
$$

**适用条件**：

1. $a,b$ 是实数（否则两边的"酉"性不再成立，$e^{iab}$ 也不是相位）；
2. 用本仓库约定 $[\hat q,\hat p]=i$、$\hat p=-i\partial_q$；
3. $e^{\pm ia\hat p}$、$e^{\pm ib\hat q}$ 有定义（有界时处处，无界时在解析向量上）。

**它在讲什么**：位置与动量的酉群不交换，交换一次要付一个**相位** $e^{iab}$。这个相位不是修正项，它是 $[\hat q,\hat p]=i$ 的**全部内容**的指数形式。

---

## 1. 证明

由 [D05](D05-commutator-phase.md)：若 $[A,B]=c$ 是数，则 $e^{A}e^{B}=e^{c}e^{B}e^{A}$。

取

$$
A=ia\hat p,\qquad B=ib\hat q
$$

先算对易子：

$$
[A,B]=(ia)(ib)\,[\hat p,\hat q]
=-ab\cdot(-i)=iab
$$

于是 $c=iab$ 是数，代入 D05：

$$
\boxed{\,e^{ia\hat p}\,e^{ib\hat q}=e^{iab}\,e^{ib\hat q}\,e^{ia\hat p}\,}
$$

**证毕。**

**注意符号链里的两处负号**：$(ia)(ib)=-ab$ 是一处，$[\hat p,\hat q]=-i$ 是另一处，两者相乘得 $+iab$。写错任何一处，结论都会差一个复共轭。

---

## 2. 一致性检验

| 检验 | 结果 |
|---|---|
| $a=0$ 或 $b=0$ | 因子为 $1$，两边相等 ✅ |
| 与 [D05](D05-commutator-phase.md) 一致 | $c=iab$ 直接代回 ✅ |
| 两式相除 | $e^{iab}/e^{-iab}=e^{2iab}$，与"$q$ 在前"版本相差 $e^{2iab}$ ✅ |
| 与 $[\hat p,\hat q]=-i$ 一致 | 若误用 $[\hat p,\hat q]=+i$，会得 $e^{-iab}$，与 D02 的平移方向矛盾 |
| 模长 | $\lvert e^{iab}\rvert=1$（$a,b$ 实），两边都是酉算子 ✅ |

---

## 3. 备注与边界

1. **符号判据只有一条**：$e^{ia\hat p}$ 把 $\lvert q\rangle$ 移到 $q+a$ 还是 $q-a$（见 [D02](D02-translation.md)）。本仓库取 $e^{ia\hat p}\lvert q\rangle=\lvert q-a\rangle$，故 $p$ 在前时因子取 $+iab$。
2. **混用两式会差 $e^{2iab}$。** 这不是"差不多"，是相位差一个有限量；在高斯积分里会变成一个实因子 $e^{-2ab}$ 或 $e^{+2ab}$，量纲上看不出来。
3. **它是 D08 的直接上游。** $\langle q\lvert p\rangle=e^{ipq}$ 的推导要用本式把 $\lvert p\rangle$ 的平移性质定下来。
4. **更对称的生成元形式**：若取 $W(a,b)=e^{i(a\hat q+b\hat p)}$，则乘法律为

$$
W(a,b)\,W(a',b')=e^{-\frac{i}{2}(ab'-ba')}\,W(a+a',b+b')
$$

相位里的 $ab'-ba'$ 是相空间辛形式。**注意这里出现 $1/2$**，与 D07 的 $e^{iab}$ 不矛盾：那个 $1/2$ 是"与对称中点比"的结果（见 [D06](D06-three-bch-forms.md) §0），这里是"两个群元相乘"。两条不同的比较，各自的系数不同。

5. **无穷自由度时失效。** [D13](D13-stone-von-neumann.md) 在无穷自由度下不成立，Weyl 关系的不可约表示不唯一，本式只在指定表示（如 Fock 表示）内有意义。

---

## 4. 自检

- [ ] 不看本文，算出 $[ia\hat p,ib\hat q]$，并指出两个负号的来源
- [ ] 写出 $q$ 在前的版本，说明两者相差多少
- [ ] 说明符号如何由 $e^{ia\hat p}$ 的平移方向决定
- [ ] 解释为什么 $W(a,b)$ 的乘法律出现 $1/2$，而本式没有
- [ ] 说明本式在哪一步被 D08 用到
