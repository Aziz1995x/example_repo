echo [$(date)]: "START"
echo [$(date)]: "Creating ENV with python v3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activating the environment"
source activate ./env
echo [$(date)]: "Installing the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"