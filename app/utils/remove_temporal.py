import os
import shutil
import logging

# Set up a logger
logger = logging.getLogger(__name__)


def delete_temporary_files(temporary_directory):
    files_deleted = 0
    try:
        for file in os.listdir(temporary_directory):
            path_file = os.path.join(temporary_directory, file)
            if os.path.isfile(path_file):
                os.remove(path_file)
                files_deleted += 1
            elif os.path.isdir(path_file):
                shutil.rmtree(path_file)
        logger.info(
            f"{files_deleted} items in the folder '{temporary_directory}' have been deleted."
        )
    except FileNotFoundError as e:
        # Handle the case when a file doesn't exist
        logger.warning(f"File not found: {str(e)}")
    except IsADirectoryError as e:
        # Handle the case when trying to remove a non-empty directory
        logger.warning(f"Cannot remove non-empty directory: {str(e)}")
    except PermissionError as e:
        # Handle the case when you don't have permission to remove a file or directory
        logger.error(f"Permission error: {str(e)}")
    except Exception as e:
        # Handle other exceptions
        logger.error(f"An error occurred: {str(e)}")
