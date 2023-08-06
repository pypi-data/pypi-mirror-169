
import pandas as pd


def color_df(
    df: pd.DataFrame, color: str, names: list, axis: int = 1
) -> pd.io.formats.style.Styler:
    return df.style.apply(
        lambda x: [f"background: {color}" if (x.name in names) else "" for _ in x],
        axis=axis,
    )