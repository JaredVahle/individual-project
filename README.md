

<!-- Add banner here -->
![Banner](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.commercialintegrator.com%2Fbusiness_resources%2Foperations%2Fu-s-tech-jobs-5-cities%2F&psig=AOvVaw3MhgmvWmgRiqDOP47GnjDW&ust=1634182673315000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCNja7Iu7xvMCFQAAAAAdAAAAABAJ)

# Estimating Salaries or Jobs in Tech

<!-- Add buttons here -->

![GitHub release (latest by date including pre-releases)](https://img.shields.io/badge/release-draft-yellow)
![GitHub last commit](https://img.shields.io/badge/last%20commit-Oct%202021-green)

<!-- Describe your project in brief -->
Link to the original dataset (https://www.kaggle.com/jackogozaly/data-science-and-stem-salaries)

I was interested in looking deeper into datascience salary and education requirements. In this project I used the data above to create a linear regression model for predicting yearly earnings.



# Executive Summary
<!-- Add a demo for your project -->

The main features that drive earnings for employees in the tech and stem jobs, is location, education, and experience. If you are willing to move you can make much larger amounts of money. I would also recomend that if you find or initially are with a company that you enjoy, it is financially worth it to continue working and trying to move up in that company.

**Project Goals**

Build a linear regression model to predict total yearly earnings for Tech, and STEM jobs.

**Data summary**

- The dataset was halved in size after cleaning.
- Education level, location, years of experience were used in modeling.


### Statistical testing:
- From the statistical test there is no difference between male and female earnings in the dataset.
- You make more money staying at one company vs moving companies when both employees have similar work experience.
- Employees with lower education make less then employees with higher education
- There is a relationship between location and total earnings.


### Recommendations
- If you are in it for the money it might be worth it to pursue a masters or doctorate degree.
- Location plays a factor in pay, if your life circumstances allow for it, moving to an area with higher pay could increase your salary.

# Table of contents
<!-- Add a table of contents for your project -->

- [Project Title](#project-title)
- [Executive Summary](#executive-summary)
- [Table of contents](#table-of-contents)
- [Data Dictionary](#data-dictionary)
- [Data Science Pipeline](#data-science-pipline)
    - [Acquire](#acquire)
    - [Prepare](#prepare)
    - [Explore](#explore)
    - [Model](#model)
    - [Evaluate](#evaluate)
- [Conclusion](#conclusion)
- [Given More Time](#given-more-time)
- [Recreate This Project](#recreate-this-project)
- [Footer](#footer)

# Data Dictionary
[(Back to top)](#table-of-contents)
<!-- Drop that sweet sweet dictionary here-->

| Feature                    | Datatype                | Definition   |
|:---------------------------|:------------------------|:-------------|
| total_earnings|int64|Gives a sum of the total earnings|
| yearsofexperience|Float64|Gives the number of years an employee has in that field|
| yearsatcompany|Float64|Gives the number of years an employee was at that company|
| cityid|int64|Returns a number for the city the job is located in|
| masters_degree|int64|Bool 1 for if they have a masters degree 0 if they do not|
| bachelors_degree|int64|Bool 1 for if they have a bachelors degree 0 if they do not|
| doctorate_degree|int64|Bool 1 for if they have a doctorate degree 0 if they do not|
| highschool|int64|Bool 1 for if they have highschool education 0 if they do not|
| some_college|int64|Bool 1 for if they have some college  0 if they do not|
| title_*|uint8|Bool title columns were created 1 for if they held that title 0 if they did not|
| highly_experienced| int64|Bool 1 for if the employee has over 4 years of experience 0 if not|

# Data Science Pipeline
[(Back to top)](#table-of-contents)
<!-- Describe your Data Science Pipeline process -->
Following best practices I documented my progress throughout the project and will provide quick summaries and thoughts here.

### Acquire
[(Back to top)](#table-of-contents)
<!-- Describe your acquire process -->
The data was acquired from keggle. I downloaded a csv of the data, and put that data into a pandas dataframe

My goal with this acquisition was to give me as much data as possible moving foward.
At this point our data has
* *62642 rows*
* *29 columns*

This can all be found in my acquire.py file in my github

### Prepare
[(Back to top)](#table-of-contents)
<!-- Describe your prepare process -->
Performed the following on my acquired data.

**General Breakdown**

- Breakdown of my prep for my models prepare/clean function:
    - Function creates a dummy variable for title and concats it with the current dataframe.
    - Drops columns that are not useful, or would make the dataset too large to use dummies on.
    - Drops nulls, removes any rows that do not have education documented.
    - Renames some columns for readability.
    - Adds a column for highly experienced.
    
- Breakdown of my prep for my explore prepare/clean fucntion:
    - Creates dummy variable for gender.
    - Removes some columns I do not want insite about or that contain to many nulls.
    - Drops nulls, removes any rows that do not have education documented.
    - Renames some columns for readability.
    - Adds a column for highly experienced.

**The reason that there are two data clean functions is because they contain the same data, although I wanted some deeper exploration into some extra variables that couldnt be translated into my model given the timeframe.**

At this point our data has
* *29946 rows*
* *25 columns*

We will now split our data into train, validate, and split.
- Split the data into 60% train, 20% validate, 20% test


### Explore
[(Back to top)](#table-of-contents)
<!-- Describe your explore process -->

- Visualized using both univariate analysis and bivariate, and with more time i will do multivariate exploration.
- Ran four statistical test comparing different variables and total earnings.

### Model
[(Back to top)](#table-of-contents)
<!-- Describe your modeling process -->
Model types: linear regression, polynomial 3rd degree, lasso lars, tweedie, Decision Tree Regression.
**Winning model: Decision Tree Regression**
The features used were:
- yearsofexperience
- highly_experienced
- doctorate_degree
- bachelors_degree
- cityid


Baseline RMSE on test data: 107140.062039

**My models RMSE on test data: 74904.849480**

This is a significant improvement over the baseline, with a prediction average of over 30,000$ better then the baseline model.

### Evaluate
[(Back to top)](#table-of-contents)
<!-- Describe your evaluation process -->
I gathered the RMSE and R^2 for all of my models and put them into dataframes for easy comparison.

# Conclusion
[(Back to top)](#table-of-contents)
<!-- Wrap up with conclusions and takeaways -->

The main features that drive earnings for employees in the tech and stem jobs, is location, education, and experience. If you are willing to move you can make much larger amounts of money. I would also recomend that if you find or initially are with a company that you enjoy, it is financially worth it to continue working and trying to move up in that company.

The decision Tree regression model outperformed the baseline by **~32,236$**

Many features were found that can be used to find the salary of employees.
The biggest factors were:

- experience
- location
- education

# Given More Time/ Next steps
[(Back to top)](#table-of-contents)
<!-- LET THEM KNOW WHAT YOU WISH YOU COULD HAVE DONE-->
- Create clusters in the data, that will make my model more successful.
- Find a way to numerate some of the columns that were strings.
- Go deeper into exploration, ask more probing questions from the data.
# Recreate This Project
[(Back to top)](#table-of-contents)
<!-- How can they do what you do?-->
**To Recreate This Project**
- Create a copy of the kaggle dataframe, and run the wrangle functions to get the same cleaned dataframe.
- I created a wrangle file that will do all of the acquir/prepare stage.
- Use the seed 174
- Importing all of my modules and utilizing them will help expadite the process.
# Footer
[(Back to top)](#table-of-contents)
<!-- LET THEM KNOW WHO YOU ARE (linkedin links) close with a joke. -->

You can find the rest of my work here: https://github.com/JaredVahle

Add me on Linkedin here: https://www.linkedin.com/in/jared-vahle-data-science/