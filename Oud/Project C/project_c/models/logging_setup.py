import logging

logging.basicConfig(
    filename = 'project_c.log',    # None or to a file 'example.log',
    level = logging.DEBUG,   # DEBUG, INFO, WARNING, ERROR, CRITICAL
    format = '%(asctime)s %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S')

def logger(f):
    def wrapper(*args, **kwargs):
        logging.info(f'entering function [{f.__name__}] - args: {args} - kwargs: {kwargs}')
        return_value = f(*args, **kwargs)
        logging.info(f'leaving function [{f.__name__}] - return value: {return_value}')
        return return_value
    return wrapper


if __name__ == '__main__':

    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warning message')
    logging.error('error message')
    logging.critical('citical message')

    @logger
    def f(x):
        return 10*x

    print(f(2))
