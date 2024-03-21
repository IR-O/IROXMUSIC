import logging  # Import the logging module, which provides a flexible framework for emitting log messages from Python programs

# Configure the logging module with some basic settings
logging.basicConfig(
    level=logging.INFO,  # Set the root logger level to INFO, so that all messages with level INFO and above will be tracked
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",  # Set the log format to include a timestamp, log level, name, and message
    datefmt="%d-%b-%y %H:%M:%S",  # Set the date format to include the day, month (abbreviated), year, hour, minute, and second
    handlers=[
        logging.FileHandler("log.txt"),  # Create a FileHandler to write logs to a file named 'log.txt'
        logging.StreamHandler(),  # Create a StreamHandler to write logs to the console
    ],
)

# Set the logger level for specific modules to ERROR, so that only ERROR level messages and above will be tracked
logging.getLogger("httpx").setLevel(logging.ERROR) 
