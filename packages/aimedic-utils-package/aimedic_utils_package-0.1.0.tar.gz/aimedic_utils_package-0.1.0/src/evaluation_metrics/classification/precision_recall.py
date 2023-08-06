import matplotlib.pyplot as plt
import mlflow
import os
import tempfile

from loguru import logger
from sklearn.metrics import PrecisionRecallDisplay
from sys import prefix
from ...utils.make_binary_pred import BinaryPrediction
from ...base.evaluation_interface import MetricsInterface
from ...utils.set_mlflow_run import get_mlflow_experiment, get_mlflow_run


class PrecisionRecallCurve(MetricsInterface):
    """
    A class used to represent a Precision Recall curve

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

        super(PrecisionRecallCurve, self).__init__(metric_list, y_true, y_pred,
                                        run_id, experiment_id)
        self.class_names = class_names

        self.num_class = len(self.class_names)
        self.description()


    def apply_metrics(self):
        """compute precision recall plot and log in mlflow

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
            plot_file = self._plot_precision_recall_curve(cls_ind)
            self.log_metrics(cls_ind,
                             metric_file_name=plot_file,
                             run_name="Test_Evaluation_Metrics")

            if len(self.class_names) == 2:
                break

        return


    def _plot_precision_recall_curve(self, cls_ind):
        fig_size = (10, 10)
        plot_name = None
        fig, axis = plt.subplots(figsize=fig_size)

        if self.num_class == 2:
            name = 'Precision-Recall (PPV-Sensitivity) Curve'
            prefix = 'precision_recall'
        else:
            name = f'Precision-Recall (PPV-Sensitivity) Curve (class {cls_ind})'
            prefix = f'precision_recall-{cls_ind}_'


        _ = PrecisionRecallDisplay.from_predictions(self.y_true,
                                                    self.y_pred,
                                                    ax=axis,
                                                    name=name)

        with tempfile.NamedTemporaryFile(prefix=prefix, suffix='.png', delete=False) as f:
            plt.savefig(f.name, format="png")
            logger.info(f'[INFO] f.name in fig saving ->> {f.name}')
            plot_name = f.name

        return plot_name



    def description(self) -> str:
        """describe a description of the precision recall curve metric

        Args:
            str: a string value or a url to the metric

        Returns:
            no value
        """
        definition = ("Precision-Recall curves should be used when \
                      there is a moderate to large class imbalance.")
        return definition


    def log_metrics(self, cls_ind, metric_file_name=None, metric_value=None,
                    run_name=None):
        """log precision recall curve metric in mlflow

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
