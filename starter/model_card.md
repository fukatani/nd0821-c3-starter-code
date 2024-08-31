# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

DecisionTreeClassifier which predict whether income exceeds $50K/yr based on census data.
Model was trained with [Census Bureau data](https://archive.ics.uci.edu/dataset/20/census+income)
Hyperparamter:
 - criterion is 'gini'
 - max_depth is None

## Intended Use

It can be used by salespeople to decide what products to recommend to customers.

## Training Data

80% of data was used for training.

## Evaluation Data

20% of data was used for evaluation.

## Metrics

|fbeta|precision| recall |
|----|------|--------|
|0.61|0.59| 0.63   |

## Ethical Considerations

The accuracy of the model varies depending on the race of the subject.

race:  White

| fbeta |precision|recall|
|-----|---------|------|
| 0.61 |0.60|0.63|

race:  Amer-Indian-Eskimo

| fbeta | precision | recall |
|-------|-----------|--------|
| 0.33  | 0.22      | 0.67   |

race:  Black

| fbeta | precision | recall |
|-------|-----------|--------|
| 0.54  | 0.51      | 0.57   |

race:  Asian-Pac-Islander

| fbeta | precision | recall |
|-------|-----------|--------|
| 0.65  | 0.65      | 0.65   |

race:  Other

| fbeta | precision | recall |
|-------|-----------|--------|
| 0.77  | 0.83      | 0.71   |

## Caveats and Recommendations

The accuracy of the model for Amer-Indian-Eskimo is extremely low, so care must be taken when handling it.
