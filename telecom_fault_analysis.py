from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


DATA_FILE = "telecom_fault_data.csv"
RESULTS_DIR = Path("results")


def load_data(path: str = DATA_FILE) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def print_summary(df: pd.DataFrame) -> None:
    total_faults = len(df)
    avg_downtime = df["downtime_minutes"].mean()
    total_affected_users = df["affected_users"].sum()
    repeated_sites = df["site_id"].value_counts().head(5)

    print("Telecom Network Fault Analysis")
    print("=" * 35)
    print(f"Total faults: {total_faults}")
    print(f"Average downtime: {avg_downtime:.1f} minutes")
    print(f"Total affected users: {total_affected_users}")
    print("\nTop repeated fault sites:")
    print(repeated_sites.to_string())


def save_bar_chart(series: pd.Series, title: str, filename: str, xlabel: str = "", ylabel: str = "Count") -> None:
    RESULTS_DIR.mkdir(exist_ok=True)
    plt.figure(figsize=(8, 5))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(RESULTS_DIR / filename)
    plt.close()


def create_charts(df: pd.DataFrame) -> None:
    save_bar_chart(
        df["region"].value_counts(),
        "Fault Count by Region",
        "faults_by_region.png",
        xlabel="Region",
    )
    save_bar_chart(
        df["technology"].value_counts(),
        "Fault Count by Technology",
        "faults_by_technology.png",
        xlabel="Technology",
    )
    save_bar_chart(
        df["fault_type"].value_counts(),
        "Most Common Fault Types",
        "fault_types.png",
        xlabel="Fault Type",
    )
    save_bar_chart(
        df.groupby("region")["downtime_minutes"].mean().sort_values(ascending=False),
        "Average Downtime by Region",
        "average_downtime_by_region.png",
        xlabel="Region",
        ylabel="Average downtime minutes",
    )


def generate_recommendations(df: pd.DataFrame) -> list[str]:
    top_region = df["region"].value_counts().idxmax()
    top_fault_type = df["fault_type"].value_counts().idxmax()
    highest_downtime_region = df.groupby("region")["downtime_minutes"].mean().idxmax()
    repeated_site = df["site_id"].value_counts().idxmax()

    return [
        f"Focus preventive maintenance in {top_region}, which has the highest number of faults.",
        f"Review root causes for {top_fault_type}, the most frequent fault type.",
        f"Check outage handling in {highest_downtime_region}, where average downtime is highest.",
        f"Monitor site {repeated_site} because it appears repeatedly in the fault records.",
    ]


def run_analysis() -> None:
    df = load_data()
    print_summary(df)
    create_charts(df)

    print("\nRecommendations:")
    for item in generate_recommendations(df):
        print(f"- {item}")

    print("\nCharts saved in the 'results' folder.")


if __name__ == "__main__":
    run_analysis()
