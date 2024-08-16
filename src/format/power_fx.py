import src.format.color as format


def generate(colors: list[tuple], brightness: str) -> list[str]:
  lines: list[str] = [f"// {brightness} Mode"]

  for color_name, color_hex in colors:
    if brightness in color_name:
      formatted_color_name: str = format.name(color_name, convertToUppercase=True)
      lines.append(f'Set(M3{formatted_color_name}, ColorValue("#{color_hex}"));')

  return lines
