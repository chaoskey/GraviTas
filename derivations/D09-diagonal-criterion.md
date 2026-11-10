# D09 · 对角判据：$[\hat q,f(\hat q)]=0$ ⇒ 核正比于 $\delta$

> 建档 2026-11-07 · 上游：[D00](D00-commutator-axiom.md)、[D01](D01-spectral-theorem.md)、[D03](D03-position-eigen-equation.md)、[D04](D04-normalization-convention.md)
> 下游：[D20](D20-hamiltonian.md)
> 原为 [N003 §4.2](../notes/N003-basis-and-operator-relations.md)，2026-11-07 移入网格。

---

## 0. 命题

对任意只含 $\hat q$ 的算子 $f(\hat q)$，

$$
\langle q'\lvert f(\hat q)\lvert q''\rangle=f(q')\,\delta(q'-q'')
$$

等价说法：

$$
\bigl[\hat q,f(\hat q)\bigr]=0
$$

**它在讲什么**：算子与 $\hat q$ 对易 $\iff$ 它在 $q$ 基下对角。对角算子的核必然是"一个函数乘以 $\delta$"。

---

## 1. 证明（两条路，第二条更根本）

### 1.1 路线一：谱分解

由 [D06](D06-functional-calculus.md) 与 [D01](D01-spectral-theorem.md)：

$$
f(\hat q)=\int dq\,f(q)\,\lvert q\rangle\langle q\rvert
$$

核直接读出：$\langle q'\lvert f(\hat q)\lvert q''\rangle=\int dq\,f(q)\delta(q'-q)\delta(q-q'')=f(q')\delta(q'-q'')$。

### 1.2 路线二：对易子论证

**不需要 $f$ 能展开，只需要"$f$ 是 $\hat q$ 的函数"这一件事。**

对任意 $q',q''$：

$$
\begin{align}
0&=\bigl\langle q'\bigr\lvert\bigl[\hat q,f(\hat q)\bigr]\bigl\lvert q''\bigr\rangle \\
&={\color{red}{\bigl\langle q'\bigr\lvert\hat q}}\,f(\hat q)\bigl\lvert q''\bigr\rangle
-\bigl\langle q'\bigr\lvert f(\hat q)\,{\color{blue}{\hat q\bigl\lvert q''\bigr\rangle}} \\
&={\color{red}{q'\bigl\langle q'\bigr\lvert}}\,f(\hat q)\bigl\lvert q''\bigr\rangle
-{\color{blue}{q''}}\bigl\langle q'\bigr\lvert f(\hat q)\,{\color{blue}{\bigl\lvert q''\bigr\rangle}} \\
&=(q'-q'')\,\langle q'\lvert f(\hat q)\lvert q''\rangle
\end{align}
$$

**第 3 行第一个等号依赖 $\hat q$ 自伴**：本征方程只给右矢 $\hat q\lvert q'\rangle=q'\lvert q'\rangle$；取伴随并用 $\hat q^{\dagger}=\hat q$，才得到左矢版本 $\langle q'\rvert\hat q=q'\langle q'\rvert$。而第二个等号（取出 $q''$）直接来自右矢本征方程——**两边的来源并不对称**，这一步不能省。

由 $(q'-q'')\,T=0$（记 $T\equiv\langle q'\lvert f(\hat q)\lvert q''\rangle$）：

- 若 $q'\ne q''$，则 $T=0$——**对角线之外一律为零**；
- 若 $q'=q''$，方程不约束 $T$——**对角线上可以"无限大"**。

所以 $T$ 只能集中在 $q'=q''$ 上，形如

$$
T=c(q')\,\delta(q'-q'')
$$

**为什么是 $\delta$，而不是它的导数**：把 $(q'-q'')$ 乘回去验算——$\delta$ 给出 $0$（符合要求），而 $\delta'$ 给出 $-\delta$（不符合）。所以对角线上只能放 $\delta$ 本身，不能放它的导数。

系数由"作用在态上"定：$f(\hat q)\lvert q''\rangle=f(q'')\lvert q''\rangle$，故 $c=f$。

**为什么这条路更根本**：它把"对角"这件事归因于**对易**，而不是归因于"$f$ 长什么样"。所以对不可微、不可展开的函数也成立。

---

## 2. 它用在哪

1. **$e^{-\varepsilon V(\hat q)}$ 在 $q$ 基下对角**——这是下游"位能那块直接提出去"的前提；
2. **解释一个常见困惑**：为什么 $V(q)$ 与 $V(q')$ 在 $\langle q'\lvert e^{-\varepsilon V(\hat q)}\lvert q''\rangle$ 里可以随便换？因为 $\delta$ 的支撑上 $q'=q''$，两者**精确**相等。差 $\mathcal{O}(\varepsilon^{3/2})$ 的说法只出现在"$\delta$ 被 $p$ 积分抹成高斯之后"——那时两点不再重合。
3. **判据可推广**：任何"与某算子对易"的算子，在该算子的表象下都对角。

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| $f=1$ | 核 $=\delta(q'-q'')$ ✅ |
| $f=\hat q$ | 核 $=q'\delta(q'-q'')$ ✅ |
| 与 [D08](D08-commutator-p-fq.md) 对照 | $[\hat p,f(\hat q)]\neq0$（等于 $-if'$），$[\hat q,f(\hat q)]=0$——**方向不同，结论相反** ✅ |
| 不解析的 $f$（如阶跃） | 路线二仍成立，路线一需谱分解 ✅ |

---

## 4. 边界

1. **需要 $\lvert q\rangle$ 存在**（[D01](D01-spectral-theorem.md) 的 Gelfand–Maurin）。
2. **对 $f$ 无需解析**，只需 Borel 可测（走路线一）；路线二连可测都不需要，只需"是 $\hat q$ 的函数"。
3. **不能反过来用**：核对角不意味着算子是 $\hat q$ 的函数（可能有相同核的不同算子？——在同一表象下不会，但换表象时要注意）。

---

## 5. 自检

- [ ] 用对易子论证写出核的形式，并说明为什么不需要 $f$ 解析
- [ ] 说明 $[\hat q,f(\hat q)]=0$ 与 $[\hat p,f(\hat q)]=-if'$ 为什么不矛盾
- [ ] 用它解释 $V(q)$ 与 $V(q')$ 何时可以互换
