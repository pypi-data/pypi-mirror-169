# aimedic-utils

Utilities for vision group

This package is used to build an alternative class for tensorflow.keras.Model class to generally automate some works:
1. evaluate some kind of models including {`classification`, `dobject detection`, `segmentation`}. For each type of model, we used coresponding metrics.
2. export the model to mlflow server for production after training and evaluation
3. automate the model card builder 


### Implemented Model Metrics
For each model, these type of metrics are implemented as below:


|     Classification                          |     Segmentation      |
|:--------------------------------------------|----------------------:|
| confusion matrix plot                       |  Not Implemented Yet  |
| roc curve                                   |  Not Implemented Yet  |
| precision recall curve                      |  Not Implemented Yet  |
| confidence distribution curve               |  Not Implemented Yet  |
| Reliability curve                           |  Not Implemented Yet  |
| f-score, ppv, npv, sensitivity, specificity |  Not Implemented Yet  |
| Other Metrics are Not Implemented Yet       |  Not Implemented Yet  |



## Challenges
1. loading model from tfk saved model to AIMedicModel instances
2. converting tfk.Model objects into AIMedicModel object 


## Future Works
1. add multilabel classification modility, currently ( v0.1.0 ) we have just binary classification 
2. export method not implemented yet.
3. generate model card not implemented yet.
4. `segmentation` model metrics are not implemented yet.


### Prerequisites
All prerequisites that you need, are included in `requirements.txt` file.


### Installing package
install the package by this command:

```bash
pip3 install aimedic-utils
```
import the AIMedicModel class from the package

```python
from aimedic_utils.models.aimedic_model import AIMedicModel
```
you can use it as a tensorflow model to train, predict, and evaluate.

following instructions are guidlines for the evaluation part.
inputs of the evaluation method from the class:
##### Input format Of Classification Model
Inorder to compute a specific metric for a model, 4 kinds of inputs should be defined:

|     input name    |                 input format                                    |
|:------------------|----------------------------------------------------------------:|
|  y_true           | list of groundtruth values, ex [1, 0, 1, 0, 1]                  |
|  y_pred           | list of prediction probability, ex [0.54, 0.8, 0.4, 0.9, 0.17]  |
|  class_namess     | list of class names, ex ["NoneHemo", "Hemo"]                    |
|  metric_list      | list of integer number, ex [1, 2, 3, ...]                       |


```python
y_true = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0 , 1, 1]
y_pred = [0.53, 0.044, 0.49, 0.81, 0.23, 0.93,
            0.16, 1, 0.51, 0.73, 0.33, 0.9, 0.45]
class_names = ["Non-MLS", "MLS"]
run_id = "0d0f1b7690dd4143a0763d84f221d0dd" # your desired exp run_id
experiment_id = "50" # your desired exp_id

metrics_list = ["acc", "confusion_matrix"] # metrics

model = AIMedicModel(run_id=run_id, exp_id=experiment_id)
model.eval(y_true, y_pred, class_names, metrics_list=metrics_list)
```

### Ruuning Example
One can easily run the sample by using `python3 test.py` with no argument. 

```bash
python3 test.py
```

### Metric List format
Metric List is a list of strings, that each strings represents a specific metric name.
List of available metrics are listed as below:


|     metric name                                                 |
|:---------------------------------------------------------------:|
| confusion matrix                                                |
| npv                                                             |
| sensitivity, specificity                                        |
| roc                                                             |
| precision-recall                                                |
| confidence distribution                                         |
| reliability diagram                                             |


### Authors
`Name`: Benyamin Ghahremani Nezhad, `Email`: benyamin.ghahremani@aimedic.co