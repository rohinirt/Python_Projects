#  House Price Prediction  

##  Overview  
This project applies **machine learning techniques** to predict house prices based on various factors such as property features, location, and amenities. By analyzing historical housing data, the model aims to uncover the relationship between these features and property prices, providing a reliable prediction framework for buyers, sellers, and real estate professionals.  

##  Objective  
To build a predictive model that estimates **house prices accurately** and identifies the most influential features impacting property valuation.  

##  Dataset  
- **File Used**: `housing_prices_dataset.csv`  
- **Key Fields** (selected):  
  - `Id`: Unique property identifier  
  - `LotArea`: Lot size in square feet  
  - `OverallQual`: Overall material and finish quality (rating)  
  - `YearBuilt`: Year the house was constructed  
  - `GrLivArea`: Above ground living area (sq ft)  
  - `FullBath`: Number of full bathrooms  
  - `BedroomAbvGr`: Number of bedrooms above ground  
  - `GarageCars`: Garage size in car capacity  
  - `SalePrice`: Target variable (house price)  

## 🛠 Tools and Technologies  
- **Python (Jupyter Notebook)**  
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`  

## 🔍 Methods  
1. **Data Cleaning & Preprocessing**  
   - Handling missing values  
   - Encoding categorical variables  
   - Feature scaling & transformation  

2. **Exploratory Data Analysis (EDA)**  
   - Visualizing distributions of house prices  
   - Correlation heatmap of numerical features  
   - Identifying important predictors (e.g., `OverallQual`, `GrLivArea`, `YearBuilt`)  

3. **Feature Engineering**  
   - Creating derived features like house age  
   - Combining related variables for better predictive power  

4. **Modeling**  
   - Regression techniques: Linear Regression, Decision Tree, Random Forest, Gradient Boosting  
   - Hyperparameter tuning for optimal performance  
   - Evaluation metrics: RMSE, R² score  

## 📈 Key Insights  
Accuracy of Model
  - Mean Absolute Error (MAE): 28881.69566440968
  - R-squared (R2): 0.8010156395205392  

## Conclusion  
The project successfully demonstrates that **machine learning models can predict house prices with high accuracy**. Among all features, **overall quality, living area, and construction year** emerged as the most influential. Such predictive modeling can help real estate stakeholders in **pricing strategies, investment decisions, and risk assessment**.  
