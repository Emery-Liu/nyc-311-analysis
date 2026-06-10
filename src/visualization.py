import matplotlib.pyplot as plt

# Purpose: Draws a horizontal bar chart of the top complaint types.
# Parameters: complaints (pd.Series) – indexed by complaint type, values = counts.
# Output: Horizontal bar chart 
def plot_top_complaints(complaints):

    plt.figure(figsize=(10,6))

    complaints.sort_values().plot.barh(
        color="steelblue"
    )

    plt.xlabel("Number of Complaints")
    plt.ylabel("Complaint Type")
    plt.title("Top Complaint Types")

    plt.show()


# Purpose: Draws a pie chart of complaint distribution by borough.
# Parameters: borough_counts (pd.Series) – indexed by borough.
# Output: Pie chart with percentage labels.
def plot_borough_distribution(borough_counts):

    plt.figure(figsize=(8,8))

    borough_counts.plot.pie(
        autopct="%1.1f%%"
    )

    plt.ylabel("")

    plt.title("Complaint Distribution by Borough")

    plt.show()


# Purpose: Draws a horizontal bar chart of average resolution time per agency.
# Parameters: agency_times (pd.Series) – indexed by agency
# Output: Bar chart
def plot_agency_resolution(agency_times):

    plt.figure(figsize=(10,6))

    agency_times.plot.barh(
        color="orange"
    )

    plt.xlabel("Average Resolution Time (Hours)")

    plt.ylabel("Agency")

    plt.title("Average Resolution Time by Agency")

    plt.tight_layout()

    plt.show()


# Purpose: Plots a histogram of resolution times.
# Parameters: hours (pd.Series) – values in hours.
# Output: Histogram with 50 bins
def plot_resolution_histogram(hours):

    plt.figure(figsize=(10,6))

    plt.hist(
        hours,
        bins=50,
        edgecolor="black"
    )

    plt.xlabel("Resolution Time (Hours)")

    plt.ylabel("Count")

    plt.title("Distribution of Resolution Times")

    plt.tight_layout()

    plt.show()


# Purpose: Creates a 2D histogram (heatmap) of complaint density using longitude and latitude.
# Parameters: DataFrame df with longitude and latitude columns.
# Output: a hist2d plot
def plot_heatmap(df):

    plt.figure(figsize=(10,8))

    plt.hist2d(
        df["longitude"],
        df["latitude"],
        bins=120,
    )

    plt.xlabel("Longitude")

    plt.ylabel("Latitude")

    plt.title("NYC Complaint Density Heatmap")

    plt.tight_layout()

    plt.show()