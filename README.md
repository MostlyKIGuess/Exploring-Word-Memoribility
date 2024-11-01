- Dataset Link: [Madan 2020](https://osf.io/m4gdh)

# Word Memorability Analysis and Quiz

## Overview

This project analyzes word memorability using a dataset of word properties and recall probabilities. The analysis is performed in `analysis.py`, and a quiz is provided in `quiz.py` , run the quiz only after reading the report.


## Analysis

The `analysis.py` script performs the following tasks:

1. **Descriptive Statistics and Data Exploration**: Summarizes the dataset and visualizes distributions of key variables.
2. **Correlation Analysis**: Computes and visualizes the correlation matrix between recall probability and word properties.
3. **Linear Regression**: Fits linear regression models to predict recall probability based on word properties.
4. **Extended Analysis**: Explores the impact of word length on memorability across frequency bands and the interaction effects of animacy and usefulness.

### Visualizations

The results of the analysis are saved as images in the `images/` directory:

- `correlationmatrix.png`: Correlation matrix of word properties.
- `distributionofrecallprob.png`: Distribution of recall probabilities.
- `freqvsarousal.png`: Distribution of arousal.
- `freqvsconcreteness.png`: Distribution of concreteness.
- `recallprobvsfreqbin.png`: Box plot of recall probability by frequency bin.
- `recallprobvsfreqbinviolin.png`: Violin plot of recall probability by frequency bin.
- `corelation.png`: Pairwise scatterplot matrix of key variables.

## Quiz

The `quiz.py` script provides a quiz to test your understanding of the analysis. It generates multiple-choice questions based on the concepts discussed in the report.

### Running the Quiz

Before that do the setup properly.For that after cloning the repo run:

```
pip install -r requirements.txt
```

then you can run the quiz by:

```sh
python quiz.py
```





