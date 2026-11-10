# D15 · Weyl 相位：$e^{ia\hat p}e^{ib\hat q}=e^{iab}e^{ib\hat q}e^{ia\hat p}$

> 建档 2026-11-06 · 上游：[D00](D00-commutator-axiom.md)、[D13](D13-commutator-phase.md)；默认：D06
> 下游：[D17](D17-qp-overlap.md)
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

由 [D13](D13-commutator-phase.md)：若 $[A,B]=c$ 是数，则 $e^{A}e^{B}=e^{c}e^{B}e^{A}$。

取

$$
A=ia\hat p,\qquad B=ib\hat q
$$

先算对易子：

$$
[A,B]=(ia)(ib)\,[\hat p,\hat q]
=-ab\cdot(-i)=iab
$$

于是 $c=iab$ 是数，代入 D13：

$$
\boxed{\,e^{ia\hat p}\,e^{ib\hat q}=e^{iab}\,e^{ib\hat q}\,e^{ia\hat p}\,}
$$

**证毕。**

**注意符号链里的两处负号**：$(ia)(ib)=-ab$ 是一处，$[\hat p,\hat q]=-i$ 是另一处，两者相乘得 $+iab$。写错任何一处，结论都会差一个复共轭。

---

### 1.6 反过来：从 Weyl 关系回到对易子

本卡的关系可以"求导"回到 [D00](D00-commutator-axiom.md) 的公理。**这一步是 D15 与 D00 的接缝**，放在这里而不是 D00，是因为它用的全是 Weyl 关系。

**前提**：$U(a)=e^{ia\hat p}$、$V(b)=e^{ib\hat q}$ 强连续（Stone 定理给出生成元）；$\psi$ 取在公共不变稠密域内。

把关系写成"差为零"：

$$
W(a,b)\equiv U(a)\,V(b)-e^{iab}\,V(b)\,U(a)=0
$$

**对 $b$ 求导**：

$$
\partial_b W
=U(a)\,\partial_b V(b)-\bigl(ia\,e^{iab}\bigr)V(b)U(a)
-e^{iab}\bigl(\partial_b V(b)\bigr)U(a)
$$

**再对 $a$ 求导**：

$$
\begin{aligned}
\partial_a\partial_b W
={}&(\partial_aU)\,(\partial_bV)
-i\,e^{iab}VU+ab\,e^{iab}VU-ia\,e^{iab}V(\partial_aU)\\
&-ib\,e^{iab}(\partial_bV)U-e^{iab}(\partial_bV)(\partial_aU)
\end{aligned}
$$

**取 $a=b=0$**，只剩三项：

$$
0=(i\hat p)(i\hat q)-i-(i\hat q)(i\hat p)
=-\hat p\hat q-i+\hat q\hat p
=[\hat q,\hat p]-i
\quad\Longrightarrow\quad
[\hat q,\hat p]=i
$$

**那个 $-i$ 从哪来**：$\partial_b e^{iab}=ia\,e^{iab}$，再对 $a$ 求导时那个 $ia$ 变成常数 $i$。**它是中心荷的残余**——若两个群对易（相因子为 $1$），这一项消失，得到 $[\hat q,\hat p]=0$。所以**非零对易子完全由相位 $e^{iab}$ 产生**。

**另证（更短）**：把关系写成共轭形式 $U(a)V(b)U(a)^{-1}=e^{iab}V(b)$。先对 $a$ 求导得 $[\hat p,V(b)]=b\,V(b)$，再对 $b$ 求导得 $i[\hat p,\hat q]=\mathbb{1}$。

**三点注意**：

1. **结论只在稠密子集上成立**：$[\hat q,\hat p]\psi=i\psi$（$\psi\in D$），不是全空间的算子等式；
2. **$W$ 是算子的差**，$W=0$ 指它在 $D$ 上作用为零；
3. **反向不成立**：由对易子推回本卡的关系，还要补"自伴、公共不变稠密域、强连续"三条——这正是本卡比公理"更强"的地方。

---

## 2. 一致性检验

| 检验 | 结果 |
|---|---|
| $a=0$ 或 $b=0$ | 因子为 $1$，两边相等 ✅ |
| 与 [D13](D13-commutator-phase.md) 一致 | $c=iab$ 直接代回 ✅ |
| 两式相除 | $e^{iab}/e^{-iab}=e^{2iab}$，与"$q$ 在前"版本相差 $e^{2iab}$ ✅ |
| 与 $[\hat p,\hat q]=-i$ 一致 | 若误用 $[\hat p,\hat q]=+i$，会得 $e^{-iab}$，与平移方向矛盾 |
| 模长 | $\lvert e^{iab}\rvert=1$（$a,b$ 实），两边都是酉算子 ✅ |

---

## 3. 备注与边界

1. **符号判据只有一条**：$e^{ia\hat p}$ 把 $\lvert q\rangle$ 移到 $q+a$ 还是 $q-a$。本仓库取后者。
2. **混用两式会差 $e^{2iab}$。** 这不是"差不多"，是相位差一个有限量；在高斯积分里会变成一个实因子 $e^{-2ab}$ 或 $e^{+2ab}$，量纲上看不出来。
3. **它是下游平面波公式的直接上游。** $\langle q\lvert p\rangle=e^{ipq}$ 的推导要用本式把 $\lvert p\rangle$ 的平移性质定下来。
4. **更对称的生成元形式**：若取 $W(a,b)=e^{i(a\hat q+b\hat p)}$，则乘法律为

$$
W(a,b)\,W(a',b')=e^{-\frac{i}{2}(ab'-ba')}\,W(a+a',b+b')
$$

相位里的 $ab'-ba'$ 是相空间辛形式。**注意这里出现 $1/2$**，与 D15 的 $e^{iab}$ 不矛盾：那个 $1/2$ 是"与对称中点比"的结果（见 [D14](D14-three-bch-forms.md) §0），这里是"两个群元相乘"。两条不同的比较，各自的系数不同。

5. **无穷自由度时失效。** [D05](D05-stone-von-neumann.md) 在无穷自由度下不成立，Weyl 关系的不可约表示不唯一，本式只在指定表示（如 Fock 表示）内有意义。

---

## 4. 自检

- [ ] 写出裸对易子与 Weyl 关系，并说明为什么后者更严格
- [ ] 不做任何假设，从 Weyl 关系求导导出 $[\hat q,\hat p]=i$，并指出那个 $-i$ 从哪来
- [ ] 不看本文，算出 $[ia\hat p,ib\hat q]$，并指出两个负号的来源
- [ ] 写出 $q$ 在前的版本，说明两者相差多少
- [ ] 说明符号如何由 $e^{ia\hat p}$ 的平移方向决定
- [ ] 解释为什么 $W(a,b)$ 的乘法律出现 $1/2$，而本式没有
- [ ] 说明本式在下游哪一步被用到
