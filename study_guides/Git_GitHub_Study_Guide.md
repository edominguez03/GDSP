# Git + GitHub Study Guide

## 1. What Git and GitHub are

**Git** tracks the history of your project on your computer.

**GitHub** stores a remote copy of your Git repository online.

Typical workflow:

```text
Write code
   ↓
git status
   ↓
git add
   ↓
git commit
   ↓
git push
   ↓
GitHub
```

---

## 2. Configure Git once on your computer

Check Git:

```bash
git --version
```

Set your name:

```bash
git config --global user.name "Your Name"
```

Set your email:

```bash
git config --global user.email "your_email@example.com"
```

Verify:

```bash
git config --global user.name
git config --global user.email
```

---

## 3. Go to the project folder

Example:

```bash
cd ~/Desktop/GDSP
```

Verify where you are:

```bash
pwd
```

Important: run Git commands from inside the project folder or one of its subfolders.

---

## 4. Turn the folder into a Git repository

Only do this once for a new project:

```bash
git init
```

Git creates a hidden folder:

```text
.git/
```

That hidden folder stores the repository history.

Check:

```bash
git status
```

Typical first output:

```text
On branch main

No commits yet

Untracked files:
...
```

---

## 5. Create a `.gitignore`

A `.gitignore` tells Git which files it should ignore.

Create it:

```bash
touch .gitignore
```

For a basic Python project on macOS, put this inside the file:

```text
.DS_Store
__pycache__/
```

Then save it.

Check:

```bash
git status
```

---

## 6. Stage files

`git add` moves changes into the **staging area**.

Add one file:

```bash
git add lesson27.py
```

Add a file using its path:

```bash
git add 01_python_fundamentals/lesson27.py
```

Add several specific files:

```bash
git add file1.py file2.py file3.py
```

Check what is staged:

```bash
git status
```

You want to see:

```text
Changes to be committed:
```

---

## 7. Make a commit

A commit is a saved snapshot of the project.

Example:

```bash
git commit -m "Add Lesson 27: Dictionaries"
```

Good commit messages describe what changed.

Examples:

```text
Add Lesson 27: Dictionaries
Fix typo in Lesson 1
Add .gitignore
```

---

## 8. Inspect the repository

See the current state:

```bash
git status
```

See exactly what changed in a tracked file:

```bash
git diff filename.py
```

See commit history:

```bash
git log --oneline
```

See the history as a graph:

```bash
git log --oneline --graph --decorate --all
```

Useful meanings:

```text
HEAD = your current position ("bookmark")
main = your current branch
* = a commit
```

If Git opens the pager and you see `:` or `(END)`, press:

```text
q
```

to return to the normal Terminal prompt.

---

## 9. Create the GitHub repository

On GitHub:

1. Create a new repository.
2. Give it the same project name, for example `GDSP`.
3. If the local project already has files and commits, do **not** initialize the GitHub repository with a README, `.gitignore`, or license.

The new GitHub repository should initially be empty.

---

## 10. Connect the local repository to GitHub

Copy the HTTPS repository URL from GitHub.

It will look like:

```text
https://github.com/YOUR_USERNAME/GDSP.git
```

Add it as the remote named `origin`:

```bash
git remote add origin https://github.com/YOUR_USERNAME/GDSP.git
```

Verify:

```bash
git remote -v
```

Expected structure:

```text
origin  https://github.com/YOUR_USERNAME/GDSP.git (fetch)
origin  https://github.com/YOUR_USERNAME/GDSP.git (push)
```

`origin` is simply the conventional nickname for the remote repository.

---

## 11. Authenticate GitHub CLI (first-time setup)

If GitHub CLI is not installed:

```bash
brew install gh
```

Verify:

```bash
gh --version
```

Authenticate:

```bash
gh auth login
```

Choose:

```text
GitHub.com
HTTPS
Authenticate Git with your GitHub credentials: Yes
Login with a web browser
```

Follow the browser authorization process.

You can verify later with:

```bash
gh auth status
```

---

## 12. Push to GitHub for the first time

The first push:

```bash
git push -u origin main
```

Meaning:

```text
git push = upload commits
origin   = the GitHub remote
main     = the branch being uploaded
-u       = remember the tracking relationship
```

After this succeeds, your local branch tracks:

```text
origin/main
```

---

## 13. Normal workflow after setup

For each new lesson or feature:

```bash
git status
git add path/to/file.py
git commit -m "Describe the change"
git push
```

Example:

```bash
git status
git add 01_python_fundamentals/lesson30.py
git commit -m "Add Lesson 30: Dictionary methods"
git push
```

---

## 14. Important distinction: commit vs push

`git commit` saves the snapshot **locally on your computer**.

`git push` sends those commits to **GitHub**.

So:

```text
Saved locally only:
git commit

Saved locally + uploaded to GitHub:
git commit
git push
```

If you forget to push, the newest commits are still only on your computer.

---

## 15. Quick command reference

```bash
git status
```
See the current repository state.

```bash
git add <file>
```
Stage a file for the next commit.

```bash
git commit -m "message"
```
Create a snapshot.

```bash
git push
```
Upload committed changes to GitHub.

```bash
git diff <file>
```
See exactly what changed.

```bash
git log --oneline --graph --decorate --all
```
See repository history.

```bash
git remote -v
```
See the connected GitHub repository.

```bash
q
```
Exit the Git log pager.

---

## 16. The mental model

```text
Working directory
      │
      │ git add
      ▼
Staging area
      │
      │ git commit
      ▼
Local Git history
      │
      │ git push
      ▼
GitHub
```

Remember:

- **Working directory** = files you are editing now.
- **Staging area** = changes selected for the next commit.
- **Commit** = local snapshot.
- **Push** = copy local commits to GitHub.

---

## 17. Recommended GDSP routine

Start a work session:

```bash
git status
```

Work on the lesson.

Run and test the program.

Then:

```bash
git status
git add 01_python_fundamentals/lessonXX.py
git commit -m "Add Lesson XX: Topic"
git push
```

Finally:

```bash
git status
```

Ideal ending:

```text
On branch main
nothing to commit, working tree clean
```

That means the local work is fully committed. If `git push` also succeeded, GitHub has the latest committed version too.
