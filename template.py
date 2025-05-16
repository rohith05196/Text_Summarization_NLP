import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

name_of_project = 'textsummarizer'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{name_of_project}/__init__.py",
    f"src/{name_of_project}/components/__init__.py", 
    f"src/{name_of_project}/utils/__init__.py",
    f"src/{name_of_project}/utils/common_func.py",
    f"src/{name_of_project}/logging/__init__.py",
    f"src/{name_of_project}/config/__init__.py",
    f"src/{name_of_project}/config/configuration.py",
    f"src/{name_of_project}/pipeline/__init__.py",
    f"src/{name_of_project}/entities/__init__.py",
    f"src/{name_of_project}/pipeline/__init__.py",
    f"src/{name_of_project}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "DockerFile",
    "setup.py",
    "trial/trials.ipynb",
    "main.py",
    "app.py"
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)

    if filedir!= '':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory: {filedir}")
        
    if (not os.path.isfile(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File {filepath} already exists and is not empty.")


