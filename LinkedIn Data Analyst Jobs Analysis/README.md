# LinkedIn Data Analyst Jobs – Market Analysis

## Overview
This project analyzes data analyst job postings on LinkedIn to uncover market trends: popular keywords in job descriptions and titles, top-paying industries and roles, and job availability by location. The goal is to translate raw postings into actionable insights that improve job-search strategy and targeting.

## Objective
- Identify frequent keywords in job descriptions and titles to optimize resumes and applications.
- Quantify job availability by location, company, and industry.
- Compare compensation by industry, company, and job type (hourly vs yearly).
- Summarize hiring patterns (onsite/remote/hybrid; full-time/contract/internship).

##  Dataset
- **File Used**: `linkedin_jobs.csv`
- **Key Fields (observed in notebook)**:
  - `title` (Job Title), `company`, `Industry`
  - `Job Description`
  - `location`
  - `Mode` (e.g., Onsite/Remote/Hybrid)
  - `Type` (e.g., Full-time/Contract/Internship)
  - `Avg Salary`, `Min Salary`, `Max Salary`
  - Salary basis flags: `Hourly`, `Yearly`

## Tools and Technologies: Python (Jupyter Notebook)
- **Data & Viz**: `pandas`, `numpy`, `matplotlib` (and basic `seaborn` styles if used)
- **NLP**: `nltk` (`punkt`, `stopwords`, `FreqDist`) for tokenization, stopword removal, and keyword frequency
- **Visualization aids**: word frequency plots / wordclouds (if included)

##  Methods (if applicable)
1. **Data Preparation**
   - Load CSV; set display options.
   - Basic cleaning: lowercasing text, punctuation removal, stopword filtering for text fields.

2. **NLP Keyword Mining**
   - Concatenate text from `Job Description`, `title`, `company`, and `Industry`.
   - Tokenize (`word_tokenize`) → remove punctuation/stopwords → frequency distribution (`FreqDist`).
   - Extract **Top 10 keywords** for:
     - Job Descriptions
     - Job Titles
     - Companies
     - Industries

3. **Market Structure & Supply**
   - `value_counts()` and `groupby().count()` to rank:
     - **Top 10 locations by number of jobs**
     - **Top 10 companies by number of jobs**
     - Distribution by **Mode** (Onsite/Remote/Hybrid) and **Type** (FT/Contract/Intern)

4. **Compensation Analysis**
   - `groupby().mean()` on `Avg Salary` for:
     - **Industries** (hourly and yearly subsets)
     - **Companies** (top-N by postings)
     - **Job Type** (Hourly vs Yearly; Full-time vs Contract)
   - Bar charts for comparisons.

## Key Insights

- **Top Keywords (Title):** e.g., `[Data]`, `[Software]`, `[Senior]`, `[Analyst]`, `[power bi]`, `[Developer]`, `[Learning]`.
- **Top Keywords (Titles):** e.g., `[data]`, `[Team]`, `[analytics]`, `[bi analyst]`.
- **Job Type & Mode:** Majority **[Full-time]** (92%);
- **Strategy Implications:** Align resume with high-frequency skills (e.g., SQL, Excel, Python, Tableau/Power BI); target **[top cities]** and **[industries]** for higher pay; prioritize **[mode/type]** based on availability trends.

## Conclusion
This analysis maps the LinkedIn data analyst job market across skills demand, geography, hiring organizations, and compensation. High-frequency keywords guide resume optimization; location and company rankings reveal where roles cluster; and industry-level salary comparisons highlight the best-paying sectors for both hourly and yearly roles. Together, these insights support a focused application strategy: emphasize in-demand skills, target top locations and industries, and choose job types/modes aligned with market availability and pay
