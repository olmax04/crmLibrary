# Library for KommoCRM(AmoCRM) by olmax04
## Requirements specification
>If you wanna add this library in your project, and add to requirements.txt, add also this

```shell
--extra-index-url https://test.pypi.org/simple/
crmLibrary==<version>

#For example 
crmLibrary==1.3.1
```
## .ENV SETTINGS

Required to add:

```dotenv
RIELTOR_API_KEY=<YOUR-RIELTOR-MODULE-API-KEY>
MONGO_DB=<MONGO-DB-URL>

# INTEGRATION DATA

INTEGRATION_ID=<INTEGRATION-ID>
SECRET_KEY=<SECRET-KEY>
```

## Commands to build new version

### Remove previous version from ./dist
```shell

rm -r .\dist\

```
### Build new version 
>Remember to change version in ./pyproject.toml
```shell
# Windows
py -m build

# Linux
python -m build
```

### Upload new version using username and token 
>Remember to change version in ./pyproject.toml
```shell
python3 -m twine upload --repository testpypi dist/*
```

