# Fraud in Financial Payment Services

## Objective

Analyze a dataset of mobile money transactions to detect fraudulent activities.

## Dataset Description

The dataset contains records of mobile money transactions categorized into five distinct types:

- **CASH-IN**: Any deposit into a user's account.
- **CASH-OUT**: Any withdrawal from a user's account.
- **DEBIT**: A specific type of withdrawal where money is sent directly to the user’s bank account.
- **PAYMENT**: Transactions involving the purchase of goods or services.
- **TRANSFER**: Transactions where money is moved from one user’s account to another user’s account.

### Fraud Detection Fields

The dataset includes two important fields related to fraud detection:

- **IsFlaggedFraud**: Indicates whether the transaction was flagged as potentially fraudulent by the system’s automated fraud detection mechanism.
- **IsFraud**: Indicates whether the transaction was confirmed as fraudulent after further investigation.

## Project Objectives

The primary objectives of this project are:

1. **Data Exploration**: Understand the structure and content of the dataset, including the distribution of transaction types and the occurrence of flagged and confirmed fraud.
2. **Fraud Detection Analysis**: Evaluate the performance of the automated fraud detection system by comparing the flagged fraud transactions against the confirmed fraud transactions.
3. **Insights and Patterns**: Identify patterns and insights related to fraud in mobile money transactions, which could help in improving fraud detection mechanisms and preventing fraudulent activities in the future.

## File Structure

The project includes the following files and directories:

- **README.md**: This readme file providing an overview of the project.
- **dataset/**: Directory containing the dataset files.
- **colab/**: Jupyter notebooks used for data exploration and analysis.
- **python/**: Generated python file from the colab file.

## Getting Started

To get started with the analysis, follow these steps:

1. **Clone the Repository**: Clone the project repository to your local machine.

    ```bash
    git clone <url>
    ```

2. **Install Dependencies**: Ensure you have the required Python libraries installed. You can use the provided requirements.txt file to install dependencies.

    ```bash
    pip install -r requirements.txt
    ```

3. **Explore the Data**: Use the Jupyter notebooks in the notebooks/ directory to explore the dataset and perform initial analysis.

## Skills Gained:

1. Data Analysis
2. Fraud Detection Techniques
3. Machine Learning
4. Data Visualization
