# Notes for Week 3 - data analysis and modelling

## Overview of big data in healthcare
* The [*-omics*](https://www.ncbi.nlm.nih.gov/books/NBK202165/): the systematic system of data in a specific field. Examples:
    * Genomics, proteomics, transcriptomics, radiomics, etc.
* Main technical challenges:
    * Storage of the data
    * Analysis of the data, i.e. making knowledge from the data
* Formats:
    * Text-based (e.g. DNA sequencing data in a fastq file);
    * Image-based (e.g. [histology](http://www.histologyguide.com/) slides, medical imaging data)

## Data in a tabular form
* Rows: represents samples;
* Columns: represent variable names. Can also be called as attributes or properties. In supervised learning, one column will correspond to the *label* and the remaining as *features*.

## Data wrangling
* Aim: to prepare the data in a clean form for subsequent analysis or modelling.
* Main issues to address:
    * Missing values
        * Solutions
            * Remove the rows
            * Replaced by the mean
            * Replaced by the median
            * Calculate from other columns (*imputation*)
    * Impossible values
        * Can be due to mistakes during inputting or intermediate calculation.
        * Solutions
            * Fix if the meaning is clear
            * Treat as a missing value
        * The process to check impossible values is often call the *sanity check*.
    * Outliers
        * Extreme values
        * Outliers are still *possible* values.
        * Solutions
            * Exclude from the analysis
    * Get a feel of the data
        * Data visualisations are often used in this step.
        * Check single columns: e.g. distributions.
        * Check column pairs: e.g. correlation or patterns.

## Data visualisation
Commonly used plot types include:
* Scatter plot (sometimes with fitted lines);
* Scatter matrix: pair-wise scatter plots with a density plot along the diagonal line;
* Box plot / jitter plot / violin plot: for visualising the distribution of data;
* Density plot.

A gallery of Python visualisations can be found [here](https://python-graph-gallery.com/).

## Correlation analysis
* Correlation examines the association between two variables. Correlation coefficients are used to quantify the level.
* Types of correlation coefficients
    * Pearson correlation: quantifies the linear relationship. Use this if there is a linear assumption.
    * Spearman correlation: quantifies the monotonic relationship. Use this if there is not linear assumption.

## Predictive modelling
* The aim: to predict information using existing data.
* AI, machine learning and deep learning
    * AI (artificial intelligence) is the general term for methods that can enable computer to perform intellectual tasks.
    * AI mainly contains the rule-based approached and machine learning.
    * Deep learning is part of machine learning which uses deep neural networks for the learning.
* Types of learning
    * Supervised learning: learning with a label;
        * Classification: if the label is categorical (e.g. yes or no).
            * Example: support vector machines (SVM)
        * Regression: if the label is numerical (e.g. age of a patient).
            * Example: Linear regression
    * Unsupervised learning: learning without a label. Since no label is provided, the method will try to find any intrinsic patterns within the data, such as the main groups.
        * Clustering: the most common unsupervised learning method. It aims to divide the data into groups based on the similarity.

## Studies overview
* Most studies falls into either correlation analysis or predictive modelling. They may use a combination of methods and could have a specific name. For example, survival analysis is a common analysis to model the survival rate over time. It mainly uses regression methods to model the data. A survival analysis example using Python can be found [here](https://medium.com/towards-artificial-intelligence/survival-analysis-with-python-tutorial-how-what-when-and-why-19a5cfb3c312).
* [Scikit-learn](https://scikit-learn.org/stable/) is a popular machine learning package in Python.

## Overfitting
* The model fits the data too hard and hence over-learns. It might learn the general pattern (well generalised) as well as the random noise (pooly generalised) in the data. The model can perform well on the fitted data but is hard to generalised to unseen data.

## Data partitioning
To avoid overfitting and get the fair assessment of the model, data is typically split into two parts.
    * Training data: the data to train the model.
    * Test data: the data held out to assess the model performance.
If overfitting takes place (i.e. the model over-learns), it won't perform well on the test data.

## Business intelligence (BI)
BI tools are available from vendors which provides an easy gateway for data analysis and modelling without heavy programming. AI methods are used behind the scenes, supported by visualisations in the front-end. Examples include
* Domo
* Tableau
* MYOB
* Microsoft Power BI

A comparison of BI tools can be found [here](https://www.capterra.com/sem-compare/business-intelligence-software).