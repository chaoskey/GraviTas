# D12 · 谱定理与 Gelfand–Maurin

> 建档 2026-11-06 · 类型：**引用卡**——陈述定理、说清用法与边界，**不复现证明**（证明属泛函分析，不在本仓库范围内）
> 上游：无（外部数学定理）
> 下游：[D01](D01-commutator-p-fq.md)、[D02](D02-translation.md)、[D08](D08-qp-overlap.md)、[D11](D11-functional-calculus.md)

---

## 0. 两张定理，各一句话

| 定理 | 一句话 |
|---|---|
| **谱定理** | 自伴算子 $\iff$ 一族投影（投影值测度），算子就是"按谱参数把这些投影积起来" |
| **Gelfand–Maurin** | 在核空间条件下，这族投影可以"对角化"成**广义本征矢**——代价是本征矢搬到 Hilbert 空间外面 |

**分工**：谱定理管"算子长什么样"，Gelfand–Maurin 管"能不能写出本征基"。前者给函数演算与完备性，后者给 $\lvert q\rangle$ 本身。

---

## 1. 谱定理

### 1.1 陈述

设 $\hat A$ 是 Hilbert 空间 $\mathcal{H}$ 上的自伴算子（可以无界）。则存在**唯一**的投影值测度 $E$（定义在 $\mathbb{R}$ 的 Borel 集上，支撑在谱 $\sigma(\hat A)$ 上），使

$$
\hat A=\int_{\sigma(\hat A)}\lambda\;dE(\lambda),
\qquad
D(\hat A)=\Bigl\{\psi\;\Big|\;\int\lambda^{2}\,d\langle\psi\lvert E(\lambda)\lvert\psi\rangle<\infty\Bigr\}
$$

对**有界** Borel 函数 $f$：

$$
f(\hat A)=\int f(\lambda)\;dE(\lambda),
\qquad
\lVert f(\hat A)\rVert=\sup_{\lambda\in\sigma(\hat A)}\lvert f(\lambda)\rvert
$$

### 1.2 它给什么（四条）

1. **函数演算**——[D11](D11-functional-calculus.md) §1.2 的全部依据；
2. **resolution of identity**——$\mathbb{1}=\int dE(\lambda)$，取 $f=1$ 即得（[D08](D08-qp-overlap.md) §1.5 的完备性）；
3. **谱的信息**——$\sigma(\hat A)$ 是 $E$ 的支撑；$E(\{\lambda\})\neq0$ 的点就是点谱；
4. **一个"对角化"模型**——谱简单时 $\hat A$ 酉等价于"在 $L^{2}(\mathbb{R},d\mu)$ 上乘以 $\lambda$"。**"让 $\hat q$ 对角"这句话的严格含义就是这个。**

### 1.3 它不给什么（三条，最要紧）

1. **连续谱时不给本征矢。** 对连续谱的每个单点，$E(\{q\})=0$，于是**不存在** $\psi\in\mathcal{H}$ 满足 $\hat A\psi=q\psi$。谱定理给的是"一族投影"，不是"一族向量"。
2. **不告诉你谱是什么。** 定理对**任何**自伴算子都成立，所以它对"$\hat q$ 的谱是 $\mathbb{R}$ 还是格点"一无所知。谱由你选的算子与边界条件决定。
3. **不固定归一化。** 广义本征矢的归一化系数是约定（[D02](D02-translation.md) 的相位、[D08](D08-qp-overlap.md) 的整体相位都是这一类）。

---

## 2. Gelfand–Maurin（核空间谱定理）

### 2.1 需要的结构：rigged Hilbert space

$$
\Phi\;\subset\;\mathcal{H}\;\subset\;\Phi^{\times}
$$

- $\Phi$：一个**核空间**（nuclear space），典型取 Schwartz 空间 $\mathcal{S}(\mathbb{R})$；
- $\mathcal{H}$：真正的 Hilbert 空间；
- $\Phi^{\times}$：$\Phi$ 上的连续线性泛函，即缓增分布。

两层嵌入都连续且稠密。"核"这个条件是关键：它保证谱测度能被"数出来"、本征矢系能被"积出来"。**一般 Fréchet 空间不够**——这条定理对 $\Phi$ 的选择是敏感的。

### 2.2 陈述

设 $\hat A$ 自伴，$\Phi$ 核空间、连续稠密嵌入，且 $\hat A\Phi\subset\Phi$（$\hat A$ 在 $\Phi$ 上连续）。则存在谱测度 $\mu$ 与一族广义本征矢 $F_\lambda\in\Phi^{\times}$，使

$$
\hat A F_\lambda=\lambda F_\lambda
$$

且这族**完备**：对任意 $\phi,\psi\in\Phi$，

$$
\langle\phi\lvert\psi\rangle=\int\langle\phi\lvert F_\lambda\rangle\,\langle F_\lambda\lvert\psi\rangle\;d\mu(\lambda)
$$

写成算子的样子：

$$
\mathbb{1}=\int\lvert F_\lambda\rangle\langle F_\lambda\rvert\;d\mu(\lambda)
$$

### 2.3 它给什么

- $\lvert q\rangle$ **本身**：$[\hat q,f(\hat q)]$ 与 $\hat q$ 的谱分解都能写出来，靠的就是它；
- $\delta$ 归一化 $\langle q\lvert q'\rangle=\delta(q-q')$ 的严格地位；
- 狄拉克记号的下限——$\langle q\lvert\psi\rangle=\psi(q)$ 是**求值泛函**，不是 $L^{2}$ 内积。

**具体画面**（这也是"为什么必须扩大空间"的最短说明）：取 $\hat q$ 为 $L^{2}(\mathbb{R})$ 上"乘以 $x$"。则 $\lvert q\rangle$ 就是求值泛函 $\psi\mapsto\psi(q)$。这个泛函在 $L^{2}$ 上**不连续**（函数可在一点很高而范数很小），但在 Schwartz 空间 $\mathcal{S}$ 上连续——所以它住在 $\mathcal{S}^{\times}$ 里，不在 $\mathcal{H}$ 里。

---

## 3. 在本网格里的位置

| 卡片 | 依赖哪一条 |
|---|---|
| [D11](D11-functional-calculus.md) | §1.2 的函数演算与谱映射定理 |
| [D01](D01-commutator-p-fq.md) | §2.2 的 $\lvert q\rangle$（"分布意义"的来源） |
| [D02](D02-translation.md) | §1.2 的"重数为 1"（谱定理术语）+ §2.2 的基 |
| [D08](D08-qp-overlap.md) | §1.5 的完备性 + §2.2 的 $\lvert q\rangle$ |

**这就是网格最底下的那层**。它之上的一切都用它，它自己则不被本仓库证明。

---

## 4. 一致性检验

| 检验 | 结果 |
|---|---|
| 乘法算子（$\hat q$ 乘 $x$） | 谱为 $\mathbb{R}$，$E(B)$ 为"乘以 $B$ 的特征函数"，广义本征矢为 $\delta(x-q)$（即求值泛函）✅ |
| 动量算子（$\hat p=-i\partial_q$） | 广义本征矢为 $e^{ipx}$，$\langle p\lvert p'\rangle=2\pi\delta(p-p')$，与 [D08](D08-qp-overlap.md) 一致 ✅ |
| 离散谱特例 | 有界区间上的算子给出 $\sum_n$ 而非 $\int$，$\delta$ 变 $\delta_{nm}$——与 [D02](D02-translation.md) §3 第 2 条一致 ✅ |
| 与 D11 自洽 | $\sigma(f(\hat A))=f(\sigma(\hat A))$ 是谱定理的直接推论（[D11](D11-functional-calculus.md) §2）✅ |

---

## 5. 边界

1. **非自伴算子全都没有。** 谱定理要求自伴；非自伴只有"谱"这个较弱的对象，没有 PVM，也没有广义本征矢系。这是整套量子力学要求可观测量自伴的**数学**理由，而不只是习惯。
2. **核性不可省。** 换成一般的稠密子空间，Gelfand–Maurin 可能失效。所以"随便找个稠密子空间就能定义 $\lvert q\rangle$"是错的。
3. **归一化依赖谱测度密度。** 若 $d\mu=\rho(q)\,dq$，则 $\langle q\lvert q'\rangle=\delta(q-q')/\rho(q)$。平直空间 $\rho=1$，弯曲空间 $\rho=\sqrt{g}$——**这是曲空间路径积分里测度因子的数学出处**。
4. **重数大于 1 时要加标签。** 本征矢写成 $F_{\lambda,i}$，完备性多一个 $\sum_i$，归一化变成 $\delta_{ij}$。物理上就是自旋、味道、超选扇区。
5. **这张卡不做证明。** 本仓库不重推泛函分析；能推的是"给定这些定理，物理结论如何落地"。**引用与证明的界限要一直守住**——[D08](D08-qp-overlap.md) §3 已经因此错过一次（把引用当证明）。

---

## 6. 自检

- [ ] 用一句话说清谱定理与 Gelfand–Maurin 各负责什么
- [ ] 解释为什么连续谱时"Hilbert 空间里没有本征矢"
- [ ] 用"求值泛函"说明 $\lvert q\rangle$ 为什么不在 $\mathcal{H}$ 里
- [ ] 说明核空间条件为什么不可省
- [ ] 指出 $\langle q\lvert q'\rangle=\delta(q-q')$ 里的"$\delta$ 系数"由什么决定
- [ ] 举一个本网格里"引用谱定理"而非"证明"的具体位置
