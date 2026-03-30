#!/usr/bin/env python3
"""
Plot the piecewise function:

U(d) = 0,                                   d > tau_out
    cos^2( (pi / (2 tau_out)) d ),       0 < d <= tau_out
    A d^3 + B d^2 + 1,                   tau_in < d <= 0
    (k / tau_out) (d - tau_in),          d <= tau_in

with
A = k/(tau_in^2 * tau_out) + 2/(tau_in^3)
B = -k/(tau_in * tau_out) - 3/(tau_in**2)

Adjust tau_in, tau_out, k below.
"""

# ruff: noqa: N802, N806

import matplotlib.pyplot as plt
import numpy as np

from utils.plot_utils import set_size


def U(d: np.ndarray, tau_in: float, tau_out: float, k: float) -> np.ndarray:
    """
    Vectorized evaluation of U(d).
    Assumes tau_in < 0 < tau_out.
    """
    A = k / (tau_in**2 * tau_out) + 2.0 / (tau_in**3)
    B = -k / (tau_in * tau_out) - 3.0 / (tau_in**2)

    out = np.empty_like(d, dtype=float)

    mask_outside = d > tau_out
    mask_cos = (d > 0) & (d <= tau_out)
    mask_poly = (d > tau_in) & (d <= 0)
    mask_linear = d <= tau_in

    out[mask_outside] = 0.0
    out[mask_cos] = np.cos((np.pi / (2.0 * tau_out)) * d[mask_cos]) ** 2
    out[mask_poly] = A * d[mask_poly] ** 3 + B * d[mask_poly] ** 2 + 1.0
    out[mask_linear] = (k / tau_out) * (d[mask_linear] - tau_in)

    return out


def main():
    # Adjustable parameters
    tau_out = 0.2  # positive
    tau_in = -0.15 * tau_out  # must be negative in this formulation
    k = 15

    # Domain for plotting
    d_min = tau_out * -0.3
    d_max = tau_out * 1.1
    d = np.linspace(d_min, d_max, 4000)

    y = U(d, tau_in, tau_out, k)

    # set width to 3.5 inches and height to 42% of width
    plt.figure(figsize=set_size("one_column", height_ratio=0.42))
    plt.plot(d, y, label="s(d)")

    # 画出 tau_in 和 tau_out 两条竖线并在旁边标注
    plt.axvline(tau_in, color="red", lw=1, ls="--")
    plt.text(
        tau_in,
        plt.ylim()[1] * 0.5,
        r"$\tau_{\mathrm{in}}$",
        rotation=0,
        va="bottom",
        ha="right",
        color="red",
        fontsize=9,
    )

    plt.axvline(tau_out, color="red", lw=1, ls="--")
    plt.text(
        tau_out + 0.001,
        plt.ylim()[1] * 0.5,
        r"$\tau_{\mathrm{out}}$",
        rotation=0,
        va="bottom",
        ha="left",
        color="red",
        fontsize=9,
    )

    plt.xlabel("d")
    plt.ylabel("s(d)")
    plt.xlim(d_min, d_max)
    plt.tight_layout()
    plt.savefig("fig/refine_score_plot")


if __name__ == "__main__":
    main()
