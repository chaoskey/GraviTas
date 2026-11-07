# D14 · $\langle q\lvert p\rangle=e^{ipq}$

> 建档 2026-11-06 · 上游：[D00](D00-commutator-axiom.md)、[D13](D13-translation.md)、[D12](D12-weyl-phase.md)、[D03](D03-stone-von-neumann.md)；默认：D04、D01
> 下游：[D15](D15-p-completeness.md)、[D16](D16-momentum-representation.md)、[D17](D17-path-integral-representation.md)
> 原为 [N003 §0.5](../notes/N003-basis-and-operator-relations.md) 的三步概括，2026-11-06 补全并移入网格。

---

## 0. 命题

$$
\langle q\lvert p\rangle=e^{ipq}
$$

**适用条件**（缺一不可，这是本条最要紧的部分）：

1. $\hat q$ 的谱**简单**（重数为 $1$）、纯绝对连续、等于 $\mathbb{R}$——于是有 $\delta$ 归一化的 $\lvert q\rangle$；
2. 位置与动量满足 Weyl 关系（[D12](D12-weyl-phase.md)）；
3. 归一化方案：$\langle q\lvert q'\rangle=\delta(q-q')$、$\langle p\lvert p'\rangle=2\pi\delta(p-p')$；
4. 相位约定：本征矢的相位取到使 $\langle 0\lvert p\rangle=1$（见 §1 第五步）。

**推导的层次**（这一点必须说清，否则会把"引用定理"当成"证明"）：

| 部分 | 谁负责 | 能否推 |
|---|---|---|
| **模长** $\lvert\langle q\lvert p\rangle\rvert=1$ | 归一化（§1 第五步） | **可推** |
| **相位线性于 $pq$** | 平移性质（§1 第一至四步） | **可推** |
| 整体相位 | 约定 | 不可推 |
| 这个表示**存在且唯一** | Stone–von Neumann | **不可推，只能引用** |

**它在讲什么**：位置本征态与动量本征态的重叠是平面波。等价说法是"$\hat p$ 在 $q$ 表象下是 $-i\partial_q$"——但这句等价性依赖上面的全部条件。

---

## 1. 证明

### 1.1 第一步：$e^{ia\hat p}$ 在谱上是平移

由 [D09](D09-two-term-truncation.md)（取 $A=ia\hat p$、$B=\hat q$）：

$$
[A,B]=ia[\hat p,\hat q]=ia\cdot(-i)=a
$$

$a$ 是数，故

$$
e^{ia\hat p}\,\hat q\,e^{-ia\hat p}=\hat q+a
$$

（这正是 [D13](D13-translation.md) 的起点。）

### 1.2 第二步：作用到本征矢上

右乘 $e^{ia\hat p}$：

$$
e^{ia\hat p}\hat q=(\hat q+a)e^{ia\hat p}
$$

作用在 $\lvert q\rangle$ 上并整理：

$$
\hat q\bigl(e^{ia\hat p}\lvert q\rangle\bigr)=(q-a)\bigl(e^{ia\hat p}\lvert q\rangle\bigr)
$$

由条件 1（重数为 $1$）：

$$
e^{ia\hat p}\lvert q\rangle=\phi(a,q)\lvert q-a\rangle,
\qquad \lvert\phi\rvert=1
$$

### 1.3 第三步：把相位 $\phi$ 规范掉

由群律 $e^{i(a+a')\hat p}=e^{ia\hat p}e^{ia'\hat p}$ 得余圈条件

$$
\phi(a+a',q)=\phi(a,q)\,\phi(a',q-a)
$$

重新定义基矢 $\lvert q\rangle\to e^{i\chi(q)}\lvert q\rangle$，则 $\phi\to\phi\,e^{i\chi(q)-i\chi(q-a)}$。差分方程可解（$\mathbb{R}$ 单连通，无拓扑障碍），故可取 $\phi=1$：

$$
e^{ia\hat p}\lvert q\rangle=\lvert q-a\rangle
$$

### 1.4 第四步：把 $\lvert q\rangle$ 与 $\lvert 0\rangle$ 连起来

在第三步中取 $a=-q$：

$$
e^{-iq\hat p}\lvert 0\rangle=\lvert q\rangle
\quad\Longrightarrow\quad
\langle q\lvert=\langle 0\lvert\,e^{iq\hat p}
$$

又由函数演算，$\hat p\lvert p\rangle=p\lvert p\rangle$ 给出

$$
e^{iq\hat p}\lvert p\rangle=e^{iqp}\lvert p\rangle
$$

于是

$$
\langle q\lvert p\rangle=\langle 0\lvert e^{iq\hat p}\lvert p\rangle
=e^{ipq}\,\langle 0\lvert p\rangle
$$

记 $c(p)\equiv\langle 0\lvert p\rangle$，则

$$
\langle q\lvert p\rangle=e^{ipq}\,c(p)
$$

### 1.5 第五步：$\lvert c(p)\rvert=1$ 由归一化逼出

用完备性 $\int dq\lvert q\rangle\langle q\rvert=\mathbb{1}$：

$$
\langle p\lvert p'\rangle
=\int dq\;\overline{\langle q\lvert p\rangle}\,\langle q\lvert p'\rangle
=\overline{c(p)}\,c(p')\int dq\;e^{i(p'-p)q}
=2\pi\delta(p-p')\,\overline{c(p)}\,c(p')
$$

按条件 3，$\langle p\lvert p'\rangle=2\pi\delta(p-p')$，故

$$
\lvert c(p)\rvert^{2}=1
$$

**这一步是"模长为 1"的真正来源**——不是假设，是归一化逼出来的。

再取 $c(p)=1$（条件 4 的相位约定），得

$$
\boxed{\ \langle q\lvert p\rangle=e^{ipq}\ }
$$

**证毕。**

---

## 2. 一致性检验

| 检验 | 结果 |
|---|---|
| 模长 | $\lvert e^{ipq}\rvert=1$，与第五步一致 ✅ |
| 回到波函数 | $\psi_p(q)=e^{ipq}$，正是 $\hat p=-i\partial_q$ 的本征函数：$-i\partial_q e^{ipq}=p\,e^{ipq}$ ✅ |
| 直接模型验算 | 取 $\langle x\lvert q\rangle=\delta(x-q)$、$\langle x\lvert p\rangle=e^{ipx}$，则 $\langle q\lvert p\rangle=\int dx\,\delta(x-q)e^{ipx}=e^{ipq}$ ✅ |
| 与 D13 相容 | $\langle q\lvert=\langle 0\lvert e^{iq\hat p}$ 正是 [D13](D13-translation.md) 取 $a=-q$ ✅ |
| $q\to0$ | $\langle 0\lvert p\rangle=1$，与相位约定一致 ✅ |

**注意第三行只是"存在一个模型使结论成立"，不是证明。** 唯一性仍靠 Stone–von Neumann——举一个例子 ≠ 证明所有情形。

---

## 3. 备注与边界

1. **$c(p)$ 的模长是定理，整体相位是约定。** 混淆这两者会在换基时"证出"矛盾。
2. **重数大于 $1$ 时结论变形。** 若 $\hat q$ 有内部指标，第一步给的是 $\sum_j S_{ij}(a)\lvert q-a,j\rangle$，于是

$$
\langle q,i\lvert p,j\rangle=e^{ipq}\,c_{ij}(p)
$$

且第五步只给出"$c$ 是酉矩阵"，不是"$c$ 是相位"。这就是 [N003 §0.5](../notes/N003-basis-and-operator-relations.md) 里 $\delta_{ij}$ 的来源——**谱的重数 = 内部自由度数**。

3. **Stone–von Neumann 负责的是"存在且唯一"。** 本卡片的五步只证明：**若**存在这样的表示，则重叠必为 $e^{ipq}$（差归一化）。存在性与唯一性无法由这五步得到，必须引用定理。**把引用当证明，是本条最常见的误读。**

4. **符号约定。** 若取 $[\hat q,\hat p]=-i$（即 $\hat p=+i\partial_q$），则结果变为 $e^{-ipq}$。判据仍是 [D13](D13-translation.md)：看 $e^{ia\hat p}\lvert q\rangle$ 移到 $q+a$ 还是 $q-a$。

5. **无穷自由度时失效。** 表示不唯一，"平面波"不再有唯一含义；这是量子场论的入口。

---

## 4. 自检

- [ ] 不看本文，从 $e^{ia\hat p}\hat qe^{-ia\hat p}=\hat q+a$ 推出 $e^{ia\hat p}\lvert q\rangle=\lvert q-a\rangle$
- [ ] 说明为什么 $\langle q\lvert p\rangle=e^{ipq}c(p)$ 里的 $c(p)$ 模长必为 $1$
- [ ] 指出推导中**哪一部分**依赖 Stone–von Neumann，哪一部分不依赖
- [ ] 说清重数大于 $1$ 时结论如何变形
- [ ] 举出一个具体模型验证结论，并说明"举模型"为什么不算证明
- [ ] 说明符号约定如何决定结果是 $e^{ipq}$ 还是 $e^{-ipq}$
