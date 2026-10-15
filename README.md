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
