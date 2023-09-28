## Setup project

1. Create virtual enviroment in Windows

```cmd

c:\>c:\Python35\python -m venv c:\path\to\myenv

```

If you setup variables into PATH use:

```cmd

c:\>python -m venv c:\path\to\myenv

```

2. Activate virtual enviroment in Windows

Using cmd

```cmd

C:\> <venv>\Scripts\activate.bat

```

Using PowerShell

```cmd
PS C:\> <venv>\Scripts\Activate.ps1

```

3. Install dependencies

```cmd

pip install -r requirements.txt

```

4. Run application in Development Mode

```cmd

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

```

## File Structure

```

financial_server/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── routers/
    │   │   ├── __init__.py
    │   │   ├── amortization.py
    │   ├── services/
    │   │   ├── __init__.py
    │   │   ├── amortization_service.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_amortization.py
    ├── requirements.txt
    ├── main.py


```

## Get dependencies

```cmd

pip freeze > requirements.txt

```
