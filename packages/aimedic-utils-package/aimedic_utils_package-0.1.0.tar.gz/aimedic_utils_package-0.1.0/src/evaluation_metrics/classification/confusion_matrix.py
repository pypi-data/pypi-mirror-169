
from cProfile import run
import itertools
import matplotlib.pyplot as plt
import matplotlib
import mlflow
import numpy as np
import tempfile
import uuid

from loguru import logger
from sklearn.metrics import confusion_matrix
from sys import prefix
from ...utils.make_binary_pred import BinaryPrediction
from ...utils.create_confusion_mat import get_conf_mat
from ...utils.set_mlflow_run import get_mlflow_experiment, get_mlflow_run
from ...base.evaluation_interface import MetricsInterface


class ConfusionMatrix(MetricsInterface):
    """
    A class used to compute a Confusion Matrix

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

        # self.metric_list = metric_list
        # self.y_true = y_true
        # self.y_pred = y_pred
        # self.run_id = str(run_id)
        # self.experiment_id = str(experiment_id)
        super(ConfusionMatrix, self).__init__(metric_list, y_true, y_pred,
                                             run_id, experiment_id)
        self.class_names = class_names

        logger.info(f'[INFO] ** self.class_name in confusion_mat class : {self.class_names}')
        logger.info(f'[INFO] ** self.run_id in confusion_mat class : {self.run_id}')
        logger.info(f'[INFO] ** self.experiment_id in confusion_mat class : {self.experiment_id}')
        self.num_class = len(self.class_names)
        self.description()


    def apply_metrics(self):
        """compute confusion_matrix plot and log in mlflow

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
            conf_mat, accuracy, misclass, npv, ppv, sensitivity, \
                specificity, f1_score = get_conf_mat(self.y_true, self.y_pred)

            plot_file = self._plot_confusion_mat(cls_ind,
                                                           conf_mat,
                                                           accuracy,
                                                           misclass)
            self.log_metrics(cls_ind,
                             metric_file_name=plot_file,
                             run_name="Test_Evaluation_Metrics")

            value_list = [npv, ppv, sensitivity,
                          specificity, accuracy, f1_score]
            self.log_metrics(cls_ind, metric_value=value_list,
                             run_name="Test_Evaluation_Metrics")
            if len(self.class_names) == 2:
                break

        return


    def _plot_confusion_mat(self, cls_ind, cf, accuracy,
                            misclass, normalize = True):
        """plot confusion matrix

        Args:
            cf: array of shape (n_classes, n_classes)
            accuracy: float input value
            misclass: float input value
            normalize: bool input value

        Returns:
            plt: plot object in png format
        """
        plot_name = None
        cmap = plt.get_cmap('Blues')
        plt.figure(figsize=(8, 6))
        plt.imshow(cf, interpolation='nearest', cmap=cmap)
        plt.title("confusion_matrix")
        plt.colorbar()

        tick_marks = np.arange(self.num_class)
        plt.xticks(tick_marks, self.class_names, rotation=45)
        plt.yticks(tick_marks, self.class_names)

        if normalize:
            cf = cf.astype('float') / cf.sum(axis=1)[:, np.newaxis]


        thresh = cf.max() / 1.5 if normalize else cf.max() / 2
        for i, j in itertools.product(range(cf.shape[0]), range(cf.shape[1])):
            if normalize:
                plt.text(j, i, "{:0.3f}".format(cf[i, j]),
                         horizontalalignment="center",
                         color="white" if cf[i, j] > thresh else "black")
            else:
                plt.text(j, i, "{:,}".format(cf[i, j]),
                         horizontalalignment="center",
                         color="white" if cf[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label\naccuracy={:0.3f}; \
                    misclass={:0.3f}'.format(accuracy, misclass))

        if self.num_class == 2:
            prefix = 'confusion_mat_'
        else:
            prefix = f'confusion_mat-{cls_ind}_'
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
        return "indicates confusion matrix"


    def _save_file_metrics_by_experiment(self,
                                         metric_file_name,
                                         run_name):

        active_run = get_mlflow_experiment(self.experiment_id,
                                           run_name=run_name)
        if active_run is not None:
            mlflow.active_run()
            mlflow.log_artifact(local_path=metric_file_name)
            logger.info('[INFO] plot Metrics are logged in Mlflow by experiment.')
            mlflow.end_run()

        return


    def _save_file_metrics_by_run(self,
                                  metric_file_name,
                                  run_name):

        active_run = get_mlflow_run(self.run_id, run_name=run_name)
        if active_run is not None:
            mlflow.active_run()
            mlflow.log_artifact(local_path=metric_file_name)
            logger.info('[INFO] plot Metrics are logged in Mlflow by run.')
            mlflow.end_run()

        return


    def _save_value_metrics_by_run(self,
                                   metric_value,
                                   run_name,
                                   suffix):

        active_run = get_mlflow_run(self.run_id, run_name=run_name)
        if active_run is not None:
            mlflow.active_run()
            # mlflow.log_artifact(local_path=metric_file_name)
            # mlflow.end_run()

            mlflow.log_metrics(
                {f'eval_NPV{suffix}': metric_value[0],
                f'eval_PPV-Precision{suffix}': metric_value[1],
                f'eval_Sensitivity-Recall{suffix}': metric_value[2],
                f'eval_Specificity{suffix}': metric_value[3],
                f'eval_Accuracy{suffix}': metric_value[4],
                f'eval_F1-Score{suffix}': metric_value[5]})
            mlflow.end_run()
            logger.info('[INFO] value Metrics are logged in Mlflow by run.')

        return


    def _save_value_metrics_by_experiment(self,
                                          metric_value,
                                          run_name,
                                          suffix):

        active_run = get_mlflow_experiment(self.experiment_id,
                                           run_name=run_name)
        if active_run is not None:
            mlflow.active_run()
            mlflow.log_metrics(
                {f'eval_NPV{suffix}': metric_value[0],
                f'eval_PPV-Precision{suffix}': metric_value[1],
                f'eval_Sensitivity-Recall{suffix}': metric_value[2],
                f'eval_Specificity{suffix}': metric_value[3],
                f'eval_Accuracy{suffix}': metric_value[4],
                f'eval_F1-Score{suffix}': metric_value[5]})
            mlflow.end_run()
            logger.info('[INFO] value Metrics are logged in Mlflow by experiment.')

        return


    def log_metrics(self, cls_ind, metric_file_name=None, metric_value=None,
                    run_name=None):
        """log confusion matrix metric in mlflow

        Args:
            metric_file: a file , plot, ... input
            metric_value: a float, int or a dictionary input value

        Returns:
            no value

        """

        if metric_file_name is not None:
            if self.run_id != "None":
                logger.info('[INFO] calling _save_file_metrics_by_run()')
                self._save_file_metrics_by_run(metric_file_name, run_name)
            elif self.experiment_id != "None":
                logger.info('[INFO] calling _save_file_metrics_by_experiment()')
                self._save_file_metrics_by_experiment(metric_file_name,
                                                      run_name)

            else:
                mlflow.log_artifact(local_path=metric_file_name)

            logger.info('[INFO] plot Metrics are logged in Mlflow.')
            logger.info('*************************************************')

        if metric_value is not None:
            if isinstance(metric_value, list):
                suffix = f'_class{cls_ind}'
                if self.num_class == 2:
                    suffix = ''
                if self.run_id != "None":
                    self._save_value_metrics_by_run(metric_value, run_name, suffix)

                elif self.experiment_id != "None":
                    self._save_value_metrics_by_experiment(metric_value, run_name, suffix)

                else:
                    mlflow.log_metrics(
                        {f'eval_NPV{suffix}': metric_value[0],
                        f'eval_PPV-Precision{suffix}': metric_value[1],
                        f'eval_Sensitivity-Recall{suffix}': metric_value[2],
                        f'eval_Specificity{suffix}': metric_value[3],
                        f'eval_Accuracy{suffix}': metric_value[4],
                        f'eval_F1-Score{suffix}': metric_value[5]})

            else:
                if self.run_id != "None":
                    active_run = get_mlflow_run(
                        self.run_id,
                        run_name=run_name)
                    if active_run is not None:
                        mlflow.log_metrics(metric_value)
                        mlflow.end_run()
                elif self.experiment_id != "None":
                    active_run = get_mlflow_experiment(
                        experiment_id=self.experiment_id, run_name=run_name)
                    if active_run is not None:
                        mlflow.log_metrics(metric_value)
                        mlflow.end_run()
                else:
                    mlflow.log_metrics(metric_value)

            logger.info('[INFO] value Metrics are logged in Mlflow.')

        return
