*Case Study: Retail Price Optimization for a Clothing Store*

Company Background:
Imagine a clothing store called "Fashionista" that sells a wide range of apparel and accessories. Fashionista operates both physical stores and an online e-commerce platform. The company wants to optimize its pricing strategy to maximize revenue and improve competitiveness in the market.

Challenges Faced:
Fashionista is facing several challenges in pricing its products effectively:

Competitive Landscape: The retail industry is highly competitive, with multiple competitors offering similar products. Fashionista wants to gain a competitive edge by offering attractive prices without sacrificing profitability.

Inventory Management: Fashionista needs to manage its inventory effectively by setting prices that balance supply and demand. Optimizing prices based on inventory levels can help prevent overstocking or understocking of products.

Seasonal and Trend Variations: Fashion trends change rapidly, and demand for specific items fluctuates throughout the year. Fashionista needs to adapt its prices to reflect these seasonal and trend variations to capture maximum sales opportunities.

TASK
To optimize prices of their products to stay competitive in the market with increasing profit and attracting customers.
Forecasting demand Using advanced analytics techniques develops demand forecasting models that consider factors such as seasonality, trends, promotional activities, and external factors to predict customer demand accurately to estimate the demand for different products at different price points.
Conducts price elasticity analysis to understand how changes in price affect demand for its products. This analysis helps identify price points at which demand becomes more or less responsive, allowing Fashionista to set optimal prices that maximize revenue.


Data Source
Kaggle: https://www.kaggle.com/datasets/bhanupratapbiswas/retail-price-optimization-case-study
Column	Description
product_id	Unique identifier for each product.
product_category_name	Category of the product (e.g., bed_bath_table, clothing, accessories).
month_year	Month and year of transaction (e.g., 01-05-2017).
qty	Number of units sold in that month.
total_price	Total revenue for that product in that period (qty × unit_price).
freight_price	Cost of shipping for the product.
unit_price	Unit price of the product.
product_name_lenght	Length of the product name (possibly used for NLP or metadata analysis).
product_description_lenght	Number of characters in the product description.
product_photos_qty	Number of product images uploaded.
product_weight_g	Weight of the product in grams.
product_score	Average review rating of the product.
customers	Number of unique customers for that product in that period.
weekday	Numeric indicator for weekday (1–7).
weekend	Binary (0/1), whether the sale occurred on a weekend.
holiday	Binary (0/1), whether the sale occurred during a holiday period.
month	Extracted month as a number (1–12).
year	Year of sale.
s	Seasonality factor (possibly pre-calculated demand index).
volume	Total sales volume (may be same as qty but often adjusted by weight or package).
comp_1	Competitor 1’s price for the product.
ps1	Competitor 1’s product score.
fp1	Competitor 1’s freight price.
comp_2	Competitor 2’s price for the product.
ps2	Competitor 2’s product score.
fp2	Competitor 2’s freight price.
comp_3	Competitor 3’s price for the product.
ps3	Competitor 3’s product score.
fp3	Competitor 3’s freight price.
lag_price	Previous period’s price for the same product (used for trend modeling).

Approach
1)Exploratory Data Analysis
  a)Data Understaning
  b)Data cleaning and Transformation
-Removed Unnecessary columns
-changing the datatypes of columns
  c)Data Analysis
  -distribution of unit price, revenue, and qty 
  - distributio by products and category
  - trend over time
    
2)Feature Engineering
 -Calculating Profit Margin
 -calculating price change indicators: lag price
 -price difference with competitors

 3)Calculating Price Elasticity
 - calculated elasticity using the formula
 - visualised elasticity of each products by month

4)Demand Forecasting 
-Built Random Forest model to predict the demand
MAE: 13.24
RMSE: 16.98
-predicted demand for next 4 months and visualised

5)Price Optimization
Step 1: Take the current price of a product and its features (like category, competition, etc.).

##### Step 2: Try a range of prices (from 80% to 120% of the current price).

##### Step 3: Use the trained model to predict sales quantity for each price.

##### Step 4: Calculate the revenue = price × predicted quantity for each price.

##### Step 5: Identify the price that gives the highest predicted revenue (optimal price).

##### Step 6: Compare the current revenue vs optimized revenue to calculate potential improvement (in %).

##### Step 7: visualise Price change percent vs revenue change percent


INSIGHTS
-The prices of maximum products ranges from 10 - 150, indiacating low pricing for maximum products. 
-The histogram for qty is left skewed
-Health beauty products generate highest revenue while console_games products the least
- garden_tools products has the hight qty demand while console games has the least.
- garden_tools products has the highest customers while console games has the least.
- The overall total revenue increasing over months with few small drops. It suddnly after may 2018.
- Maximum products falls near 0 elasticity indicating-----

Result
- Random Forest model forest model is built to predict demand based on different price for different products.
- Based on the model the best price for each product optimized to generate high demand and generate more revenue.
- On average 28% revenue per product gained using optimized Product price
