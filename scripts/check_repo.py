#!/usr/bin/env python3
"""
GraviTas 仓库自检。

检查项：
  1. problems/*.md 的 YAML front-matter 是否完整、字段是否合法
  2. id 与文件名是否一致、id 是否重复
  3. problems/README.md 的索引是否覆盖了所有问题档案
  4. 所有相对 Markdown 链接是否指向真实存在的文件
  5. 是否存在空档案（正文过短）

用法：
    python3 scripts/check_repo.py        # 正常检查
    python3 scripts/check_repo.py -v     # 打印每个文件的结果
"""

from __future__ import annotations

import datetime as _dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
INDEX = PROBLEMS_DIR / "README.md"

REQUIRED_FIELDS = ["id", "title", "cluster", "difficulty", "status", "prereq", "updated"]
VALID_STATUS = {"open", "candidate", "contested", "settled"}
VALID_CLUSTERS = {"信息与全息", "紫外完备", "时空的量子性质", "宇宙学", "检验"}

# 这些目录里的链接不参与检查（模板里是占位符）
SKIP_LINK_DIRS = {"templates", "scripts", ".git", "node_modules"}

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks = 0

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def ok(self) -> None:
        self.checks += 1


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """极简 front-matter 解析：只支持 `key: value` 与 `key: [a, b]`。"""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    data: dict[str, str] = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data, text[m.end():]


def parse_list(raw: str) -> list[str]:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    return [item.strip().strip("'\"") for item in raw.split(",") if item.strip()]


def iter_markdown() -> list[Path]:
    files = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in SKIP_LINK_DIRS:
            continue
        files.append(path)
    return files


def check_problems(report: Report, verbose: bool) -> set[str]:
    ids: set[str] = set()
    files = sorted(PROBLEMS_DIR.glob("P*.md"))
    if not files:
        report.error("problems/ 下没有找到任何 P*.md 档案")
        return ids

    for path in files:
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        fm, body = parse_front_matter(text)

        if not fm:
            report.error(f"{rel}: 缺少 YAML front-matter")
            continue

        missing = [f for f in REQUIRED_FIELDS if f not in fm]
        if missing:
            report.error(f"{rel}: front-matter 缺少字段 {missing}")
            continue

        pid = fm["id"]
        if not re.fullmatch(r"P\d{2}", pid):
            report.error(f"{rel}: id '{pid}' 不符合 P## 格式")
        if not path.name.startswith(pid):
            report.error(f"{rel}: 文件名与 id '{pid}' 不一致")
        if pid in ids:
            report.error(f"{rel}: id '{pid}' 重复")
        ids.add(pid)

        if fm["cluster"] not in VALID_CLUSTERS:
            report.error(
                f"{rel}: cluster '{fm['cluster']}' 不在 {sorted(VALID_CLUSTERS)} 中"
            )

        try:
            difficulty = int(fm["difficulty"])
            if not 1 <= difficulty <= 5:
                raise ValueError
        except ValueError:
            report.error(f"{rel}: difficulty '{fm['difficulty']}' 必须是 1–5 的整数")

        if fm["status"] not in VALID_STATUS:
            report.error(
                f"{rel}: status '{fm['status']}' 不在 {sorted(VALID_STATUS)} 中"
            )

        if len(parse_list(fm["prereq"])) < 1:
            report.error(f"{rel}: prereq 不能为空")

        try:
            _dt.date.fromisoformat(fm["updated"])
        except ValueError:
            report.error(f"{rel}: updated '{fm['updated']}' 不是 YYYY-MM-DD 格式")

        if len(body.strip()) < 400:
            report.warn(f"{rel}: 正文过短（{len(body.strip())} 字符），可能只是占位")

        report.ok()
        if verbose:
            print(f"  ok  {rel}")

    return ids


def check_index(report: Report, ids: set[str]) -> None:
    if not INDEX.exists():
        report.error("problems/README.md 不存在")
        return
    text = INDEX.read_text(encoding="utf-8")
    linked = {Path(t).stem.split("-")[0] for t in LINK_RE.findall(text) if Path(t).stem.startswith("P")}
    missing = sorted(ids - linked)
    extra = sorted(linked - ids)
    if missing:
        report.error(f"problems/README.md 索引缺少: {', '.join(missing)}")
    if extra:
        report.error(f"problems/README.md 索引指向不存在的档案: {', '.join(extra)}")
    report.ok()


def check_links(report: Report, verbose: bool) -> None:
    for path in iter_markdown():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("file:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                report.error(f"{rel}: 死链 -> {raw_target}")
        report.ok()
        if verbose:
            print(f"  ok  {rel}")


HARD_MATH = set("∫∑∏√∝≪≫∞∂∇²³½¼ħℓ")
GREEK = set("αβγδεζηθικλμνξπρστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ")

FENCE_RE = re.compile(r"```(\w*)\n(.*?)```", re.S)
INLINE_CODE_RE = re.compile(r"`([^`\n]*)`")


def looks_like_formula(text: str) -> bool:
    """粗糙但有用的判据：含等号/希腊字母/上标，且不是命令行。"""
    if "=" in text:
        return True
    if re.search(r"[\^]", text):
        return True
    return any(ch in GREEK for ch in text)


def strip_math_and_code(text: str) -> str:
    text = FENCE_RE.sub("", text)
    text = INLINE_CODE_RE.sub("", text)
    text = re.sub(r"\$\$.*?\$\$", "", text, flags=re.S)
    text = re.sub(r"\$[^$\n]*\$", "", text)
    return text


def check_math(report: Report) -> None:
    """公式必须用 LaTeX：不允许凑合写法（围栏块、行内代码、Unicode 符号）。"""
    for path in iter_markdown():
        rel = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")

        bare = INLINE_CODE_RE.sub("", text)
        if len(re.findall(r"(?<!\\)\$\$", bare)) % 2:
            report.error(f"{rel}: 行间公式 $$...$$ 不配对")

        for lineno, line in enumerate(bare.splitlines(), 1):
            if line.strip().startswith("```"):
                continue
            if len(re.findall(r"(?<!\\)\$", line)) % 2:
                report.error(f"{rel}:{lineno}: 行内 $ 不配对 -> {line.strip()[:50]}")

        for lang, body in FENCE_RE.findall(text):
            if lang or not looks_like_formula(body):
                continue
            snippet = body.strip().splitlines()[0][:50]
            report.error(f"{rel}: 公式写在围栏代码块里，请改成 $$...$$ -> {snippet}")

        for code in INLINE_CODE_RE.findall(text):
            if not looks_like_formula(code):
                continue
            if any(ch in "|" for ch in code):
                continue
            report.error(f"{rel}: 公式写在行内代码里，请改成 $...$ -> {code[:50]}")

        for lineno, line in enumerate(strip_math_and_code(text).splitlines(), 1):
            bad = sorted({ch for ch in line if ch in HARD_MATH})
            if bad:
                report.error(f"{rel}:{lineno}: Unicode 数学符号 {' '.join(bad)} -> {line.strip()[:50]}")
        report.ok()


def main(argv: list[str]) -> int:
    verbose = "-v" in argv or "--verbose" in argv
    report = Report()

    print("GraviTas 仓库自检")
    print("=" * 48)
    ids = check_problems(report, verbose)
    check_index(report, ids)
    check_links(report, verbose)
    check_math(report)

    print("-" * 48)
    print(f"问题档案: {len(ids)} 个   检查项: {report.checks}")
    for w in report.warnings:
        print(f"  !  {w}")
    for e in report.errors:
        print(f"  ✗  {e}")

    if report.errors:
        print(f"\n失败：{len(report.errors)} 个错误")
        return 1
    print("\n通过：仓库结构一致。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
