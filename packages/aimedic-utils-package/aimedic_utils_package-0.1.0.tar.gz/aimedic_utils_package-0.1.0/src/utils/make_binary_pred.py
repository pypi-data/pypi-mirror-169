"""
    convert probility to int number
"""


def BinaryPrediction(y_pred):
    """convert label_vector and prediction_vector into binary vector

        Args:
            y_pred: array of shape (n_samples, 1) in float range
            (represent prediction probability)

        Returns:
            binary_y_pred: array of shape (n_samples, 1) in integers {0, 1}
    """

    binary_y_pred = []
    for item in y_pred:
        if item <= 0.5:
            binary_y_pred.append(0)
        else:
            binary_y_pred.append(1)

    return binary_y_pred
