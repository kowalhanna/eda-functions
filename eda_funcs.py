# Function for model selection

def model_selection(models, scoring_metric, X_train=X_train, y_train=y_train):
    '''
    This function performs model selection by evaluating the performance of different models using cross-validation.
    
    Parameters:
    - models (dict): A dictionary containing model names as keys and corresponding model instances as values.
    - scoring_metric (str): The evaluation metric to use for comparing models.
    - X_train (array-like): The feature matrix of the training data.
    - y_train (array-like): The target vector of the training data.
    
    Returns:
    - results (dict): A dictionary containing model names as keys and the corresponding cross-validation results as values.
    '''
    results = {}
    
    for model_name, model in models.items():
        kf = KFold(n_splits=3, random_state=12, shuffle=True)
        cv_results = cross_val_score(model, X_train, y_train, cv=kf, scoring=scoring_metric)
        results[model_name] = cv_results

    plt.figure(figsize=(10, 6))
    plt.boxplot(results.values(), labels=results.keys())
    plt.title('Model Performance Comparison')
    plt.xlabel('Model')
    plt.ylabel(scoring_metric)
    plt.grid(True)
    plt.show()
    
    return results

# Function for plotting categorical features in a DataFrame

def plot_cats(df=df, color='navy'):
    '''
    Plot Normalized Value Counts for Categorical Columns

    Filters categorical columns from the DataFrame and plots their normalized value counts for exploratory data analysis.

    '''
    ## Select categorical columns from the DataFrame
    cat_columns = df.select_dtypes(include=['object', 'category']).columns

    # Check if there are any categorical columns
    if len(cat_columns) == 0:
        print("No categorical columns found in the DataFrame.")
        return

    # Adjust the number of subplots and plot size with accordance to the number of columns
    num_columns = len(cat_columns)
    num_rows = (num_columns + 1) // 2  

    fig, axes = plt.subplots(num_rows, 2, figsize=(12, 6*num_rows))
    axes = axes.flatten()
    plt.subplots_adjust(hspace=0.5)
    # Loop through all columns and plot normalized value counts
    for i, col in enumerate(cat_columns):
        ax = axes[i]
        value_counts_norm = df[col].value_counts(normalize=True)
        value_counts_norm.plot(kind='bar', ax=ax, color=color)
        ax.set_title(f'Normalized Value Counts of {col}')
        ax.set_xlabel(None)
        ax.set_ylabel('Proportion')
        ax.set_xticklabels(value_counts_norm.index, rotation=45)

    if len(axes) > num_columns:
        fig.delaxes(axes[-1])

    plt.show()

# Function for calculating IQR and identifying outliers
def iqr_outliers(df, column):
    '''
    Calculate IQR and identify outliers for a specific column

    Calculates the Interquartile Range (IQR) of the specified column in the DataFrame and identifies the number of outliers based on the IQR method.

    '''
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        print(f"Column '{column}' does not exist in the DataFrame.")
        return None, None, None, None

    # Check if the DataFrame is empty
    if df.empty:
        print("DataFrame is empty.")
        return None, None, None, None

    # Calculate the IQR of the column
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    print(f"IQR: {iqr}")

    # Identify lower outliers below q1 - 1.5 * iqr and upper outliers above q3 + 1.5 * iqr
    lower_outliers = df[df[column] < q1 - 1.5 * iqr]
    upper_outliers = df[df[column] > q3 + 1.5 * iqr]

    # Calculate the number of lower outliers and upper outliers
    num_lower_outliers = len(lower_outliers)
    num_upper_outliers = len(upper_outliers)
    num_total_outliers = num_lower_outliers + num_upper_outliers
    print(f"Number of lower outliers: {num_lower_outliers}")
    print(f"Number of upper outliers: {num_upper_outliers}")
    print(f"Total number of outliers: {num_total_outliers}")

    # Calculate proportion of outliers in the dataset
    proportion_outliers = num_total_outliers / len(df) * 100
    print(f"Proportion of outliers in the dataset: {proportion_outliers:.2f}%")

    return lower_outliers, upper_outliers, num_total_outliers

# Function for plotting histograms of numerical columns in a DataFrame

def plot_hist(df, color='navy'):
    '''
    Plot Histogram for Numerical Features in a DataFrame

    Filters numerical columns from the provided DataFrame and plots their histograms for exploratory data analysis.

    '''
    # Select numerical columns from the DataFrame
    num_columns = df.select_dtypes(include='number').columns

    # Check if there are any numerical columns
    if len(num_columns) == 0:
        print("No numerical columns found in the DataFrame.")
        return

    # Calculate the number of rows needed for subplots
    number_columns = len(num_columns)
    number_rows = (number_columns + 1) // 2

    # Create subplots
    fig, axes = plt.subplots(number_rows, 2, figsize=(12, 6*number_rows))
    axes = axes.flatten()
    plt.subplots_adjust(hspace=0.5)

    # Loop through numerical columns and plot histogram
    for i, col in enumerate(num_columns):
        ax = axes[i]
        sns.histplot(data=df, x=col, color=color, ax=ax)
        ax.set_title(f'Histogram of {col}')
        ax.set_xlabel(None)
        ax.set_ylabel('Count')

    # Remove excess subplot if the number of columns is odd
    if number_columns % 2 != 0:
        fig.delaxes(axes[-1])

    plt.show()

# Function for plotting histograms of numerical columns in a DataFrame
def plot_box(df, color='navy'):
    '''
    Plot Boxplots for Numerical Features in a DataFrame

    Filters numerical columns from the provided DataFrame and plots their histograms for exploratory data analysis.

    '''
    # Select numerical columns from the DataFrame
    num_columns = df.select_dtypes(include='number').columns

    # Check if there are any numerical columns
    if len(num_columns) == 0:
        print("No numerical columns found in the DataFrame.")
        return

    # Calculate the number of rows needed for subplots
    number_columns = len(num_columns)
    number_rows = (number_columns + 1) // 2

    # Create subplots
    fig, axes = plt.subplots(number_rows, 2, figsize=(12, 6*number_rows))
    axes = axes.flatten()
    plt.subplots_adjust(hspace=0.25)

    # Loop through numerical columns and plot histogram
    for i, col in enumerate(num_columns):
        ax = axes[i]
        sns.boxplot(data=df, x=col, color=color, ax=ax)
        ax.set_title(f'Boxplot of {col}')
        ax.set_xlabel(None)
        ax.set_ylabel('Value')

    # Remove excess subplot if the number of columns is odd
    if number_columns % 2 != 0:
        fig.delaxes(axes[-1])

    plt.show()