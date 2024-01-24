# Financial Server 📊💼

## Overview 📖

Financial Server is an API designed for handling financial calculations. It performs tasks such as generating loan amortization tables, interest calculations, financial statements reports, and Excel file generation. The project includes tests to validate each API endpoint.

## Screenshots / Demonstration 📸

[Link to the Application](URL_APPLICATION)

(Captures screenshots in the specific repository folder)

## Technologies Used 🚀

- Python
- FastAPI
- Pytest
- XlsxWriter
- Docker

## Features ✨

- **Loan Amortization:** Generate tables for loan amortization.
- **Interest Calculations:** Calculate interest for financial purposes.
- **Financial Statements Reports:** Generate reports for financial statements.
- **Excel File Generation:** Create Excel files for financial data.

## Installation 🛠️

### Setup Project

1. **Create Virtual Environment (Windows):**

   ```cmd
   c:\>c:\Python35\python -m venv c:\path\to\myenv
   ```

   If you have set up variables into PATH, use:

   ```cmd
   c:\>python -m venv c:\path\to\myenv
   ```

2. **Activate Virtual Environment (Windows):**

   - Using cmd:

   ```cmd
   C:\> <venv>\Scripts\activate.bat
   ```

   - Using PowerShell:

   ```cmd
   PS C:\> <venv>\Scripts\Activate.ps1
   ```

3. **Install Dependencies:**

   ```cmd
   pip install -r requirements.txt
   ```

4. **Run Application in Development Mode:**

   ```cmd
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

### File Structure

```
financial_server/
    ├── app/
    │   ├── data/
    │   ├── models/
    │   ├── routers/
    ├── ├── services/
    ├── ├── temp/
    ├── ├── utils/
    │   ├── main.py
    ├── tests/
    ├── Dockerfile
    ├── main.py
    ├── requirements.txt
```

### Get Dependencies

```cmd
pip freeze > requirements.txt
```

## Project Status 🚧

The project is completed, and no additional functionalities are planned at the moment.

## Contribution 🤝

No contribution guidelines are established at the moment. The project is part of the portfolio, but suggestions are welcome. You can find contact information to provide feedback.

## License ⚖️

This project is distributed under the MIT License.
