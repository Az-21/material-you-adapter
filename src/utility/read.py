import os
import zipfile
from pathlib import Path


def kt_theme_file(source_path: Path) -> str:
  return source_path.read_text(encoding="utf-8")


def kt_theme_file_from_zips(input_folder):
  color_kt_files = {}

  for file_name in os.listdir(input_folder):
    if file_name.endswith(".zip"):
      zip_path = os.path.join(input_folder, file_name)
      try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
          if "ui/theme/Color.kt" in zip_ref.namelist():
            with zip_ref.open("ui/theme/Color.kt") as color_kt_file:
              content = color_kt_file.read().decode("utf-8")
              color_kt_files[file_name] = content
          else:
            print(f"'ui/theme/Color.kt' not found in {file_name}")
      except zipfile.BadZipFile:
        print(f"Error: {file_name} is not a valid zip file.")

  return color_kt_files
