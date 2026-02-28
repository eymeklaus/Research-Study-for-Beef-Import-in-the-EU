# **Research Study for Beef Import in the EU**

## **Business Case**
We are a big processing meat company in south America and we are expanding our food business in Europe. As part of this expansion strategy, we intend to begin exporting beef to European Union countries within the next year. However, due to limited market knowledge, the company currently lacks clarity on which specific EU country would provide the most favorable conditions for successful market entry and long-term growth.

This research aims to support strategic decision-making by analyzing key market indicators, including beef prices, per capita consumption, and total consumer expenditure across European countries. By examining these factors, the study seeks to better understand consumer behavior and market dynamics within the European Union. The ultimate objective is to identify the most attractive and economically viable country for market penetration, thereby maximizing the potential for profitability and sustainable business expansion.

---
## **Problem Statement**

### 1.**Price Competitiveness Problem**  
Identify which country has the most advantageous price, in order to evaluate profitability potential and pricing competitiveness for market penetration.

### 2. **Demand Potential Problem**
Assess which country demonstrates the highest demand for beef, as measured by per capita consumption and total expenditure, to determine the market with the greatest revenue potential.

### 3.**Market Entry Problem**  
Determine which country offers the most favorable market conditions for entering and expanding a new beef business, based on price levels, consumption patterns, and expenditure trends.

---

## **Data Collection & Preparation**

For the project preparation, we decided to collect API data from the Agri Food Markets of the European Commission and the dataset related to beef consumption from Our World in Data. The Agri Food Markets provided prices for the beef market in 27 countries of the European Union from 2000 until 2026. The consumption dataset was obtained from Our World in Data for 27 countries in the European Union from 2000 to 2022.

In order to compare the price and consumption from each country, the total expenditure was calculated and added to the dataset. Finally, based on the missing data, we decided to work within the period from 2013 to 2022 for all countries.

Following the data collection, we proceeded with the application of different cleaning and standardization techniques. First, we conducted a descriptive analysis. Secondly, we continued with cleaning columns, handling null values, formatting columns, grouping, filtering, merging, applying functions, and creating crosstab and pivot tables in order to conduct the exploratory data analysis (EDA).

---
## **Analysis**

Following the data collection, cleaning, and preparation stages, the analysis was conducted in accordance with the defined problem statements and research objectives. The purpose of this phase was to identify the most attractive European market for beef export by evaluating price levels, consumption patterns, and total consumer expenditure.

### 1. **Comparative Overview**  
The first graph provided a comparative overview of the average total expenditure (2013-2022) for all countries. This visualization allowed for an initial assessment of the relative attractiveness and positioning of each country in terms of average of total expenditure, which allowed us to choose the top 5 countries. 

### 2. **Price per Kilogram Evolution**  
The second graph focused on the evolution of price per kilogram, enabling the evaluation of pricing structures and identifying markets with higher profitability potential. This analysis helped determine which countries offer favorable price conditions for exporters.

### 3. **Per Capita Beef Consumption**  
The third graph examined per capita beef consumption, providing insights into consumer demand and market size. Higher consumption levels indicate stronger demand and greater opportunities for sustained sales volume and long-term market penetration.

### 4. **Total Expenditure on Beef**  
The fourth graph analyzed total expenditure on beef, which reflects the overall economic value of the market. This indicator combines both price and consumption effects, offering a comprehensive measure of market revenue potential and profitability.

By comparing price competitiveness, consumption demand, and total expenditure, the analysis enabled the identification of the most promising country for successful market entry and business expansion within the European Union.

---
## **Tools Used**
- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- GitHub
---
## **Presentation**
You can find the presentation in the following link: 

## **References**
- Agri Food Markets, European Commission  
  [Agri Food Markets](https://agridata.ec.europa.eu/extensions/DataPortal/agricultural_markets.html)

- Our World in Data  
  [Per Capita Meat Consumption](https://ourworldindata.org/grapher/per-capita-meat-consumption-by-type-kilograms-per-year?facet=entity&country=OWID_EU27~FRA~IRL~ITA~DNK~BEL~BGR~HRV~CYP~EST~FIN~DEU~GRC~HUN~LVA~LTU~LUX~MLT~NLD~POL~PRT~ROU~SVK~SVN~SWE~ESP~CZE~AUT)
