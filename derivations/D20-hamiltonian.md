# D20 · Hamiltonian 与时间演化

> 建档 2026-11-08 · 上游：[D00](D00-commutator-axiom.md)、[D05](D05-functional-calculus.md)、[D08](D08-diagonal-criterion.md)
> 下游：[D21](D21-path-integral-representation.md)、[D23](D23-density-matrix.md)、[D26](D26-energy-basis.md)
> 本卡补的是"$\hat H$ 从哪来"——[D21](D21-path-integral-representation.md) 一上来就写 $e^{-\beta H}$，却从没交代过它。

---

## 0. 命题

$$
\hat H=\frac{\hat p^{2}}{2m}+V(\hat q),
\qquad
\lvert\psi(t)\rangle=e^{-i\hat Ht}\lvert\psi(0)\rangle,
\qquad
i\,\partial_{t}\lvert\psi\rangle=\hat H\lvert\psi\rangle
$$

**它在讲什么**：$\hat H$ 是"动能 + 位能"两块的叠加。**它不是一个从公理推出来的东西，而是三项要求逼出来的最小形式**。

---

## 1. 为什么是这个形式

| 要求 | 逼出的部分 |
|---|---|
| 平移应当由某个自伴算子生成（[D16](D16-translation.md)） | 动能必须是 $\hat p$ 的函数，最低阶是 $\hat p^{2}/2m$ |
| 位置测量要有"势"（经典极限 $\to V(q)$） | 位能是 $\hat q$ 的函数 $V(\hat q)$，在 $q$ 基对角（[D08](D08-diagonal-criterion.md)） |
| 概率守恒（演化必须酉） | $\hat H$ 必须**自伴**（[D05](D05-functional-calculus.md) 的酉判据） |

**第三条最要紧**：不是"我们喜欢自伴"，而是**只有自伴的生成元才给出酉演化**，酉演化才保住概率。

---

## 2. 三条直接后果

**① 演化算子酉。** $\hat H$ 自伴随 $\Rightarrow$ $\lVert e^{-i\hat Ht}\rVert=1$（[D05](D05-functional-calculus.md) §2.2 的酉判据），故

$$
\langle\psi(t)\lvert\psi(t)\rangle=\langle\psi(0)\lvert\psi(0)\rangle
$$

**② 定态。** 若 $\hat H\lvert E\rangle=E\lvert E\rangle$，则

$$
\lvert\psi(t)\rangle=e^{-iEt}\lvert E\rangle
$$

——只差一个相位，所有概率都不随时间变。

**③ 欧氏化。** 取 $\beta=it$：

$$
e^{-i\hat Ht}\;\longrightarrow\;e^{-\beta\hat H}
$$

**这件事的意义**：实时间下是"振荡"（$\lvert e^{-iEt}\rvert=1$），虚时间下变成"衰减"（$e^{-\beta E}$）。**这是下游全部内容的起点。**

---

## 3. 一致性检验

| 检验 | 结果 |
|---|---|
| 概率守恒 | $\frac{d}{dt}\langle\psi\lvert\psi\rangle=\langle\psi\lvert i\hat H^{\dagger}-i\hat H\lvert\psi\rangle=0$ ✅ |
| 经典极限 | 位能 $V(\hat q)$ 在 $\hbar\to0$ 时回到经典势 ✅ |
| 与 [D08](D08-diagonal-criterion.md) 相容 | $V(\hat q)$ 在 $q$ 基对角，故 $\langle q\lvert V(\hat q)\lvert q'\rangle=V(q)\delta(q-q')$ ✅ |

---

## 4. 边界

1. **这是非相对论的。** 相对论要用场（[D15](D15-stone-von-neumann.md) §6 的失效条件），$\hat p^{2}/2m$ 换成 Dirac 或 Klein–Gordon 型。
2. **时间在量子力学里是参数，不是算子。** 本卡的 $t$ 不是可观测量；这是 [P11](../problems/P11-problem-of-time.md) 的入口。
3. **$V$ 的形式是输入。** 谐振子、库仑势、自由粒子，都是你选的，不是推出来的。
4. **多粒子要加张量积与相互作用项**，本卡只写单粒子。

---

## 5. 自检

- [ ] 说明为什么 $\hat H$ 必须自伴，以及这与概率守恒的关系
- [ ] 写出欧氏化的替换，并说明"振荡→衰减"意味着什么
- [ ] 说明定态为什么"概率不随时间变"
- [ ] 指出本卡哪一条是物理输入（不是推导）
