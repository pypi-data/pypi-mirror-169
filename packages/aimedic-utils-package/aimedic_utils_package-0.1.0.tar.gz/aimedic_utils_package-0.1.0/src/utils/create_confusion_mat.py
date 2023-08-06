"""
    Compute these metrics:
        1. create confusion matrix
        2. Positive Predictive Value (PPV): it's a probability that
            following a positive test result, that individual will truly have
            that specific disease (PPV is the probability that a subject/sample
            that returns a positive result really is positive).
        3. Negative Predictive Value (NPV): it's a probability that
            following a negative test result, that individual will truly not
            have that specific disease (NPV is the probability that a
            subject/sample that returns a negative result really is negative).
        4. Accuracy: a ratio of correctly predicted observation
            to the total observations.
        5. Precision: ratio of correctly predicted positive observations
            to the total predicted positive observations.
        6. Recall: a ratio of correctly predicted positive observations
            to the all observations in actual class.
        7. F-Score: It is the weighted average of Precision and Recall.
"""
import numpy as np
from loguru import logger
from sklearn.metrics import confusion_matrix


def get_conf_mat(y_true, y_pred):
    """create confusion matrix

    Args:
        y_true: array of shape (n_samples, 1) in {0, 1}
        y_pred: array of shape (n_samples, 1) in {0, 1}
        num_class: int number

    Returns:
        conf_mat: array of shape (n_classes, n_classes)
        accuracy: float input value
        misclass: float input value

    """
    conf_mat = confusion_matrix(y_true, y_pred).astype(float)
    true_neg, false_pos = conf_mat[0]
    false_neg, true_pos = conf_mat[1]

    eps = np.finfo(float).eps

    npv = true_neg / (true_neg + false_neg + eps)
    ppv = true_pos / (true_pos + false_pos + eps)  # Precision
    sensitivity = true_pos / (true_pos + false_neg + eps)  # Recall
    specificity = true_neg / (true_neg + false_pos + eps)
    accuracy = (true_pos + true_neg) / (true_pos + true_neg + \
                                        false_pos + false_neg + eps)
    f1_score = 2 * (ppv * sensitivity) / (ppv + sensitivity + eps)
    logger.info(f'confusion_mat: {conf_mat}')

    misclass = 1 - accuracy


    return conf_mat, accuracy, misclass, npv, ppv, \
        sensitivity, specificity, f1_score
