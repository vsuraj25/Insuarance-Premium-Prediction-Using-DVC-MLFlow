import os
from pathlib import Path

package_name = 'Premium_Predictor'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{package_name}/components/__init__.py',
    f'src/{package_name}/utils/__init__.py',
    f'src/{package_name}/config/__init__.py',
    f'src/{package_name}/pipeline/__init__.py',
    f'src/{package_name}/entity/__init__.py',
    f'src/{package_name}/constants/__init__.py',
    f'src/{package_name}/__init__.py',
    'configs/config.yaml',
    'documents/.gitkeep',
    'hyper_param_testing/.gitkeep',
    "prediction_service/__init__.py",
    "prediction_service/prediction.py",
    "tests/__init__.py",
    'tests/conftest.py',
    'tests/test_config.py'
    'dvc.yaml',
    'params.yaml',
    'setup.py',
    'tox.ini',
    'Procfile',
    'app.py',
    'research/trails.ipynb'   
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as file:
            pass ## Creating an empty file

    else:
        pass