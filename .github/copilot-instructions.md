# Copilot Instructions for Python Course Assignments

## Project Overview
This repository contains Python course assignments across multiple days (day01, day02, day03, day04, etc.). Each day contains lesson files, class assignments, and home assignments with varying complexity.

## Key Directories & Files
- `day01/`, `day02/`, `day03/`, `day04/`: Assignment folders organized by day
- `day02/home assignment/`: Contains dilution calculator scripts (CLI and GUI versions)
- `day03/`: Lesson files and assignments
- `day04/`: Advanced assignments (web scraping, API calls, GUI projects)
- `.gitignore`: Excludes `__pycache__/`, `venv/`, `env/`, logs, and OS files
- `requirements.txt`: Python package dependencies (requests, beautifulsoup4, etc.)

## Python Environment Setup
- **Python Version**: 3.11+ (installed at `C:\Users\ronyh\AppData\Local\Programs\Python\Python311`)
- **Virtual Environment**: `.venv/` (created via `python -m venv .venv`)
- **Activation**: `.\.venv\Scripts\Activate.ps1` (PowerShell)
- **Package Manager**: pip (upgrade with `python -m pip install --upgrade pip`)

### Common Packages
- `requests==2.32.5` — HTTP library for API calls and web requests
- `beautifulsoup4==4.14.2` — HTML/XML parsing
- `numpy`, `pandas` — Data manipulation (if needed)
- `tkinter` — GUI toolkit (bundled with Python)

## Running Scripts
### From Command Line (PowerShell)
```powershell
# Activate venv first
.\.venv\Scripts\Activate.ps1

# Run a script
python .\day04\main.py

# Run with piped input (non-interactive)
"query`noutput.json" | python .\day04\main.py
```

### Direct Python Execution
```powershell
# Use full path if venv not active
C:\Users\ronyh\AppData\Local\Programs\Python\Python311\python.exe .\day04\main.py
```

## Common Development Tasks

### Install New Packages
```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install <package_name>
```

### Add/Update `requirements.txt`
```powershell
python -m pip freeze > requirements.txt
```

### Git Workflow
```powershell
# Check status
git status

# Stage and commit changes
git add -A
git commit -m "Your message" --no-verify

# Push to remote
git push
```

### Troubleshooting Slow Commits
- **OneDrive interference**: Pause OneDrive (system tray → Help & Settings → Pause syncing)
- **Pre-commit hooks**: Use `git commit --no-verify` to skip hooks
- **File locks**: Ensure no editor/explorer is holding `.git` files
- **Solution**: Pause OneDrive before committing large files

## Known Issues & Fixes

### Issue: Python not found / WindowsApps stub
- **Solution**: Use full path or ensure Python is on PATH:
  ```powershell
  setx PATH "C:\Users\ronyh\AppData\Local\Programs\Python\Python311;C:\Users\ronyh\AppData\Local\Programs\Python\Python311\Scripts;$env:PATH"
  ```
- Disable Microsoft Store app alias (Settings → Apps → App execution aliases → turn OFF `python.exe`)

### Issue: Requests returns 0 items (web scraping)
- **Cause**: CSS selectors outdated, site uses JavaScript rendering, or blocks scraping
- **Solution**: 
  - Inspect page HTML (`response.text`) to find correct selectors
  - Update `logic.py` with new CSS selectors
  - Consider Selenium for JavaScript-heavy sites

### Issue: Git rebase stuck / "Deletion of directory failed"
- **Cause**: OneDrive or antivirus holding `.git` files
- **Solution**: 
  1. Pause OneDrive
  2. Run: `git rebase --abort` and `git fetch && git pull --no-rebase`
  3. Commit with `--no-verify` if hooks are slow

## Best Practices
1. **Always activate venv** before running/installing:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
2. **Use `--no-verify` for fast commits** when pre-commit hooks are slow:
   ```powershell
   git commit -m "message" --no-verify
   ```
3. **Create `requirements.txt`** after installing new packages for reproducibility.
4. **Test scripts interactively** before committing:
   ```powershell
   python .\day04\main.py
   ```
5. **Keep `.gitignore` up to date** to avoid tracking cache, venv, or sensitive files.

## Useful Commands for Copilot
- "Install [package name]" → Install into active venv with `pip install`
- "Run [script name]" → Execute with venv Python + show output
- "Commit changes" → Add, commit with `--no-verify`, and push
- "Fix [error message]" → Diagnose and provide solution

## Notes for Future Development
- **Day 04 projects** often require web scraping or API integration; ensure `requests` and `beautifulsoup4` are in venv.
- **GUI projects** (tkinter) are bundled with Python; no extra install needed.
- **CSV/Data files** should be gitignored if they contain sensitive data; use `.gitignore`.
- **Test coverage**: Consider adding unit tests in `tests/` folder if projects grow.
