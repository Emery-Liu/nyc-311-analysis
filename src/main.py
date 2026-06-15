import pandas as pd


from cleaning import add_resolution_col

from analysis import (
    top10_complaints,
    borough_counts,
    agency_resolution_time,
    resolution_summary
)

from visualization import (
    plot_top_complaints,
    plot_borough_distribution,
    plot_agency_resolution
)

from load_data import (
    load_data
)


def main() -> None:
    # This demo shows the core analysis: summary stats and three plots.
    # For additional analyses (e.g., resolution time by complaint type,
    # top complaints per borough, agency complaint counts, histograms, heatmaps),
    # see functions in analysis.py and visualization.py – simply call them here.
    df = load_data("data/raw/nyc_311_2025_sample.csv")

    df = add_resolution_col(df)

    print(
        resolution_summary(df)
    )

    plot_top_complaints(
        top10_complaints(df)
    )

    plot_borough_distribution(
        borough_counts(df)
    )

    plot_agency_resolution(
        agency_resolution_time(df)
    )

if __name__ == "__main__":
    main()