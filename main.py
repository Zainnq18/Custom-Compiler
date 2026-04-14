# ============================================================
#  Compiler Driver  –  main.py
#  Usage:  python main.py <source_file>
# ============================================================

import sys
import os
from lexer  import Lexer
from parser import Parser
from icg    import IntermediateCodeGenerator
from codegen import CodeGenerator


def compile_source(source_code: str, source_filename: str = "input"):
    """
    Full compiler pipeline.
    Returns (listing_text, target_code_text, had_errors).
    """
    source_lines = source_code.splitlines()

    # ── Collect all errors from every phase ──────────────────
    all_errors = []   # list of (line_no, message)

    # ── Phase 1 : Lexical Analysis ───────────────────────────
    print("[ Phase 1 ] Lexical Analysis...")
    lexer = Lexer(source_code)
    tokens, lex_errors = lexer.tokenize()
    for e in lex_errors:
        all_errors.append((e.line, str(e)))

    # ── Phase 2 : Parsing ────────────────────────────────────
    print("[ Phase 2 ] Parsing / Syntax Analysis...")
    parser = Parser(tokens)
    ast, parse_errors = parser.parse()
    for e in parse_errors:
        all_errors.append((e.line, str(e)))

    # ── Phase 3 : Intermediate Code Generation ───────────────
    tac_instructions = []
    tac_text = ""
    if not all_errors:
        print("[ Phase 3 ] Intermediate Code Generation...")
        icg = IntermediateCodeGenerator()
        tac_instructions, icg_errors = icg.generate(ast)
        for e in icg_errors:
            all_errors.append((e.line, str(e)))
        tac_text = '\n'.join(str(i) for i in tac_instructions)
    else:
        print("[ Phase 3 ] Skipped (errors in earlier phase)")

    # ── Phase 4 : Code Generation ────────────────────────────
    target_code = ""
    if not all_errors:
        print("[ Phase 4 ] Code Generation...")
        cg = CodeGenerator(tac_instructions)
        target_code = cg.generate()
    else:
        print("[ Phase 4 ] Skipped (errors present — no target code generated)")

    # ── Build listing file ───────────────────────────────────
    listing_lines = []
    listing_lines.append("=" * 70)
    listing_lines.append(f"  COMPILER LISTING  :  {source_filename}")
    listing_lines.append("=" * 70)
    listing_lines.append("")

    # Group errors by line
    err_by_line = {}
    for (lineno, msg) in all_errors:
        err_by_line.setdefault(lineno, []).append(msg)

    for idx, src_line in enumerate(source_lines, start=1):
        listing_lines.append(f"{idx:4d}  |  {src_line}")
        if idx in err_by_line:
            for msg in err_by_line[idx]:
                listing_lines.append(f"      ***  {msg}")

    # Errors not tied to a specific line
    if 0 in err_by_line:
        for msg in err_by_line[0]:
            listing_lines.append(f"      ***  {msg}")

    listing_lines.append("")
    listing_lines.append("=" * 70)
    if all_errors:
        listing_lines.append(f"  Compilation FAILED  –  {len(all_errors)} error(s) found.")
    else:
        listing_lines.append("  Compilation SUCCESSFUL  –  No errors.")
    listing_lines.append("=" * 70)

    # Append token list
    listing_lines.append("")
    listing_lines.append("──── TOKEN LIST ────")
    for tok in tokens:
        listing_lines.append(f"  {tok}")

    # Append TAC if generated
    if tac_text:
        listing_lines.append("")
        listing_lines.append("──── INTERMEDIATE CODE (TAC) ────")
        listing_lines.append(tac_text)

    listing_text = '\n'.join(listing_lines)
    return listing_text, target_code, bool(all_errors)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <source_file>")
        sys.exit(1)

    src_path = sys.argv[1]
    if not os.path.exists(src_path):
        print(f"Error: File '{src_path}' not found.")
        sys.exit(1)

    with open(src_path, 'r') as f:
        source_code = f.read()

    base = os.path.splitext(src_path)[0]
    listing_path = base + ".lst"
    target_path  = base + ".asm"

    listing_text, target_code, had_errors = compile_source(
        source_code, os.path.basename(src_path))

    # Write listing file
    with open(listing_path, 'w') as f:
        f.write(listing_text)
    print(f"\nListing written to : {listing_path}")

    # Write target code only if no errors
    if not had_errors:
        with open(target_path, 'w') as f:
            f.write(target_code)
        print(f"Target code written: {target_path}")
    else:
        print("Target code NOT generated due to errors.")

    print()
    print(listing_text)


if __name__ == '__main__':
    main()
