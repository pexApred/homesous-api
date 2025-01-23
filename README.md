# homesous-api

This project is for ...?

---

## Getting Started

### Step 1: Setting Up the Local Dev Environment

1. Create a virtual environment:

   ```bash
   python -m venv $HOME/.local/share/virtualenvs/homesous-api
   ```

2. Activate the virtual environment:

   ```bash
   source $HOME/.local/share/virtualenvs/homesous-api/bin/activate
   ```

   Verify that the virtual environment is activated:
 
   ```bash
   $ which python
   /Users/me/.local/share/virtualenvs/homesous-api/bin/python
   ```

3. Install project dependencies

   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Running the Application
Once the dependencies are installed, you can run the Flask app:

```bash
python hello.py
```

### Step 3: Exiting the Virtual Env

When done working on the project/needing to invoke a different Python interpreter, deactivate the virtual env:

```bash
deactivate
```

---

## Note
Keep `requirements.txt` up to date whenever a dependency is `pip install`ed:

```bash
pip freeze > requirements.txt
```