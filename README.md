# Project Credit Card Churn Analysis

**Project Credit Card Churn Analysis** is a data analysis project focused on assessing which bank customers are likely to churn or become attrited so the bank can take proactive measures to retain them. Using a real-world dataset, this project investigates how account attributes (such as credit limit, tenure with company, income level and account inactivity) alongside more personal attributes such as age and gender may impact a customer churning. The analysis includes data cleaning, visualization, and predictive modeling to provide actionable insights for estimating healthcare expenses.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Dataset Content
The dataset used in this project is sourced from [Kaggle: Healthcare Insurance Dataset](https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers). It contains records of individuals, capturing both personal and account specific attributes, such as account utlization, that may influence a customer churning.

**Features include:**
customer status
- `age`: Age of the primary beneficiary (numeric)
- `gender`: Gender of the insured individual (male as `m`, `female` as `f`)
- `income level`: The current earnings of the individual
- `tenure in months`: How long the individual has been trading with the credit card company
- `inactivity in the last 12 months`: Continuous inactivity within the span of 12 months
- `total transaction amount`: The amounted figure of total transactions
- `total transaction count`: The amount of transactions performed on the account
- `average utilization ratio`: The average account usage ratio

## Business Requirements
I will be focusing on 3 requirements:
* 1. Is there a discrepancy between income levels of male and female customers, attrited and existing, and also consider the male and female ratio here.
* 2. Is there a relationship between transaction amount, alongside transaction count between existing and attrited customer?
* 3. Is there a large discrepancy between credit limit and account usage between existing and attrited customers?


## Hypothesis and how to validate?

**Hypothesis:** There will be more female than male customers and of course this may look to increase attrition levels amongst females.

   - **Validation** Created a clustered column chart comparing Total_Trans_Amt for attrited vs. existing customers using a custom visual. -------

**Hypothesis:** There will be more middle aged account holders than younger or older. This may of coursework to increase the attrition levels with this group ----- add to visualization 


   - **Validation** Created a clustered column chart comparing Total_Trans_Amt for attrited vs. existing customers using a custom visual.

**Hypothesis:** Attrited customers will have generally lower income levels than existing customers and females will have more accounts than males.


   - **Validation** Created a clustered column chart comparing Total_Trans_Amt for attrited vs. existing customers using a custom visual.


1. **Hypothesis:** Attrited customers will have generally lower income levels than existing customers and females will have more accounts than males.


   - **Validation** Created a clustered column chart comparing Total_Trans_Amt for attrited vs. existing customers using a custom visual.

2. **Hypothesis** Customer attrition is higher among clients with lower credit limits.
   - **Validation:** Created a bar chart showing average Credit_Limit grouped by Attrition_Flag.

3. **Hypothesis:** Attrition rates vary by marital status, with single customers having higher churn.
   - **Validation:** Clustered bar chart of Attrition_Flag counts by Marital_Status.

4. **Hypothesis:** Customers with lower education levels tend to churn more often than those with higher education levels.  
   - **Validation:** Create a 100% stacked bar chart in Power BI showing the proportion of attrited versus existing customers for each education level to compare churn rates across education groups.

## Project Plan
The project followed these steps:
* 1. Data Extraction: Load the CSV dataset using pandas.
* 2. Data Cleaning and Transformation: Checked for missing values, duplicates and ensured correct data types.
* 3. Data visualisation: Used matplotlib, seaborn and plotly to explore relationships and patterns.
* 4. Analysis and Interpretation: Each visualisation answered a business question and helped confirm or reject the hypothesis.

## The rationale to map the business requirements to the Data Visualisations
I used a different type of visualisation for each of th business requirements. For each question I used:
1. Boxplot for comparing the distribution of smoker vs non smoker in comparison to charges.
2. Barchart to show regional averages.
3. Scatterplot with trendline for analysing correlation of BMI and smoking against insurance charges.
I chose those specific visualisations as it was easier to see the relationship between the different factors and insurance charges. Also, it was appropriate for the type of data that was given.

## Analysis techniques used
* Descriptive statistics (describe(), groupby() methods)
* Boxplots and bar charts for comparison
* Scatter plots for correlation
* OLS trendline in Plotly for regression pattern detection
**Limitations**: I would have hoped the numbers of existing customers and attrited customer were similar in some cases to draw different insights


The dataset lacks variables like pre-existing conditions, income, or employment type, which could further explain insurance charges.
**Alternative approaches**: Machine learning models could be used for prediction, but this was outside the scope of this exploratory analysis.
**Use of AI tools**: ChatGPT was used to get help with coding issues, visualisation tweaks, and Markdown formatting.

## Ethical considerations
* This data did not include any personal identifiable information so there were no data privacy concerns.

## Development Roadmap
**Challenges faced**:
* Depicting the visualizations and finding the proper layouts.
* Sections not loading due to others not running.
* Finding the proper libraries and modules.
**Overcoming them**:
* I utilized Copilot to help me render my visualizations.
* I had to remember to continously load each correlating section when working 
through.
* I had to sift through the internet and use Copilot to help with this.
**Next steps**:
* Explore more comparisons, plotting different attributes against each other.
* Explore more visualizations for further insights from their depictions.

## Main Data Analysis Libraries
* pandas – for data loading, cleaning, and transformation
df = pd.read_csv('bank-churners.csv')
* matplotlib – for static plots
plt.figure(plt.hist, crosstab, fix(ax1, ax2))
* seaborn – for statistical visualisations
sns.boxplot(data=df, x='smoker', y='charges')
* plotly.express – for interactive charts
px.scatter(df, x='bmi', y='charges', color='smoker', trendline='ols')

## Reflection
I feel it would have been better if the data stipulated that after a particular period of time, a customer became attrited and hold that parallel with existing customers. ---- in some cases, this is the assumption I went with

----- I would have hoped the numbers of existing customers and attrited customer were similar in some cases to draw different insights,,,,  -----



Working on this project was a great learning experience. At the beginning, I ran into a few bumps — like setting up the virtual environment and trying to get GitHub to stop asking me to log in every time I pushed something. It was a bit annoying, but after some trial and error (and help from ChatGPT), I managed to sort it all out.

I also had to troubleshoot a few coding issues, especially when using Plotly. Sometimes the graph wouldn’t show or there were strange errors I didn’t understand at first. Each time, I took the time to dig into what was going wrong and learned a bit more about how things work in Python and Jupyter Notebooks.

Throughout the project, I made sure to stay on track with the business goals and keep my code and markdown sections tidy and clear. If I were to improve anything, I’d maybe try to use even more visualisation types or dig deeper into prediction techniques. But overall, I’m happy with how the project turned out and I feel like I’ve come a long way from where I started.

## Credits 
### Content 
- **GitHub Copilot**  
GitHub Copilot in VS Code allowed for better coding structure and syntax, feasible recommendations and the reduction of repetition. I found it extraordinary useful during the visualization process.

  
  sqqwdefrgthyjuhrgfedsc 
  I used ChatGPT extensively to guide me through the project when I encountered issues. Specific examples include:
  - Understanding how to structure markdown cells and write hypotheses and objectives.
  - Troubleshooting errors such as:
    - The `plotly` error due to a missing `nbformat` installation.
    - A `SyntaxError` with no clear trace — eventually resolved by restarting VS Code.
    - Problems with activating the virtual environment in the terminal.
  - Helping to format visualizations, like:
    - Removing error bars from a seaborn bar plot.
    - Adding a box around the legend in a Plotly scatter plot.
  - Explaining technical concepts including:
    - What `groupby().mean().reset_index()` does.
    - The difference between `sns.barplot()` and `plt.bar()`.
    - The purpose and function of legends and trendlines in data visualisations.

## Acknowledgements
Thanks to:
* Code Institute for the project structure
* Kaggle for providing the dataset
* ChatGPT
* GitHub Copilot for coding support
* Code Institute peers for aiding throughout
