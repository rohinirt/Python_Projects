# Heart Disease Risk Factors Analysis  

##  Overview  
This project investigates the multifactorial influences contributing to cardiovascular health risks. By analyzing demographic details, lifestyle behaviors, and medical history, the study aims to identify key risk factors that increase susceptibility to heart disease. Statistical methods and machine learning models are applied to uncover correlations and patterns, helping highlight the most significant contributors to cardiovascular conditions.  

## Objective  
The objectives of this project are:  
- To explore the relationships between health indicators, lifestyle choices, and demographic factors in relation to heart disease.  
- To identify the most significant predictors of cardiovascular issues.  
- To apply statistical and visualization methods for risk factor discovery.  
- To provide actionable insights for preventive healthcare and early interventions.  

## Dataset   
- **Key Fields**:  
  - `HeartDiseaseorAttack` – Whether the respondent has ever reported CHD or MI  
  - `HighBP` – High blood pressure status  
  - `HighChol` – High cholesterol history  
  - `CholCheck` – Cholesterol check in past five years  
  - `BMI` – Body Mass Index  
  - `Smoker` – Smoking history  
  - `Stroke` – Stroke history  
  - `Diabetes` – Diabetes diagnosis  
  - `PhysActivity` – Physical activity levels  
  - `Fruits` / `Veggies` – Daily consumption habits  
  - `HvyAlcoholConsump` – Heavy alcohol consumption  
  - `AnyHealthcare` – Access to healthcare coverage  
  - `NoDocbcCost` – Couldn’t see a doctor due to cost  
  - `GenHlth` – Self-reported general health  
  - `MentHlth` / `PhysHlth` – Days of poor mental/physical health  
  - `DiffWalk` – Difficulty in walking or climbing stairs  
  - `Sex`, `Age`, `Education`, `Income` – Demographic attributes  

## Tools and Technologies  
- **Python** (Jupyter Notebook)  
- **Libraries**:  
  - `Pandas`, `NumPy` – Data handling and preprocessing  
  - `Seaborn`, `Matplotlib`, `Plotly` – Data visualization  

##  Methods  
1. **Data Exploration & Cleaning**  
   - Checked dataset info, null values, and column distributions.  
   - Encoded categorical variables for analysis.  

2. **Statistical Analysis**  
   - Applied **ANOVA tests** to investigate the influence of factors such as age, lifestyle, and medical history.  
   - Correlation analysis between health indicators and cardiovascular risks.  

3. **Visualization**  
   - Used bar charts, heatmaps, and boxplots to compare risk factors across demographic and lifestyle groups.  

4. **Predictive Modeling (if included in notebook)**  
   - Logistic regression / classification models to identify significant predictors of heart disease.  

## Key Insights  
- **Medical History**: High blood pressure, cholesterol, diabetes, and prior strokes show strong associations with heart disease.  
- **Lifestyle Factors**: Lack of physical activity, smoking, and heavy alcohol consumption significantly increase risk.  
- **Demographics**: Age and income play crucial roles, with older adults and lower-income groups being more vulnerable.  
- **General Health**: Respondents reporting poor overall health, mobility issues, or frequent mental/physical health struggles have higher susceptibility.  

## Conclusion
The study confirms that cardiovascular health is influenced by an interplay of lifestyle, genetics, medical history, and demographics. Among the strongest risk factors identified were high blood pressure, high cholesterol, diabetes, and smoking habits, while protective factors included physical activity and healthier dietary habits. Age and income inequalities were also evident, highlighting the importance of targeted healthcare interventions. Overall, this project demonstrates how data-driven analysis can aid in understanding and mitigating cardiovascular risks through early detection and lifestyle changes.
