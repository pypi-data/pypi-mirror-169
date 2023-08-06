import tensorflow as tf
tfk = tf.keras
import numpy as np
import logging
import os, sys
from pathlib import Path
import warnings
from ..evaluation_metrics.classification import *


# ROOT_PATH = os.path.dirname(__file__)
# new_path = os.path.join(os.path.dirname(__file__), '/src/evaluation_metrics/classification/')
# ALL_FILES = os.listdir(new_path)
# AVAILABLE_METRICS = [x.split('.')[0] for x in ALL_FILES if ('py' in x) & ('__' not in x)]
AVAILABLE_METRICS = ['confidence_distribution', 'confusion_matrix', 'npv_specificity_curve', 
                    'precision_recall', 'reliability_diagram', 'roc_curve', 'specificity_sensitivity_curve' ]


class AIMedicModel(tfk.Model):
    """AIMedic Model is an alternative class for tfk.Model with some extra features:
        1. Customized evaluation method to calcualte metrics and log the results on mlflow
        2. Export method to export the model to mlflow server
        3. A method to automatically generate model card 
        4. loading model from checkpoints to return AIMedicMOdel class

    ...

    Attributes
    ----------
        run_id: str
            mlflow run id
        exp_id: str
            mlflow experiment id
        metrics_list: list[str]
            list of the desired metrics name
        task_type: str
            name of the type of the task the model build for it
        tf_model: tensorflow.keras.Model
            the tfk.Model we want to convert it to AIMedicModel

    Methods
    -------
        eval
        generate model card
        export
        load model

    """
    def __init__(self, run_id: str = '', exp_id: str = '', 
                 metrics_list: list = [], task_type: str = 'classificiton',
                 tf_model: tfk.Model = None, *args, **kawrgs):
        super(AIMedicModel, self).__init__(*args, **kawrgs)
        self.run_id = run_id
        self.exp_id = exp_id
        self.metrics_list = metrics_list
        self.task_type = task_type
        self.tf_model = tf_model

    def eval(self, y_true, y_pred, class_names, data_generator=None, metrics_list=[], run_id=None):
        '''custom evaluation on customized metrics and log the outputs on mlflow
        
        Args:
            y_true : list[int/floats]
                a list of integer/float numbers, represents the actual labels
            y_pred : list[int/floats]
                a list of integer/float numbers, represents the predicted labels
            class_names: list[str]
                a list of the class names
            data_generator (optional, not implemeneted yet): DataGenerator
                data generator contains labels data pathes to get predictions
            metrics_lsit: list[str]
                list of the desired metrics name
            run_id: str
                mlflow run id

        Returns:
            ( logs on the mlflow server and displaying the outputs )
        '''
        if data_generator is not None:
            warnings.warn("The data-generator option is not implemented yet!!!")
            pass

        if run_id != None:
            self.run_id = run_id

        # run metrics 
        if len(metrics_list)!=0:
            self.metrics_list = metrics_list

        if len(self.metrics_list) == 0:
            warnings.warn(f"The evaluator is using the built-in metrics. \nAvailable metrics: {AVAILABLE_METRICS}")
            self.metrics_list = AVAILABLE_METRICS

        for metric_name in self.metrics_list:
            if metric_name in AVAILABLE_METRICS:
                module_name = ''.join([x for x in metric_name.split('_')])
                Metric = [x[1] for x in globals().items() if module_name in x[0].lower()][0]
                metric = Metric(self.metrics_list,
                                y_true,
                                y_pred,
                                self.run_id,
                                self.exp_id,
                                class_names)
                metric.apply_metrics()
                logging.info(f"The \"{metric_name}\" metric logged successfully.")
            else:
                warnings.warn(f"The \"{metric_name}\" metric is not available.")

        logging.info("done successfully!")

    def generate_model_card(self):
        '''generate model cards and create log on mlflow server
        
        Args:
        
        Returns:
        '''
        pass

    def export(self):
        '''export the model on mlflow server
        
        Args:
        
        Returns:
        '''
        pass

    def load_model(self):
        '''load saved model as AIMedicModel from tfk saved model path
        
        Args:

        Returns:
        '''
        pass
