# Visual Pinball X Gamepad Mapper
A motivação do projeto é poder jogar o [Virtual Pinball X](https://www.vpforums.org/index.php?app=tutorials&article=1) no controle do XBox de forma simples.

## Como usar
Essa aplicação é feita para rodar no Windows (testado no 11).
> Esta sendo disponibilizado executavel dessa aplicação nos assets da release (via pyinstaller).

### Requisitos
- S.O. Windows
- Python >=3.13,<3.14

### Virtualenv e dependências
```sh
python -m venv .venv
.\.venv\Scripts\activate
pip install 'poetry>=2.0.0,<3.0.0'
poetry install
```

### Iniciar
```sh
python .\app.py
```
> É possivel passar o argumento `--verbose`

## Extra

### Criar o EXE da aplicação
```sh
poetry run build
```
O executavel estará disponivel no `./dist/vpx_gamepad.exe`
