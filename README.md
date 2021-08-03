# Omaha House Price Prediction
Building a web app to predict house prices in Omaha, NE using model trained with data scraped from Realtor.com.

Web app and choropleth map could be found here: https://share.streamlit.io/kirshan-tx/omaha-house-price-prediction/main/omaha_house_app.py

## Data 
Data collected using realtor-scraper python script in the scraper folder; for single-family homes, condos, townhomes and multi-family homes (all existing homes and not foreclosures) listed on July 2021.

## Packages used
- **Beautiful Soup** is a python package for parsing HTML and XML documents.
```
conda install -c anaconda beautifulsoup4 
```
- **Folium** is a python library used for visualizing geospatial data.
```
conda install -c conda-forge folium
```
- **Streamlit** is a python library for custom web apps for machine learning and data science.
```
conda install -c conda-forge streamlit 
```

## Process
1. Web Scraping
2. Data Cleaning
3. EDA
4. Outlier Detection
5. Model Selection
6. Deployment
