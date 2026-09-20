# Student Performance Analyzer – Streamlit Workshop

## Requirements
- Python 3.10–3.14
- VS Code (recommended)
- Internet connection for first-time package installation

## Windows setup

Open the VS Code terminal inside this folder.

### Option A – easiest
```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks activation, use Command Prompt:
```cmd
.venv\Scripts\activate.bat
```

Or run Streamlit without activating:
```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

### Run the app
```bash
python -m streamlit run app.py
```

The browser should open the local Streamlit app.

## Workshop activity
1. Upload `sample_students.csv`.
2. Change the selected metric.
3. Add one new numeric column to the CSV.
4. Add a new `st.metric()` card.
5. Change the title and caption.
6. Try adding another chart.

## Core idea
Python + Pandas -> Data Analysis -> Streamlit -> Interactive Data App
