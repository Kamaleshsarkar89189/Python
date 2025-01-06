# Python - Logging

'''
Logging in Python
Logging in Python is a standard way to track events that happen when software runs. It helps developers monitor and debug applications by recording messages about the program’s execution, errors, or other information.
'''

'''
Why Use Logging?
Debugging: Understand and fix issues in code by analyzing log records.
Monitoring: Track the application’s behavior in real time or analyze historical logs.
Error Reporting: Get details about errors without displaying them to users.
Replace print: Logging offers more control and can write logs to files, consoles, or remote systems.'''

# Advanced Example: Logging to a File
import logging

# Create logger
logger = logging.getLogger('my_app')
logger.setLevel(logging.DEBUG)  # Set global log level

# Create console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)

# Example usage
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
