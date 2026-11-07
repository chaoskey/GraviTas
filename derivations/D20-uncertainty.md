# D20 · 不确定关系：$\Delta q\,\Delta p\ge\frac{1}{2}$

> 建档 2026-11-07 · 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)
> 下游：无卡片依赖（结论只被笔记引用）
> 原为 [N003 §5.1](../notes/N003-basis-and-operator-relations.md) 的一句话，2026-11-07 补全证明并移入网格。

---

## 0. 命题

对任意归一化态 $\psi$（$\hbar=1$）：

$$
\Delta q\,\Delta p\ge\frac{1}{2},
\qquad
\Delta q\equiv\sqrt{\langle\hat q^{2}\rangle-\langle\hat q\rangle^{2}}
$$

**它在讲什么**：不是"测量会扰动系统"，而是**同一条波函数上，两个量的弥散不能同时很小**。证明只用到对易关系与 Cauchy–Schwarz，不涉及任何测量过程。

---

## 1. 证明（Robertson 不等式）

### 1.1 第一步：移到均值处

记

$$
\delta\hat q\equiv\hat q-\langle\hat q\rangle\,\mathbb{1},
\qquad
\delta\hat p\equiv\hat p-\langle\hat p\rangle\,\mathbb{1}
$$

则 $\langle\delta\hat q^{2}\rangle=(\Delta q)^{2}$、$\langle\delta\hat p^{2}\rangle=(\Delta p)^{2}$，且 $[\delta\hat q,\delta\hat p]=[\hat q,\hat p]=i$。

### 1.2 第二步：Cauchy–Schwarz

$$
(\Delta q)^{2}(\Delta p)^{2}
=\lVert\delta\hat q\,\psi\rVert^{2}\,\lVert\delta\hat p\,\psi\rVert^{2}
\ge\bigl\lvert\langle\delta\hat q\,\psi\lvert\delta\hat p\,\psi\rangle\bigr\rvert^{2}
=\bigl\lvert\langle\delta\hat q\,\delta\hat p\rangle\bigr\rvert^{2}
$$

### 1.3 第三步：拆成对称与反对称两部分

任何算子都能拆成 Hermitian 与反 Hermitian 之和：

$$
\delta\hat q\,\delta\hat p
=\underbrace{\tfrac{1}{2}\{\delta\hat q,\delta\hat p\}}_{\text{Hermitian}}
+\underbrace{\tfrac{1}{2}\bigl[\delta\hat q,\delta\hat p\bigr]}_{\text{反 Hermitian}}
$$

两者对易（一个是 Hermitian、一个是纯虚数倍单位），故内积正交，模方可以相加：

$$
\bigl\lvert\langle\delta\hat q\,\delta\hat p\rangle\bigr\rvert^{2}
=\Bigl\langle\tfrac{1}{2}\{\delta\hat q,\delta\hat p\}\Bigr\rangle^{2}
+\Bigl\lvert\Bigl\langle\tfrac{1}{2}\bigl[\delta\hat q,\delta\hat p\bigr]\Bigr\rangle\Bigr\rvert^{2}
$$

### 1.4 第四步：丢掉第一项，代入对易子

$$
\ge\Bigl\lvert\tfrac{1}{2}\bigl\langle[\hat q,\hat p]\bigr\rangle\Bigr\rvert^{2}
=\Bigl\lvert\tfrac{i}{2}\Bigr\rvert^{2}=\frac{1}{4}
$$

开平方即得 $\Delta q\,\Delta p\ge\frac{1}{2}$。**证毕。**

---

## 2. 一致性检验

| 检验 | 结果 |
|---|---|
| 高斯波包 | $\psi\propto e^{-q^{2}/4\sigma^{2}}$ 使 $\Delta q\,\Delta p=\frac{1}{2}$，恰好取等 ✅ |
| 恢复 $\hbar$ | $\Delta q\,\Delta p\ge\hbar/2$（$\hbar$ 回到 $[\hat q,\hat p]=i\hbar$）✅ |
| 界与态无关 | $\langle[\hat q,\hat p]\rangle=i$ 是常数，故右边对所有态都是 $1/2$ ✅ |
| 与 [D00](D00-commutator-axiom.md) 一致 | 界完全由对易子给出；$[\hat q,\hat p]=0$ 时界消失（经典极限）✅ |

---

## 3. 边界

1. **它不涉及测量**。"测量扰动"是另一条命题（误差-扰动关系），两者常被混为一谈；本条的推导里没有任何"测量"二字。
2. **要求态归一化且两个量都有有限二阶矩**。$\lvert q\rangle$ 本身不适用（$\Delta p=\infty$）。
3. **界可以更紧**：保留 §1.3 的第一项得 Robertson–Schrödinger 不等式

$$
(\Delta q)^{2}(\Delta p)^{2}\ge\Bigl(\tfrac{1}{2}\langle\{\delta\hat q,\delta\hat p\}\rangle\Bigr)^{2}+\frac{1}{4}
$$

压缩态正是靠第一项非零与第二项取等来实现的。
4. **对非对易但非正则的量**，形式相同，把 $[\hat q,\hat p]$ 换成相应算子即可。

---

## 4. 自检

- [ ] 不看本文，写出 Cauchy–Schwarz 那一步并说明它作用在哪两个向量上
- [ ] 解释为什么要先把算子移到均值处（$\delta\hat q$、$\delta\hat p$）
- [ ] 说明"对称 + 反对称"的拆分为什么能直接相加模方
- [ ] 举出取等号的态（高斯波包）并验证
- [ ] 说清本条与"测量扰动"的区别
