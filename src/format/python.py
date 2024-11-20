import src.format.color as format


def generate(colors: list[tuple]) -> list[str]:
  lines: list[str] = []

  # Imports
  lines.append("from dataclasses import dataclass")

  #  Light color variable definition
  lines.append("@dataclass(frozen=True)")
  lines.append("class LightTheme:")
  for color_name, color_hex in colors:
    if "Light" in color_name:
      formatted_color_name: str = format.name(color_name, convertToUppercase=False)
      lines.append(f'  {formatted_color_name}: str = "#{color_hex}"')

  # Spacer
  lines.append("")

  # Dark color variable definition
  lines.append("@dataclass(frozen=True)")
  lines.append("class DarkTheme:")
  for color_name, color_hex in colors:
    if "Dark" in color_name:
      formatted_color_name: str = format.name(color_name, convertToUppercase=False)
      lines.append(f'  {formatted_color_name}: str = "#{color_hex}"')

  # Optionally initialize
  lines.append("\n\n# dark = DarkTheme()")
  lines.append("# light = LightTheme()")

  return lines
