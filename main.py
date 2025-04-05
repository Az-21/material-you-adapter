import pathlib

from rich.console import Console

import src.format.power_fx as m3_power_fx
import src.format.python as m3_python
import src.format.tailwind as m3_tailwind
import src.format.typst as m3_typst
import src.parse.theme
import src.utility.read
import src.utility.save

console = Console()


class ThemeConverter:
  def __init__(self, input_dir: str = "Input") -> None:
    self.input_dir = pathlib.Path(input_dir)
    self.ensure_input_directory()

  def ensure_input_directory(self) -> None:
    self.input_dir.mkdir(parents=True, exist_ok=True)

  def process_all_themes(self) -> None:
    self._process_zip_files()

  def _process_zip_files(self) -> None:
    color_kt_files: dict = src.utility.read.kt_theme_file_from_zips(str(self.input_dir))
    if not color_kt_files:
      console.print("⚠️ No ZIP files with Kotlin themes found in input directory", style="bold yellow")
      return

    for zip_file, content in color_kt_files.items():
      zip_path: pathlib.Path = self.input_dir / zip_file
      console.print(f"\n✨ Working on [bold blue]{zip_file}")
      self._convert_theme(zip_path, content)

  def _convert_theme(self, theme_path: pathlib.Path, theme_content: str) -> None:
    # Parse theme
    colors: list[tuple] = src.parse.theme.from_kt_variable(theme_content)
    console.print("\t📑 Kotlin theme parsed successfully")

    # Convert to different formats
    self._convert_to_power_fx(colors, theme_path.stem)
    self._convert_to_typst(colors, theme_path.stem)
    self._convert_to_python(colors, theme_path.stem)
    self._convert_to_tailwind(colors, theme_path.stem)

  def _convert_to_power_fx(self, colors: list[tuple], theme_stem: str) -> None:
    power_fx_dark_colors: list[str] = m3_power_fx.generate(colors, brightness="Dark")
    power_fx_light_colors: list[str] = m3_power_fx.generate(colors, brightness="Light")
    src.utility.save.to_file(power_fx_dark_colors, "PowerFx", f"{theme_stem}_Dark", ".txt")
    src.utility.save.to_file(power_fx_light_colors, "PowerFx", f"{theme_stem}_Light", ".txt")
    console.print("\t✅ Power FX")

  def _convert_to_typst(self, colors: list[tuple], theme_stem: str) -> None:
    typst_colors: list[str] = m3_typst.generate(colors)
    src.utility.save.to_file(typst_colors, "Typst", theme_stem, ".typ")
    console.print("\t✅ Typst")

  def _convert_to_python(self, colors: list[tuple], theme_stem: str) -> None:
    python_colors: list[str] = m3_python.generate(colors)
    src.utility.save.to_file(python_colors, "Python", theme_stem, ".py")
    console.print("\t✅ Python")

  def _convert_to_tailwind(self, colors: list[tuple], theme_stem: str) -> None:
    tailwind_colors: list[str] = m3_tailwind.generate(colors)
    src.utility.save.to_file(tailwind_colors, "TailwindCSS", theme_stem, ".css")
    console.print("\t✅ TailwindCSS")


def main() -> None:
  converter = ThemeConverter()
  converter.process_all_themes()
  console.print("\n✅ All theme conversions completed", style="bold green")


if __name__ == "__main__":
  main()
