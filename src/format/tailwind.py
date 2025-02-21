import src.format.color as format


def generate(colors: list[tuple]) -> list[str]:
  lines: list[str] = []

  #  Light color variable definition
  lines.append("@theme {")
  for color_name, color_hex in colors:
    if "Light" in color_name:
      formatted_color_name: str = format.name(color_name, convertToUppercase=False)
      lines.append(f"  --color-m3-light-{formatted_color_name}: #{color_hex};")

  # Spacer
  lines.append("")

  # Dark color variable definition
  for color_name, color_hex in colors:
    if "Dark" in color_name:
      formatted_color_name: str = format.name(color_name, convertToUppercase=False)
      lines.append(f"  --color-m3-dark-{formatted_color_name}: #{color_hex};")

  lines.append("}")

  return lines
