1 - Para rodar o projeto, primeiro instale as dependências com os comandos;
pip install -r requirements.txt
playwright install chromium

2 - Para crir um arquivo executável do projeto, execute o comando em terminal;
pyinstaller --onefile --add-data "C:/Users/SEU_USER/AppData/Local/ms-playwright;playwright" seu_script.py

3 - Caso queira rodar sem o executável, basta comentar ou deletar a linha 3 do arquivo "main.py".
