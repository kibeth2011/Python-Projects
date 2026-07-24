print("=" * 70)
print("DATA IMPORT AND INITIAL EXPLORATION")
print("=" * 70)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Display all columns
pd.set_option("display.max_columns", None)

# Format decimal numbers
pd.options.display.float_format = "{:,.2f}".format

# Load the dataset
df = pd.read_excel(r"D:\Academic\My tasks\Python\Malaria Analysis\Malaria incidence.xlsx", header=2)
print(df.head())

print("=" * 70)
print("DATA UNDERSTANDING")
print("=" * 70)

print("\n1. Dataset Shape")
print(df.shape)

print("\n2. Data Types")
print(df.info())

print("\n3. Column Names")
print(df.columns.tolist())

print("\n4. First Five Rows")
print(df.head())

print("\n" + "=" * 70)
print("DATA QUALITY ASSESSMENT")
print("=" * 70)

print("\n1. Missing Values")
print(df.isnull().sum())

print("\n2. Missing Value Percentage")
missing_percent = (df.isnull().mean() * 100).round(2)
print(missing_percent)

print("\n3. Duplicate Records")
print(df.duplicated().sum())

print("\n4. Number of Countries")
print(df["Location"].nunique())

print("\n5. Years Covered")
print("Earliest Year:", df["Period"].min())
print("Latest Year:", df["Period"].max())

print("\n6. WHO Regions")
print(df["ParentLocation"].unique())

print("\n" + "=" * 70)
print("DATA CLEANING")
print("=" * 70)

# Select only the variables needed for analysis
analysis_df = df[
    [
        "Location",
        "ParentLocation",
        "Period",
        "FactValueNumeric"
    ]
].copy()

# Rename columns
analysis_df.rename(
    columns={
        "Location": "Country",
        "ParentLocation": "WHORegion",
        "Period": "Year",
        "FactValueNumeric": "MalariaIncidence"
    },
    inplace=True
)

print("\nClean Dataset")
print(analysis_df.head())

# Keep only African countries
africa_df = analysis_df[
    analysis_df["WHORegion"] == "Africa"
].copy()

print(f"\nAfrican dataset shape: {africa_df.shape}")

print("\n" + "=" * 70)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 70)

print("\nResearch Question 1: How many African countries are represented?")

num_countries = africa_df["Country"].nunique()

print(f"\nNumber of African countries: {num_countries}")

countries = sorted(africa_df["Country"].unique())

print("\nCountries included:")

for country in countries:
    print(country)

print("\n" + "-" * 70)
print("Research Question 2: What time period does the dataset cover?")

print(f"\nEarliest Year: {africa_df['Year'].min()}")
print(f"Latest Year: {africa_df['Year'].max()}")
print(f"Total Years: {africa_df['Year'].nunique()}")

years = sorted(map(int, africa_df["Year"].unique()))

print("\nAvailable Years:")

print(years)

print("\n" + "-" * 70)
print("Research Question 3: Distribution of malaria incidence")

print(f"\n{africa_df['MalariaIncidence'].describe()}")

print("\n" + "-" * 70)
print("Research Question 4: Which African countries had the highest malaria incidence in 2024?")

latest_df = africa_df[africa_df["Year"] == 2024].copy()
top10 = latest_df.sort_values(
    by="MalariaIncidence",
    ascending=False
).head(10)

print(f"\n{top10[['Country', 'MalariaIncidence']]}")

plt.figure(figsize=(12,7))

plt.barh(
    top10["Country"],
    top10["MalariaIncidence"]
)

# Add values to the bars
for index, value in enumerate(top10["MalariaIncidence"]):
    plt.text(value + 3, index, f"{value:.1f}", va="center")

plt.xlabel("Estimated Malaria Incidence per 1,000 Population at Risk")
plt.ylabel("Country")
plt.title("Top 10 African Countries by Estimated Malaria Incidence (2024)")

# Add gridlines
plt.grid(axis="x", linestyle="--", alpha=0.5)

# Highest value at the top
plt.gca().invert_yaxis()

plt.tight_layout()

# Source
plt.figtext(
    0.99,
    0.01,
    "Source: World Health Organization (WHO)",
    ha="right",
    fontsize=9
)

# Save figure
plt.savefig(
    "images/top10_malaria_incidence_2024.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\n" + "-" * 70)
print("Research Question 5: How has malaria incidence changed across Africa between 2000 and 2024?")
yearly_trend = (
    africa_df
    .groupby("Year")["MalariaIncidence"]
    .mean()
    .reset_index()
)

print(yearly_trend)

plt.figure(figsize=(12,6))

plt.plot(
    yearly_trend["Year"],
    yearly_trend["MalariaIncidence"],
    marker="o",
    markersize=5,
    linewidth=3
)

plt.title("Average Malaria Incidence in Africa (2000–2024)")
plt.xlabel("Year")
plt.ylabel("Average Malaria Incidence per 1,000 Population at Risk")

plt.grid(True, linestyle="--", alpha=0.5)

plt.axvspan(
    2020,
    2022,
    color="orange",
    alpha=0.2,
    label="COVID-19 period"
)

plt.legend()

plt.tight_layout()

plt.figtext(
    0.99,
    0.01,
    "Source: World Health Organization (WHO)",
    ha="right",
    fontsize=9
)

plt.savefig(
    "images/africa_malaria_trend_2000_2024.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\n" + "-" * 70)
print("Research Question 6: Which African countries achieved the greatest reduction in malaria incidence between 2000 and 2024?")

# Select only the years of interest
comparison_df = africa_df[
    africa_df["Year"].isin([2000, 2024])
].copy()

# Reshape the data so each country has one row
comparison_df = comparison_df.pivot(
    index="Country",
    columns="Year",
    values="MalariaIncidence"
).reset_index()

# Rename columns
comparison_df.columns = [
    "Country",
    "Incidence2000",
    "Incidence2024"
]

# Remove countries with missing values
comparison_df = comparison_df.dropna()

# Calculate reduction in malaria incidence
comparison_df["Reduction"] = (
    comparison_df["Incidence2000"]
    - comparison_df["Incidence2024"]
)

# Sort countries by reduction (largest first)
comparison_df = comparison_df.sort_values(
    by="Reduction",
    ascending=False
)

# Display top 10 countries
print(
    comparison_df[
        [
            "Country",
            "Incidence2000",
            "Incidence2024",
            "Reduction"
        ]
    ].head(10)
)

top10 = comparison_df.head(10)

plt.figure(figsize=(12,7))

plt.barh(
    top10["Country"],
    top10["Reduction"]
)

for index, value in enumerate(top10["Reduction"]):
    plt.text(value + 1, index, f"{value:.1f}", va="center")

plt.xlabel("Reduction in Malaria Incidence")
plt.ylabel("Country")

plt.title(
    "Top 10 African Countries with the Greatest Reduction in Malaria Incidence (2000–2024)"
)

plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.gca().invert_yaxis()

plt.figtext(
    0.99,
    0.01,
    "Source: World Health Organization (WHO)",
    ha="right",
    fontsize=9
)

plt.tight_layout()

plt.savefig(
    "images/greatest_reduction_malaria.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\n" + "-" * 70)
print("Research Question 7: How do malaria incidence trends in Kenya compare with those of Uganda, Tanzania, Rwanda, and Ethiopia?")

# Selected East African countries
comparison_countries = [
    "Kenya",
    "Uganda",
    "United Republic of Tanzania",
    "Rwanda",
    "Ethiopia"
]

# Filter data for selected countries
east_africa = africa_df[
    africa_df["Country"].isin(comparison_countries)
].copy()

print("\nCountries Included:")
print(sorted(east_africa["Country"].unique()))

plt.figure(figsize=(12, 7))

for country in comparison_countries:

    country_data = east_africa[
        east_africa["Country"] == country
    ]

    plt.plot(
        country_data["Year"],
        country_data["MalariaIncidence"],
        marker="o",
        linewidth=2,
        label=country
    )

plt.title(
    "Malaria Incidence Trends in Selected East African Countries (2000–2024)"
)

plt.xlabel("Year")
plt.ylabel("Malaria Incidence per 1,000 Population at Risk")

plt.grid(
    linestyle="--",
    alpha=0.5
)

plt.legend()

plt.figtext(
    0.99,
    0.01,
    "Source: World Health Organization (WHO)",
    ha="right",
    fontsize=9
)

plt.tight_layout()

plt.savefig(
    "images/east_africa_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# Latest Comparison (2024)

latest = (
    east_africa[east_africa["Year"] == 2024]
    [
        [
            "Country",
            "MalariaIncidence"
        ]
    ]
    .sort_values(
        by="MalariaIncidence",
        ascending=False
    )
)

print("\nMalaria Incidence in 2024\n")
print(latest.to_string(index=False))

print("\n" + "-" * 70)
print("Research Question 8: Which years showed the greatest improvement in malaria incidence?")

# Calculate the average malaria incidence for each year
yearly_change = yearly_trend.copy()

# Calculate the reduction from the previous year
yearly_change["YearlyReduction"] = (
    yearly_change["MalariaIncidence"].shift(1)
    - yearly_change["MalariaIncidence"]
)

# Select the top 10 years with the greatest reductions
top_improvement = (
    yearly_change
    .dropna()
    .sort_values(by="YearlyReduction", ascending=False)
    .head(10)
)

print(
    top_improvement[
        ["Year", "MalariaIncidence", "YearlyReduction"]
    ].to_string(index=False)
)

# Plot
plt.figure(figsize=(11, 6))

plt.bar(
    top_improvement["Year"].astype(str),
    top_improvement["YearlyReduction"]
)

# Add value labels
for i, value in enumerate(top_improvement["YearlyReduction"]):
    plt.text(
        i,
        value + 0.5,
        f"{value:.1f}",
        ha="center",
        fontsize=10
    )

plt.title("Top 10 Years with the Greatest Reduction in Malaria Incidence")
plt.xlabel("Year")
plt.ylabel("Reduction from Previous Year\n(per 1,000 Population at Risk)")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.figtext(
    0.99,
    0.01,
    "Source: World Health Organization (WHO)",
    ha="right",
    fontsize=9
)

plt.tight_layout()

plt.savefig(
    "images/top_yearly_improvements.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()