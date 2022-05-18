import os
from pytorch_lightning import Trainer
from pytorch_lightning.loggers import TensorBoardLogger

# default logger used by trainer
logger = TensorBoardLogger(save_dir=os.getcwd(), version=1, name="lightning_logs")
Trainer(logger=logger)