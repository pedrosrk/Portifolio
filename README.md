# Portifolio

## Production Enviroment
- python -m venv env
- .\env\Scripts\activate
- pip install -r requirements.txt
- .\env\Scripts\python.exe -m pip install --upgrade pip
- python .\__init__.py


## Development Enviroment
- python -m venv env
- .\env\Scripts\activate
- pip install -r requirements.txt
- .\env\Scripts\python.exe -m pip install --upgrade pip
- replace serve(app, host="0.0.0.0", port=5000) for app.run(debug=True)
- python .\__init__.py

## Git
- git init
- git add .
- git commit -m "test"
- git push

## Update Requirements
- pip freeze > requirements.txt