# *Retail Price Optimization*

## *Case Study Overview*

**Fashionista** is a clothing retailer operating through physical stores and an online platform. The goal of this project is to **optimize product pricing** to stay competitive, **increase revenue**, and **improve customer acquisition and retention**.

---

## *Business Challenges*

* **Competitive Landscape:** High competition with similar product offerings, requiring attractive yet profitable pricing.
* **Inventory Management:** Need to balance supply and demand to avoid overstocking or stockouts.
* **Seasonal & Trend Variations:** Fast-changing fashion trends demand adaptive, dynamic pricing strategies.

## *Objective*

Optimize the prices of Fashionista’s products to:

* **Maximize Revenue and demand**
* **Forecasting demand Using advanced analytics techniques to estimate the demand for different products at different price points**
* **Estimate price elasticity analysis to understand how changes in price affect demand for its products**
* **Stay Competitive** in the market prices with increasing profit and attracting customers

## *Dataset*

Source: [Kaggle – Retail Price Optimization Case Study](https://www.kaggle.com/datasets/bhanupratapbiswas/retail-price-optimization-case-study)

### **Column Descriptions**

| Column                       | Description                                    |
| ---------------------------- | ---------------------------------------------- |
| `product_id`                 | Unique identifier for each product             |
| `product_category_name`      | Product category (e.g., clothing, accessories) |
| `month_year`                 | Month and year of transaction                  |
| `qty`                        | Units sold                                     |
| `total_price`                | Total revenue for the product in that period   |
| `freight_price`              | Shipping cost                                  |
| `unit_price`                 | Unit price of the product                      |
| `product_name_lenght`        | Length of the product name                     |
| `product_description_lenght` | Characters in product description              |
| `product_photos_qty`         | Number of images uploaded                      |
| `product_weight_g`           | Product weight in grams                        |
| `product_score`              | Average customer review score                  |
| `customers`                  | Number of unique customers                     |
| `weekday`                    | Day of the week (1-7)                          |
| `weekend`                    | Binary indicator for weekend sales             |
| `holiday`                    | Binary indicator for holiday periods           |
| `month`                      | Numeric month (1-12)                           |
| `year`                       | Year of sale                                   |
| `s`                          | Seasonality factor                             |
| `volume`                     | Adjusted sales volume                          |
| `comp_1, comp_2, comp_3`     | Competitor prices                              |
| `ps1, ps2, ps3`              | Competitor product scores                      |
| `fp1, fp2, fp3`              | Competitor freight prices                      |
| `lag_price`                  | Previous period’s price                        |

## *Approach*

### **1️) Exploratory Data Analysis (EDA)**

* **Data Understanding**
* **Data Cleaning & Transformation**

  * Removed unnecessary columns
  * Changed data types for proper analysis
* **Data Analysis**

  * Distribution of **unit price, revenue, and quantity**
  * Distribution of metrics by **products and categories**
  * Trends over time by **products and categories**

### **2️) Feature Engineering**

* Calculated **profit margin**
* Created **price change indicators**:
* Created **competitor price gaps**:

### **3️) Price Elasticity Analysis**

* Calculated **price elasticity**:
    Elasticity = % Change in Quantity/% Change in Price
  
* Visualized elasticity for each product across months.
  
### **4️)Demand Forecasting**

* Built a **Random Forest Regression model** to predict demand.

  * **Performance Metrics:**

    * **MAE:** 13.24
    * **RMSE:** 16.98
* Predicted demand for the **next 4 months** and visualized the trend.

### **5️)Price Optimization**

**Steps:**

1. Take the current price of a product and its related features.
2. Generate a range of prices (80% to 120% of the current price).
3. Use the trained model to **predict demand** for each simulated price.
4. Calculate revenue: Quantity* Unit Price
5. Identify the **optimal price** that maximizes predicted revenue.
6. Compare **current vs optimized revenue** to calculate percentage improvement.
7. Converted all the results into a dataframe
8. Visualize **price change % vs revenue change %** for all products.

## *Insights*

* Most products are priced between **\$10 and \$150** — indicating a **low-price product strategy**.
* **Quantity distribution** is **left-skewed**, showing fewer products sell at high volumes.
* **Health & Beauty** generates the **highest revenue**, while **console games** generate the least.
* **Garden tools** have the **highest demand and customer base**, while console games rank lowest.
* **Total revenue** showed a consistent upward trend until May 2018, then plateaued.
* Most products have elasticity near **0**, indicating **low sensitivity to price changes**.

## *Results*

* Developed a **Random Forest demand forecasting model** for predicting future demand considering factors such as seasonality, trends, promotional activities,  external factors (e.g.,weekdays, holidays, weekends), product_score, price, competitors price.
* Derived **optimal prices** for products to maximize revenue.
* Achieved an **average 28% revenue increase per product** through price optimization.

---

## *References*

* Kaggle Dataset: [Retail Price Optimization Case Study](https://www.kaggle.com/datasets/bhanupratapbiswas/retail-price-optimization-case-study)
* Article: [Price Optimization Using Python](https://amanxai.com/2024/07/22/price-optimization-using-python/)

