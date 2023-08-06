"""
    create an Interface class for metrics package
"""
from abc import ABCMeta, abstractmethod


class MetricsInterface:
    """
    An interface class used to handle subclasses methods

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
    apply_metrics   (public function)
    log_metrics     (public function)
    """
    __metaclass__ = ABCMeta
    def __init__(self, metric_list, y_true, y_pred,
                 run_id=None, experiment_id=None):
        self.metric_list = metric_list
        self.y_true = y_true
        self.y_pred = y_pred
        self.run_id = str(run_id)
        self.experiment_id = str(experiment_id)


    @abstractmethod
    def apply_metrics(self) -> None:
        """compute all user input metrics and logged in mlflow
        metrics include: confusion_matrix, roc, npv, ppv, sensitivity,
        specificity, accuracy, f1-score

        Args:
            y_true: array of shape (n_samples, 1) in {0, 1}
            y_pred: array of shape (n_samples, 1) in {0, 1}
            metric_list: array of shape (n_metrics, 1) in {0, 1, 2, 3, ...}
            class_names: array of shape (n_classes, 1) in {"NoneHemo", "Hemo"}

        Returns:
            no value

        """

    @abstractmethod
    def log_metrics(self) -> None:
        """log all computed metrics

        Args:
            metric_file: a file , plot, ... input
            metric_value: a float, int or a dictionary input value

        Returns:
            no value

        """

    @abstractmethod
    def description(self) -> str:
        """describe a description of the metric

        Args:
            str: a string value or a url to the metric

        Returns:
            no value

        """
