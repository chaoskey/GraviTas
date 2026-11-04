# N003 · 表象与算子的基础关系清单

> 写于 2026-11-04 · 关联：[N002](N002-finite-temperature-path-integral.md)、[N001](N001-hawking-temperature.md)
> 用途：[N002](N002-finite-temperature-path-integral.md) §2 那套"切片 + 插完备性 + 高斯积分"用到的全部表象关系，
> 集中一页。卡住时先查这里，不要再去翻教材——翻教材会顺手读掉两小时。
> 约定：$\hbar = 1$；号差 $(-,+,+,+)$；§6 之前是实时间，§6 是欧氏。

---

## 0. 结论：最小记忆集

只有五条。其余所有关系都能由这五条当场推出来。

$$
\hat q\,|q\rangle=q\,|q\rangle,
\qquad
[\hat q,\hat p]=i,
\qquad
\langle q|q'\rangle=\delta(q-q')
$$

$$
\langle q|p\rangle=e^{ipq},
\qquad
\int\frac{dp}{2\pi}\,|p\rangle\langle p|=\mathbb{1}
$$

**要点：五条里只有一条是物理的。** $[\hat q,\hat p]=i$（等价地：$\hat p$ 在 $q$ 表象下是 $-i\partial_q$）是量子力学的输入；另外四条是**基的选取**与**归一化的记账**。改它们不改变任何物理，只让中间步骤换一副长相。

这意味着什么：推导卡住时，九成不是"不懂量子力学"，而是某处 $2\pi$ 掉了一个，或者基换了没跟着换。§10 列了六种具体的翻车方式。

---

## 1. 三类东西：定义、约定、定理

把这三类混在一起看，是这一页所有困惑的来源。

| 类别 | 内容 | 能否改 |
|---|---|---|
| 定义 | 本征方程 $\hat q\lvert q\rangle=q\lvert q\rangle$；$\hat p$ 的作用方式；算子的核 | 不能 |
| 约定 | $\langle q\lvert q'\rangle$ 前有没有系数；$dp$ 前有没有 $2\pi$ | 能，但必须**成对**改 |
| 定理 | 完备性、谱分解、迹的基无关性、$\langle q\lvert p\rangle=e^{ipq}$ | 由上面两类推出 |

### 1.1 成对的两种常见方案

| 方案 | 位置归一化 | 动量归一化 | 内积 |
|---|---|---|---|
| 常用（本仓库、物理文献） | $\langle q\lvert q'\rangle=\delta(q-q')$ | $\langle p\lvert p'\rangle=2\pi\delta(p-p')$ | $\langle q\lvert p\rangle=e^{ipq}$ |
| 对称（数学文献） | $\langle q\lvert q'\rangle=\delta(q-q')$ | $\langle p\lvert p'\rangle=\delta(p-p')$ | $\langle q\lvert p\rangle=e^{ipq}/\sqrt{2\pi}$ |

**纪律：一页之内只能有一种。** 混用会差 $2\pi$ 的幂，而这种错误在高斯积分里不会自己暴露——它只会让你最后的结果比正确答案多一个常数，而你还在检查物理。

---

## 2. 基、内积、完备性

### 2.1 四条

$$
\langle q|q'\rangle=\delta(q-q'),
\qquad
\int dq\;|q\rangle\langle q|=\mathbb{1}
$$

$$
\langle p|p'\rangle=2\pi\,\delta(p-p'),
\qquad
\int\frac{dp}{2\pi}\;|p\rangle\langle p|=\mathbb{1}
$$

注意**不对称**：$q$ 那边没有 $2\pi$，$p$ 那边有。这不是笔误，是被 §2.2 的向量锁死的。

### 2.2 锁：两条验算

做完这两条，整套约定就自洽了。任何一次改动都必须让这两条继续成立。

$$
\langle q|\Bigl(\int\frac{dp}{2\pi}|p\rangle\langle p|\Bigr)|q'\rangle
=\int\frac{dp}{2\pi}\,e^{ip(q-q')}=\delta(q-q')
$$

$$
\langle p|\Bigl(\int dq\,|q\rangle\langle q|\Bigr)|p'\rangle
=\int dq\,e^{i(p-p')q}=2\pi\,\delta(p-p')
$$

**这两条为什么必须查**：完备性是"用不用得上"的问题，正交归一是"系数对不对"的问题。只查一条，另一条错了你发现不了。

### 2.3 那个 $2\pi$ 的来历

它来自傅里叶变换的约定，而约定来自 $\delta$：

$$
\int\frac{dp}{2\pi}\,e^{ipx}=\delta(x)
$$

所以 $2\pi$ 不是"配平出来的"，是 $\delta$ 函数的定义式搬过来的。凡是看到 $dp$ 前面挂 $2\pi$、而 $dq$ 前面光秃秃，原因都是这一条。

---

## 3. 算子的表示

### 3.1 作用在波函数上

$$
\langle q|\hat q|\psi\rangle=q\,\psi(q),
\qquad
\langle q|\hat p|\psi\rangle=-i\,\frac{d}{dq}\psi(q)
$$

$$
\langle p|\hat p|\psi\rangle=p\,\tilde\psi(p),
\qquad
\langle p|\hat q|\psi\rangle=i\,\frac{d}{dp}\tilde\psi(p)
$$

**注意**：$\hat p=-i\partial_q$ 是**表示**，不是定义。定义只有 $[\hat q,\hat p]=i$ 加 $\hat q$ 的谱。换成别的基，$\hat p$ 就换成别的样子。

### 3.2 核（矩阵元）

$$
\langle q'|\hat q|q''\rangle=q'\,\delta(q'-q'')
$$

$$
\langle q'|\hat p|q''\rangle=-i\,\partial_{q'}\delta(q'-q'')
$$

$$
\langle p'|\hat p|p''\rangle=p'\,2\pi\delta(p'-p'')
$$

读法：**对角项带 $\delta$，非对角项带 $\delta$ 的导数。** 这个模式在所有表象里重复。

### 3.3 乘积的核（路径积分的引擎）

$$
\langle q'|\hat A\hat B|q''\rangle=\int dq\;\langle q'|\hat A|q\rangle\langle q|\hat B|q''\rangle
$$

这一条就是"在中间插一张快照"。[N002 §2.1](N002-finite-temperature-path-integral.md) 的时间切片全靠它；连乘 $N$ 次再取极限，得到的对象就叫路径积分。

### 3.4 波函数与其傅里叶变换

$$
\tilde\psi(p)=\int dq\,e^{-ipq}\,\psi(q),
\qquad
\psi(q)=\int\frac{dp}{2\pi}\,e^{ipq}\,\tilde\psi(p)
$$

---

## 4. 函数演算与平移

### 4.1 谱分解

$$
f(\hat q)=\int dq\,f(q)\,|q\rangle\langle q|,
\qquad
f(\hat p)=\int\frac{dp}{2\pi}\,f(p)\,|p\rangle\langle p|
$$

由此

$$
\langle q'|f(\hat q)|q''\rangle=f(q')\,\delta(q'-q'')
$$

$$
\langle q'|f(\hat p)|q''\rangle=\int\frac{dp}{2\pi}\,e^{ip(q'-q)}f(p)
$$

**第二行是 [N002 §2.2](N002-finite-temperature-path-integral.md) 的母公式**：取 $f(p)=e^{-\varepsilon p^2/2m}$ 就得到那一行。所以"短时核"这个东西不需要单独记，它是谱分解的一个特例。

### 4.2 对角判据（比展开级数更根本）

$$
\bigl[\hat q,f(\hat q)\bigr]=0
\quad\Longrightarrow\quad
(q'-q'')\,\langle q'|f(\hat q)|q''\rangle=0
\quad\Longrightarrow\quad
\text{核}\propto\delta(q'-q'')
$$

**对易子为零，核必然对角。** 这条判据的好处是它不需要 $f$ 解析、不需要展开，也不怕 $f$ 是哪个具体函数。

顺带解释一件事：为什么 $V(q)$ 和 $V(q')$ 在 $\langle q'\lvert e^{-\varepsilon V(\hat q)}\lvert q''\rangle$ 里可以随便换？因为 $\delta$ 的支撑上 $q'=q''$，两者**精确**相等。上一轮讨论过的 $\mathcal{O}(\varepsilon^{3/2})$ 差别不在这里，它出现在**把 $\delta$ 用 $p$ 积分抹开成高斯之后**——那时两点不再重合，差别才显形。

### 4.3 平移算子

$$
e^{-ia\hat p}\,|q\rangle=|q+a\rangle,
\qquad
e^{ib\hat q}\,|p\rangle=|p+b\rangle
$$

等价地

$$
\langle q|e^{-ia\hat p}|q'\rangle=\delta(q-q'-a),
\qquad
\langle q|e^{ib\hat q}|q'\rangle=e^{ibq}\,\delta(q-q')
$$

### 4.4 平面波的来历

由 $e^{i\alpha\hat q}\hat p\,e^{-i\alpha\hat q}=\hat p+\alpha$：

$$
\hat p\left(e^{ip\hat q}|0_{p}\rangle\right)=p\left(e^{ip\hat q}|0_{p}\rangle\right)
\quad\Longrightarrow\quad
|p\rangle\propto e^{ip\hat q}|0_{p}\rangle
$$

投影到 $q$ 基，指数上的 $p$ 就成了 $\langle q\lvert p\rangle=e^{ipq}$，系数由 §2.2 的锁定死为 $1$。

**这意味着什么**：平面波不是"猜出来的"，它是"动量平移算子在位置基上的矩阵元"。

---

## 5. 对易、迹、$\delta$ 的记账

### 5.1 对易关系与不确定关系

$$
[\hat q,\hat p]=i,
\qquad
\Delta q\,\Delta p\ge\frac{1}{2}
$$

$$
[\hat q,f(\hat p)]=i\,f'(\hat p),
\qquad
[\hat p,g(\hat q)]=-i\,g'(\hat q)
$$

### 5.2 迹（基无关）

$$
\mathrm{Tr}\,\hat A=\int dq\,\langle q|\hat A|q\rangle
=\int\frac{dp}{2\pi}\,\langle p|\hat A|p\rangle
$$

$$
\mathrm{Tr}(\hat A\hat B)=\mathrm{Tr}(\hat B\hat A),
\qquad
\mathrm{Tr}\bigl(|q\rangle\langle q'|\bigr)=\delta(q-q')
$$

**第一行是 [N002 §2.4](N002-finite-temperature-path-integral.md) 的许可证**：迹不依赖基，所以可以放心在 $q$ 基下取迹、把两端焊起来。

### 5.3 有限盒子（离散化）

取 $q\in[0,L]$、周期边界，动量取 $p_m=2\pi m/L$：

$$
\langle q_n|q_m\rangle=\delta_{nm},
\qquad
\sum_n|q_n\rangle\langle q_n|=\mathbb{1},
\qquad
\langle q_n|p_m\rangle=\frac{1}{\sqrt{L}}\,e^{ip_mq_n}
$$

$$
\int\frac{dp}{2\pi}\;\longrightarrow\;\frac{1}{L}\sum_m,
\qquad
2\pi\delta(p-p')\;\longrightarrow\;L\,\delta_{mm'}
$$

**这就是 [N002 §4.1](N002-finite-temperature-path-integral.md) 里那个 $L$ 的来历**：自由粒子的 $Z=L\left(m/2\pi\beta\right)^{1/2}$，那个 $L$ 就是"对 $q$ 积分的长度"。写格点、写数值时，用这一行换掉连续谱，比跟 $\delta(0)$ 搏斗省事。

### 5.4 $\delta$ 与高斯的实用公式

$$
\delta(ax)=\frac{1}{\lvert a\rvert}\,\delta(x),
\qquad
\delta\bigl(f(x)\bigr)=\sum_i\frac{\delta(x-x_i)}{\lvert f'(x_i)\rvert}
$$

$$
\int_{-\infty}^{\infty}e^{-ap^2+bp}\,dp=\sqrt{\frac{\pi}{a}}\;e^{b^2/4a},
\qquad
\mathrm{Re}\,a>0
$$

取 $a=\varepsilon/2m$、$b=i(q'-q)$，就是 [N002 §2.2](N002-finite-temperature-path-integral.md) 那一步高斯积分。

---

## 6. 欧氏与热核（N002 正文专用）

$$
K(q',q;\beta)\equiv\langle q'|e^{-\beta H}|q\rangle,
\qquad
Z(\beta)=\mathrm{Tr}\,e^{-\beta H}=\int dq\,K(q,q;\beta)
$$

$$
\mathrm{Tr}\,e^{-\beta H}
=\oint_{q(0)=q(\beta)}\mathcal{D}q\;e^{-S_E[q]}
$$

$$
e^{-\beta H}=\lim_{N\to\infty}\left(e^{-\beta H/N}\right)^{N},
\qquad
e^{-\varepsilon(\hat T+\hat V)}=e^{-\varepsilon\hat V}e^{-\varepsilon\hat T}\left(1+\mathcal{O}(\varepsilon^2)\right)
$$

短时核（用 §4.1 的谱分解 + §4.2 的对角判据拼出来）：

$$
\langle q'|e^{-\varepsilon H}|q\rangle
=\int\frac{dp}{2\pi}\,e^{ip(q'-q)}\,e^{-\varepsilon\left[p^2/2m+V(q)\right]}
$$

**一句话串起来**：切片给了乘积的核（§3.3），$V$ 那块用对角判据吃掉（§4.2），动能那块用谱分解吃成傅里叶积分（§4.1），剩下的就是高斯积分（§5.4）。四步，一个都不多。

---

## 7. 恢复 $\hbar$

| $\hbar=1$（本仓库） | 恢复 $\hbar$ |
|---|---|
| $\langle q\lvert p\rangle=e^{ipq}$ | $e^{ipq/\hbar}$ |
| $\int\dfrac{dp}{2\pi}\lvert p\rangle\langle p\rvert$ | $\int\dfrac{dp}{2\pi\hbar}\lvert p\rangle\langle p\rvert$ |
| $\langle p\lvert p'\rangle=2\pi\delta(p-p')$ | $2\pi\hbar\,\delta(p-p')$ |
| $\hat p=-i\partial_q$ | $-i\hbar\,\partial_q$ |
| $[\hat q,\hat p]=i$ | $i\hbar$ |
| $e^{-ia\hat p}\lvert q\rangle=\lvert q+a\rangle$ | $e^{-ia\hat p/\hbar}\lvert q\rangle=\lvert q+a\rangle$ |
| 高斯宽度 $\sqrt{\varepsilon/m}$ | $\sqrt{\hbar\varepsilon/m}$ |

**最后一行值得盯一眼**：宽度正比于 $\sqrt{\hbar}$，所以 $\hbar\to0$ 时历史塌缩到经典轨道——这就是"稳相近似"的定量内容，也是 [N002 §1.2](N002-finite-temperature-path-integral.md) 说"经典极限从相位稳定点掉出来"的具体机制。

---

## 8. 一致性检验

| 检验 | 结果 |
|---|---|
| 两条完备性互相封闭 | 代入分别得 $\delta(q-q')$ 与 $2\pi\delta(p-p')$，成立 |
| 平面波给出本征值 | $-i\partial_q e^{ipq}=p\,e^{ipq}$，$i\partial_p e^{ipq}=q\,e^{ipq}$，成立 |
| 自由热核的短时极限 | 宽度 $\sqrt{\varepsilon/m}\to 0$，核趋于 $\delta(q-q')$，成立 |
| 函数演算与核的两种算法 | 谱分解与级数展开给出同一个核，成立 |
| 迹的基无关性 | $q$ 基与 $p$ 基给出同一个数，成立 |
| 量纲（$\hbar=1$） | $q$ 与 $p$ 互为倒数，$\langle q\lvert p\rangle$ 的指数无量纲，成立 |
| 量纲（恢复 $\hbar$） | 高斯宽度 $\sqrt{\hbar\varepsilon/m}$ 是长度，$\varepsilon$ 是时间，成立 |

---

## 9. 我一开始错在哪

这一节按错误被发现的顺序写，越靠前越基础。

1. **把 $\lvert q\rangle$ 当成可归一化的向量。** 看到 $\langle q\lvert q\rangle=\delta(0)=\infty$ 以为算错了。
   实际是连续谱，本征矢在 rigged Hilbert space 里，一切等式都在分布意义下成立。**凡见 $\delta(0)$，那是"对角元个数"的记账，不是灾难。**

2. **以为 $\langle q\lvert q'\rangle=\delta$ 与 $\langle p\lvert p'\rangle=2\pi\delta$ 的不对称是错误。** 总觉得两个基应该一样。
   实际是 $dp$ 前面那个 $2\pi$ 把不对称收走了：**两个基各自自洽，之间的转换才自洽。**

3. **把 $V(q)$ 与 $V(q')$ 的差别当成立刻存在。** 以为"算子排序"从一开始就留下 $\mathcal{O}(\varepsilon)$ 或 $\mathcal{O}(\varepsilon^{3/2})$ 的修正。
   实际单看 $e^{-\varepsilon V(\hat q)}$ 这一因子，$\delta$ 把 $q'$ 与 $q''$ 钉死，两者**精确**相等；差别只在 $\delta$ 被 $p$ 积分抹成有限宽度的核之后才出现，量级 $\mathcal{O}(\varepsilon^{3/2})$。

4. **以为 $\hat p=-i\partial_q$ 是"定义"。** 于是遇到别的表象就不知道怎么办。
   实际定义只有 $[\hat q,\hat p]=i$；$-i\partial_q$ 是这条对易关系在 $q$ 表象下的**长相**。换表象就换长相，比如 $\hat q=i\partial_p$。

5. **遇到 $\int\frac{dp}{2\pi}$ 以为 $2\pi$ 是"凑出来的"或"习惯写法"。** 于是复制到别处时就漏。
   实际它来自 $\int\frac{dp}{2\pi}e^{ipx}=\delta(x)$，而后者来自 $\delta$ 的定义——**改 $2\pi$ 等于改 $\delta$**。

6. **把 §2.1 那个路径积分的上下限当积区间。** 读过 $\int_a^b dx$ 再看 $\int_{q(0)=q_i}^{q(\beta)=q_f}\mathcal{D}q$，第一反应是"这是不是 $\tau$ 从 $0$ 到 $\beta$ 的积分"。
   实际那是**定义域约束**（被积变量是整条函数），不是积分区间；等价写法是乘两个泛函 $\delta$，[N002 §2.4](N002-finite-temperature-path-integral.md) 的取迹就是把这两个 $\delta$ 拿掉。

---

## 10. 混用陷阱（照此自查）

| 陷阱 | 症状 |
|---|---|
| 用 $dp/2\pi$ 却写 $\langle p\lvert p'\rangle=\delta$ | 少一个 $2\pi$，高斯积分结果差 $2\pi$ 的幂 |
| 对称归一化与常用归一化混用 | 内积少一个 $\sqrt{2\pi}$，且不在量纲上暴露 |
| $\hat p$ 在 $q$ 基写成 $+i\partial_q$ | 符号错，推出 $[\hat q,\hat p]=-i$ |
| 对 $\delta$ 做非线性变换不留 $\lvert f'\rvert$ | 数值与量纲同时错 |
| 用 $\delta(0)$ 却不说明它是 $\int dq$ | 发散来路不明，无法判断能否约掉 |
| 把 $q'$、$q''$、$q$ 三个符号混着用 | 插完备性时少插一次，路径积分少一段 |

---

## 11. 与 N002 的落点

| N002 位置 | 依赖本页哪一条 |
|---|---|
| §1.1 路径积分 | 无（那是定义，不是推导） |
| §2.1 切片 | §2 完备性、§3.3 乘积的核、§6 半群 |
| §2.2 单片核 | §4.1 第二行、§4.2 对角判据、§5.4 高斯 |
| §2.3 连续极限 | §5.4、§5.3（测度归一化） |
| §2.4 取迹 | §5.2 迹的基无关性 |
| §4.1 自由粒子 | §5.3（那个 $L$） |
| §4.2 谐振子行列式 | §4.1（$\det$ 来自谱分解的谱） |

---

## 12. 自检

- [ ] 不看本页，写出 §0 的五条，并指出哪一条是物理输入
- [ ] 从 $\langle q\lvert p\rangle=e^{ipq}$ 出发，推出 $\langle p\lvert p'\rangle=2\pi\delta(p-p')$
- [ ] 用对角判据（§4.2）证明 $\langle q'\lvert f(\hat q)\lvert q''\rangle$ 必然正比于 $\delta$，不展开级数
- [ ] 把 [N002 §2.2](N002-finite-temperature-path-integral.md) 那一行按 §4.1 + §4.2 重新拆成两步，说清哪一步用了什么
- [ ] 恢复 $\hbar$ 后重算高斯宽度，说明为什么它随 $\hbar\to0$ 收缩
- [ ] 解释为什么 §9 第 3 条里"排序差别"单看一个因子时不存在
