import logging


def setup_logging(app):
    app.logger.setLevel(logging.INFO)
    # Log to stdout
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # Add the handler to the app logger
    app.logger.addHandler(handler)
