# azure_sql_django

Template for Auzre SQL and restAPI in Django Python

## Set Python environment

```
python3 -m venv .venv
source .venv/bin/activate
```

## Check current Python path

```
where python
```

## Install packages

```
pip install -r requirements.txt
```

## Run Application

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

```
python3 manage.py runserver
```

## Install Mac odbc driver

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew update
HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18 mssql-tools18
```

## Install Window odbc driver

```
msiexec /i msodbcsql.msi ADDLOCAL=ALL
```
