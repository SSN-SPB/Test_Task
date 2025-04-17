import numpy as np

from ..ai_resorse_function.iris_iteraction_functions import (evaluate_model,
                                                             load_data,
                                                             train_model)
import logging

logger = logging.getLogger(__name__)


def test_data_shape():
    X, y = load_data()
    logger.info(X.shape[0])
    assert X.shape[0] == len(y)
    assert X.shape[1] == 4  # 4 features in the Iris dataset


def test_model_accuracy():
    X, y = load_data()
    model, X_test, y_test = train_model(X, y)
    accuracy = evaluate_model(model, X_test, y_test)
    assert accuracy >= 0.9  # model should perform well


def test_predict_single_sample():
    X, y = load_data()
    model, _, _ = train_model(X, y)
    sample = np.array([X[0]])
    pred = model.predict(sample)
    assert pred.shape == (1,)
