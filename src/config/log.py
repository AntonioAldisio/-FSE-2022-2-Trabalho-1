import logging

def log():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-4s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='src/log/trabalho1_antonio_aldisio.csv',
                        filemode='a')