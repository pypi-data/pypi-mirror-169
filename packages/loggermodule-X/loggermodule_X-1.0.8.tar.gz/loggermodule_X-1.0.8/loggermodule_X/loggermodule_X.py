import logging
from pathlib import Path
import sys
from datetime import datetime
from logging import handlers

LEVEL_LIST = ['NOTSET', 'INFO', 'DEBUG', 'ERROR', 'WARNING']
mode = ['split', 'midnight']

def namer(name):
    return name.replace(".log", "") + ".log"

def configLogger(name, filename=None, mode=mode, console_lv=LEVEL_LIST, file_lv=LEVEL_LIST):

    logging.getLogger().setLevel(level='NOTSET')
    logging.getLogger("filelock").setLevel(logging.ERROR) ## Avoid lockfile log

    if filename:
    # Add stdout handler, with level INFO
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(level=console_lv)
        formatter = logging.Formatter('[%(asctime)s] [PID:%(process)d ThreadID:%(thread)d] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d]  %(message)s')
        # formatter = logging.Formatter('Level: %(levelname)s PID: %(process)d - ThreadID: %(thread)d - Time: %(asctime)s -  - Function: %(funcName)s - Message: %(message)s')
        console.setFormatter(formatter)
        logging.getLogger().addHandler(console)
        path = Path(filename).parent.absolute()
        rawlog_path = path / "log"
        logName = Path(filename).stem
        logNameWithExtension = Path(filename).stem + '.log'
        logFileFullPath = rawlog_path / logNameWithExtension

        # logFileFullPath = rawlog_path / logFormat
        if mode and mode == 'midnight':
            rawlog_path.mkdir(parents=True, exist_ok=True)
            file_handler = handlers.TimedRotatingFileHandler(logFileFullPath, when='midnight', backupCount=0, encoding='utf-8')
        elif mode and mode == 'split':
            rawlog_path = rawlog_path / datetime.now().strftime("%Y%m%d")
            rawlog_path.mkdir(parents=True, exist_ok=True)
            file_handler = handlers.RotatingFileHandler(logFileFullPath, maxBytes=400000000, backupCount=10, encoding='utf-8')
        else:
            rawlog_path = rawlog_path / datetime.now().strftime("%Y%m%d")
            rawlog_path.mkdir(parents=True, exist_ok=True)
            file_handler = handlers.TimedRotatingFileHandler(logFileFullPath, when='midnight', backupCount=0, encoding='utf-8')
        # file_handler.suffix = "%Y-%m-%d.log"
        file_handler.namer = namer

        # file_handler = logging.FileHandler(logFileFullPath, encoding='utf-8')
        file_handler.setLevel(level=file_lv)
        file_handler.setFormatter(formatter)
        logging.getLogger().addHandler(file_handler)
        log = logging.getLogger("app." + logName)
    else:
        log = logging.getLogger("app." + name)

    # log.debug('Debug message, should only appear in the file.')
    # log.info('Info message, should appear in file and stdout.')
    # log.warning('Warning message, should appear in file and stdout.')
    # log.error('Error message, should appear in file and stdout.')
    return log

if __name__ == '__main__':
    configLogger(__name__, __file__, console_lv='INFO', file_lv='INFO')
