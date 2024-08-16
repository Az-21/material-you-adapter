# Material You Adapter
Adapt Material You (M3) theme files to various languages and technologies

## Usage
1. Export *Jetpack Compose* (Kotlin) theme from [Material Theme Builder](https://material-foundation.github.io/material-theme-builder/).
2. Extract `Color.kt` from the archive generated by Material Theme Builder. Optionally rename the `.kt` file.
3. Place the `.kt` file in `Input/` folder of this program.
4. Run `main.py`.
5. Find generated outputs in `Output/` folder.

> [!TIP]
> This script supports multiple theme files. All `.kt` files inside `Input/` folder will be adapted.

## Sample Input
```kt
// Generated by Material Theme Builder
val primaryLight = Color(0xFF4C662B)
val onPrimaryLight = Color(0xFFFFFFFF)
// ...
val primaryDark = Color(0xFFB1D18A)
val onPrimaryDark = Color(0xFF1F3701)
// ...
```

## Typst Adapter
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

## Power FX | Power Apps Adapter
[Power Apps](https://www.microsoft.com/en-us/power-platform/products/power-apps) is a low-code application building tool.

### Sample Output
> [!NOTE]
> To reduce modifications required when switching themes, this module generates dark mode and light mode in separate files.
```c
// Dark
Set(M3Primary, ColorValue("#B1D18A"));
Set(M3OnPrimary, ColorValue("#1F3701"));
// ...
```
```c
// Light
Set(M3Primary, ColorValue("#4C662B"));
Set(M3OnPrimary, ColorValue("#FFFFFF"));
// ...
```

### Usage
- Copy paste the variable declarations in the `OnStart` $f x$ parameter of the *App*.
