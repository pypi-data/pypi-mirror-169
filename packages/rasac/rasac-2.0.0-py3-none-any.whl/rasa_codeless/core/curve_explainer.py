import logging
import os
from typing import Text, List, Tuple

from rasa_codeless.shared.constants import (
    DEFAULT_TENSORBOARD_LOGDIR,
    TENSORBOARD_INTENT_ACCURACY_TAG,
    TENSORBOARD_INTENT_LOSS_TAG,
    TENSORBOARD_SIMPLE_VALUE_TAG,
    TENSORBOARD_RESULTS_FILE_EXTENSION,
    TensorboardDirectories,
)
from rasa_codeless.utils.tensorboard import TensorBoardResults

logger = logging.getLogger(__name__)
tensorboard_results = TensorBoardResults()


class CurveExplainer:
    def __init__(self, logdir: Text = DEFAULT_TENSORBOARD_LOGDIR):
        self.logdir = logdir
