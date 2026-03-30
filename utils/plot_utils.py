from typing import Literal


def set_size(
    width: float | Literal["one_column", "two_column"] | None = None,
    height: float | None = None,
    fraction: float = 1.0,
    height_ratio: float = (5**0.5 - 1) / 2,
) -> tuple[float, float]:
    """Set figure dimensions to avoid scaling in LaTeX.

    Parameters
    ----------
    width: float or string
            Document width in points, or string of predefined document type
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    if width:
        if width == "one_column":
            fig_width_in = 3.5
        elif width == "two_column":
            fig_width_in = 7.16
        elif isinstance(width, (float, int)):
            fig_width_in = width
        else:
            raise ValueError("Width must be a float or supported document type.")
        fig_width_in *= fraction
        if height:
            fig_height_in = height
        else:
            fig_height_in = fig_width_in * height_ratio
    elif height:
        fig_height_in = height
        fig_width_in = height / height_ratio
    else:
        raise ValueError("You must specify at least one of width or height.")

    return (fig_width_in, fig_height_in)


def color_background(data, ax, start_cond, color="grey", alpha=0.1):
    if data.shape[0] == 0:
        return
    start = None
    # Iterate over the length of the attention data
    for i in range(len(data[0])):
        # If we find a '1', and no start is recorded, mark the start of the sequence
        if start_cond(data[1, i]) and start is None:
            start = data[0, i]
        # If the sequence has ended (we find a '0' and a start is recorded), mark the end
        elif not start_cond(data[1, i]) and start is not None:
            # if data["holo_attention"][0, i - 1] - start > 1:
            ax.axvspan(start, data[0, i - 1], facecolor=color, alpha=alpha)
            start = None  # Reset the start marker
    # Check if the last entry in the list was a '1' and the sequence did not end
    if start is not None:
        # if data["holo_attention"][0, i - 1] - start > 1:
        ax.axvspan(start, data[0, i], facecolor=color, alpha=alpha)
