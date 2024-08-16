# primaryDark -> Primary
def name(name: str, convertToUppercase: bool = True) -> str:
  # Strip "Dark" and "Light" from color name to reduce changes required if changing theme mode | primaryDark -> primary
  name = name.replace("Dark", "").replace("Light", "")

  # First char to uppercase | primary -> Primary
  if convertToUppercase:
    name = name[0].upper() + name[1:]

  return name
