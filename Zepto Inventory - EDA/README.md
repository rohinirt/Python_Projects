# Zepto Product Data – Exploratory Data Analysis (EDA)

## Objective
This project performs an in-depth exploratory data analysis (EDA) on Zepto's product listing dataset. The goal is to understand product variety, pricing trends, discount strategies, inventory levels, and category performance to provide actionable business insights.

## Dataset Overview

The dataset contains detailed information on thousands of Zepto’s products across different categories. Below are the columns:

| Column Name         | Description                                      |
|---------------------|--------------------------------------------------|
| `Category`          | Product category (e.g., Fruits, Dairy, Snacks)   |
| `name`              | Product name                                     |
| `mrp`               | Maximum Retail Price of the product              |
| `discountPercent`   | Discount applied to the product (%)              |
| `availableQuantity` | Number of units available in stock               |
| `weightInGms`       | Weight of the product in grams                   |
| `outOfStock`        | Binary indicator: 1 = out of stock, 0 = available|
| `quantity`          | Units per pack or SKU-specific quantity          |


## Key Exploratory Steps

### 1. **Univariate Analysis**
- Distribution plots for `mrp`, `discountPercent`, `availableQuantity`, and `weightInGms`
- Count plots for categories and top product names
- Pie chart of in-stock vs out-of-stock products

### 2. **Bivariate Analysis**
- Relationships between:
  - `mrp` and `discountPercent`
  - `weightInGms` and `mrp`
  - `discountPercent` and `availableQuantity`
- Bar plots and scatter plots for deeper visual insights

### 3. **Category-Level Analysis**
- Average price (`mrp`) per category
- Total available quantity per category
- Boxplots for product prices across different categories
- Derived metric: `MRP per 100g` for normalized price comparison


## Insights About Zepto from This Dataset

- **Product Distribution**: Zepto offers over 3,200 products, with a concentration in categories like **Fruits & Vegetables**, **Dairy**, and **Snacks**, reflecting a focus on daily essentials and fast-moving consumer goods.

- **Pricing Landscape**: The majority of products are affordably priced below ₹200, but the presence of high-MRP items introduces a **right-skewed price distribution**, indicating a mix of mass-market and premium SKUs.

- **Discount Strategy**: Discounts are modest for most items (mostly ≤10%), with some **structured tiers (5%, 10%, 15%)** commonly applied — hinting at planned promotions rather than aggressive discounting across the board.

- **Stock Levels & Availability**: While most items are **in stock (≈89%)**, a small but relevant percentage are **out of stock (≈11%)**, which may indicate high demand or gaps in supply chain planning.

- **Category-wise Pricing**: Certain categories like **Health & Nutrition** and **Beauty & Hygiene** show significantly **higher average MRPs**, while others like **Staples** and **Bakery** remain cost-effective — revealing Zepto’s category-specific pricing tiers.

- **Normalized Pricing**: The analysis of **MRP per 100g** standardizes product value and reveals outliers — such as lightweight yet costly items, often in beauty or health segments.

- **Inventory Strategy**: Some items show disproportionately high availableQuantity, possibly due to **stockpiling of high-demand or slow-moving goods**, with discounting used as a clearing tool in these cases.

- **Multivariate Insights**:
  - No strong correlation between price and discount — pricing and promotion seem to be handled independently.
  - Heavier products generally cost more, but outliers suggest **premium pricing not solely tied to size or weight**.

