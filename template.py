import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')
package_name = 'deepClassifier'

list_of_files = [
    '.github/workflows/.gitkeep', #helps in doing CI CD; .gitkeep does not commits any empty folder in github
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/components/__init__.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/config/__init__.py',
    f'src/{package_name}/entity/__init__.py',
    f'src/{package_name}/pipeline/__init__.py',
    f'src/{package_name}/constants/__init__.py',
    'tests/__init__.py',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    'configs/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'init_setup.sh', #shell script file
    'requirements.txt',
    'requirements_dev.txt', #libraries only used for development and not use case
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini', #doing testing of code locally
    'research/trials.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # Creating Directories
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating dir: {filedir} for filename: {filename}')
    # Creating Files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass #create an empty file only if the file is not created before
            logging.info(f'Created file of name: {filename}')
    else:
        logging.info(f'{filename} already exists in {filepath}')