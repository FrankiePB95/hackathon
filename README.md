# Project Credit Card Churn Analysis

**Project Credit Card Churn Analysis** is a data analysis project focused on assessing which bank customers are likely to churn or become attrited so the bank can take proactive measures to retain them. Using a real-world dataset, this project investigates how account attributes (such as credit limit, tenure with company, income level and account inactivity) alongside more personal attributes such as age and gender may impact a customer churning. The analysis includes data cleaning, visualization, and predictive modeling to provide actionable insights for estimating healthcare expenses.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Target Audience
The target audience is an accounts analyst, a marketer and a customer service representative all working for the credit card compant and their wants can be found in the user stories file.

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
I will be focusing on 4 requirements:
* 1. Is there a discrepancy between income levels of male and female customers, attrited and existing, and also consider the male and female ratio here.
* 2. Is there a relationship between transaction amount, alongside transaction count between existing and attrited customer?
* 3. Is there a large discrepancy between credit limit and account usage between existing and attrited customers?
* 4. Is there a relationship between gender, transaction amount and attrition?

## Hypothesis and how to validate?
1. **Hypothesis:** There will be more female than male customers and of course this may look to increase attrition levels amongst females.

   - **Validation** Created a histogram that counts each customer's gender.

2. **Hypothesis:** There will be more middle aged account holders than younger or older. This may of course work to increase the attrition levels with this group 

   - **Validation** Created a comparative bar chart that plots ages of attrited customers next to existing customers.

3. **Hypothesis:** Does tenure hold some relationship to account inactivity and might this relate to attrition?

   - **Validation** Created a line chart and bar chart next to each other for comparison that tenure and inactivity in months respectively.

4. **Hypothesis:** There is a relationship between credit limit and utlization.

   - **Validation** Created two dsitribution plots using bars. One to gauge credit limit and the other for utilization frequencies. 

5. **Hypothesis:** Attrited customers will have generally lower income levels than existing customers and females will have more accounts than males.

   - **Validation** Created an interactive sunburst chart that compares income levels of attrited and existed male and female customers.

6. **Hypothesis** Existing customers will have more frequent transactions of higher values.

   - **Validation:** Created an interactive scatter plot graph plotting transaction amounts and their transaction counts for existing and attrited customers.

7. **Hypothesis:** Customer attrition is higher among clients with lower credit limits.
   
   - **Validation:** Created a parallel coordinates graph showing utilization ratio alongside credit limits between existed and attrited customers.

8. **Hypothesis:** We will witness lower attrition levels among male customers and a greater transaction amount sum amongst females.
   
   - **Validation:** Create visualizations that will allow for the creation of a dashboard to draw insights from.

## Project Plan
The project followed these steps:
* 1. Data Extraction: Downloaded the CSV dataset from Kaggle and load it using Pandas.
* 2. Data Cleaning and Transformation: Checkd the dataset for missing values, duplicates and ensured correct data types, and created transformers using Feature-Engine that fit into a pipeline to then call later.
3. Data loading: Extracted a sample dataset from the orginal using the previously created transformers fitted into a pipeline using SciKit-Learn to work with through the project. Created two random state samples, so as not to incur bias; one to work with in Jupyter and one for Databox.
* 3. Data visualization: Used Matplotlib, Seaborn and Plotly to generate visualizations that allow for the exploration of relationships and patterns between data. Also created a dashboard using GoodData to help further interpret data.
* 4. Analysis and Interpretation: Each visualization helped to prove or disprove a hypothesis. The visualisations also helped in answering our business requirements.

## The rationale to map the business requirements to the Data Visualisations
I used a different type of visualization for each of the hypotheses, allowing for diversity across data, a different perspective, as well as a better way to depict certain observations. For instance, I used:
1. Histogram to gauge gender distribution.
2. Barchart to compare ages of attrited and existing customers.
3. Line and bar charts to compare tenured months with inactive months.
4. Frequency charts to compare credit limit and utilization distributions.
5. Sunburst chart to compare the income levels of existed and attrited male and female customers.
6. Scatter plot diagram to compare the transactions satisfied by existing and attrited customers, and their total amounts.
7. Parallel coordinates diagram to compare credit utilization with credit limits of attrited and existing customers.
8. We created a table, a bullet chart, a heatmap, a bar chart and a stacked area chart for our dashboard to plot gender of attrited and existing customers against the sum of all transaction amounts for each respective gender.
There was a wealth of options available, such as radio graphs and heatmaps, but the visualizations I used proved more appropriate and ultimately allowed for observation and inspection of the data I looked to analyze. 

## Analysis techniques used
* Descriptive statistics to describe what was taking place within different visualizations
* Boxplots and bar charts for comparison
* Scatter plots for correlation
* A wealth of charts side by side within our dashboard
**Limitations**: I would have hoped the numbers of existing customers and attrited customer were similar in some cases to draw different more unbiased insights. 
**Alternative approaches**: OLS trendline in Plotly for regression pattern detection.
**Use of AI tools**: Copilot was used to help with coding issues and visualisations.

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
* Pandas – for data loading, cleaning and transformation
* Matplotlib – for static plots
* Seaborn – for statistical visualisations
* Plotly – for interactive charts
* Feature-Engine - for creating transformers
* SciKit-Learn - for fitting the pipeline

## Reflection
I was pleased to take on this challenge and there are a few things I looked to reflect on. For instance:

I feel it would have been easiler in there were similar numbers of attrited customers against existing customers. 

Also, I noticed there seemed to be a huge discrepancy within the customer tenure category. This may have been due to outside factors such as are their credit plans and whether they simply left after a fixed term following a payment, for instance. 

Further, I had considered whether existed customer numbers would have been higher along the high credit limit scale, but this didn't seem to be the case, and I am assuming it might be for a few reasons, including, for instance, customer risk in taking on more credit, and company risk in affording more credit to these customers. And also with some being potentially newer customers, they may be afforded lower credit limits.

There were things I had to troubleshoot, such as coding issues, visualization issues, finding the right libraries, VS Code not loading, GitHub issues, amongst other things. Also, network connectivity presented difficulties, for intance, with my commit and push phase. In the future, I look to rectify this. 

Further, I found difficult choosing the right application ro generate my dashboard due to network constraints, sign up constraints and not being able to visualize what I wanted to, but eventually I managed to get through.

The project definitely kept me on my toes and presented many different challenges for me to overcome. Despite this, I worked to answer the business requirements and provide sound insights. I would indeed hope for more visualizations and more oberservation time. I'm pleased with the overal project and look forward to future challenges.

## Credits 
### Content 
- **GitHub Copilot**  
GitHub Copilot in VS Code allowed for better coding structure and syntax, feasible recommendations and the reduction of repetition. I found it extraordinary useful during the visualization process.

  I used Copilot to guide me through the project when I encountered issues. Specific examples include:
  - Troubleshooting errors such as:
    - Syntax errors - fixes included rewriting code.
    - Path errors - fixes included adding a module that helped better trace a path location.
  - Helping to format visualizations, like:
    - Creating labels.
    - Editing colours.
    - Adding legends.
  - Explaining technical concepts including:
    - What `plt.show()` is used for.
    - `Transformers` and `pipelines` and their purposes.

## Acknowledgements
Thanks to:
* Code Institute for the project structure
* Kaggle for providing the dataset
* Monday for project management tools
* GoodData for dashboard tools
* GitHub Copilot for coding support
* Code Institute peers for being there throughout