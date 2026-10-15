# diabetes-triage
# Virtual Diabetes Clinic Triage
## Initial setup

### 1. Clone the repository

```bash
git clone https://github.com/yuktiChaudhary/diabetes-triage.git
cd diabetes-triage
```

### 2. Set up a virtual environment

We only need to do this once when you first clone the project.

**Mac / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (I think? this is the correct command for windows but I'm not sure):**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### Why I think we should be using a virtual environment

I remember having issues in a previous group project because we had different packages and versions installed, so something would work on one person's laptop but not on someone else's. I'd rather not deal with that again lol.

So I thought we could use virtual environments this time. Basically, everyone gets their own isolated Python environment for the project, meaning whatever we install for this assignment won't interfere with packages from other projects.

We'll still need to make sure we're using compatible package versions, but this should at least help avoid some unnecessary issues.

### 3. When you come back to the project

We **don't need to create the virtual environment again** every time you work on the assignment. Once it's created, it stays in the project folder.

You just need to activate it again when you open a new terminal.

**Mac / Linux:**

```bash
source .venv/bin/activate
```

**Windows :**

```powershell
.venv\Scripts\Activate.ps1
```

If you see `(.venv)` in your terminal, it's active. VS Code might also activate it automatically, so I would suggest checking before running the command.

### 4. When you're done

You can either close the terminal or deactivate the environment using:

```bash
deactivate
```

### A few things to remember

- Everyone needs to create their own virtual environment locally. We shouldnt be uploading those to GitHub.
- Make sure `.venv/` is in `.gitignore` so it doesn't accidentally get committed.
- You only create the environment once. After that, just activate it whenever you're working on the project.
- Once we start dividing the work, we should probably use separate branches and pull requests instead of everyone pushing directly to `main`.

### How to check that the dataset works

After activating your virtual environment and installing the requirements, make sure you're in the main `diabetes-triage` folder.

Run:

```bash
python -c "from src.data import X, y; print(X.shape, y.shape)"
```

Expected output:

```text
(442, 10) (442,)
```

You can also check the feature names:

```bash
python -c "from src.data import X; print(X.columns.tolist())"
```

Expected output:

```text
['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
```

I've tested both commands locally and they work.

### Using the dataset in other files

Instead of loading the dataset separately, we can import it from `src/data.py`:

```python
from src.data import X, y
```

Run Python from the main project folder when using this import. 

---

## Installing the same package versions

I've added a `requirements.txt` file so we can all use the same versions of scikit-learn and pandas.

The versions I'm using are:

```text
scikit-learn==1.9.1
pandas==3.0.6
```

I'm using Python 3.13.0, so we should try to use Python 3.13 if it works for everyone. Check yours with:

```bash
python --version
```

Once your virtual environment is active, install the packages with:

```bash
python -m pip install -r requirements.txt
```

To check the installed versions:

```bash
python -c "import sklearn, pandas; print('scikit-learn:', sklearn.__version__); print('pandas:', pandas.__version__)"
```

Expected output:

```text
scikit-learn: 1.9.1
pandas: 3.0.6
```

You can also check for dependency issues:

```bash
python -m pip check
```

If everything is okay, it should say `No broken requirements found.`

If someone adds a new library later, we should update `requirements.txt` and commit it. After pulling any changes to that file, run the installation command again.

The two main packages are pinned, but their dependencies aren't all pinned yet. I guess we can sort that out when we work on Docker and CI/CD.

---

## Docker setup

We'll also be using Docker for this assignment.

If you don't already have it, download Docker.

Once it's installed, open Docker Desktop and make sure the engine is running.

Check the installation using:

```bash
docker --version
```

Then test it with:

```bash
docker run hello-world
```

If everything works, you should see `Hello from Docker!` in your terminal.

I've tested this locally too. We don't need to build our project's Docker image yet; we'll do that when we start implementing the API and model.

---

## Project structure

- `app/` — API code
- `src/` — Shared Python code and dataset loader
- `models/` — Saved models
- `metrics/` — Evaluation results, including RMSE
- `tests/` — Automated tests
- `.github/workflows/` — GitHub Actions
- `CHANGELOG.md` — Changes between v0.1 and v0.2
- `requirements.txt` — Shared package versions

Some folders currently just contain `.gitkeep` placeholder files. We'll later add the actual code once we divide the work.
  