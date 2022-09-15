import logging

def initialize_logger(name):
    logger = logging.getLogger(name)
    logger.propogate = False
    formater = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler(f'reports/log.log')
    file_handler.setFormatter(formater)
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    logger.debug(f'{name} logger initialized')
    # logger.debug('Delete the data folder')
    # shutil.rmtree(f'{name}/data', ignore_errors=True)
    # logger.debug('Create the data folder')
    # os.makedirs(f'{name}/data', exist_ok=True)
    return logger