# D06 · 指数映射与 BCH 三条闭式

> 建档 2026-11-26 · 类型：**定义 + 定理**——四组命题共用一套符号：单参数指数族 $e^{tA}$、伴随作用 $\mathrm{ad}_A$、中心对易子 $c\mathbb{1}$
> 上游：[D05](D05-functional-calculus-and-kernel.md)（§1.1 幂级数定义、§1.2 同态乘法律、§2.1 同源函数对易律、§2.3 酉判据）
> 下游：[D09](D09-weyl-phase.md)、[D11](D11-translation.md)、[D12](D12-qp-overlap.md)

---

## 0. 命题

本卡把四组彼此咬合的结论放在一处：**指数映射**给出"算子幂级数的微积分"，**伴随作用**把共轭转成线性方程，**两项截断**把无穷级数砍成两项，**BCH 三条闭式**在中心对易子下把指数乘积化成单个指数。

| 组 | 内容 | 逻辑地位 | 节 |
|---|---|---|---|
| 甲 | 单参数指数族 $e^{tA}$ 的四条运算律（群律与逆、与生成元对易、求导、含时链式前提） | **定义 + 推论** | §1.1 |
| 甲 | 共轭 $e^{A}(\cdot)e^{-A}$ 是代数自同构；算子函数穿透律 $e^{A}f(B)e^{-A}=f(e^{A}Be^{-A})$ | **定理** | §1.2 |
| 乙 | 伴随作用 $\mathrm{ad}_A X\equiv[A,X]$ 的线性、Leibniz、Jacobi 三条性质 | **定义 + 推论** | §2.1 |
| 乙 | Hadamard 引理 $e^{A}Be^{-A}=e^{\mathrm{ad}_A}B=\sum_{n}\frac{1}{n!}\mathrm{ad}_A^{\,n}B$ | **定理** | §2.2 |
| 丙 | $[A,B]=c\mathbb{1}$ 时两项截断 $e^{A}Be^{-A}=B+c\mathbb{1}$ | **定理** | §3.2 |
| 丁 | 交换相位 $e^{A}e^{B}=e^{c}e^{B}e^{A}$（只定比值） | **定理** | §4.1 |
| 丁 | BCH 三条闭式 $e^{A}e^{B}=e^{c/2}e^{A+B}$、$e^{B}e^{A}=e^{-c/2}e^{A+B}$、$e^{A/2}e^{B}e^{A/2}=e^{A+B}$ | **定理** | §5.1 |

**它在讲什么**：上一条对易关系（[D00](D00-commutator-axiom.md)）只告诉你 $\hat q,\hat p$ 不对易；本卡告诉你**不对易在指数上留下的全部代价**——共轭要给出一串嵌套对易子，而一旦这个对易子是**中心元素**（数），代价就塌缩成一个标量因子 $e^{c}$，甚至精确分给两半。

**适用条件**（全卡通用）：

1. $e^{\pm A}$、$e^{\pm B}$ 有定义——$A,B$ 有界时处处成立；无界时在公共解析向量子空间上成立（幂级数定义见 [D05](D05-functional-calculus-and-kernel.md) §1.1）；
2. 所出现的级数在收敛域内，或按解析向量上的强收敛理解；
3. 丙、丁两组额外要求 $[A,B]=c\mathbb{1}$，其中 $c\in\mathbb{C}$ 是**数**（与一切算子对易）；这一条缺一不可，见 §7 第 2 条。

**四条红线**（本卡最容易被含糊带过的地方）：这是**精确恒等式**不是微扰近似；系数是 $\frac{1}{n!}$ 不是组合数；截断由**幂零**决定与 $c$ 的大小无关；交换相位**只定比值**、定不出 $c/2$。

---

## 1. 单参数指数族与共轭穿透律

### 1.1 四条运算律

指数函数 $\exp(t\lambda)=\sum_{n}\frac{t^{n}}{n!}\lambda^{n}$ 是整函数，其幂级数定义与谱积分定义在 [D05](D05-functional-calculus-and-kernel.md) §1.2 已证相等，故

$$
e^{tA}\equiv\sum_{n=0}^{\infty}\frac{t^{n}}{n!}\,A^{n}=\int_{\sigma(A)}e^{t\lambda}\;dE(\lambda)\tag{1}
$$

取 [D05](D05-functional-calculus-and-kernel.md) §1.2 的同态乘法律与 §2.1 的同源对易律，立刻读出四条：

$$
e^{tA}e^{sA}=e^{(t+s)A},
\qquad
e^{0\cdot A}=\mathbb{1},
\qquad
\bigl(e^{tA}\bigr)^{-1}=e^{-tA}\tag{2}
$$

$$
\bigl[A,\,e^{tA}\bigr]=\mathbb{0}
\quad\Longleftrightarrow\quad
A\,e^{tA}=e^{tA}\,A\tag{3}
$$

$$
\frac{d}{dt}\,e^{tA}=\sum_{n=1}^{\infty}\frac{t^{n-1}}{(n-1)!}\,A^{n}=A\,e^{tA}=e^{tA}\,A\tag{4}
$$

$$
\bigl[f(t),\,\dot f(t)\bigr]=\mathbb{0}
\quad\Longrightarrow\quad
\frac{d}{dt}\,e^{f(t)}=\dot f(t)\,e^{f(t)}=e^{f(t)}\,\dot f(t)\tag{5}
$$

**关于 (5)**：对第 $n$ 项 $f^{n}$ 求导得 $\dot f f^{n-1}+f\dot f f^{n-2}+\cdots+f^{n-1}\dot f$，一般不对易时**无法**合并成 $n\dot f f^{n-1}$；只有 $\dot f$ 能穿过所有 $f$ 时才恢复标量链式法则。这条前提在 §5.2 第二步是决定性的。

### 1.2 共轭是一个自同构：穿透律

把算子映成 $e^{A}Xe^{-A}$ 的映射记作 $\mathrm{Ad}(e^{A})$。在乘积中间插入 $\mathbb{1}=e^{-A}e^{A}$，

$$
e^{A}(XY)\,e^{-A}=e^{A}X\bigl(e^{-A}e^{A}\bigr)Y\,e^{-A}=\bigl(e^{A}Xe^{-A}\bigr)\bigl(e^{A}Ye^{-A}\bigr)\tag{6}
$$

故它是**保乘法的自同构**；归纳得 $e^{A}B^{n}e^{-A}=\bigl(e^{A}Be^{-A}\bigr)^{n}$，代入 [D05](D05-functional-calculus-and-kernel.md) §1.1 的幂级数定义，逐项穿入：

$$
\color{blue}{e^{A}f(B)\,e^{-A}
=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}\,\bigl(e^{A}Be^{-A}\bigr)^{n}
=f\bigl(e^{A}Be^{-A}\bigr)}\tag{7}
$$

**这意味着什么**：任何算子函数的共轭问题，都归结为**单个算子**的共轭 $e^{A}Be^{-A}$——而那一半由 §2 解决。

---

## 2. 伴随作用与 Hadamard 引理

### 2.1 伴随作用的三条性质

$$
\color{blue}{\mathrm{ad}_A X\equiv[A,X]=AX-XA}\tag{8}
$$

连续作用 $n$ 次即 $n$ 层嵌套（约定 $\mathrm{ad}_A^{\,0}B\equiv B$）：$\mathrm{ad}_A^{\,1}B=[A,B]$、$\mathrm{ad}_A^{\,2}B=[A,[A,B]]$、$\mathrm{ad}_A^{\,3}B=[A,[A,[A,B]]]$，$\dots$。展开定义即得三条：

1. **线性**：$\mathrm{ad}_A(\alpha X+\beta Y)=\alpha[A,X]+\beta[A,Y]$。
2. **Leibniz（导子性质）**：
   $$
   \mathrm{ad}_A(XY)=\bigl(\mathrm{ad}_A X\bigr)Y+X\bigl(\mathrm{ad}_A Y\bigr)\tag{9}
   $$
   即在代数意义上，"与 $A$ 取对易子"就是算子空间上的**求导**。
3. **Jacobi**：
   $$
   \bigl[A,[B,C]\bigr]+\bigl[B,[C,A]\bigr]+\bigl[C,[A,B]\bigr]=\mathbb{0}
   \quad\Longleftrightarrow\quad
   \mathrm{ad}_A\bigl([B,C]\bigr)=\bigl[\mathrm{ad}_A B,\,C\bigr]+\bigl[B,\,\mathrm{ad}_A C\bigr]\tag{10}
   $$
   即 $\mathrm{ad}_A$ 对李括号本身也是导子。

**正是这条导子性质，保证 $e^{t\,\mathrm{ad}_A}$ 是保持算子乘法的代数自同构**——与 (6) 精确对应。

### 2.2 Hadamard 引理

$$
\color{blue}{e^{A}Be^{-A}=e^{\mathrm{ad}_A}B=\sum_{n=0}^{\infty}\frac{1}{n!}\,\mathrm{ad}_A^{\,n}B
=B+[A,B]+\frac{1}{2!}\bigl[A,[A,B]\bigr]+\frac{1}{3!}\Bigl[A,\bigl[A,[A,B]\bigr]\Bigr]+\cdots}\tag{11}
$$

一句话记法：$\mathrm{Ad}\bigl(e^{A}\bigr)=e^{\mathrm{ad}_A}$（**共轭的无穷小生成元是对易子**）。

**证明（三步）**：

- **第一步：求导得方程。** 令
  $$
  F(t)\equiv e^{tA}\,B\,e^{-tA}\qquad\bigl(F(0)=B,\;F(1)=e^{A}Be^{-A}\bigr)\tag{12}
  $$
  由乘积法则与 (3)(4)，
  $$
  \frac{dF(t)}{dt}=A\,e^{tA}Be^{-tA}-e^{tA}Be^{-tA}\,A=A\,F(t)-F(t)\,A=\bigl[A,F(t)\bigr]
  $$
  即
  $$
  \frac{dF(t)}{dt}=\mathrm{ad}_A F(t),
  \qquad F(0)=B\tag{13}
  $$
- **第二步：积分因子。** 取 $G(t)\equiv e^{-t\,\mathrm{ad}_A}F(t)$，则
  $$
  \frac{dG}{dt}=-e^{-t\,\mathrm{ad}_A}\mathrm{ad}_A F+e^{-t\,\mathrm{ad}_A}\dot F=\mathbb{0}
  $$
  故 $G$ 为常算子，$G(t)=G(0)=B$，左乘 $e^{t\,\mathrm{ad}_A}$ 得 $F(t)=e^{t\,\mathrm{ad}_A}B$。
- **第三步：展开取 $t=1$。** 把 $e^{t\,\mathrm{ad}_A}=\sum_{n}\frac{t^{n}}{n!}\mathrm{ad}_A^{\,n}$ 代入，取 $t=1$，得 (11)。

【证毕】

**两条要点**：(11) 是**恒等式**，等号在两边良定义处逐字成立；系数 $\frac{1}{n!}$ 来自指数的泰勒展开，**二阶项前是 $\frac{1}{2!}$ 不是 $1$**。

---

## 3. 两项截断

### 3.1 级数的两种终止方式

(11) 一般含无穷多项。能在有限步停下，只有两条路：

- **幂零截断**：存在 $N$ 使 $\mathrm{ad}_A^{\,N}B=\mathbb{0}$。则 $\mathrm{ad}_A^{\,n}B=\mathrm{ad}_A^{\,n-N}(\mathbb{0})=\mathbb{0}$（$\forall n\ge N$），级数**精确截断为前 $N$ 项**。$N=1$ 即 $[A,B]=\mathbb{0}$，只剩 $B$。
- **本征重现**：若 $\mathrm{ad}_A B=\lambda B$（$\lambda\in\mathbb{C}$），则 $\mathrm{ad}_A^{\,n}B=\lambda^{n}B$，一项都不截断，但每项正比于 $B$，可直接求和：
  $$
  e^{A}Be^{-A}=\sum_{n=0}^{\infty}\frac{\lambda^{n}}{n!}B=e^{\lambda}B
  $$

**这说明截断是特例，不是通例**：$\lambda\neq0$ 时级数是真无穷。

### 3.2 两项截断定理

**定理**：设 $[A,B]=c\mathbb{1}$（$c\in\mathbb{C}$ 与一切算子对易）。则

$$
\color{blue}{[A,B]=c\mathbb{1}
\quad\Longrightarrow\quad
e^{A}B\,e^{-A}=B+c\,\mathbb{1}}\tag{14}
$$

**证明**：在 (11) 中逐项看。$n=0$：$B$；$n=1$：$[A,B]=c\mathbb{1}$。而

$$
\mathrm{ad}_A^{\,2}B=\bigl[A,[A,B]\bigr]=[A,\,c\mathbb{1}]=c\,[A,\mathbb{1}]=\mathbb{0}\tag{15}
$$

**这一步正是"$c$ 与一切算子对易"起作用的地方。** 此后由幂零性全部归零，只剩前两项。

【证毕】

### 3.3 三条边界

1. **$c$ 必须是 $c\mathbb{1}$，不能是算子函数。** 若算出 $[A,B]=g(\hat q)$ 而 $A$ 与 $\hat q$ 不对易，则 $\mathrm{ad}_A^{\,2}B=[A,g(\hat q)]\neq\mathbb{0}$，第三项不消失，(14) 当场失效。
2. **截断与 $c$ 的大小无关。** $c=10^{-6}$ 与 $c=10^{6}$ 结论相同；决定因素只有 $\mathrm{ad}_A^{\,2}B=\mathbb{0}$。这**不是**"$c$ 小的一阶近似"。
3. **$c\neq0$ 没有有限维实现。** 若用 $N\times N$ 矩阵实现 $[A,B]=cI$，两边取迹：左端 $\operatorname{tr}[A,B]=\operatorname{tr}(AB)-\operatorname{tr}(BA)=0$，右端 $\operatorname{tr}(cI_{N})=cN$。只要 $N<\infty$ 就逼出 $c=0$。

$$
0=\operatorname{tr}[A,B]=cN\quad\Longrightarrow\quad c=0\qquad(N<\infty)\tag{16}
$$

**这意味着什么**：$[\hat q,\hat p]=i\mathbb{1}$ 这样的对易关系天生只能住在无穷维空间，且至少一方无界——任何有限维截断都不是"精度不够"，而是**原理性破坏**。

---

## 4. 交换相位公式

### 4.1 四步证明

$$
\color{blue}{[A,B]=c\mathbb{1}
\quad\Longrightarrow\quad
e^{A}e^{B}=e^{c}\,e^{B}e^{A}}\tag{17}
$$

1. 在 (7) 中取 $f(B)=e^{B}$（整函数，无条件成立）：$e^{A}e^{B}e^{-A}=\exp\bigl(e^{A}Be^{-A}\bigr)$。
2. 由 (14)，$e^{A}Be^{-A}=B+c\mathbb{1}$，故 $e^{A}e^{B}e^{-A}=\exp\bigl(B+c\mathbb{1}\bigr)$。
3. 因 $[B,c\mathbb{1}]=\mathbb{0}$，同态律把标量提出：$\exp\bigl(B+c\mathbb{1}\bigr)=e^{B}e^{c}=e^{c}e^{B}$。
4. 两边**右乘** $e^{A}$（标量 $e^{c}$ 与一切算子可交换）：

$$
\bigl(e^{A}e^{B}e^{-A}\bigr)e^{A}=e^{A}e^{B}=e^{c}e^{B}e^{A}
$$

【证毕】互换 $A,B$ 时因 $[B,A]=-c\mathbb{1}$，得 $e^{B}e^{A}=e^{-c}e^{A}e^{B}$。

### 4.2 它只定比值，定不出半角

(17) 只给出**比值** $e^{A}e^{B}/e^{B}e^{A}=e^{c}$。考察带任意 $\lambda\in\mathbb{C}$ 的族

$$
e^{A}e^{B}=e^{\lambda c}\,e^{A+B},
\qquad
e^{B}e^{A}=e^{(\lambda-1)c}\,e^{A+B}\tag{18}
$$

两式相除恒得 $e^{c}$，与 $\lambda$ 无关。**故单凭 (17) 推不出 $\lambda=\frac{1}{2}$**（甚至推不出"$e^{A}e^{B}$ 正比于 $e^{A+B}$"）。要钉死 $\lambda=\frac{1}{2}$，必须补 (17) 所没有的输入——**对连续参数 $t$ 的求导**，这正是下一节。

---

## 5. 三条 BCH 闭式

### 5.1 定理与对称中点

$$
\color{blue}{e^{A}e^{B}=e^{c/2}\,e^{A+B},
\qquad
e^{B}e^{A}=e^{-c/2}\,e^{A+B},
\qquad
e^{A/2}e^{B}e^{A/2}=e^{A+B}}\tag{19}
$$

**几何图像**：第三条说明"把 $A$ 的一半放在 $e^{B}$ 两侧"正好落回 $e^{A+B}$——所以 $e^{A+B}$ 是正反两个次序的**对称中点**；第一、二条说两个次序相对中点各偏半步（$e^{\pm c/2}$），彼此相差 $e^{c}$，恰是 (17)。

**记住分工**：$c/2$ 属于"单一次序相对中点"，$c$ 属于"两个次序之间"。

### 5.2 五步证明

- **第一步：对 $F(t)=e^{tA}e^{tB}$ 求导。** 插入 $\mathbb{1}=e^{-tA}e^{tA}$：
  $$
  \frac{dF}{dt}=A\,F(t)+e^{tA}B\,e^{-tA}\,F(t),\qquad
  e^{tA}Be^{-tA}=B+tc\mathbb{1}\tag{20}
  $$
  （第二式由 (14) 取 $A\to tA$，此时 $[tA,B]=tc\mathbb{1}$。）于是
  $$
  \frac{dF}{dt}=\bigl(A+B+tc\,\mathbb{1}\bigr)F(t),
  \qquad F(0)=\mathbb{1}\tag{21}
  $$
- **第二步：验证 $[f,\dot f]=\mathbb{0}$，用积分因子求解。** 令 $\dot f=A+B+tc\mathbb{1}$，则 $f(t)=(A+B)t+\frac{c}{2}t^{2}\mathbb{1}+K$。由 $G(0)=e^{-f(0)}=\mathbb{1}$ 定出 $K=\mathbb{0}$。此时 $f$ 与 $\dot f$ 只由 $A+B$ 与中心标量构成，故 $[f,\dot f]=\mathbb{0}$，可对 $G=e^{-f}F$ 用 (5)：
  $$
  \frac{dG}{dt}=e^{-f}\bigl(-\dot f+A+B+tc\mathbb{1}\bigr)F=\mathbb{0}
  \quad\Longrightarrow\quad
  F(t)=\exp\Bigl((A+B)t+\frac{c}{2}t^{2}\mathbb{1}\Bigr)\tag{22}
  $$
  **$tc$ 这一项就是 $\frac{1}{2}$ 的来源**：$\int_{0}^{1}t\,dt=\frac{1}{2}$。
- **第三步：取 $t=1$。** 由 $[A+B,\frac{c}{2}\mathbb{1}]=\mathbb{0}$ 提出标量：
  $$
  e^{A}e^{B}=\exp\Bigl(A+B+\frac{c}{2}\mathbb{1}\Bigr)=e^{c/2}e^{A+B}\tag{23}
  $$
- **第四步：第二条。** 由 (17) 的 $e^{B}e^{A}=e^{-c}e^{A}e^{B}$ 代入 (23)，或直接互换算子标签（$[B,A]=-c\mathbb{1}$）：
  $$
  e^{B}e^{A}=e^{-c}\cdot e^{c/2}e^{A+B}=e^{-c/2}e^{A+B}\tag{24}
  $$
- **第五步：对称夹心。** 按结合律先并前两个因子（**半个 $A$ 配整个 $B$**）：$[A/2,B]=\frac{c}{2}\mathbb{1}$，故
  $$
  e^{A/2}e^{B}=e^{c/4}\,e^{A/2+B}\tag{25}
  $$
  再与右边的 $e^{A/2}$ 合并：此时 $[A/2+B,\,A/2]=[B,A/2]=-\frac{c}{2}\mathbb{1}$，故
  $$
  e^{A/2+B}e^{A/2}=e^{-c/4}\,e^{A+B}\tag{26}
  $$
  两式相乘，$\pm\frac{c}{4}$ 精确相消：
  $$
  e^{A/2}e^{B}e^{A/2}=e^{A+B}\tag{27}
  $$

【证毕】

### 5.3 配对方式决定中间量

上一步若改按 $\bigl(e^{A/2}e^{B/2}\bigr)\bigl(e^{B/2}e^{A/2}\bigr)$ 配对，因 $[A/2,B/2]=\frac{c}{4}\mathbb{1}$，半角因子是 $e^{\pm c/8}$ 而非 $e^{\pm c/4}$。结果仍是 $e^{A+B}$（$c/8$ 与 $-c/8$ 也相消，剩下同源的 $e^{(A+B)/2}e^{(A+B)/2}=e^{A+B}$），但**中间量差了一倍**。所以推导必须指明谁与谁配对。

---

## 6. 一致性检验

| 检验 | 结果 |
|---|---|
| $[A,B]=\mathbb{0}$（$c=0$） | (14) 给 $e^{A}Be^{-A}=B$；(17) 给交换无相位；(19) 三式都退化为 $e^{A+B}$ ✅ |
| (11) 取 $t=0$ | 左 $B$、右 $\mathrm{ad}_A^{0}B=B$ ✅ |
| (11) 系数 | 二阶项为 $\frac{1}{2!}[A,[A,B]]$，非组合数 ✅ |
| (14) 与 (11) 相容 | 令 $\mathrm{ad}_A^{2}B=\mathbb{0}$，级数自然只剩两项 ✅ |
| (17) 与 (19) 相容 | (19) 两式相除得 $e^{c/2-(-c/2)}=e^{c}$ ✅ |
| (19) 第三条与第一、二条 | 两次配对得 $e^{c/4}$ 与 $e^{-c/4}$，乘积为 $1$ ✅ |
| $A=i\alpha\hat X$（$\hat X$ 自伴，$\alpha\in\mathbb{R}$） | 由 [D05](D05-functional-calculus-and-kernel.md) §2.3 酉判据，$e^{A}$ 酉，且 $(e^{A})^{-1}=(e^{A})^{\dagger}=e^{-A}$，与 (2) 一致 ✅ |
| 标量情形 $A=a$、$B=b$ | $c=0$，三式退化为 $e^{a+b}=e^{a}e^{b}$ ✅ |
| 有限维 | (16) 排除 $c\neq0$，故数值检验必须在无穷维做 ✅ |

---

## 7. 备注与边界

1. **这是恒等式，不是近似。** 级数"停"与"不停"取决于 $\mathrm{ad}_A$ 是否幂零，与精度无关。
2. **$c$ 必须是中心元素。** $[A,B]=g(\hat q)$ 这类算子情形没有两项截断，也就没有 (17)–(19)；只剩 BCH 的无穷级数（一般情形确实没有闭式）。
3. **无界算子改口径。** $A,B$ 无界时 (11)(19) 只在公共解析向量域上成立，$\frac{d}{dt}$ 与共轭都要配定义域条件；结构不变，"处处成立"改成"在公共定义域上成立"。
4. **链式前提不能省。** (5) 的 $[f,\dot f]=\mathbb{0}$ 在 (22) 处自动满足（因 $f,\dot f$ 只由 $A+B$ 与 $\mathbb{1}$ 张成），但一般情形必须逐例检验；不满足时 $\frac{d}{dt}e^{f}\neq\dot f e^{f}$。
5. **积分常数 $K$ 不能丢。** $K=\mathbb{0}$ 由 $F(0)=\mathbb{1}$ 定出；丢了它，(23) 会多一个整体因子。
6. **交换相位只定比值**（§4.2）。想要 $c/2$ 必须用连续参数求导；这条差别是"有闭式"与"只有级数"的分水岭。
7. **配对方式要写明。** $c/4$ 还是 $c/8$ 取决于谁与谁配对（§5.3）。
8. **三条闭式不适用于 $[A,B]$ 是算子的一般情形。** 那时 $\mathrm{ad}_A$ 不幂零，(19) 不再成立。
9. **$n$ 重推广属下游。** 多项乘积的截断与重排（有序化、正规序）不在本卡。

---

## 8. 自检

- [ ] 不看本卡，写出 $\dot F=\mathrm{ad}_A F$ 的三行推导，并说明用了哪条运算律
- [ ] 说明为什么 $[A,B]=c\mathbb{1}$ 时级数恰好停在第二项，指出"$c$ 与一切对易"用在何处
- [ ] 举一个 $c$ 是算子导致截断失效的例子
- [ ] 用迹论证说明 $c\neq0$ 为何无有限维实现
- [ ] 不看本卡，从 (14) 推出 (17)，并指出最后一步是左乘还是右乘
- [ ] 写出 $\lambda$ 参数族，说明为什么 (17) 定不出 $c/2$
- [ ] 写出 $F(t)=e^{tA}e^{tB}$ 的微分方程，并指出 $\frac{1}{2}$ 从哪个积分来
- [ ] 说明 (5) 的 $[f,\dot f]=\mathbb{0}$ 在 BCH 证明中是否自动满足、为什么
- [ ] 用两种配对算对称夹心，说出中间量的差别
