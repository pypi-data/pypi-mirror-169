"""
    convert probility to int number
"""
import mlflow

from loguru import logger


MLFLOW_TRACKING_URI_COLAB = "http://185.110.190.127:7080/"
MLFLOW_TRACKING_URI = "https://mlflow.aimedic.co/"

"""
def _get_experiment_id_remote(experiment_name):
    mlflow.set_tracking_uri("https://mlflow.aimedic.co")
    mlflow.set_experiment(experiment_name)
    current_experiment = dict(mlflow.get_experiment_by_name(
                                experiment_name))
    experiment_id = current_experiment['experiment_id']
    logger.info(f'[INFO] experiment_id : {experiment_id}')

    return experiment_id


def get_mlflow_run(experiment_name,
                   run_name="Evaluation",
                   session_type="evaluation"):

    experiment_id = _get_experiment_id_remote(experiment_name)
    active_run = mlflow.start_run(experiment_id=experiment_id,
                                  run_name=run_name)
    mlflow.set_tag("session_type", session_type)

    return active_run
"""


def get_mlflow_experiment(experiment_id,
                          run_name="Evaluation",
                          session_type="evaluation",
                          is_colab = False):
    """convert label_vector and prediction_vector into binary vector

        Args:
            y_pred: array of shape (n_samples, 1) in float range
            (represent prediction probability)

        Returns:
            binary_y_pred: array of shape (n_samples, 1) in integers {0, 1}
    """
    if is_colab:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI_COLAB)
    else:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

    data_info = mlflow.get_experiment(experiment_id)
    exp_dict = dict(data_info)
    active_status = exp_dict['lifecycle_stage']
    if active_status == "active":
        active_run = mlflow.start_run(experiment_id=experiment_id,
                                      run_name=run_name)
        mlflow.set_tag("session_type", session_type)
        logger.info(f'>>> [INFO] active run_id  : {active_run.info.run_id}')
    else:
        active_run = None
        logger.info(f'>>> [Warning] This experiment is not active,\
                    so metrics are not logged in Mlflow.')

    return active_run


def get_mlflow_run(run_id,
                   run_name="Evaluation",
                   session_type="evaluation",
                   is_colab=False):
    """convert label_vector and prediction_vector into binary vector

        Args:
            y_pred: array of shape (n_samples, 1) in float range
            (represent prediction probability)

        Returns:
            binary_y_pred: array of shape (n_samples, 1) in integers {0, 1}
    """
    if is_colab:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI_COLAB)
    else:
        mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
        
    data_info = mlflow.get_run(run_id)
    data_dict = dict(data_info)
    run_info = data_dict['info']
    run_dict = dict(run_info)
    active_status = run_dict['lifecycle_stage']


    if active_status == "active":
        # logger.info(f'>>> [INFO] experiment_id  : {experiment_id}')
        logger.info('>>> [INFO] starting active run')
        # active_run = mlflow.start_run(experiment_id=experiment_id,
        #                               run_id=run_id,
        #                               run_name=run_name)
        # mlflow.end_run()
        active_run = mlflow.start_run(run_id=run_id,
                                      run_name=run_name)
        logger.info('>>> [INFO] active run is created .')
        mlflow.set_tag("session_type", session_type)

        logger.info(f'>>> [INFO] active run_id  : {active_run.info.run_id}')
    else:
        active_run = None
        logger.info(f'>>> [Warning] This run is not active,\
                    so metrics are not logged in Mlflow.')
    return active_run
