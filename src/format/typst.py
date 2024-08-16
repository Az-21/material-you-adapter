import src.format.color as format


def generate(colors: list[tuple]) -> list[str]:
  lines: list[str] = []

  #  Light color variable definition
  lines.append("#let m3light = (")
  for color_name, color_hex in colors:
    if "Light" in color_name:
      formatted_color_name: str = format.name(color_name, convertToUppercase=False)
      lines.append(f'  {formatted_color_name}: rgb("#{color_hex}"),')
  lines.append(")")

  # Spacer
  lines.append("")

  # Dark color variable definition
  lines.append("#let m3dark = (")
  for color_name, color_hex in colors:
    if "Dark" in color_name:
      formatted_color_name: str = format.name(color_name, convertToUppercase=False)
      lines.append(f'  {formatted_color_name}: rgb("#{color_hex}"),')
  lines.append(")")

  return lines
