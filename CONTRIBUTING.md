# CONTRIBUTING.md

---
## Main Branches:

### ```master``` or ```main```— The branch for production-ready code. Only stable, fully-tested code is merged here.

### ```develop``` or ```dev``` — The branch for ongoing development. All new features and changes are integrated and tested here before being pushed to production.

---
## Supporting Branches:

### ```Feature Branches (feature/*)``` — Used to develop new features or make changes. Each feature has its own branch and is created from develop. 

To create: ```git checkout -b feature/feature_name develop```

To merge: After completing the feature, merge it back into develop:

```git checkout develop```,

```git merge feature/feature_name```.

Then, delete the feature branch:

```git branch -d feature/feature_name```

Example: ```feature/registration```

### ```Bugfix Branches (bugfix/*)``` — Used to fix bugs. Each bugfix has its own branch and is created from develop. 

To create: ```git checkout -b bugfix/bugfix_name develop```

To merge: After completing the bug fixing, merge it back into develop:

```git checkout develop```,

```git merge bugfix/bugfix_name```.

Then, delete the bugfix branch:

```git branch -d bugfix/bugfix_name```

Example: ```bugfix/registration```

### ```Hotfix Branches (hotfix/*)``` — Used for urgent bug fixes in production. Created from master or develop when a critical issue needs to be resolved.

To create:

```git checkout -b hotfix/fix_name develop```

To merge: After fixing the issue, merge it into both master and develop:

```git checkout master```, 

```git merge hotfix/fix_name```

```git checkout develop```,

```git merge hotfix/fix_name```

Then, delete the hotfix branch:

```git branch -d hotfix/fix_name```

---
## Workflow Process:

### Updating Project:
Use rebase option during update your local repository.

### Feature Development:
Developers create feature/* branches from develop, work on features, commit changes, push changes, create PR and after approve merge them back into develop.

### Bug Fixing:
Developers create bugfix/* branches from develop, work on bug, commit changes, push changes, create PR and after approve merge them back into develop.

### Hotfixes:
If a bug appears in production, a hotfix/* branch is created from master or develop, the issue is fixed, commited, PR created, approved and the branch is merged into both master and develop.

---
## Linters and Code Formatters:
We use only `black` as a code formatter and linter in GitHub Actions. For a successful push or pull request, the developer must manually format the code using the command `black .` in the terminal. After formatting, commit the changes and push them to your working branch.

**IMPORTANT**
If the developer does not run `black`, there might be an error during the push or pull request.

This GitHub Action could works for all new branches and for branches that might contains the `.github/workflow/lint.yaml` file.

### Expanded Explanation and Guidelines:
In our development process, it is crucial to maintain consistent code formatting standards to avoid issues and simplify code review. For this reason, we rely on `black` to automatically format Python code according to strict guidelines. Code must be formatted using `black` before every push or pull request.

### Steps for Developers:
1. Before pushing, run the command `black .` in your terminal to automatically format your Python code according to the project's standards.
2. After successful formatting, commit the changes and push them to your working branch.
3. When you create a pull request, GitHub Actions will automatically check if your code follows the formatting standards with `black`. If the formatting is incorrect, you will receive an error notification.

### What Happens in Case of an Error:
If the code does not comply with the formatting standards, GitHub Actions will stop the process and notify you that formatting is required. In this case, you need to run the `black .` command locally, correct the formatting, and then push the changes again.

This setup ensures clear and consistent code formatting checks, helping to avoid issues with improper code style during team development.

---
### Using `black` with VSCode and PyCharm Plugins
To make the process of formatting your code even easier, you can set up `black` as a plugin in your preferred IDE (VSCode or PyCharm). This way, your code will automatically be formatted upon saving, or you can trigger the formatting process with a shortcut.

### Setting up `black` in VSCode:
1. **Install the Python extension:**
   - Open VSCode.
   - Go to the Extensions view by clicking the Extensions icon on the left or pressing `Ctrl+Shift+X`.
   - Search for "Python" and install the official Python extension by Microsoft.

2. **Install `black`:**
   - Open the terminal in VSCode (`` Ctrl+` ``).
   - Run the command to install `black` globally or in your virtual environment:
   
    ```bash
     pip install black
     ```

3. **Configure VSCode to use `black` for formatting:**
   - Open your settings by clicking on `File -> Preferences -> Settings` or pressing `Ctrl+,`.
   - Search for "format on save" and enable the setting. This will automatically format your code every time you save a file.
   - Next, search for `python formatting provider` and select `black` as the default formatter.
   - You can also set this in your `settings.json` file:
  
   ```json
     {
       "python.formatting.provider": "black",
       "editor.formatOnSave": true
     }
     ```
4. **Run formatting manually (optional):**
   - If you prefer to format manually, you can trigger the formatter with `Shift+Alt+F` (Windows/Linux) or `Shift+Option+F` (Mac).

### Setting up `black` in PyCharm:
1. **Install `black`:**
   - Open PyCharm and go to your project.
   - Open the terminal in PyCharm by clicking `View -> Tool Windows -> Terminal`.
   - Install `black` by running:

   - ```bash
     pip install black
     ```

2. **Configure PyCharm to use `black` for formatting:**
   - Open `Preferences -> Tools -> External Tools`.
   - Click the `+` button to add a new external tool.
   - Fill in the following details:
     - **Name**: `black`
     - **Program**: path to your Python interpreter (e.g., `/usr/bin/python3`).
     - **Arguments**: `-m black $FilePathRelativeToProjectRoot$`
     - **Working Directory**: `$ProjectFileDir$`

3. **Run `black` manually from PyCharm:**
   - Once configured, you can run `black` by right-clicking a file or folder in the Project view and selecting `External Tools -> black`.
   
4. **Configure `black` to format on save (optional, with a plugin):**
   - Go to `Preferences -> Plugins`.
   - Search for the "black formatter" plugin and install it.
   - Restart PyCharm after installation.
   - Go to `Preferences -> Tools -> Actions on Save` and enable the "Reformat code" option, choosing `black` as the formatter.

---
This keeps the workflow focused and efficient while ensuring production stability.
