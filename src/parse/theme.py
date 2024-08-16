import re


def from_kt_variable(data: str) -> list[tuple]:
  # val <<ColorName>> = Color(0XFF<<ColorHex>>)
  color_pattern: re.Pattern[str] = re.compile(r"val (.*?) = Color\(0xFF(.*?)\)")
  return color_pattern.findall(data)
