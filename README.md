# Visual Pinball X Mapper
Mapeador do controle do XBOX para o Teclado.
Projeto iniciado para usar o [Virtual Pinball X](https://www.vpforums.org/index.php?app=tutorials&article=1).

## Como usar
Essa aplicação é feita para rodar no Windows.
> Criado e testado apenas no Windows 11.

### Requisitos
- Python 3.12

### Virtualenv e dependências
```sh
python -m venv .venv
.\.venv\Scripts\activate
pip install poetry
poetry install
```

### Iniciar
```sh
python .\app.py
```

## Desenvolvedor

### Compilar e empacotar o código
```sh
pyinstaller -F --python-option "PYTHONDONTWRITEBYTECODE=1" --optimize 2 --name 'vpx_mapper.exe' app.py
```
