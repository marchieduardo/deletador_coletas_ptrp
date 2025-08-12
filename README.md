1 - Para rodar o projeto, primeiro instale as dependências com os comandos;<br>
pip install -r requirements.txt<br>
playwright install chromium<br>
<br>
2 - Para crir um arquivo executável do projeto, execute o comando em terminal;<br>
pyinstaller --onefile --add-data "C:/Users/SEU_USER/AppData/Local/ms-playwright;playwright" seu_script.py<br>
<br>
3 - Caso queira rodar sem o executável, basta comentar ou deletar a linha 3 do arquivo "main.py".<br>
