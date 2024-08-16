from pathlib import Path
import pathlib
import os.path


def to_file(data: list[str], category: str, filename: str, extension: str) -> None:
  pathlib.Path(os.path.join("Output", category)).mkdir(parents=True, exist_ok=True)
  output_path = Path(os.path.join("Output", category, filename + extension))
  output_path.write_text("\n".join(data), encoding="utf-8")
