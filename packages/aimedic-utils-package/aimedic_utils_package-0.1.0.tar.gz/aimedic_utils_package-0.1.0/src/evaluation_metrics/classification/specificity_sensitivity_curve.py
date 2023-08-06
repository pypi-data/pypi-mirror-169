import matplotlib.pyplot as plt
import mlflow
import os
import numpy as np
import tempfile

from loguru import logger
from sklearn.metrics import auc
# from sklearn.metrics import PrecisionRecallDisplay
from sys import prefix
from ...base.evaluation_interface import MetricsInterface
from ...utils.create_confusion_mat import get_conf_mat
from ...utils.make_binary_pred import BinaryPrediction
from ...utils.set_mlflow_run import get_mlflow_experiment, get_mlflow_run


class SpecificitySensitivityCurve(MetricsInterface):
    """
    A class used to represent a Specificity-Sensitivity curve

    ...

    Attributes
    ----------
        y_true : list
            a list of integer/float numbers, represents the actual labels
        y_pred : list
            a list of integer/float numbers, represents the predicted labels

    Methods
    -------
        apply_metrics
        log_metrics
        description

    """
    def __init__(self, metric_list, y_true, y_pred,
                 run_id, experiment_id,
                 class_names):

        super(SpecificitySensitivityCurve, self).__init__(metric_list, y_true, y_pred,
                                        run_id, experiment_id)
        self.class_names = class_names
        self.num_class = len(self.class_names)
        self.description()


    def apply_metrics(self):
        """compute confidence distribution plot and log in mlflow

        Args:
            y_pred: array of shape (n_samples, 1) in float range
            (represent prediction probability)

            class_names: array of shape (n_classes, 1) in {"NoneHemo", "Hemo"}

        Returns:
            no value
        """
        for cls_ind in range(len(self.class_names)):
            plot_file = self._compute_specificity_sensitivities(cls_ind)
            self.log_metrics(cls_ind,
                             metric_file_name=plot_file,
                             run_name="Test_Evaluation_Metrics")

            if len(self.class_names) == 2:
                break


        return


    def _save_sp_sen(self, specificities, sensitivities, title):
        fig, axis = plt.subplots(figsize=(10, 10))

        axis.plot(specificities, sensitivities,
                  label='AUC: {:1.2f}'.format(auc(specificities, sensitivities)))

        axis.set_xlim(0, 1)
        axis.set_ylim(0, 1)
        axis.set_xticks([i / 10 for i in range(10)])
        axis.set_yticks([i / 10 for i in range(10)])

        axis.set_xlabel('Specificity')
        axis.set_ylabel('Sensitivity')
        axis.legend()

        fig.suptitle(title)

        return plt


    def _compute_specificity_sensitivities(self, cls_ind):
        fig_size = (12, 8)
        plot_name = None
        if self.num_class == 2:
            title = 'Specificity-Sensitivity Curve'
            prefix = 'sp_sen_'
        else:
            title = f'Specificity-Sensitivity Curve (class {cls_ind})'
            prefix = f'sp_sen-{cls_ind}'

        thresholds = [i / 100 for i in range(1, 100, 1)]

        specificities = list()
        sensitivities = list()
        npvs = list()
        ppvs = list()

        for th in thresholds:
            y_pred_int = []
            y_pred_int = [1 if y > th else 0 for y in self.y_pred]

            _, _, _, npv, ppv, sensitivity, specificity, _ = get_conf_mat(
                self.y_true, y_pred_int)

            specificities.append(specificity)
            sensitivities.append(sensitivity)
            npvs.append(npv)
            ppvs.append(ppv)


        plt = self._save_sp_sen(
            specificities,
            sensitivities,
            title=title)
        
        with tempfile.NamedTemporaryFile(prefix=prefix, suffix='.png', delete=False) as f:
            plt.savefig(f.name, format="png")
            logger.info(f'[INFO] f.name in fig saving ->> {f.name}')
            plot_name = f.name


        return plot_name



    def description(self) -> str:
        """describe a description of the Confidence Distribution curve metric

        Args:
            str: a string value or a url to the metric

        Returns:
            no value
        """
        definition = ("indicates Confidence Distribution metric")
        return definition


    def log_metrics(self, cls_ind, metric_file_name=None, metric_value=None,
                    run_name=None):
        """log Confidence Distribution curve metric in mlflow

        Args:
            metric_file: a file , plot, ... input
            metric_value: a float, int or a dictionary input value

        Returns:
            no value

        """
        if metric_file_name is not None:
            if self.run_id != "None":
                active_run = get_mlflow_run(self.run_id, run_name=run_name)
                if active_run is not None:
                    mlflow.active_run()
                    mlflow.log_artifact(local_path=metric_file_name)
                    mlflow.end_run()
            elif self.experiment_id != "None":
                active_run = get_mlflow_experiment(self.experiment_id,
                                           run_name=run_name)
                if active_run is not None:
                    mlflow.active_run()
                    mlflow.log_artifact(local_path=metric_file_name)
                    mlflow.end_run()

            else:
                mlflow.log_artifact(local_path=metric_file_name)

            logger.info('[INFO] plot Metrics are logged in Mlflow.')
            logger.info('*************************************************')

        if metric_value is not None:
            raise NotImplementedError("[Warning] \
                Metric value in this class is not implemented.")

        return
