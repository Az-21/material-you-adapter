from pathlib import Path


def kt_theme_file(source_path: Path) -> str:
  return source_path.read_text(encoding="utf-8")
