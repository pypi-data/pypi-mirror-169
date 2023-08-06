import matplotlib.pyplot as plt
import matplotlib
import mlflow
import os
import tempfile

from loguru import logger
from sklearn.metrics import roc_curve, auc
from sys import prefix
from ...utils.make_binary_pred import BinaryPrediction
from ...base.evaluation_interface import MetricsInterface
from ...utils.set_mlflow_run import get_mlflow_experiment, get_mlflow_run


class ROCCurve(MetricsInterface):
    """
    A class used to represent a Confusion Matrix

    ...

    Attributes
    ----------
        metric_list : list
            a list of integer numbers, represents the metrics values
        y_true : list
            a list of integer numbers, represents the actual labels
        y_pred : list
            a list of integer numbers, represents the predicted labels

    Methods
    -------
        apply_metrics
        log_metrics
        description

    """
    def __init__(self, metric_list, y_true, y_pred,
                 run_id, experiment_id,
                 class_names):

        super(ROCCurve, self).__init__(metric_list, y_true, y_pred,
                                        run_id, experiment_id)
        self.class_names = class_names
        self.num_class = len(self.class_names)
        self.description()


    def apply_metrics(self):
        """compute roc plot and log in mlflow

        Args:
            y_pred: array of shape (n_samples, 1) in float range
            (represent prediction probability)
            y_true: array of shape (n_samples, 1) in integer {0, 1}
            (represent actual labels)


            class_names: array of shape (n_classes, 1) in {"NoneHemo", "Hemo"}

        Returns:
            no value
        """
        self.y_pred = BinaryPrediction(self.y_pred)
        for cls_ind in range(len(self.class_names)):
            plot_file = self._plot_roc(cls_ind)
            self.log_metrics(cls_ind,
                             metric_file_name=plot_file,
                             run_name="Test_Evaluation_Metrics")

            if len(self.class_names) == 2:
                break


        return


    def _plot_roc(self, cls_ind):
        """plot ROC curve and logged in mlflow

        Args:
            y_true: array of shape (n_samples, 1) in {0, 1}
            y_pred: array of shape (n_samples, 1) in {0, 1}
            num_class: int number

        Returns:
            plt: plot object in png format
        """
        plot_name = None
        fpr, tpr, roc_auc = dict(), dict(), dict()
        for i in range(self.num_class):
            fpr[i], tpr[i], _ = roc_curve(self.y_true, self.y_pred)
            roc_auc[i] = auc(fpr[i], tpr[i])

        fpr["micro"], tpr["micro"], _ = roc_curve(self.y_true,
                                                  self.y_pred)
        roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

        matplotlib.rcParams['interactive'] = True
        plt.figure()
        lw = 2
        plt.plot(fpr[1], tpr[1], color='darkorange', lw=lw,
                 label='ROC curve (area = %0.2f)' % roc_auc[1])
        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic example')
        plt.legend(loc="lower right")

        if self.num_class == 2:
            name = 'ROC Curve'
            prefix = 'roc_'
        else:
            name = f'ROC Curve {cls_ind})'
            prefix = f'roc-{cls_ind}_'


        with tempfile.NamedTemporaryFile(prefix=prefix, suffix='.png', delete=False) as f:
            plt.savefig(f.name, format="png")
            logger.info(f'[INFO] f.name in fig saving ->> {f.name}')
            plot_name = f.name

        return plot_name


    def description(self) -> str:
        """describe a description of the roc metric

        Args:
            str: a string value or a url to the metric

        Returns:
            no value
        """
        definition = ("ROC curves should be used when there are \
                      roughly equal numbers of observations for each class.")
        return definition


    def log_metrics(self, cls_ind, metric_file_name=None, metric_value=None,
                    run_name=None):
        """log roc metric in mlflow

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
