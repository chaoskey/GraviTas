# D26 · 能量表象与能级展开：$Z=\sum_n e^{-\beta E_n}$

> 建档 2026-11-08 · 上游：[D05](D05-functional-calculus.md)（函数演算）、[D06](D06-trace.md)（迹）、[D20](D20-hamiltonian.md)（$\hat H$）、[D23](D23-density-matrix.md)（配分函数）
> 下游：无卡片依赖
> 本卡把 $Z$ 从"路径积分/迹的形式写法"变成"**可以逐级计算的数**"。

---

## 0. 命题

设 $\hat H$ 的谱是**离散**的，本征矢与本征值为

$$
\hat H\lvert n\rangle=E_n\lvert n\rangle,
\qquad
\mathbb{1}=\sum_n\lvert n\rangle\langle n\rvert
$$

则**能量表象**（以 $\lvert n\rangle$ 为基）下：

$$
e^{-\beta\hat H}=\sum_n e^{-\beta E_n}\lvert n\rangle\langle n\rvert,
\qquad
\boxed{\;Z=\mathrm{Tr}\,e^{-\beta\hat H}=\sum_n e^{-\beta E_n}\;}
$$

热核（传播子在虚时间）的核：

$$
K(q_f,q_i;\beta)=\langle q_f\lvert e^{-\beta\hat H}\lvert q_i\rangle
=\sum_n e^{-\beta E_n}\,\psi_n(q_f)\,\psi_n^{*}(q_i)
$$

其中 $\psi_n(q)=\langle q\lvert n\rangle$。

---

## 1. 证明（两步，都是已有卡片）

**第一步：函数演算给出 $e^{-\beta\hat H}$ 的谱分解。**

由 [D05](D05-functional-calculus.md) §1.3（本征基展开），对离散谱：

$$
f(\hat H)=\sum_n f(E_n)\lvert n\rangle\langle n\rvert
$$

取 $f(\lambda)=e^{-\beta\lambda}$ 即得。

**第二步：迹就是对角元之和。**

由 [D06](D06-trace.md) §0，$\mathrm{Tr}=\sum_n\langle n\lvert\cdot\lvert n\rangle$，故

$$
\mathrm{Tr}\,e^{-\beta\hat H}
=\sum_n\langle n\lvert\Bigl(\sum_m e^{-\beta E_m}\lvert m\rangle\langle m\rvert\Bigr)\lvert n\rangle
=\sum_n e^{-\beta E_n}
$$

**核的形式**同理：插一次完备性 $\mathbb{1}=\sum_n\lvert n\rangle\langle n\rvert$。

**证毕。**

---

## 2. 三条直接后果

**① 低温：基态主导。** $\beta\to\infty$ 时

$$
Z\simeq e^{-\beta E_0}\Bigl(1+g_1e^{-\beta(E_1-E_0)}+\cdots\Bigr)
\quad\Longrightarrow\quad
F=-\frac{1}{\beta}\ln Z\;\to\;E_0
$$

**② 高温：所有能级等权。** $\beta\to0$ 时 $Z\to\sum_n 1$，即态空间维数——量子结构被"压平"。

**③ 热力学量变成能级的求和。** 由 [D23](D23-density-matrix.md) §3：

$$
E=\frac{\sum_n E_n e^{-\beta E_n}}{\sum_n e^{-\beta E_n}},
\qquad
S=\ln Z+\beta E
$$

**这就是"配分函数是母函数"的实际含义**：只要知道能谱 $\{E_n\}$，热力学全有。

---

## 3. 与路径积分的等价（闭合那一环）

[D22](D22-trace-is-loop.md) 说迹可以写成闭合路径积分：

$$
Z=\oint_{q(0)=q(\beta)}\mathcal{D}q\;e^{-S_E[q]}
$$

本卡说迹等于能级求和：

$$
Z=\sum_n e^{-\beta E_n}
$$

**两者是同一个数**，两种算法：

| 算法 | 输入 | 适用 |
|---|---|---|
| 能级求和 | 解出 $\{E_n\}$ | 可积系统、束缚态 |
| 路径积分 | 作用量 $S_E$ | 非微扰、半经典、场论推广 |

**这就是路径积分"合法"的最终检验**：凡能解出能谱的系统，两条路必须给同一个 $Z$。

---

## 4. 边界

1. **离散谱是前提。** 连续谱时要加积分：$Z=\int dE\,\rho(E)e^{-\beta E}$，$\rho(E)$ 是态密度。
2. **简并要加重数。** 若 $E_n$ 有 $g_n$ 重简并，$Z=\sum_n g_n e^{-\beta E_n}$。
3. **能谱本身是物理输入。** 解 $\hat H\psi=E\psi$ 属于具体系统问题（谐振子、氢原子……），不在本网格内。
4. **它不是"新的物理"**：只是 [D05](D05-functional-calculus.md) 与 [D06](D06-trace.md) 取同一条谱分解的两种读法。

---

## 5. 自检

- [ ] 用函数演算写出 $e^{-\beta\hat H}$ 的谱分解，再取迹
- [ ] 写出带简并的 $Z=\sum_n g_n e^{-\beta E_n}$，并说明 $g_n$ 从哪来
- [ ] 说清低温/高温两个极限各由什么主导
- [ ] 说明为什么能级求和与路径积分必须给同一个 $Z$
- [ ] 指出本卡哪一步是物理输入（不是推导）
