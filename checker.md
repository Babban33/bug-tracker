# Dependency Checker 🛠️

A **GitHub Actions workflow** that automatically checks for outdated dependencies in your project and updates a `dependency_status.md` file with the results. This helps you keep your project up-to-date and secure with minimal effort. 🚀

---

## ⚡ Features

- **Automatic Dependency Check:**
  - Runs every week (or manually) to check for outdated dependencies.
- **Markdown Report:**
  - Updates a `dependency_status.md` file with:
    - A list of outdated dependencies.
    - The last checked date and time.
- **Dynamic File Handling:**
  - Automatically creates required files (`requirements.txt`, `outdated.txt`, `dependency_status.md`) if they don’t exist.
- **Easy Customization:**
  - Works seamlessly with Python projects (Django/Flask) and can be extended for other ecosystems.

---

## 📂 Files Managed by the Workflow

1. **`requirements.txt`:**
   - Contains the list of Python dependencies for the project.
   - If missing, a placeholder file is created with example dependencies.

2. **`outdated.txt`:**
   - Temporary file that stores outdated dependencies.
   - Automatically generated and updated by the workflow.

3. **`dependency_status.md`:**
   - Markdown file summarizing the results.
   - Includes:
     - Timestamp of the last check.
     - List of outdated dependencies, or a note if everything is up-to-date.

---

## 🔄 How It Works

1. **Trigger the Workflow:**
   - Automatically runs every Monday at midnight (can be customized).
   - Can also be manually triggered from the Actions tab.

2. **Check Dependencies:**
   - Uses `pip list --outdated` to find outdated Python packages.

3. **Generate a Report:**
   - Updates `dependency_status.md` with:
     - A timestamp.
     - A list of outdated dependencies.
     - A note if all dependencies are current.

4. **Commit the Changes:**
   - Commits and pushes the updated files to the repository.

---