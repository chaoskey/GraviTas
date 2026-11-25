# D04 · 位置算子与位置表象

> 建档 2026-11-07 · 类型：推导卡（含**一次尺度选择**）
> 上游：[D00](D00-commutator-axiom.md)（接口约定、自伴）、[D01](D01-spectral-theorem.md)（谱定理、函数演算）、[D02](D02-gelfand-maurin.md)（广义本征矢、$E(B)$ 的密度）、[D03](D03-born-rule.md)（Born 规则、期望值定理）
> 下游：[D05](D05-functional-calculus-and-kernel.md)、[D06](D06-trace.md)、[D14](D14-translation.md)、[D15](D15-qp-overlap.md)、[D16](D16-p-completeness.md)
> 本卡把通用框架**第一次特化到具体算子 $\hat q$**：读出位置基"四件套"，并明确其中**哪一步是定理特化、哪一步是尺度选择**。

---

## 0. 命题：位置基的"四件套"

$$
\begin{gathered}
\hat q\,\lvert q\rangle=q\,\lvert q\rangle,
\qquad
\mathbb{1}=\int_{\mathbb{R}}\lvert q\rangle\langle q\rvert\;dq,\\
\hat q=\int_{\mathbb{R}}q\,\lvert q\rangle\langle q\rvert\;dq,
\qquad
\langle q\lvert q'\rangle=\delta(q-q')
\end{gathered}\tag{1}
$$

**四句话**：$\lvert q\rangle$ 是广义本征矢；所有 $\lvert q\rangle$ 拼回恒等算子（完备性）；外积按 $q$ 加权积分重构出 $\hat q$（谱分解）；连续谱下的广义本征态满足 $\delta$ 归一。

**它们的逻辑地位完全不同**：

| 公式或性质 | 地位 | 落实 |
|---|---|---|
| $\lvert q\rangle\in\Phi^{\times}$ 的存在性与 $\hat q\lvert q\rangle=q\lvert q\rangle$ | **定理**（直接特化） | §1 |
| 谱测度微元的形式 $dE(q)=\lvert q\rangle\langle q\rvert\,d\mu(q)$ | **定理**（直接特化） | §1 |
| 取标量谱测度为 $d\mu(q)=dq$ | **选择 / 约定**（固定 $\lvert q\rangle$ 尺度） | §2 |
| $\hat q=\int q\lvert q\rangle\langle q\rvert dq$ 与 $\mathbb{1}=\int\lvert q\rangle\langle q\rvert dq$ | **定理**（代入推论） | §3 |
| $\langle q\lvert q'\rangle=\delta(q-q')$ | **定理**（代入推论） | §4 |

**本卡只做"取 $\hat A=\hat q$ 并选定 $d\mu(q)=dq$"这一件事**，把定理给的部分与人为选的部分彻底剥离。

---

## 1. 第一步：Gelfand–Maurin 直接给出本征方程与带 $d\mu$ 的完备性

由 [D00](D00-commutator-axiom.md) §1，一维单粒子的位置可观测量对应自伴算子 $\hat q$，其谱是整条实轴（连续谱），且**谱无简并**（重数指标 $k=1$）。

调用 [D02](D02-gelfand-maurin.md) §2–§3（核空间取 $\Phi=\mathcal{S}(\mathbb{R})$）：对自伴 $\hat A$，存在标量谱测度 $\mu$ 与广义本征矢 $\lvert\lambda\rangle\in\Phi^{\times}$，使

$$
\hat A\lvert\lambda\rangle=\lambda\lvert\lambda\rangle,
\qquad
\mathbb{1}=\int_{\sigma(\hat A)}\lvert\lambda\rangle\langle\lambda\rvert\;d\mu(\lambda),
\qquad
dE(\lambda)=\lvert\lambda\rangle\langle\lambda\rvert\;d\mu(\lambda)\tag{2}
$$

（第三式是 [D02](D02-gelfand-maurin.md) §4 的（10）。）做一次符号特化——$\hat A=\hat q$、$\lambda=q$、$\lvert\lambda\rangle=\lvert q\rangle$：

$$
\hat q\lvert q\rangle=q\lvert q\rangle,
\qquad
\mathbb{1}=\int_{\mathbb{R}}\lvert q\rangle\langle q\rvert\;d\mu(q),
\qquad
dE(q)=\lvert q\rangle\langle q\rvert\;d\mu(q)\tag{3}
$$

**这一步的分量**：

1. **本征方程只有一行**——它不是解微分方程得到的（此时还没有定义位置表象下的微分算子），而是 [D02](D02-gelfand-maurin.md) 的直接特化。$\lvert q\rangle$ 存在性的全部合法性都在这里。
2. **两个积分等式是弱等式**：与 [D02](D02-gelfand-maurin.md) §3 的（5）、§4 的（9）（10）一样，只有夹在测试探针 $\langle\phi\lvert\,\cdot\,\lvert\psi\rangle$（$\phi,\psi\in\Phi$）之间才是数。后面照物理惯例当算子等式书写，底层依据是这一条。

---

## 2. 第二步：选定 $d\mu(q)=dq$（本卡唯一的选择）

[D02](D02-gelfand-maurin.md) 只保证"存在标量谱测度"，**没有强迫它等于 Lebesgue**。因为（3）里有一个**尺度自由度**：$dE(q)$ 由 $\hat q$ 唯一决定（[D01](D01-spectral-theorem.md) §0），对任意 $\rho(q)>0$ 同时做

$$
d\mu(q)\;\longrightarrow\;d\tilde\mu(q)=\rho(q)\,d\mu(q),
\qquad
\lvert q\rangle\;\longrightarrow\;\lvert\tilde q\rangle=\frac{1}{\sqrt{\rho(q)}}\lvert q\rangle\tag{4}
$$

则

$$
\lvert\tilde q\rangle\langle\tilde q\rvert\;d\tilde\mu(q)
=\frac{1}{\rho(q)}\lvert q\rangle\langle q\rvert\cdot\rho(q)\,d\mu(q)
=\lvert q\rangle\langle q\rvert\;d\mu(q)=dE(q)\tag{5}
$$

本征方程 $\hat q\lvert\tilde q\rangle=q\lvert\tilde q\rangle$ 也照旧。**所以"测度取什么权重"与"本征矢取什么尺度"是同一件事。**

**本卡的唯一约定**：把标量谱测度缩放到标准 Lebesgue（$\rho(q)\,d\mu(q)=dq$），于是

$$
d\tilde\mu(q)=dq,
\qquad
dE(q)=\lvert\tilde q\rangle\langle\tilde q\rvert\;dq,
\qquad
E(B)=\int_B\lvert\tilde q\rangle\langle\tilde q\rvert\;dq
$$

再由 [D03](D03-born-rule.md) §2 的"态是射线"，$\lvert\tilde q\rangle$ 与 $\lvert q\rangle$ 只差一个比例系数、代表同一个态，故可写回：

$$
dE(q)=\lvert q\rangle\langle q\rvert\,dq,
\qquad
E(B)=\int_B\lvert q\rangle\langle q\rvert\,dq\tag{6}
$$

**必须分清**：（6）里"外积密度的**形状** $\lvert q\rangle\langle q\rvert$"来自 [D02](D02-gelfand-maurin.md) 的定理，是**推出来的**；"测度因子取不带权重的 $dq$"是**本卡的选择**。一旦选定，$\lvert q\rangle$ 的模长尺度被锁死，只剩相位 $e^{i\theta(q)}$。

---

## 3. 第三步：谱分解与完备性

[D01](D01-spectral-theorem.md) §0 给

$$
\hat q=\int_{\mathbb{R}}q\;dE(q)\tag{7}
$$

把（6）的 $dE(q)=\lvert q\rangle\langle q\rvert dq$ **代入**右端的 $dE(q)$：

$$
\hat q=\int_{\mathbb{R}}q\,\lvert q\rangle\langle q\rvert\;dq\tag{8}
$$

**是"代入"，不是"对照"**：谱定理说 $dE$ 在积分号的什么位置，§1–§2 说 $dE$ 长什么样。

同法把 $dE(q)=\lvert q\rangle\langle q\rvert dq$ 代进 [D01](D01-spectral-theorem.md) §1 的函数演算 $f(\hat q)=\int f(q)\,dE(q)$：

$$
f(\hat q)=\int_{\mathbb{R}}f(q)\,\lvert q\rangle\langle q\rvert\;dq\tag{9}
$$

再由 [D01](D01-spectral-theorem.md) §0 的 $\int dE(q)=E(\mathbb{R})=\mathbb{1}$ 与（6），得位置基的**完备性**：

$$
\mathbb{1}=\int_{\mathbb{R}}\lvert q\rangle\langle q\rvert\;dq\tag{10}
$$

（10）与（3）的 $\mathbb{1}=\int\lvert q\rangle\langle q\rvert d\mu(q)$、与（6）的 $E(\mathbb{R})=\int\lvert q\rangle\langle q\rvert dq$ 是**同一选择下的不同写法**，不互相证明。【证毕】

---

## 4. 第四步：广义正交归一性 $\langle q\lvert q'\rangle=\delta(q-q')$

$\mathcal{H}$ 里没有有限范数的 $\lvert q\rangle$（$E(\{q\})=\mathbb{0}$），所以 $\langle q\lvert q'\rangle$ 不是内积——它是**分布**，含义由对偶配对给出：对任意 $\phi\in\Phi$，

$$
\phi(q')\equiv\langle q'\lvert\phi\rangle
=\int_{\mathbb{R}}\langle q'\lvert q\rangle\,\phi(q)\;dq
$$

右边是把（10）当作**恒等算子在 $q$ 表象下的核**来读：$\langle q'\lvert q\rangle$ 就是那个核 $K_{\mathbb{1}}(q',q)$。它与 $\delta$ 的定义式

$$
\phi(q')=\int_{\mathbb{R}}\phi(q)\,\delta(q'-q)\;dq
$$

对**所有** $\phi$ 逐一相同，而分布由它的全部配对唯一确定，故

$$
\langle q\lvert q'\rangle=K_{\mathbb{1}}(q',q)=\delta(q-q')\tag{11}
$$

**两条要看清**：

1. **它不是 $\mathcal{H}$ 的内积**——$\lvert q\rangle\notin\mathcal{H}$，这是对偶配对下的 $\delta$ 分布。
2. **它不是新公理**——选定 $d\mu(q)=dq$ 之后，它就是（10）在对偶意义下的表现；换一个权重 $\rho$，它就变成 $\delta(q-q')/\rho(q)$。

---

## 5. 第五步：位置表象的四大基本公式

由（10）（6）（8）代进 [D03](D03-born-rule.md) 的框架。

**波函数**：对归一化纯态 $\lvert\psi\rangle\in\Phi$，定义

$$
\psi(q)\equiv\langle q\lvert\psi\rangle,
\qquad
\overline{\psi(q)}=\langle\psi\lvert q\rangle\tag{12}
$$

（由 [D02](D02-gelfand-maurin.md) §1、§3，$\langle q\lvert\psi\rangle$ 是广义本征矢作为共轭线性泛函在 $\psi$ 上的**取值**，不是 $L^{2}$ 内积。）

1. **展开与 Parseval**：把（10）插进 $\langle\phi\lvert\psi\rangle$（即 [D02](D02-gelfand-maurin.md) §3 的（4\*）取 $d\mu=dq$）：
   $$
   \lvert\psi\rangle=\int_{\mathbb{R}}\psi(q)\,\lvert q\rangle\;dq,
   \qquad
   \langle\phi\lvert\psi\rangle=\int_{\mathbb{R}}\overline{\phi(q)}\,\psi(q)\;dq\tag{13}
   $$
   取 $\phi=\psi$ 并用 [D03](D03-born-rule.md) §2.2 的归一化，得平方可积条件：
   $$
   \int_{\mathbb{R}}\lvert\psi(q)\rvert^{2}\;dq=1\tag{14}
   $$

2. **乘法作用**：由 $\hat q$ 自伴给出左矢本征方程 $\langle q\lvert\hat q=q\langle q\lvert$，故
   $$
   (\hat q\psi)(q)\equiv\langle q\lvert\hat q\lvert\psi\rangle=q\langle q\lvert\psi\rangle=q\,\psi(q)\tag{15}
   $$
   这就是 [D01](D01-spectral-theorem.md) §5 对角化定理在 $\hat q$ 上的样子：**本征基下它就是"乘以 $q$"**。

3. **区间概率与概率密度**：把（6）的 $E(B)=\int_B\lvert q\rangle\langle q\rvert dq$ 代进 [D03](D03-born-rule.md) §1 的 Born 规则（即其 §5 的（20）–（22））：
   $$
   p(B)=\int_B\lvert\langle q\lvert\psi\rangle\rvert^{2}\,dq=\int_B\lvert\psi(q)\rvert^{2}\,dq,
   \qquad
   \rho(q)\equiv\frac{dp(q)}{dq}=\lvert\psi(q)\rvert^{2}\tag{16}
   $$

4. **期望值**：把（8）（9）代进 [D03](D03-born-rule.md) §3：
   $$
   \langle\hat q\rangle=\int_{\mathbb{R}}q\,\lvert\psi(q)\rvert^{2}\,dq,
   \qquad
   \langle f(\hat q)\rangle=\int_{\mathbb{R}}f(q)\,\lvert\psi(q)\rvert^{2}\,dq\tag{17}
   $$

---

## 6. 总结：从抽象广义本征态到位置表象

本卡把前四张卡建立的通用框架**第一次特化到具体算子 $\hat q$**，确立位置基与位置表象。

1. **一步定理特化（§1）**：取 $\hat A=\hat q$，不借任何微分方程，一行读出 $\hat q\lvert q\rangle=q\lvert q\rangle$、带抽象谱测度的弱完备性 $\mathbb{1}=\int\lvert q\rangle\langle q\rvert d\mu(q)$ 与算子值测度微元 $dE(q)=\lvert q\rangle\langle q\rvert d\mu(q)$。
2. **一次尺度选择（§2～§4）**：指明"测度权重与本征矢模长"的同步缩放自由度，据此选定 $d\mu(q)=dq$，代入 [D01](D01-spectral-theorem.md) 锁定谱分解 $\hat q=\int q\lvert q\rangle\langle q\rvert dq$、完备性 $\mathbb{1}=\int\lvert q\rangle\langle q\rvert dq$ 与 $\delta$ 归一 $\langle q\lvert q'\rangle=\delta(q-q')$。
3. **一套位置表象（§5）**：把完备性与谱分解代进 [D03](D03-born-rule.md) 的 Born 规则与期望值定理，得波函数 $\psi(q)=\langle q\lvert\psi\rangle$、Parseval 内积、坐标乘法作用 $(\hat q\psi)(q)=q\psi(q)$、概率密度 $\rho(q)=\lvert\psi(q)\rvert^{2}$。

**一句话**：位置基不是"假设出来的"，是"特化 + 一次选尺度"得到的；$\delta$ 不是公理，是那次选择的对偶表现。

---

## 7. 边界

1. **"无简并"是写成单矢外积的前提。** 一维无自旋粒子的位置本征值重数为 $1$；三维或带自旋时重数 $>1$，$dE$ 的密度要写成 [D02](D02-gelfand-maurin.md) 的 $\sum_k\lvert q,k\rangle\langle q,k\rvert$。
2. **"连续谱、绝对连续"是写成 $dq$ 积分的前提。** 纯点谱（如晶格、谐振子）时积分退成求和，$\delta(q-q')$ 退成 $\delta_{nn'}$。
3. **弯曲空间 $d\mu(q)$ 不必取 $dq$。** 平直空间才用 Lebesgue；黎曼流形上自然的体积测度带 $\sqrt{g}$，此时若仍按该测度完备展开，$\lvert q\rangle$ 的尺度与 $\delta$ 归一都要带 $\sqrt{g}$ 因子。
4. **不能倒果为因。** $\lvert q\rangle\in\Phi^{\times}$ 是站在 [D02](D02-gelfand-maurin.md) 肩上的对象；方向只能是 D01+D02 → 本卡，不能用 $\lvert q\rangle$ 的形式演算去"证明"谱定理。
5. **本卡只定了测度权重（$w=1$），$\delta$ 是它的对偶表现。** 换一个 $\rho$，$\delta$ 就变成 $\delta/\rho$——所以（11）不是独立公理。
6. **本卡不展开 $f(\hat q)$ 的一般理论。** （9）只是一次代入；$f(\hat A)$ 的两种定义、一致性、谱映射与范数公式属下游。

---

## 8. 自检

- [ ] 说出"四件套"里哪一条是定理特化、哪一条是尺度选择、哪两条是代入推论
- [ ] 说明本征方程为什么"只有一行"，$\lvert q\rangle$ 的存在性来自哪条定理
- [ ] 用 $\rho(q)$ 写出测度与本征矢的同步缩放，并说明为什么 $dE$ 不变
- [ ] 说明 $\hat q=\int q\lvert q\rangle\langle q\rvert dq$ 是"代入"而不是"对照"
- [ ] 说明 $\langle q\lvert q'\rangle=\delta$ 为什么不是内积、为什么不需要另立公理
- [ ] 从（10）（6）（8）导出区间概率（16），并说明连续谱为什么单点概率为零
