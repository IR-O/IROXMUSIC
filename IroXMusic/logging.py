import logging  # Import the logging module

logging.basicConfig(
    level=logging.INFO,  # Set the root logger level to INFO, so that all messages with level INFO and above will be tracked
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",  # Set the log format
    datefmt="%d-%b-%y %H:%M:%S",  # Set the date format
    handlers=[
        logging.FileHandler("log.txt"),  # Create a FileHandler to write logs to a file named 'log.txt'
        logging.StreamHandler(),  # Create a StreamHandler to write logs to the console
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)  # Set the logger level for 'httpx' to ERROR, so that only ERROR level messages and above will be tracked
logging.getLogger("pyrogram").setLevel(logging.ERROR)  # Set the logger level for 'pyrogram' to ERROR
logging.getLogger("pytgcalls").setLevel(logging.ERROR)  # Set the logger level for 'pytgcalls' to ERROR


def LOGGER(name: str) -> logging.Logger:  # Define a function to get a named logger
    return logging.getLogger(name)  # Return the named logger
