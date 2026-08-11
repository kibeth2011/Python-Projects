# Global AI Adoption and Readiness: A Python Data Analysis
## Project Overview
Artificial Intelligence (AI) is transforming economies, governments, and societies across the world. However, countries differ significantly in their readiness to adopt and govern AI technologies. Understanding the socioeconomic factors associated with AI readiness can provide valuable insights for policymakers, researchers, and technology stakeholders.

This project demonstrates an end-to-end data analysis workflow using Python to analyze the 2024 Government AI Readiness Index together with socioeconomic indicators from the World Bank to explore how economic development, internet access, and population relate to national AI readiness.

## Objectives
The objectives of this project are to:
- Analyze global AI Readiness scores.
- Examine whether GDP per capita is associated with AI Readiness.
- Investigate whether internet access influences AI Readiness.
- Compare Kenya with selected East African countries.
- Identify which socioeconomic factor is most strongly associated with AI Readiness.

## Research Questions
1. Which countries had the highest AI Readiness scores in 2024?
2. Is GDP per capita associated with AI Readiness?
3. Does internet access influence AI Readiness?
4. How does Kenya compare with selected East African countries in AI Readiness?
5. Which socioeconomic factor is most strongly associated with AI Readiness?

## Dataset
This project combines four publicly available datasets.

### Source: Oxford Insights
1. <a href="https://oxfordinsights.com/ai-readiness/government-ai-readiness-index-2024">Government AI Readiness Index (2024)</a> or <a href="https://github.com/kibeth2011/Python-Projects/blob/main/Global%20AI%20Adoption%20and%20Readiness/Data/2024-GAIRI-data.xlsx">GAIRI(2024) Data Copy</a>

### Source: World Health Organization (WHO)
2. <a href="https://data.worldbank.org/indicator/NY.GDP.PCAP.CD">GDP per capita (current US$)</a> or <a href="https://github.com/kibeth2011/Python-Projects/blob/main/Global%20AI%20Adoption%20and%20Readiness/Data/API_NY.GDP.PCAP.CD_DS2_en_excel_v2_33108.xls">GDP Data Copy</a>
3. <a href="https://data.worldbank.org/indicator/IT.NET.USER.ZS">ndividuals using the Internet (% of population)</a> or <a href="https://github.com/kibeth2011/Python-Projects/blob/main/Global%20AI%20Adoption%20and%20Readiness/Data/API_IT.NET.USER.ZS_DS2_en_excel_v2_33090.xls">Internet Data Copy</a>
4. <a href="https://data.worldbank.org/indicator/SP.POP.TOTL">Population, total</a> or <a href="https://github.com/kibeth2011/Python-Projects/blob/main/Global%20AI%20Adoption%20and%20Readiness/Data/API_SP.POP.TOTL_DS2_en_excel_v2_33073.xls">Population Data Copy</a>

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- OpenPyXL
- Visual Studio Code

## Methodology
The project followed the following workflow:

### 1. Data Import
Four datasets were imported into Python.

### 2. Data Inspection
Each dataset was inspected by checking:
- Shape
- Column names
- Data types
- Missing values
- Duplicate records

### 3. Data Cleaning
The datasets were cleaned by:
- Selecting only required columns.
- Renaming variables for consistency.
- Removing missing observations.
- Resetting indices.

### 4. Country Name Standardization
The datasets used different naming conventions for several countries. Country names were standardized to match the WHO naming convention before the datasets were merged. For example, "United States of America" was standardized to "United States."

### 5. Data Integration
The cleaned datasets were merged using the Country field.

### 6. Exploratory Data Analysis
The merged dataset was analyzed using descriptive statistics, correlation analysis, and data visualization.

## Analysis and Findings
### Research Question 1: Which countries had the highest AI Readiness scores in 2024?
### Visualization
![Reload Image](https://github.com/kibeth2011/Python-Projects/blob/main/Global%20AI%20Adoption%20and%20Readiness/Images%20and%20Screenshots/top10_ai_readiness.png)

### Insight
The analysis shows that the United States ranked first globally, followed by Singapore, the Republic of Korea, France, and the United Kingdom. These countries recorded the highest AI Readiness scores in 2024, reflecting strong preparedness for AI adoption.

### Research Question 2: What is the relationship between GDP per capita and AI Readiness?
### Visualization
![Reload Image](https://github.com/kibeth2011/Python-Projects/blob/main/Global%20AI%20Adoption%20and%20Readiness/Images%20and%20Screenshots/gdp_vs_ai.png)

### Insight
The analysis found a moderate positive correlation (r = 0.636) between GDP per capita and AI Readiness. This suggests that wealthier countries generally tend to have higher AI Readiness scores, likely because they have greater financial resources to invest in digital infrastructure, research, and AI development. However, the relationship is not perfect, indicating that factors beyond economic wealth also influence a country's AI preparedness.

### Research Question 3: What is the relationship between internet access and AI Readiness?
### Visualization
![Reload Image](https://github.com/kibeth2011/Python-Projects/blob/main/Global%20AI%20Adoption%20and%20Readiness/Images%20and%20Screenshots/internet_vs_ai.png)

### Insight
The analysis found a strong positive correlation (r = 0.731) between internet usage and AI Readiness. Countries with greater internet access generally recorded higher AI Readiness scores, highlighting the importance of digital connectivity in supporting AI adoption. Compared to GDP per capita, internet access showed a stronger relationship with AI Readiness in this study, suggesting that widespread digital access may be a key driver of national AI preparedness.

### Research Question 4: How does Kenya compare with selected East African countries in AI Readiness?
### Visualization
![Reload Image](https://github.com/kibeth2011/Python-Projects/blob/main/Global%20AI%20Adoption%20and%20Readiness/Images%20and%20Screenshots/east_africa_ai_readiness.png)

### Insight
The comparison shows that Rwanda recorded the highest AI Readiness score (51.25) among the selected East African countries, followed by Kenya (43.56). Ethiopia (38.34), Tanzania (35.08), and Uganda (34.63) ranked lower. Kenya ranked second in the region, indicating relatively strong AI preparedness, although it still trails Rwanda by about 7.7 points.

### Research Question 5: Which socioeconomic factor is most strongly associated with AI Readiness?
### Code Snippet
![Reload Image](https://github.com/kibeth2011/Python-Projects/blob/main/Global%20AI%20Adoption%20and%20Readiness/Images%20and%20Screenshots/socioeconomic%20factor%20correlation.PNG)

### Insight
The correlation analysis shows that internet access has the strongest positive relationship with AI Readiness (r = 0.73), followed by GDP per capita (r = 0.64). Population has a weak positive relationship (r = 0.18), indicating that population size alone is not a strong predictor of AI readiness. These findings suggest that digital connectivity is more closely associated with national AI preparedness than economic wealth or population size in this study.

# Conclusion
This project analyzed the 2024 Government AI Readiness Index together with World Bank socioeconomic indicators to understand factors associated with national AI readiness. The findings showed that countries with higher GDP per capita and greater internet access generally achieved higher AI Readiness scores. Among the variables analyzed, internet access exhibited the strongest relationship with AI Readiness, while population had only a weak association. The regional comparison also showed that Kenya ranked second among the selected East African countries, behind Rwanda. Overall, the results suggest that digital connectivity and economic development are important contributors to AI preparedness.

# Recommendations
1. Governments should continue investing in digital infrastructure to improve AI readiness.
2. Expanding internet access can help strengthen AI adoption and innovation.
3. Policymakers should complement economic growth with AI governance strategies and digital skills development.
4. Future studies could include additional socioeconomic indicators such as education, research expenditure, and ICT investment.

# Limitations
- The analysis used data from a single year (2024).
- Some countries were excluded because of missing values.
- Correlation measures association and does not imply causation.
- AI Readiness is a composite index and may not fully represent actual AI adoption.

# Author

Kibet Hillary

BSc Applied Statistics, with IT (Second Class Honours, Upper Division)

Data Analyst

Email: kibeth2011@gmail.com

<a href="https://github.com/kibeth2011">GitHub</a>

<a href="https://www.linkedin.com/in/kibet-hillary-4654507b/">LinkedIn</a>




















