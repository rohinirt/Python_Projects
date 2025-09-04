# Amazon Reviews – Sentiment Analysis  

## Overview  
This project analyzes Amazon toy reviews to understand customer sentiment and opinions. Using Natural Language Processing (NLP), the reviews are classified into **positive**, **negative**, and **neutral** sentiments. The analysis also explores how these sentiments relate to product ratings and identifies the most frequent keywords associated with each sentiment.  

## Objective  
The main objectives of this project are:  
- To preprocess Amazon toy reviews for sentiment analysis.  
- To classify reviews as positive, negative, or neutral.  
- To identify the distribution of ratings within each sentiment group.  
- To extract and visualize keywords that represent customer opinions across sentiments.  
- To generate insights that can help businesses understand customer satisfaction and improve product offerings.  

## Dataset  
- **Key Fields**:  
  - `Id` – Unique identifier for each review  
  - `reviewerName` – Name of the reviewer  
  - `overall` – Rating given (numeric)  
  - `reviewText` – Written customer review  
  - `helpful_yes` – Number of helpful votes  
  - `helpful_no` – Number of unhelpful votes  
  - `wilson_lower_bound` – Statistical measure to rank reviews by helpfulness confidence
  - 
## Tools and Technologies  
- **Python** (Jupyter Notebook)  
- **Libraries**:  
  - `NLTK` (tokenization, stopwords, sentiment analysis with VADER)  
  - `Pandas` (data handling)  
  - `Matplotlib`, `Seaborn` (visualizations)  
  - `WordCloud` (keyword visualization)  

##  Methods  
1. **Data Preprocessing**  
   - Tokenization using `word_tokenize`  
   - Removal of stopwords and non-alphabetic characters  
   - Conversion to lowercase for normalization  

2. **Sentiment Analysis**  
   - Used **VADER SentimentIntensityAnalyzer** from NLTK  
   - Generated compound sentiment scores  
   - Classified reviews into **positive (compound > 0)**, **negative (compound < 0)**, and **neutral (compound = 0)**  

3. **Exploratory Analysis**  
   - Distribution of reviews across sentiments (pie charts)  
   - Ratings breakdown for each sentiment group (bar charts)  
   - Keyword extraction with word clouds to highlight common terms in positive, negative, and neutral reviews  

## Key Insights  
- **Sentiment Distribution**: Majority of reviews are **positive**(79.3%) , followed by **negative**(13.9%), with fewer(6.8%) neutral reviews.  
- **Ratings Analysis**: Positive and Neutral reviews are strongly aligned with higher ratings (5 stars) while Negative Reviews has comparable most rating in the range 1 - 4 stars
- **Keyword Trends**:  
  - Positive reviews emphasize words like *“great”*, *“good”*,*“works”* and *“price”*.  
  - Negative reviews highlight issues like *“memory”*, *“phone”*, or *“cards”*.  
  - Neutral reviews often contain descriptive but less emotional language.  
- **Business Implication**: Insights can help sellers identify product strengths that drive satisfaction and common issues that lead to dissatisfaction.  

## Conclusion
This project successfully applied sentiment analysis on Amazon toy reviews, categorizing customer feedback into positive, negative, and neutral sentiments. The results show a clear alignment between higher ratings and positive reviews, as well as lower ratings with negative reviews. Keyword analysis revealed recurring themes that highlight what customers appreciate and where products fall short. Overall, the study demonstrates how NLP techniques can transform raw text data into actionable insights, enabling businesses to enhance customer experience and improve product quality.
