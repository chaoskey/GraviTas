# 推导网格

> 建档 2026-11-06 · 关联：[AGENTS](../AGENTS.md)、[notes/](../notes/)、[problems/](../problems/)
> 用途：给每一个**单命题推导**一个稳定编号，便于被笔记、档案、日志引用，避免同一件事在三个地方各写一遍。

---

## 0. 这一页是什么

**一个命题一张卡片，一个编号，正文放别处。**

- `notes/N###` 是**叙事**：一个主题、一条线、可以很长，可以有"我一开始错在哪"。
- `derivations/D##` 是**卡片**：一个命题、一个证明、一组检验，通常一页以内。

两者的关系：笔记里需要某个中间结论时，不再重推一遍，而是引用编号（例：见 D09）。卡片里需要长篇背景时，指向笔记（例：见 [N004](../notes/N004-hadamard-lemma.md)）。

**这意味着什么**：以后你在任何地方写下一个"因为 $X$，所以 $Y$"，先查网格里有没有编号。有就引用，没有就新建一张卡片。重复推导是漂移的开始。

---

## 1. 编号规则

| 规则 | 内容 |
|---|---|
| 格式 | `D` 加两位数字：**`D00` 保留给公理**；`D01`–`D99` 为推导 |
| 唯一性 | 全局唯一，**永不复用** |
| **顺序** | **输入编号必须小于自身编号**（拓扑序）。新增卡片必须排在它**所有输入之后** |
| 稳定性 | 编号一旦满足次序就不再改动；改命题就新建编号（见"废弃"） |
| 废弃 | 命题要换时新建编号，旧编号标"已废弃，见 D##"，**不删除** |
| 文件名 | `derivations/D##-短横线英文名.md` |

**为什么强制"输入在前"**：任何卡片的上游只出现在**更小编号**里，顺着编号读就是一条合法的推导顺序，依赖图不会"往回跳"。这比"按登记顺序"更严；代价是**新增一条基础结论时要重排后面所有编号**——所以能放末尾就放末尾。

**一次性重排记录**：2026-11-07 从旧的"登记顺序"整体重排为拓扑序（此前 D01–D20 全部换号，文件同时改名）。此后遵守上表。

---

## 2. 网格

| 编号 | 命题 | 输入 | 全文 | 状态 |
|---|---|---|---|---|
| D00 | **公理**：$[\hat q,\hat p]=i$（Weyl 形式） | — | [D00](D00-commutator-axiom.md) | ✓ |
| D01 | 谱定理与 Gelfand–Maurin（引用卡） | 外部定理 | [D01](D01-spectral-theorem.md) | ✓ |
| D02 | 位置本征方程：$\hat q\lvert q\rangle=q\lvert q\rangle$，并推出正交归一 | D01 | [D02](D02-position-eigen-equation.md) | ✓ |
| D03 | 归一化约定：$\langle q\lvert q'\rangle=\delta(q-q')$（形式被迫、系数自选） | D01、D02 | [D03](D03-normalization-convention.md) | ✓ |
| D04 | Stone–von Neumann（引用卡） | 外部定理 | [D04](D04-stone-von-neumann.md) | ✓ |
| D05 | 函数演算：$f(\hat A)$ 的定义（幂级数 / 谱分解 / 本征基展开） | D01 | [D05](D05-functional-calculus.md) | ✓ |
| D06 | $[\hat q,\hat p]=i$ 推出 $[\hat p,f(\hat q)]=-i f'(\hat q)$ | D00（默认 D05；旁证 D01） | [D06](D06-commutator-p-fq.md) | ✓ |
| D07 | 对角判据：$[\hat q,f(\hat q)]=0\Rightarrow$ 核 $\propto\delta$ | D00、D01、D02、D03 | [D07](D07-diagonal-criterion.md) | ✓ |
| D08 | 乘积的核：$\langle q'\lvert\hat A\hat B\lvert q''\rangle=\int dq\cdots$ | D01 | [D08](D08-product-kernel.md) | ✓ |
| D09 | Hadamard 引理：$e^{A}Be^{-A}=\sum_{n}\frac{1}{n!}\mathrm{ad}_A^{\,n}B$ | —（默认：D05） | [D09](D09-hadamard-lemma.md) | ✓ |
| D10 | 两项截断：$[A,B]=c$ 是数时 $e^{A}Be^{-A}=B+c$ | D09 | [D10](D10-two-term-truncation.md) | ✓ |
| D11 | $e^{A}e^{B}=e^{c}e^{B}e^{A}$（$[A,B]=c$ 是数） | D10（默认：D05） | [D11](D11-commutator-phase.md) | ✓ |
| D12 | 三条 BCH 闭式：$e^{A}e^{B}=e^{c/2}e^{A+B}$ 等 | D09、D10、D11（默认：D05） | [D12](D12-three-bch-forms.md) | ✓ |
| D13 | Weyl 相位：$e^{ia\hat p}e^{ib\hat q}=e^{iab}e^{ib\hat q}e^{ia\hat p}$ | D00、D11（默认：D05） | [D13](D13-weyl-phase.md) | ✓ |
| D14 | 平移：$e^{ia\hat p}\lvert q\rangle=\lvert q-a\rangle$ | D00、D02、D03、D10（默认：D05） | [D14](D14-translation.md) | ✓ |
| D15 | $\langle q\lvert p\rangle=e^{ipq}$ | D00、D03、D04、D13、D14（默认：D05、D01） | [D15](D15-qp-overlap.md) | ✓ |
| D16 | 动量基的完备性：$\int\frac{dp}{2\pi}\lvert p\rangle\langle p\rvert=\mathbb{1}$ | D01、D03、D15 | [D16](D16-p-completeness.md) | ✓ |
| D17 | $\hat p$ 在 $q$ 表象下是 $-i\partial_q$ | D00、D15、D16（默认：D01） | [D17](D17-momentum-representation.md) | ✓ |
| D18 | 路径积分表示：$\langle q_f\lvert e^{-\beta H}\lvert q_i\rangle=\int\mathcal{D}q\,e^{-S_E}$ | D00、D15、D08、D16（默认：D01） | [D18](D18-path-integral-representation.md) | ✓ |
| D19 | 迹即闭合路径：$\mathrm{Tr}\,e^{-\beta H}=\oint\mathcal{D}q\,e^{-S_E}$ | D18（默认：D01） | [D19](D19-trace-is-loop.md) | ✓ |
| D20 | 不确定关系 $\Delta q\,\Delta p\ge\frac{1}{2}$ | D00、D01 | [D20](D20-uncertainty.md) | ✓ |

**状态含义**：✓ 已逐行核对；○ 草稿；✗ 已废弃（并在"全文"列写明去哪找）。

**"输入"列的两种标记**：

- **（默认 Dxx）**——该卡隐式使用 Dxx，为不使表格臃肿而单列。典型例子：凡出现 $e^{X}$ 的卡片都默认使用 D05（函数演算），凡出现 $\lvert q\rangle$ 或完备性的都默认使用 D01（谱定理）。
- **（旁证 Dxx）**——只在另证或备注中用到，主证明不需要。

**硬性约束**：任何条目的输入——**含默认与旁证**——其编号都必须**小于自身编号**。这条由脚本逐条校验过（见 §2.1）。

### 2.1 依赖分层（编号即拓扑序）

| 层 | 卡片 | 输入 |
|---|---|---|
| 0 | **D00 公理** | —（唯一输入） |
| 1 | **D01 谱定理**、**D04 S–vN** | 外部定理 |
| 2 | D05 函数演算 | D01 |
| 3 | D06 对易子公式、D07 对角判据、D08 乘积的核、D20 不确定关系 | D00、D01、D05 |
| 4 | D09 Hadamard | D05 |
| 5 | D10 两项截断 | D09 |
| 6 | D11 交换相位 | D10 |
| 7 | D12 三条 BCH、D13 Weyl 相位、D14 平移 | D09、D10、D11、D00 |
| 8 | D15 $\langle q\lvert p\rangle$ | D00、D14、D13、D04 |
| 9 | D17 动量表示、D18 路径积分 | D00、D15、D01、D08 |
| 10 | D19 迹即闭合路径 | D18 |

**这张表的用法**：只要每一行的"输入"列里出现的编号都**小于**本行编号，全表就自洽。**加卡片之前先查这一列**，否则就要重排。

**三条主干**：

- **代数主干**：D09 → D10 → D11 → D12 / D13（从 Hadamard 到 BCH 与 Weyl 相位）；
- **表象主干**：D14 → D15 → D17（从平移到平面波到 $\hat p=-i\partial_q$）；
- **统计主干**：D15、D08 → D18 → D19（从平面波与乘积核到路径积分到取迹）。

**D01、D04 是地基**：两张引用卡，不证但被多处默认使用（见上表下方说明）。

---

## 3. 新增一条推导

1. 取下一个未用编号 `D##`。
2. 在 `derivations/D##-英文短语.md` 建卡片，按下面的模板写。
3. 在上表登记：编号、命题（一行 LaTeX）、输入（编号或"公理"或"外部定理"）、全文（相对链接）、状态。
4. 若它改变了已有推导的依赖关系，同步更新"输入"列。

### 卡片模板

```markdown
# D## · 命题的一句话名字

> 建档 YYYY-MM-DD · 上游：D0X / 公理 / 外部定理
> 下游：被谁使用

## 0. 命题（含适用条件）

## 1. 证明

## 2. 一致性检验

至少两条：退化情形、极限、量纲、与已知结果对照。

## 3. 备注与边界

这条在什么条件下失效；哪些步骤是形式的。

## 4. 自检
```

**硬规则**（与 [AGENTS](../AGENTS.md) 同源）：

- 命题必须写**适用条件**（对 $f$ 的要求、算子是否有界、是否要求解析）；
- 证明不得引用未登记的中间结论——要么给出，要么引编号；
- 公式用 LaTeX；中文不进数学环境；
- 卡片只增不改；命题变了就新建编号。

---

## 4. 待办

- [ ] 把 [N001 §2](../notes/N001-hawking-temperature.md) 的 $\beta=2\pi/\kappa$ 独立成卡片
- [ ] 高斯积分 $\int e^{-ap^{2}+bp}$ 是否值得单独编号（出现频率高，但太初等）
