mkdir meu_projeto  # Cria uma pasta chamada "meu_projeto"
cd meu_projeto  # Entra na pasta do projeto

python3 -m venv .venv  # Cria um ambiente virtual na pasta ".venv"
source .venv/bin/activate  # Ativa o ambiente virtual

pip install numpy pandas
python -c "import numpy; import pandas; print('NumPy:', numpy.__version__, 'Pandas:', pandas.__version__)"

touch main.py  # Cria um arquivo chamado "main.py"
open main.py  # Abre o arquivo no editor padrão (ou use "code main.py" se tiver o VS Code)

python main.py

pip freeze > requirements.txt
pip install -r requirements.txt

gh auth login
git init
gh repo create py_env_numpy --public --source=. --remote=origin
git add .
git commit -m “first commit”
git branch -M main
git remote add origin git@github:matuza1977/py_env_numpy.git
git push -u origin main
