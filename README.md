# Material You Adapter
Adapt Material You (M3) theme files to various languages and technologies

## Usage
1. Export *Jetpack Compose* (Kotlin) theme from [Material Theme Builder](https://material-foundation.github.io/material-theme-builder/).
2. [Optional] Rename the zip file; output will use the name of zip file(s).
3. Place the `.zip` file in `Input/` folder of this program.
4. Run `main.py`.
5. Find generated outputs in `Output/` folder.

> [!TIP]
> This script supports multiple theme files. All `.zip` files inside `Input/` folder will be adapted.

## Outputs
<details>
<summary><h2>Typst</h2></summary>

[Typst](https://github.com/typst/typst) is a markup-based typesetting system.

### Sample Output
```typ
#let m3light = (
  primary: rgb("#4C662B"),
  onPrimary: rgb("#FFFFFF"),
  //...
)

#let m3dark = (
  primary: rgb("#B1D18A"),
  onPrimary: rgb("#1F3701"),
  // ...
)
```

### Usage
```typ
#import "color.typ": m3dark, m3light

#box(width: 32pt, height: 32pt, fill: m3dark.primary)
#box(width: 32pt, height: 32pt, fill: m3light.primary)
```
</details>

<details>
<summary><h2>Power Apps</h2></summary>

[Power Apps](https://www.microsoft.com/en-us/power-platform/products/power-apps) is a low-code application building tool.

### Sample Output
```c
// Light
Set(M3Primary, ColorValue("#4C662B"));
Set(M3OnPrimary, ColorValue("#FFFFFF"));
// ...
```
```c
// Dark
Set(M3Primary, ColorValue("#B1D18A"));
Set(M3OnPrimary, ColorValue("#1F3701"));
// ...
```

### Usage
- Copy paste the variable declarations in the `OnStart` $f x$ parameter of the *App*.
</details>

<details>
<summary><h2>Python</h2></summary>

### Sample Output
```py
@dataclass(frozen=True)
class LightTheme:
  primary: str = "#4C662B"
  onPrimary: str = "#FFFFFF"
  # ...

@dataclass(frozen=True)
class DarkTheme:
  primary: str = "#B1D18A"
  onPrimary: str = "#1F3701"
  # ...

dark = DarkTheme()
light = LightTheme()
```

### Usage
```py
from src.theme.colors import dark as m3
#                            ^--^ Easily switch theme by changing just one line

print(m3.primary)
```
```py
# Alternatively call both light and dark variants
import src.theme.colors as m3
print(m3.dark.primary)
print(m3.light.primary)
```
</details>
