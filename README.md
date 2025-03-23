mkdir meu_projeto  # Cria uma pasta chamada "meu_projeto"
cd meu_projeto  # Entra na pasta do projeto

python3 -m venv .venv  # Cria um ambiente virtual na pasta ".venv"
source .venv/bin/activate  # Ativa o ambiente virtual

pip install numpy pandas
python -c "import numpy; import pandas; print('NumPy:', numpy.__version__, 'Pandas:', pandas.__version__)"
touch main.py  # Cria um arquivo chamado "main.py"
open main.py  # Abre o arquivo no editor padrão (ou use "code main.py" se tiver o VS Code)

import numpy as np
import pandas as pd

# Criando um array NumPy
array = np.array([1, 2, 3, 4, 5])
print("Array NumPy:", array)

# Criando um DataFrame Pandas
df = pd.DataFrame({'Coluna A': [10, 20, 30], 'Coluna B': [40, 50, 60]})
print("DataFrame Pandas:\n", df)aut


python main.py

pip freeze > requirements.txt
pip install -r requirements.txt



python -c "import sys; print(sys.prefix)"

source .venv/bin/activate

gh auth login
git init
gh repo create py_env_numpy --public --source=. --remote=origin
git add .
git commit -m “first commit”
git branch -M main
git remote add origin git@github:matuza1977/py_env_numpy.git
git push -u origin main
