# Setting up your laptop for CHEM 427/527

To do the work in this course, your laptop needs five things: git, Python managed by a tool called uv, VS Code, Claude Code, and a copy of this repository. This guide installs them in that order and ends with a notebook that tells you whether everything works. Plan on about an hour and about 3 GB of free disk space.

Your laptop needs Windows 10 or 11, or macOS 14 (Sonoma) or later, and at least 4 GB of memory. To check a Mac, open the Apple menu and choose **About This Mac**. Claude Code needs macOS 13 or later, and VS Code supports only the three newest macOS releases. Every Apple silicon Mac, and most Intel Macs from 2018 or later, can update to macOS 14 for free through **System Settings**, **General**, **Software Update**. If yours cannot, say so in the setup status survey before you start, and Matt will follow up.

You do not need to finish before the first class on Thursday, October 1. Start before then if you can, and fill in the setup status survey on Canvas either way, because it tells Lucas, Chris, and Matt who needs help first. Sessions 1 to 3 have time for setup in the room, and Tuesday, October 13 (session 4) is the date by which every laptop must work.

## How to read this guide

Each step has a Windows block and a Mac block. Do only the one for your laptop. Each command sits on its own line in a gray box; copy the whole box, paste it into the terminal, and press Enter. Each step ends with a line that begins **You know it worked when**. If that line does not match what you see, stop there rather than continuing, and see "When something goes wrong" at the end.

The terminal is the text window where you type commands.

- **Windows:** open the Start menu, type `PowerShell`, and open **Windows PowerShell**. You do not need "Run as administrator".
- **Mac:** press Command and Space, type `Terminal`, and press Enter.

Several steps ask you to close the terminal and open a new one. Do it every time: a new terminal is how your laptop learns about a program you just installed.

## Step 1. Install git

Git downloads the course materials and later brings in each new session.

**Windows:**

```powershell
winget install --id Git.Git -e --source winget
```

If Windows reports that `winget` is not recognized, download the installer from the [Git for Windows download page](https://git-scm.com/downloads/win) instead and accept every default.

**Mac:**

```bash
xcode-select --install
```

A window asks whether to install the command line developer tools. Click **Install** and wait for it to finish, which can take 10 minutes. If the terminal replies that the tools are already installed, git is already there.

Close the terminal, open a new one, and run:

```bash
git --version
```

**You know it worked when** the terminal prints a line such as `git version 2.47.1`. Any version number is fine.

## Step 2. Install uv

uv installs Python and every package this course uses, at the versions the course uses, in one command in step 7. You do not need to install Python separately, and if you already have Python from Anaconda or python.org, uv leaves it alone.

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Mac:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Close the terminal, open a new one, and run:

```bash
uv --version
```

**You know it worked when** the terminal prints a line such as `uv 0.11.14`.

## Step 3. Install VS Code and its extensions

VS Code is the editor where you open notebooks and talk to Claude Code. It needs three extensions: Python, Jupyter, and Claude Code.

**Windows:**

```powershell
winget install --id Microsoft.VisualStudioCode -e --source winget
```

If `winget` is not available, download the Windows installer from the [VS Code download page](https://code.visualstudio.com/download) and leave the "Add to PATH" box checked.

**Mac:** download the Mac version from the [VS Code download page](https://code.visualstudio.com/download), open the downloaded file, and drag **Visual Studio Code** into your **Applications** folder. Open VS Code, press Command, Shift and P together, type `shell command`, and choose **Shell Command: Install 'code' command in PATH**.

On either system, close the terminal, open a new one, and install the three extensions:

```bash
code --install-extension ms-python.python
```

```bash
code --install-extension ms-toolsai.jupyter
```

```bash
code --install-extension anthropic.claude-code
```

**You know it worked when** each command ends with a line saying the extension was successfully installed. If VS Code is open, the three extensions appear in its Extensions view, the icon of four squares on the left edge.

## Step 4. Get a Claude account with Claude Code

Claude Code is not included in the free Claude plan. The course is designed around the Pro plan, which was $20 per month when this guide was written, so the quarter costs about $60 if you cancel after the final presentations on December 10. The Max plans raise the usage limits and are not needed for this course.

Go to [claude.ai](https://claude.ai), create an account or sign in, and subscribe to Pro from the settings page. Use an email address you will keep through the end of the quarter.

**You know it worked when** your account settings list Pro as your current plan.

## Step 5. Install Claude Code and sign in

The VS Code extension from step 3 is how you use Claude Code in class. The command line version installed here lets you check the install and sign in from the terminal.

**Windows:**

```powershell
irm https://claude.ai/install.ps1 | iex
```

**Mac:**

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Close the terminal, open a new one, and run:

```bash
claude --version
```

The terminal should print a version number followed by `(Claude Code)`. Then start Claude Code once to sign in:

```bash
claude
```

A browser window opens. Sign in with the account from step 4 and return to the terminal. Type `/exit` and press Enter to leave Claude Code.

**You know it worked when** the terminal showed a login success message before you exited. If no browser opened, press `c` to copy the sign-in link and paste it into a browser yourself.

## Step 6. Download the course repository

A repository is a folder whose history git tracks. These commands put the course repository in your home folder and are the same on Windows and Mac. Note that a folder synced by OneDrive or iCloud, which on many laptops includes Documents and Desktop, is the wrong place for it, because syncing the thousands of small files in the Python environment slows both down and can break it.

```bash
cd ~
```

```bash
git clone https://github.com/mfbush/signals-to-insights.git
```

```bash
cd signals-to-insights
```

**You know it worked when** `git clone` ends with `done.` and your home folder now contains a `signals-to-insights` folder with this file, `setup.md`, inside it.

## Step 7. Build the course Python environment

To give every student the same Python and the same package versions, this repository lists them in two files, `pyproject.toml` and `uv.lock`. One command reads them and builds the environment inside a hidden folder named `.venv`. Run it from inside the `signals-to-insights` folder, where step 6 left you.

```bash
uv sync
```

The first run downloads Python 3.14 and about 120 MB of packages, and the finished environment takes about 400 MB of disk. Then check that the five course packages load:

```bash
uv run python -c "import numpy, pandas, scipy, matplotlib, sklearn; print('packages ok')"
```

**You know it worked when** the last line printed is `packages ok`.

## Step 8. Run the setup check notebook in VS Code

This step tests the whole chain at once: VS Code, the Jupyter extension, the environment from step 7, and plotting. From the `signals-to-insights` folder, open it in VS Code:

```bash
code .
```

If VS Code asks whether you trust the authors of the files in this folder, choose **Yes, I trust the authors**.

1. In the file list on the left, open `setup-check.ipynb`.
2. Click **Select Kernel** at the top right of the notebook, choose **Python Environments**, and pick the entry that shows `.venv` and Python 3.14. A kernel is the running Python that executes the notebook's cells.
3. Click **Run All** at the top of the notebook. If VS Code offers to install anything for the kernel, accept.

**You know it worked when** a calibration plot appears partway down and the last cell prints `Setup check passed`. If the first cell prints `Course environment: NO`, the notebook is using a different Python; click the kernel name at the top right and choose the `.venv` entry again.

Every session notebook in this course runs the same way, starting with `sessions/S01-onboarding/activity.ipynb` in the first class.

## Step 9. Ask Claude Code about the notebook

The last step checks that Claude Code works inside VS Code and can read the course files. Click the Claude Code icon at the top right of the editor, or press Control, Shift and P (Command, Shift and P on a Mac), type `Claude Code`, and choose the command that opens it. Sign in if it asks. Then type:

```text
Explain what the third code cell of setup-check.ipynb does, one line at a time.
```

**You know it worked when** the answer describes the calibration data and the straight-line fit with `linregress`. It may differ from a classmate's answer in wording; that is expected.

## Step 10. Tell us where you are

Fill in the setup status survey on Canvas, even if you finished every step. If you stopped at a step, the survey asks which one and has a box for the error message.

## Keeping up to date during the quarter

New sessions are added to the repository through the quarter. Before each class, open a terminal in the `signals-to-insights` folder and run:

```bash
git pull
```

```bash
uv sync
```

The first command brings in the new session folder. The second matters only on the rare day the package list changes, and does nothing otherwise.

## If you already use conda

If Anaconda, Miniconda, or Miniforge is already how you run Python and you prefer to keep it, you can use conda in place of uv for steps 2 and 7. The file `environment.yml` describes the same packages, taken from the free conda-forge channel. Skip step 2, and replace step 7 with:

```bash
conda env create -f environment.yml
```

In step 8, choose the kernel named `signals` instead of `.venv`. After each `git pull`, update with `conda env update -f environment.yml --prune` instead of `uv sync`. Note that the course is taught and tested with uv, so in class the TAs can help faster with uv problems than with conda problems.

## When something goes wrong

Copy the full error text, not a description of it, and paste it into the survey or bring it to class. Most install problems have been seen before: Lucas and Chris keep a record of every fix from this quarter, and each of them looks after half the room by last name in sessions 1 to 3. The third hour of every class is an office hour, and in the first three weeks it is a setup clinic.

Once step 5 works, you can also paste the error into Claude Code in the terminal and ask what it means. That is the same habit the course asks of you with every error message this quarter.
