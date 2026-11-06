# D01 · 对易子 $[\hat p,f(\hat q)]=-i f'(\hat q)$

> 建档 2026-11-06 · 上游：公理 $[\hat q,\hat p]=i$；**旁证**（另证与备注）用 [D12](D12-spectral-theorem.md)；默认 [D11](D11-functional-calculus.md)
> 下游：无卡片把它列为上游；用于 [N004 §6.3](../notes/N004-hadamard-lemma.md) 的等比求和（不幂零但可求和）
> 网格登记见 [derivations/README](README.md)

---

## 0. 命题

$$
[\hat q,\hat p]=i
\quad\Longrightarrow\quad
\boxed{\;[\hat p,f(\hat q)]=-i\,f'(\hat q)\;}
$$

**适用条件**：

1. $f$ 在 $0$ 的邻域内解析（或 $f$ 是多项式），于是 $f(\hat q)$ 有幂级数定义；
2. 等式在"两边都有意义"的向量上成立——$\hat p$ 与 $f(\hat q)$ 无界时，指公共的稠密定义域；
3. 符号依赖本仓库约定 $[\hat q,\hat p]=i$、$\hat p=-i\partial_q$。若改约定，右侧差一个负号（见 §4）。

**它在讲什么**：$\hat p$ 与任何"只是 $\hat q$ 的函数"都不对易，但对易的结果**不再是微分算子，而是一个乘法算子**——乘以 $-if'$。这个"降格"是后面一切展开能算出来的原因。

---

## 1. 证明（归纳 + 幂级数延拓）

### 1.1 先对幂证明

**断言**：

$$
[\hat p,\hat q^{n}]=-in\,\hat q^{n-1},
\qquad n=1,2,\dots
$$

**基情形 $n=1$**：

$$
[\hat p,\hat q]=-[\hat q,\hat p]=-i
$$

**归纳步**：设 $n$ 时成立，则用对易子的 Leibniz 性质 $[A,BC]=[A,B]C+B[A,C]$：

$$
\begin{aligned}
[\hat p,\hat q^{n+1}]
&=[\hat p,\hat q^{n}\hat q]\\
&=[\hat p,\hat q^{n}]\,\hat q+\hat q^{n}\,[\hat p,\hat q]\\
&=-in\,\hat q^{n-1}\hat q+\hat q^{n}(-i)\\
&=-i(n+1)\,\hat q^{n}
\end{aligned}
$$

故对一切 $n\ge1$ 成立。

### 1.2 延拓到幂级数

设

$$
f(\hat q)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}\,\hat q^{n}
$$

**注意 $n=0$ 项为零**：$[\hat p,\mathbb{1}]=0$，所以求和可以改写为从 $n=1$ 开始：

$$
\begin{aligned}
[\hat p,f(\hat q)]
&=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}\,[\hat p,\hat q^{n}]\\
&=\sum_{n=1}^{\infty}\frac{f^{(n)}(0)}{n!}\,[\hat p,\hat q^{n}]\\
&=-i\sum_{n=1}^{\infty}\frac{f^{(n)}(0)}{n!}\,n\,\hat q^{n-1}
\end{aligned}
$$

此时用 $\dfrac{d}{d\hat q}\hat q^{n}=n\hat q^{n-1}$（对多项式的**形式导数**，见 §4 第 3 条）：

$$
\begin{aligned}
[\hat p,f(\hat q)]
&=-i\,\frac{d}{d\hat q}\sum_{n=1}^{\infty}\frac{f^{(n)}(0)}{n!}\,\hat q^{n}\\
&=-i\,\frac{d}{d\hat q}\,f(\hat q)
=-i\,f'(\hat q)
\end{aligned}
$$

末步把求和起点从 $n=1$ 写回 $n=0$：两者的差别只是一个常数项，求导后为零。

**证毕。**

---

## 2. 另证

### 2.1 表象法（两行）

在 $q$ 表象中，$\hat p=-i\partial_q$，$\hat q$ 是乘 $q$。取任意可微 $\psi$：

$$
\begin{aligned}
[\hat p,f(\hat q)]\psi
&=-i\frac{d}{dq}\bigl(f\psi\bigr)-f\Bigl(-i\frac{d}{dq}\psi\Bigr)\\
&=-i\bigl(f'\psi+f\psi'\bigr)+if\psi'=-i f'\psi
\end{aligned}
$$

第二项用乘积法则，再与 $+if\psi'$ 相消。

### 2.2 平移法（三行）

由 [D02](D02-translation.md)（平移公式）与 [D03](D03-hadamard-lemma.md)（Hadamard 引理）：

$$
e^{ia\hat p}\,\hat q\,e^{-ia\hat p}=\hat q+a
\quad\Longrightarrow\quad
e^{ia\hat p}f(\hat q)e^{-ia\hat p}=f(\hat q+a)
$$

两边对 $a$ 求导、取 $a=0$：左边得 $i[\hat p,f(\hat q)]$，右边得 $f'(\hat q)$。故 $[\hat p,f]=-if'$。

**这条路线的价值**：它说明该公式的物理内容——$\hat p$ 是 $q$ 方向平移的生成元，**$[\hat p,\cdot]$ 就是"沿 $q$ 平移"这个导子**。用 [N004](../notes/N004-hadamard-lemma.md) 的记号：

$$
\mathrm{ad}_{\hat p}=-i\,\partial_q
\qquad(\text{作用在 }\hat q\text{ 的函数上})
$$

---

## 3. 一致性检验

| 检验 | 左 | 右 | 结果 |
|---|---|---|---|
| $f=1$ | $[\hat p,\mathbb{1}]=0$ | $-i\cdot0=0$ | ✓ |
| $f=\hat q$ | $[\hat p,\hat q]=-i$ | $-i$ | ✓ |
| $f=\hat q^{2}$ | $[\hat p,\hat q]\hat q+\hat q[\hat p,\hat q]=-2i\hat q$ | $-i(2\hat q)$ | ✓ |
| $f=e^{i\lambda\hat q}$ | $\lambda e^{i\lambda\hat q}$（由公式） | $-i\cdot i\lambda e^{i\lambda\hat q}$ | ✓ |
| 取 $\lambda=1$ | $[\hat p,e^{i\hat q}]=e^{i\hat q}$ | 与 [N004 §6.3](../notes/N004-hadamard-lemma.md) 一致 | ✓ |
| 镜像命题 | $[\hat q,g(\hat p)]=ig'(\hat p)$ | 由 $[\hat q,\hat p]=i$ 同法可证，符号相反 | ✓ |

**镜像那一行值得记住**：交换 $\hat q$ 与 $\hat p$，正负号也跟着换。写错符号是这条公式最常见的错误。

---

## 4. 备注与边界

1. **$f$ 的条件不能省。** 右侧出现 $f'$，所以 $f$ 至少要可微。对不可微的 $f$（例如阶跃 $\theta(q)$），$f'=\delta$，等式仍成立，但要在分布意义下读，且 $f(\hat q)$ 的幂级数定义随之失效，需改用谱分解定义 $f(\hat q)$（见 [D11](D11-functional-calculus.md)）。
2. **无穷求和的交换是形式的。** 对多项式，求和是有限的，一步不多；对解析函数，交换 $[\hat p,\cdot]$ 与 $\sum$ 需要收敛性，严格做法是先对部分和证明、再取极限（或只在解析向量上操作）。
3. **$\dfrac{d}{d\hat q}$ 是形式导数。** 它不是"对算子求导"这种可疑操作，而是"对多项式逐项降次"的简写。等价写法是换元：

$$
\sum_{n=1}^{\infty}\frac{f^{(n)}(0)}{n!}n\hat q^{n-1}
=\sum_{m=0}^{\infty}\frac{f^{(m+1)}(0)}{m!}\hat q^{m}
=f'(\hat q)
$$

两条路给出同一个结果，后者不涉及任何"对算子求导"的说法。
4. **符号约定的影响。** 本页用 $[\hat q,\hat p]=i$。若某文献取 $[\hat q,\hat p]=-i$（等价于 $\hat p=+i\partial_q$），则同一命题写成 $[\hat p,f]=+if'$。**判据**：看 $e^{ia\hat p}$ 把 $\lvert q\rangle$ 移到 $q+a$ 还是 $q-a$（见 [D02](D02-translation.md)）。
5. **无界算子。** $\hat p$ 与 $f(\hat q)$ 都无界，等式不是"处处成立"，而是"在共同的稠密定义域上成立"。物理推导里通常默认这一点；写严格论证时要交代。

---

## 5. 自检

- [ ] 不看本文，用归纳写出 $[\hat p,\hat q^{n}]$，并说明 Leibniz 那一步用了什么
- [ ] 说明为什么 $n=0$ 项为零，以及为什么求和起点可以从 $n=1$ 改回 $n=0$
- [ ] 用换元 $m=n-1$ 验证 $\sum\frac{f^{(n)}(0)}{n!}n\hat q^{n-1}=f'(\hat q)$
- [ ] 给出 $f=\hat q^{2}$ 与 $f=e^{i\lambda\hat q}$ 两个特例的具体结果
- [ ] 说清符号约定如何决定右侧是 $-if'$ 还是 $+if'$
- [ ] 用平移法（§2.2）重推一遍，并指出它用到哪两条上游
