print("=" * 70)
print("DATA IMPORT AND INITIAL EXPLORATION")
print("=" * 70)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

pd.set_option("display.max_columns", None)
pd.options.display.float_format = "{:,.2f}".format

# Government AI Readiness Index
ai_df = pd.read_excel(r"D:\Academic\My tasks\Python\Global AI Adoption and Readiness\2024-GAIRI-data.xlsx")

# GDP per capita
gdp_df = pd.read_excel(r"D:\Academic\My tasks\Python\Global AI Adoption and Readiness\API_NY.GDP.PCAP.CD_DS2_en_excel_v2_33108.xls", header = 3)

# Internet Users
internet_df = pd.read_excel(r"D:\Academic\My tasks\Python\Global AI Adoption and Readiness\API_IT.NET.USER.ZS_DS2_en_excel_v2_33090.xls", header = 3)

# Population
population_df = pd.read_excel(r"D:\Academic\My tasks\Python\Global AI Adoption and Readiness\API_SP.POP.TOTL_DS2_en_excel_v2_33073.xls", header = 3)

# Inspect AI Rediness Dataset
print(ai_df.head())
print(ai_df.shape)
print(ai_df.columns)
print(ai_df.info())
print(ai_df.isnull().sum())

print("="*70)
print("DATA CLEANING")
print("="*70)

# Rename columns 
ai_df = ai_df.rename(columns={
    "Rank": "AIRank",
    "2024 Total": "AIReadinessScore"
})

# Check for duplicates
print(ai_df.duplicated().sum())

# Inspect GDP per capita Dataset
print(gdp_df.head())
print(gdp_df.shape)
print(gdp_df.columns.tolist())
print(gdp_df.info())

# Check for duplicate records
print(gdp_df.duplicated().sum())

# Keep only the country name and GDP per capita for 2024
gdp_df = gdp_df[
    [
        "Country Name",
        "2024"
    ]
].copy()

# Check missing values in the selected columns
print(
    gdp_df[
        [
            "Country Name",
            "2024"
        ]
    ].isnull().sum()
)

# Rename columns for consistency
gdp_df.rename(
    columns={
        "Country Name": "Country",
        "2024": "GDPPerCapita"
    },
    inplace=True
)

# Remove countries with missing GDP values for 2024
gdp_df = gdp_df.dropna(subset=["GDPPerCapita"])

# Reset the index after removing missing values
gdp_df.reset_index(drop=True, inplace=True)

# Display the cleaned dataset
print(gdp_df.head())

# Display the number of countries remaining after cleaning
print(f"Number of countries with GDP data in 2024 after cleaning: {len(gdp_df)}")

# Inspect Internet Users Dataset
print(internet_df.head())
print(internet_df.shape)
print(internet_df.columns.tolist())
print(internet_df.info())

#Check for duplicate records
print(internet_df.duplicated().sum())

# Keep only the country name and Internet Users (%) for 2024
internet_df = internet_df[
    [
        "Country Name",
        "2024"
    ]
].copy()

# Check missing values in the selected columns
print(
    internet_df[
        [
            "Country Name",
            "2024"
        ]
    ].isnull().sum()
)

# Rename columns for consistency
internet_df.rename(
    columns={
        "Country Name": "Country",
        "2024": "InternetUsersPercent"
    },
    inplace=True
)

# Remove countries with missing Internet Users values for 2024
internet_df = internet_df.dropna(subset=["InternetUsersPercent"])

# Reset the index after removing missing values
internet_df.reset_index(drop=True, inplace=True)

# Display the cleaned dataset
print(internet_df.head())

# Display the number of countries remaining after cleaning
print(f"Number of countries with Internet users in 2024 after cleaning: {len(internet_df)}")

# Inspect Population Dataset
print(population_df.head())
print(population_df.shape)
print(population_df.columns.tolist())
print(population_df.info())

# Check for duplicate records
print(population_df.duplicated().sum())

# Keep only the country name and Population for 2024
population_df = population_df[
    [
        "Country Name",
        "2024"
    ]
].copy()

# Check missing values in the selected columns
print(
    population_df[
        [
            "Country Name",
            "2024"
        ]
    ].isnull().sum()
)

# Rename columns for consistency
population_df.rename(
    columns={
        "Country Name": "Country",
        "2024": "Population"
    },
    inplace=True
)

# Remove countries with missing population values for 2024
population_df = population_df.dropna(subset=["Population"])

# Reset the index after removing missing values
population_df.reset_index(drop=True, inplace=True)

# Display the cleaned dataset
print(population_df.head())

# Display the number of countries remaining after cleaning
print(f"Number of countries with population records in 2024 after cleaning: {len(population_df)}")

print("="*70)
print("MERGE DATASETS")
print("="*70)

# Merge AI Readiness with GDP
merged_df = pd.merge(
    ai_df,
    gdp_df,
    on="Country",
    how="left"
)

# Merge Internet Users
merged_df = pd.merge(
    merged_df,
    internet_df,
    on="Country",
    how="left"
)

# Merge Population
merged_df = pd.merge(
    merged_df,
    population_df,
    on="Country",
    how="left"
)

print(merged_df.head())
print(merged_df.shape)
print(merged_df.isnull().sum())

print("="*70)
print("UNMATCHED COUNTRIES")
print("="*70)

# Display countries with missing GDP after merging
unmatched = merged_df[
    merged_df["GDPPerCapita"].isnull()
][["Country"]]

print("Countries with unmatched GDP records:\n")

for country in unmatched["Country"]:
    print(country)

# Countries in AI dataset but not in GDP dataset
ai_not_in_gdp = sorted(
    set(ai_df["Country"]) - set(gdp_df["Country"])
)

print("\nCountries in AI but not in GDP:\n")

for country in ai_not_in_gdp:
    print(country)

# Countries in GDP but not in AI dataset
gdp_not_in_ai = sorted(
    set(gdp_df["Country"]) - set(ai_df["Country"])
)

print("\nCountries in GDP but not in AI:\n")

for country in gdp_not_in_ai:
    print(country)

print(" ")

country_mapping = {

    "United States of America": "United States",

    "Republic of Korea": "Korea, Rep.",

    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",

    "Türkiye": "Turkiye",

    "Republic of Moldova": "Moldova",

    "Iran (Islamic Republic of)": "Iran, Islamic Rep.",

    "Bahamas": "Bahamas, The",

    "State of Palestine": "West Bank and Gaza",

    "Kyrgyzstan": "Kyrgyz Republic",

    "Lao People's Democratic Republic": "Lao PDR",

    "United Republic of Tanzania": "Tanzania",

    "Côte d'Ivoire": "Cote d'Ivoire",

    "Bolivia (Plurinational State of)": "Bolivia",

    "Venezuela, Bolivarian Republic of": "Venezuela, RB",

    "Gambia (Republic of The)": "Gambia, The",

    "Guinea Bissau": "Guinea-Bissau",

    "Congo": "Congo, Rep.",

    "Democratic Republic of the Congo": "Congo, Dem. Rep.",

    "Saint Kitts and Nevis": "St. Kitts and Nevis",

    "Saint Lucia": "St. Lucia",

    "Saint Vincent and the Grenadines": "St. Vincent and the Grenadines",

    "Slovakia": "Slovak Republic",

    "Somalia": "Somalia, Fed. Rep."
}

# Apply the mapping
ai_df["Country"] = ai_df["Country"].replace(country_mapping)

# Merge AI Readiness with GDP
merged_df = pd.merge(
    ai_df,
    gdp_df,
    on="Country",
    how="left"
)

# Merge Internet Users
merged_df = pd.merge(
    merged_df,
    internet_df,
    on="Country",
    how="left"
)

# Merge Population
merged_df = pd.merge(
    merged_df,
    population_df,
    on="Country",
    how="left"
)

print(merged_df.head())
print(merged_df.shape)
print(merged_df.isnull().sum())

print("="*70)
print("REMAINING UNMATCHED COUNTRIES")
print("="*70)

print("\nCountries with missing GDP:")
print(
    merged_df[
        merged_df["GDPPerCapita"].isnull()
    ][["Country"]]
)

print("\nCountries with missing Internet Users:")
print(
    merged_df[
        merged_df["InternetUsersPercent"].isnull()
    ][["Country"]]
)

print("\nCountries with missing Population:")
print(
    merged_df[
        merged_df["Population"].isnull()
    ][["Country"]]
)

print("="*70)
print("EXPLORATORY DATA ANALYSIS")
print("="*70)

print("Research Question 1: Which countries had the highest AI Readiness scores in 2024?")

top10 = merged_df.sort_values(
    by="AIReadinessScore",
    ascending=False
).head(10)

print(top10[["Country", "AIReadinessScore"]])

plt.figure(figsize=(12,7))

plt.barh(
    top10["Country"],
    top10["AIReadinessScore"]
)

for index, value in enumerate(top10["AIReadinessScore"]):
    plt.text(value+0.3, index, f"{value:.2f}", va="center")

plt.xlabel("AI Readiness Score")
plt.ylabel("Country")
plt.title("Top 10 Countries by AI Readiness (2024)")

plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    "images/top10_ai_readiness.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\n" + "-" * 70)
print("Research Question 2: IWhat is the relationship between GDP per capita and AI Readiness?")

# Remove countries with missing values
scatter_df = merged_df.dropna(
    subset=["GDPPerCapita", "AIReadinessScore"]
).copy()

# Calculate the Pearson correlation coefficient
correlation = scatter_df["GDPPerCapita"].corr(
    scatter_df["AIReadinessScore"]
)

print(f"Correlation: {correlation:.3f}")

# Create the figure
plt.figure(figsize=(10, 6))

# Scatter plot
plt.scatter(
    scatter_df["GDPPerCapita"],
    scatter_df["AIReadinessScore"],
    alpha=0.7
)

# Plot the regression (trend) line
z = np.polyfit(
    scatter_df["GDPPerCapita"],
    scatter_df["AIReadinessScore"],
    1
)

p = np.poly1d(z)

plt.plot(
    scatter_df["GDPPerCapita"],
    p(scatter_df["GDPPerCapita"]),
    linewidth=2,
    label="Trend Line"
)

# Display the correlation coefficient on the chart
plt.text(
    0.05,
    0.95,
    f"r = {correlation:.3f}",
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=dict(
        facecolor="white",
        alpha=0.8,
        edgecolor="black"
    )
)

# Annotate selected countries
important_countries = [
    "United States",
    "Rwanda",
    "Kenya"
]

for _, row in scatter_df.iterrows():

    if row["Country"] in important_countries:

        plt.text(
            row["GDPPerCapita"],
            row["AIReadinessScore"],
            row["Country"],
            fontsize=8
        )

# Chart formatting
plt.xlabel("GDP per Capita (Current US$)")
plt.ylabel("AI Readiness Score")

plt.title("GDP per Capita vs AI Readiness (2024)")

plt.grid(alpha=0.4)

plt.legend()

# Format x-axis values with commas
plt.gca().xaxis.set_major_formatter(
    StrMethodFormatter('{x:,.0f}')
)

plt.tight_layout()

# Save the figure
plt.savefig(
    "images/gdp_vs_ai.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\n" + "-" * 70)
print("Research Question 3: What is the relationship between internet access and AI Readiness?")

# Remove countries with missing values
scatter_df = merged_df.dropna(
    subset=["InternetUsersPercent", "AIReadinessScore"]
).copy()

# Calculate the Pearson correlation coefficient
correlation = scatter_df["InternetUsersPercent"].corr(
    scatter_df["AIReadinessScore"]
)

print(f"Correlation = {correlation:.3f}")

# Create the figure
plt.figure(figsize=(10, 6))

# Create the scatter plot
plt.scatter(
    scatter_df["InternetUsersPercent"],
    scatter_df["AIReadinessScore"],
    alpha=0.7
)

# Plot the trend line
z = np.polyfit(
    scatter_df["InternetUsersPercent"],
    scatter_df["AIReadinessScore"],
    1
)

p = np.poly1d(z)

plt.plot(
    scatter_df["InternetUsersPercent"],
    p(scatter_df["InternetUsersPercent"]),
    linewidth=2,
    label="Trend Line"
)

# Display the correlation coefficient on the chart
plt.text(
    0.05,
    0.95,
    f"r = {correlation:.3f}",
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=dict(
        facecolor="white",
        alpha=0.8,
        edgecolor="black"
    )
)

# Annotate selected countries
important_countries = [
    "United States",
    "Rwanda",
    "Kenya"
]

for _, row in scatter_df.iterrows():

    if row["Country"] in important_countries:

        plt.text(
            row["InternetUsersPercent"],
            row["AIReadinessScore"],
            row["Country"],
            fontsize=8
        )

# Chart formatting
plt.xlabel("Internet Users (% Population)")
plt.ylabel("AI Readiness Score")

plt.title("Internet Usage vs AI Readiness (2024)")

plt.grid(alpha=0.4)

plt.legend()

plt.tight_layout()

# Save the figure
plt.savefig(
    "images/internet_vs_ai.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\n" + "-" * 70)
print("Research Question 4: How does Kenya compare with selected East African countries in AI Readiness?")

east_africa = [
    "Kenya",
    "Uganda",
    "Tanzania",
    "Rwanda",
    "Ethiopia"
]

# Filter the selected east African countries
east_df = merged_df[
    merged_df["Country"].isin(east_africa)
].copy()

# Sort countries by AI Readiness Score (highest to lowest)
east_df = east_df.sort_values(
    by="AIReadinessScore",
    ascending=False
)

# Display the results
print(
    east_df[
        [
            "Country",
            "AIReadinessScore"
        ]
    ]
)

# Create the visualization
plt.figure(figsize=(10, 6))

plt.barh(
    east_df["Country"],
    east_df["AIReadinessScore"]
)

# Display data labels
for index, value in enumerate(east_df["AIReadinessScore"]):
    plt.text(
        value + 0.3,
        index,
        f"{value:.2f}",
        va="center"
    )

# Put the highest score at the top
plt.gca().invert_yaxis()

# Chart formatting
plt.xlabel("AI Readiness Score")
plt.ylabel("Country")
plt.title("AI Readiness of Selected East African Countries (2024)")

plt.grid(
    axis="x",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

# Save the figure
plt.savefig(
    "images/east_africa_ai_readiness.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\n" + "-" * 70)
print("Research Question 5: Which socioeconomic factor is most strongly associated with AI Readiness?")

correlations = merged_df[
    [
        "AIReadinessScore",
        "GDPPerCapita",
        "InternetUsersPercent",
        "Population"
    ]
].corr()

print(correlations)

print("\nCorrelation with AI Readiness")

print(
    correlations["AIReadinessScore"].sort_values(
        ascending=False
    )
)