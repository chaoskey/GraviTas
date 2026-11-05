# N004 · Hadamard 引理：共轭的生成元是对易子

> 写于 2026-11-05 · 关联：[N003](N003-basis-and-operator-relations.md)、[N002](N002-finite-temperature-path-integral.md)
> 目标：把 $e^{A}Be^{-A}$ 展开成对易子的幂级数，并用它三行推出 Weyl 关系的相位因子。
> 用途：[N003 §0.3](N003-basis-and-operator-relations.md) 只给了 Weyl 关系的结论，这一页给它的来历。
> 约定：$\hbar=1$；$\hat p=-i\partial_q$；$[\hat q,\hat p]=i$，故 $[\hat p,\hat q]=-i$。

---

## 0. 结论

$$
e^{A}Be^{-A}
=\sum_{n=0}^{\infty}\frac{1}{n!}\,\mathrm{ad}_A^{\,n}B
$$

写开：

$$
e^{A}Be^{-A}
=B+[A,B]+\frac{1}{2!}\bigl[A,[A,B]\bigr]
+\frac{1}{3!}\Bigl[A,\bigl[A,[A,B]\bigr]\Bigr]+\cdots
$$

其中 $\mathrm{ad}_A X\equiv[A,X]$。

**一句话**：共轭的无穷小生成元就是对易子，即

$$
\mathrm{Ad}\bigl(e^{A}\bigr)=e^{\mathrm{ad}_A}
$$

**这意味着什么**：不必背这个级数。记住"共轭的生成元是对易子"，任何具体情形现推即可——包括 Weyl 关系的相位（§5）。

---

## 1. 记号与两条性质

$$
\mathrm{ad}_A X\equiv[A,X]
$$

$\mathrm{ad}_A$ 是一个**线性算子**，作用在**算子构成的空间**上（不是作用在态上）。它满足两条：

**线性**：

$$
\mathrm{ad}_A(\alpha X+\beta Y)=\alpha[A,X]+\beta[A,Y]
$$

**导子性质（Leibniz）**：

$$
\mathrm{ad}_A(XY)=[A,XY]=[A,X]Y+X[A,Y]=\bigl(\mathrm{ad}_A X\bigr)Y+X\bigl(\mathrm{ad}_A Y\bigr)
$$

第二条保证 $e^{t\,\mathrm{ad}_A}$ 是代数自同构——这正是"共轭是自同构"的无穷小版本。

---

## 2. 推导：三步

### 2.1 第一步：求导，得到一个方程

定义

$$
F(t)\equiv e^{tA}\,B\,e^{-tA}
$$

对 $t$ 求导。两项各求一次，且 $A$ 与 $e^{tA}$ 对易（$Ae^{tA}=e^{tA}A$）：

$$
\frac{dF}{dt}
=A\,e^{tA}Be^{-tA}-e^{tA}B\,A\,e^{-tA}
=e^{tA}\bigl(AB-BA\bigr)e^{-tA}
=e^{tA}[A,B]\,e^{-tA}
$$

再用一次 $A$ 与 $e^{\pm tA}$ 对易，把结果写成对易子：

$$
\frac{dF}{dt}=\bigl[A,\ e^{tA}Be^{-tA}\bigr]=[A,F(t)]
$$

于是

$$
\boxed{\ \frac{dF}{dt}=\mathrm{ad}_A F(t)\ },\qquad F(0)=B
$$

**这一步的实质**：求导被翻译成"作用一个线性算子"。原本要算的是无穷多个对易子，现在得到一个常系数线性方程。

### 2.2 第二步：解方程

常系数线性方程 $\dot F=LF$，$L=\mathrm{ad}_A$。用积分因子：

$$
G(t)\equiv e^{-t\,\mathrm{ad}_A}F(t)
$$

$$
\frac{dG}{dt}
=-e^{-t\,\mathrm{ad}_A}\,\mathrm{ad}_A F+e^{-t\,\mathrm{ad}_A}\,\dot F
=-e^{-t\,\mathrm{ad}_A}\mathrm{ad}_A F+e^{-t\,\mathrm{ad}_A}\mathrm{ad}_A F=0
$$

所以 $G$ 是常数，$G(t)=G(0)=F(0)=B$。因此

$$
F(t)=e^{t\,\mathrm{ad}_A}B
$$

### 2.3 第三步：展开，取 $t=1$

按指数函数的定义展开 $e^{t\,\mathrm{ad}_A}$：

$$
F(t)=\sum_{n=0}^{\infty}\frac{t^{n}}{n!}\,\mathrm{ad}_A^{\,n}B
$$

取 $t=1$，得 §0 的结论。

**注意这一步没有用到任何技巧**：级数收敛性由 $\mathrm{ad}_A$ 的谱半径决定，而物理上我们只在"两边都良定义"的范围内用它。

---

## 3. 逐项核对

| $n$ | $\mathrm{ad}_A^{\,n}B$ | 显式 |
|---|---|---|
| $0$ | $B$ | $B$ |
| $1$ | $[A,B]$ | $[A,B]$ |
| $2$ | $[A,[A,B]]$ | 两层嵌套 |
| $3$ | $[A,[A,[A,B]]]$ | 三层嵌套 |
| $n$ | — | $n$ 层嵌套 |

**系数来源**：$1/n!$ 来自指数函数的泰勒展开，**不是**组合数。$[A,[A,B]]$ 前面的系数是 $1/2$，不是 $1$——这一点最容易记错（见 §8 第 2 条）。

---

## 4. 什么时候级数截断

一般情形级数是**无穷**的。截断只发生在 $\mathrm{ad}_A$ 对 $B$ **幂零**时，即某个 $N$ 使 $\mathrm{ad}_A^{\,N}B=0$。

**最重要的特例：$[A,B]=c$ 是一个数。** 数算子与一切对易，所以

$$
\mathrm{ad}_A^{2}B=[A,[A,B]]=[A,c]=0
$$

级数只剩两项：

$$
e^{A}Be^{-A}=B+[A,B]=B+c
$$

**这一条是 §5 的全部前提。** 如果 $[A,B]$ 不是数而是算子，$\mathrm{ad}_A^2B\neq0$，级数就停不下来——那正是 Baker–Campbell–Hausdorff 级数一般没有闭式的原因。

---

## 5. 用途：三行推出 Weyl 关系的相位

设 $[A,B]=c$ 是数。目标是算 $e^{A}e^{B}e^{-A}$。

**注意不要直接把 §4 的结论套上去**：§4 说的是 $e^{A}Be^{-A}=B+c$，而这里要共轭的是 $e^{B}$，不是 $B$。正确的一步是"共轭作用于函数 ≡ 作用于自变量"：

对任意能展成幂级数的 $f$，

$$
e^{A}f(B)e^{-A}=f\bigl(e^{A}Be^{-A}\bigr)
$$

理由：$e^{A}B^{n}e^{-A}=\bigl(e^{A}Be^{-A}\bigr)^{n}$，逐项相乘即得（幂级数由连续性延拓）。

取 $f(B)=e^{B}$：

$$
e^{A}e^{B}e^{-A}=\exp\bigl(e^{A}Be^{-A}\bigr)=\exp(B+c)=e^{B}e^{c}
$$

最后一步用到 $c$ 是数与 $B$ 对易。右乘 $e^{A}$：

$$
\boxed{\,e^{A}e^{B}=e^{c}\,e^{B}e^{A}\,}
$$

**代回物理量**：$A=ia\hat p$、$B=ib\hat q$，

$$
[A,B]=(ia)(ib)[\hat p,\hat q]=-ab\cdot(-i)=iab
$$

所以

$$
e^{ia\hat p}\,e^{ib\hat q}=e^{iab}\,e^{ib\hat q}\,e^{ia\hat p}
$$

**如果换成 $q$ 在前的次序**：$A=ia\hat q$、$B=ib\hat p$，则 $[A,B]=(ia)(ib)[\hat q,\hat p]=-iab$，得

$$
e^{ia\hat q}\,e^{ib\hat p}=e^{-iab}\,e^{ib\hat p}\,e^{ia\hat q}
$$

两式都对，但混用会差一个 $e^{2iab}$。

### 5.1 为什么是 $e^{c}$ 不是 $e^{c/2}$

把两个次序都与对称序比较（BCH 在 $[A,B]$ 为常数时的精确形式）：

$$
e^{A}e^{B}=e^{c/2}\,e^{A+B},
\qquad
e^{B}e^{A}=e^{-c/2}\,e^{A+B}
$$

- 每一个单独看，相对对称序的相位是 $c/2$；
- 两者相比，相位是 $c/2-(-c/2)=c$。

**记住分工**：$c/2$ 属于"相对于对称序"，$c$ 属于"两个次序之间"。Weyl 关系比较的是两个次序，所以是 $c$。

---

## 6. 三个例子

### 6.1 平移：第一项就截断

取 $A=ia\hat p$、$B=\hat q$：

$$
[A,B]=ia[\hat p,\hat q]=ia\cdot(-i)=a
$$

$a$ 是数，故 $\mathrm{ad}_A^2B=0$：

$$
e^{ia\hat p}\,\hat q\,e^{-ia\hat p}=\hat q+a
$$

**验证**：$e^{ia\hat p}\psi(x)=\psi(x+a)$（平移）。令 $\phi=e^{-ia\hat p}\psi$，则 $\phi(x)=\psi(x-a)$，故

$$
e^{ia\hat p}\hat q\,e^{-ia\hat p}\psi(x)=e^{ia\hat p}\bigl[x\,\psi(x-a)\bigr]=(x+a)\psi(x)
$$

与 $\bigl(\hat q+a\bigr)\psi$ 一致。

### 6.2 升降算符：同样截断

$[a,a^{\dagger}]=1$，取 $A=\theta a^{\dagger}$、$B=a$：

$$
[A,B]=\theta\bigl[a^{\dagger},a\bigr]=-\theta
$$

$$
e^{\theta a^{\dagger}}\,a\,e^{-\theta a^{\dagger}}=a-\theta
$$

这个式子在相干态、压缩态里反复出现。

### 6.3 不截断但可求和

取 $A=\hat p$、$B=e^{i\hat q}$。用 $[\hat p,f(\hat q)]=-i f'(\hat q)$：

$$
\mathrm{ad}_{\hat p}\,e^{i\hat q}=[\hat p,e^{i\hat q}]=-i\cdot i\,e^{i\hat q}=e^{i\hat q}
$$

**每一次作用都返回 $B$ 本身**，于是

$$
e^{t\hat p}\,e^{i\hat q}\,e^{-t\hat p}
=\sum_{n=0}^{\infty}\frac{t^{n}}{n!}\,e^{i\hat q}=e^{t}\,e^{i\hat q}
$$

**这个例子的意义**：证明级数一般真是无穷的，截断只是特例。

### 6.4 为什么有限维矩阵验不出来

若用 $n$ 维矩阵，$\mathrm{tr}\,[A,B]=\mathrm{tr}(AB)-\mathrm{tr}(BA)=0$，而 $\mathrm{tr}(cI)=cn$。故 $c\neq0$ 时矛盾。

**结论**：$[A,B]=cI$（$c\neq0$）**没有有限维实现**。所以任何数值检验都必须在无穷维做——例如谐振子的无穷基底、或波函数空间。有限维截断必然在某一处破坏对易子，那个破坏不是"数值误差"，是原理性的。

---

## 7. 一致性检验

| 检验 | 结果 |
|---|---|
| $t=0$ 退化为恒等 | 左为 $B$，右为 $\mathrm{ad}_A^0B=B$，成立 |
| $[A,B]=0$ 时 | $c=0$，级数只剩 $B$，两边都等于 $B$，成立 |
| 例 6.1 可直接算 | 得 $\hat q+a$，与级数前两项一致，成立 |
| 与 BCH 相容 | $e^{A}e^{B}=e^{c/2}e^{A+B}$、$e^{B}e^{A}=e^{-c/2}e^{A+B}$，比值 $e^{c}$，成立 |
| 导子性质 | $\mathrm{ad}_A$ 满足 Leibniz，故 $e^{\mathrm{ad}_A}$ 是代数自同构，与"共轭是自同构"一致 |
| 谱不变 | 共轭保持谱，例 6.1 中 $\hat q$ 与 $\hat q+a$ 的谱都是 $\mathbb{R}$，成立 |

---

## 8. 我一开始错在哪

1. **以为 Hadamard 引理是个近似公式。** 总想给它找"一阶近似、二阶修正"的语境。
   实际上它是**恒等式**：在两边都良定义的范围内逐字成立，没有截断误差。级数是否"停"取决于 $\mathrm{ad}_A$ 是否幂零，不取决于精度。

2. **把系数记成组合数。** 以为第二层嵌套前是 $1$。
   实际是 $1/2!$，来自指数的泰勒展开。记法：$e^{x}=\sum x^n/n!$，把 $x$ 换成 $\mathrm{ad}_A$ 即可，不要在系数上自由发挥。

3. **试图用 $2\times2$ 矩阵检验。** 结果怎么都不对，以为是代码错。
   实际是**原理性不可能**：$\mathrm{tr}[A,B]=0$ 而 $\mathrm{tr}(cI)=cn$，所以 $c\neq0$ 的 CCR 无有限维实现。这个教训值一条：**数值检验失败时，先问"这个现象在原理上能不能出现"**。

4. **把 Weyl 相位写成 $e^{-iab}$。** 记的是"$q$ 在前的教科书版本"，却套在"$p$ 在前"的写法上。
   实际两个次序的因子互为倒数。正确做法不是背符号，而是现算：$[ia\hat p,ib\hat q]=iab$，故 $p$ 在前取正号。（此错已在 [N003](N003-basis-and-operator-relations.md) 中修正。）

5. **以为 $c$ 可以是任意算子。** 于是想不通为什么级数能停。
   实际 $c$ 必须是**数**（单位算子的倍数），才能保证 $\mathrm{ad}_A^2B=[A,c]=0$。这条前提一松，整个公式失效，退回 BCH 无穷级数。

6. **以为推 Weyl 关系得搬 BCH 全级数。** 于是被无穷嵌套吓住。
   实际只需要"解一个常系数线性方程"加"标的数的性质"两步。**换个表述，难的问题就变成简单的了**——这是这一页最值得记住的方法论。

---

## 9. 延伸

- **与有序化的关系**：正规序、Weyl 序之间的换算，靠的就是反复用 $e^{A}Be^{-A}$ 这类共轭。$\mathrm{ad}_A$ 的幂零性决定了换算在几步内终止。
- **与 BCH 的关系**：[N003 §0.3](N003-basis-and-operator-relations.md) 里 $e^{A}e^{B}=e^{c}e^{B}e^{A}$ 是 BCH 的最简单闭式情形；一般情形没有闭式，本质原因就是 $\mathrm{ad}$ 不幂零。
- **与 Stone–von Neumann 的关系**：Weyl 关系的相位是**射影表示**的中心荷。`ad` 的语言下，它对应辛形式，见 [N003 §0.3](N003-basis-and-operator-relations.md) 末尾。
- **与路径积分的关系**：[N002](N002-finite-temperature-path-integral.md) 的时间切片用的是 $e^{-\varepsilon H}$，那里不需要 $\mathrm{ad}$；但若要把算子语言与路径积分对接（例如算 $\langle q(t)p(t')\rangle$ 的台阶），共轭公式会以"海森堡演化"的形式出现：$B(t)=e^{itH}Be^{-itH}$，正是本节 $A=itH$ 的特例。

---

## 10. 自检

- [ ] 不看本文，三行重推 Hadamard 引理（定义 $F(t)$、求导得 $\dot F=\mathrm{ad}_AF$、解方程）
- [ ] 说明为什么 $[A,B]=c$ 是数时级数只有两项，并指出哪一步用到"$c$ 与一切对易"
- [ ] 用这条引理推出 Weyl 相位，并说清 $p$ 在前与 $q$ 在前的符号差别
- [ ] 解释为什么 $e^{c}\neq e^{c/2}$：分别说明 $c/2$ 与 $c$ 各自对应什么比较
- [ ] 举一个 $\mathrm{ad}_A$ 不幂零的例子，并把级数求和（§6.3 可作答案）
- [ ] 用迹论证说明为什么不能用有限维矩阵检验 CCR
