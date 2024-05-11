# eda-functions
This repository stores useful Python functions for exploratory data analysis.

## Exploratory Data Analysis Functions

This repository contains several Python functions designed to facilitate EDA tasks and help to select the right model for further tuning. These functions are useful for visualizing and analyzing categorical and numerical features in a DataFrame, as well as model selection process.

### Functions Included:

1. **plot_cats**
   - *Description:* Plot Normalized Value Counts for Categorical Columns
   - *Functionality:* Filters categorical columns from the DataFrame and plots their normalized value counts for exploratory data analysis.
   - *Usage:* `plot_cats(df, color='navy')`
   - *Parameters:*
     - `df`: DataFrame - Input DataFrame containing categorical columns.
     - `color`: str, optional - Color for the plots. Default is 'navy'.

2. **iqr_outliers**
   - *Description:* Calculate IQR and Identify Outliers for a Specific Column
   - *Functionality:* Calculates the Interquartile Range (IQR) of the specified column in the DataFrame and identifies outliers below Q1 and above Q3.
   - *Usage:* `iqr_outliers(df, column)`
   - *Parameters:*
     - `df`: DataFrame - Input DataFrame.
     - `column`: str - Name of the column for which IQR and outliers are to be calculated.

3. **plot_hist**
   - *Description:* Plot Histogram for Numerical Features in a DataFrame
   - *Functionality:* Filters numerical columns from the provided DataFrame and plots their histograms for exploratory data analysis.
   - *Usage:* `plot_hist(df, color='navy')`
   - *Parameters:*
     - `df`: DataFrame - Input DataFrame containing numerical columns.
     - `color`: str, optional - Color for the plots. Default is 'navy'.

4. **plot_box**
   - *Description:* Plot Boxplots for Numerical Features in a DataFrame
   - *Functionality:* Filters numerical columns from the provided DataFrame and plots their boxplots for exploratory data analysis.
   - *Usage:* `plot_box(df, color='navy')`
   - *Parameters:*
     - `df`: DataFrame - Input DataFrame containing numerical columns.
     - `color`: str, optional - Color for the plots. Default is 'navy'.

5. **model_selection**
   - *Description:* Perform Model Selection by Evaluating Performance Using Cross-Validation
   - *Functionality:* This function evaluates the performance of different models using cross-validation and compares them based on the specified evaluation metric.
   - *Usage:* `model_selection(models, scoring_metric, X_train=X_train, y_train=y_train)`
   - *Parameters:*
     - `models`: dict - A dictionary containing model names as keys and corresponding model instances as values.
     - `scoring_metric`: str - The evaluation metric to use for comparing models.
     - `X_train`: array-like, optional - The feature matrix of the training data. Default is `X_train`.
     - `y_train`: array-like, optional - The target vector of the training data. Default is `y_train`.
   - *Returns:* `results (dict)` - A dictionary containing model names as keys and the corresponding cross-validation results as values.
