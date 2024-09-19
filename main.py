import pathlib
import src.format.power_fx as power_fx
import src.format.typst as typst
import src.parse.theme
import src.utility
import src.utility.read
import src.utility.read as read
import src.utility.save as save


def main() -> None:
  # Ensure "Input" folder exists
  pathlib.Path("Input").mkdir(parents=True, exist_ok=True)

  # Work on all Kotlin theme files in "Input" folder
  for kt_theme in pathlib.Path("Input").glob("*.kt"):
    colors_kt_file_data: str = read.kt_theme_file(kt_theme)
    parse(kt_theme, colors_kt_file_data)

  # Work on all Zip theme files in "Input" folder
  color_kt_files = src.utility.read.kt_theme_file_from_zips("Input")
  for zip_file, content in color_kt_files.items():
    zip_path = pathlib.Path("Input") / zip_file
    parse(zip_path, content)


def parse(kt_theme: pathlib.Path, colors_kt_file_data: str) -> None:
  print(f"\n✨ Working on {kt_theme}")

  # Parse theme
  colors: list[tuple] = src.parse.theme.from_kt_variable(colors_kt_file_data)
  print("  ✔️  Kotlin theme file parsed")

  # Power FX (PowerApps)
  power_fx_dark_colors: list[str] = power_fx.generate(colors, brightness="Dark")
  power_fx_light_colors: list[str] = power_fx.generate(colors, brightness="Light")
  save.to_file(power_fx_dark_colors, "PowerFx", kt_theme.stem + "_Dark", ".txt")
  save.to_file(power_fx_light_colors, "PowerFx", kt_theme.stem + "_Light", ".txt")
  print("  ✔️  Power FX theme generated")

  # Typst
  typst_colors: list[str] = typst.generate(colors)
  save.to_file(typst_colors, "Typst", kt_theme.stem, ".typ")
  print("  ✔️  Typst theme generated")


if __name__ == "__main__":
  main()
