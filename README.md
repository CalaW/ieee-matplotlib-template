# IEEE Matplotlib Template

Starter template for producing publication-ready Matplotlib figures with sane defaults for IEEE-style papers.

The repository gives you:

- a shared [`matplotlibrc`](/Users/calaw/Documents/Program/ieee-matplotlib-template/matplotlibrc) with compact font sizes, thin lines, vector PDF output, and a colorblind-friendly palette
- a small helper module in [`utils/plot_utils.py`](/Users/calaw/Documents/Program/ieee-matplotlib-template/utils/plot_utils.py) for consistent figure sizing
- an example plot script in [`refine_score.py`](/Users/calaw/Documents/Program/ieee-matplotlib-template/refine_score.py)
- a cropping utility in [`fig/autocrop.sh`](/Users/calaw/Documents/Program/ieee-matplotlib-template/fig/autocrop.sh) for trimming generated PDFs

## Why this template

Matplotlib plots often need cleanup before they fit well into a two-column paper. This template centralizes the styling choices that usually get repeated across projects:

- one-column and two-column figure widths
- small, paper-friendly typography
- PDF output with embedded TrueType fonts
- consistent line widths and tick styling
- a reusable plotting workflow

## Repository layout

```text
.
├── fig/
│   ├── autocrop.sh
│   └── refine_score_plot.pdf
├── utils/
│   └── plot_utils.py
├── matplotlibrc
├── README.md
└── refine_score.py
```

## Requirements

- Python 3.10+
- `matplotlib`
- `numpy`
- `pdfcrop` if you want automatic PDF cropping

Install the Python dependencies with:

```bash
python -m pip install matplotlib numpy
```

`pdfcrop` is available through a TeX distribution.

## Quick start

Run the example script from the repository root:

```bash
python refine_score.py
```

This writes the output figure to [`fig/refine_score_plot.pdf`](/Users/calaw/Documents/Program/ieee-matplotlib-template/fig/refine_score_plot.pdf).

If you want to crop all generated PDFs in the `fig/` directory:

```bash
./fig/autocrop.sh
```

## How it works

### 1. Global Matplotlib styling

[`matplotlibrc`](/Users/calaw/Documents/Program/ieee-matplotlib-template/matplotlibrc) is picked up automatically when you run scripts from the repository root. It defines the default appearance for all plots in this project, including:

- font sizes for axes, ticks, and legends
- grid appearance
- line widths and marker sizes
- PDF output format
- a colorblind-friendly color cycle

If you prefer serif fonts or LaTeX rendering, the file already contains commented options you can enable.

### 2. Figure sizing helper

[`utils/plot_utils.py`](/Users/calaw/Documents/Program/ieee-matplotlib-template/utils/plot_utils.py) provides `set_size(...)` so figures match common paper widths without trial and error.

Example:

```python
from utils.plot_utils import set_size

plt.figure(figsize=set_size("one_column", height_ratio=0.42))
```

Supported width presets:

- `"one_column"` -> 3.5 in
- `"two_column"` -> 7.16 in

You can also pass a numeric width directly.

### 3. Example plotting script

[`refine_score.py`](/Users/calaw/Documents/Program/ieee-matplotlib-template/refine_score.py) shows the intended workflow:

1. define the data or analytic function
2. generate values with NumPy
3. create a figure using `set_size(...)`
4. label and style the plot
5. save directly to `fig/`

## Starting a new figure

The easiest way to reuse this template is:

1. copy [`refine_score.py`](/Users/calaw/Documents/Program/ieee-matplotlib-template/refine_score.py) to a new script
2. replace the example function and plotting logic with your own data
3. keep `set_size(...)` and save to `fig/`
4. run `./fig/autocrop.sh` if you want tighter PDF bounds

A minimal skeleton looks like this:

```python
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

from utils.plot_utils import set_size

x = np.linspace(0, 1, 200)
y = np.sin(2 * np.pi * x)

plt.figure(figsize=set_size("one_column"))
plt.plot(x, y, label="example")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
plt.savefig("fig/example_plot")
```

## Notes

- `plt.savefig("fig/name")` produces a PDF because [`matplotlibrc`](/Users/calaw/Documents/Program/ieee-matplotlib-template/matplotlibrc) sets `savefig.format: pdf`.
- If you run scripts from another working directory, Matplotlib may not automatically load this repository's `matplotlibrc`.
- The current default sans-serif font is `Roboto`. If it is missing on your system, Matplotlib will fall back to another available sans-serif font.

## License

Add your preferred license here before publishing or reusing the template outside your own projects.
