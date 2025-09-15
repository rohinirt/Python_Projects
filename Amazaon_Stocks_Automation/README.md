# Amazon Stock Data Automation

## Objective
The goal of this project is to **automate the extraction, storage, and preprocessing of Amazon (AMZN) stock data** using Python. Instead of manually downloading stock prices, the workflow automatically fetches daily data, saves it in Excel, and prepares it with financial metrics such as returns and moving averages for analysis and visualization.

##  Dataset Overview
The dataset is sourced from the **Yahoo Finance API** via the `yfinance` Python library.  
Below are the key fields:

| Column         | Description                                                |
|----------------|------------------------------------------------------------|
| Date           | Trading date                                               |
| Open           | Opening price of AMZN stock                                |
| High           | Highest price during the trading session                   |
| Low            | Lowest price during the trading session                    |
| Close          | Closing price of AMZN stock                                |
| Volume         | Number of shares traded                                    |

##  Workflow
1. **Data Extraction**  
   - Used `yfinance` to download AMZN historical data.  
2. **Data Storage**  
   - Automated saving into Excel (`.xlsx`) for structured access.   
3. **Automation**  
   - Scheduled with **Windows Task Scheduler** for daily updation of data.

##  Tech Stack
- **Python** (pandas, yfinance, openpyxl)  
- **Excel** (storage)  
- **Windows Task Scheduler** (automation)  

## Conclusion
This project showcases the ability to:  
- Automate financial data collection.  
- Perform preprocessing and enrichment for analytics.

## Future Scope  
- Build dashboard in Tableau visualising Trends in different time periods(days, months, years)

