# Installation Guide

This guide is intended to enable users unused to working with code to run scripts, if you already have a development
environment you are comfortable with, you can skip to the section on [GitHub](#github).

## Text Editors

Even if you aren't intending to write new code, you may need to modify configuration files. Word processing software
adds invisible formatting characters to documents that complicate editing raw text files. Although programs like
notepad on Windows can work, [vscode](https://code.visualstudio.com) is recommended.

## Terminal Setup

At this time, all scripts are run from the command line. For those unfamiliar, the command line is accessed through
a terminal program and is simply a way of sending text-based commands for the computer to run.

![Terminal](img/terminal.png)

You should be able to configure the terminal (or shell) of your choice to run scripts from this project, though it has only
been tested on Powershell, bash, and zsh. This guide will focus on bash and zsh, as these are easiest to use with git, the
version control system we use.

### Windows
bash isn't natively available on Windows, but it does come bundled with [Git for Windows](https://git-scm.com/downloads/win).
Optionally, you can install the Terminal app from the Windows Store. If you do so, you can add a profile for Git Bash to
Terminal when you install Git for Windows. When installing Git for Windows, there are several screens with different options
to pick from, and the defaults should be acceptable.

Once git has been installed, you should be able to find Git Bash under Git in the start menu (or if you installed Terminal,
launch it and open a new tab with the Git Bash profile using the dropdown arrow in the title bar).

### macOS
macOS comes natively with the zsh shell. To find it simply press Command + Space and type "Terminal" in the search bar. 
[Homebrew](https://brew.sh) is the recommended method to install git. Once Homebrew is installed, run `brew install git`
in the terminal.

### Linux
Linux distributions vary, but most come with either bash or zsh and git. Consult your distribution's documentation
for further information.

## GitHub

The project is hosted on [GitHub](https://github.com), and you can navigate directly to the repository via the link
in the title bar. To access this private repository you will need to create an account and contact your administrator to
give you the permissions necessary to access the project.

## Cloning the Repository

Once you have your terminal open and git installed, you will need to navigate to where you want to download the project to.
Often the most convenient place is your home (or user) folder. To move the command line to your home folder, you can use the
command `cd ~`, ~ being a shortcut for the full path to your home folder. If you want to keep the files in a particular
place, you can navigate there by typing `cd /full/path/to/location/`. For example, if you have a "projects" folder on
your D drive on windows, you could type `cd /d/projects`. Note that the cloning process will automatically create a
tikkun-olam-data-club folder in this directory to keep everything in.

When you are ready, run `git clone https://github.com/zachsqueer/tikkun-olam-data-club.git` in the terminal. You will be asked
for your github credentials either in the terminal or via a browser window, and if you have the correct permissions you will
now download a copy of the repository in the rfs_data folder in whichever directory you ran the command above. Run
`cd tikkun-olam-data-club` in the terminal to move into that folder.

## uv

This project uses uv to manage python installations and dependencies. You will need the cURL utility, which
is included with Git for Windows and macOS. Some Linux distributions do not have it installed by default and you 
may have to install that first. To install uv, run `curl -LsSf https://astral.sh/uv/install.sh | sh` in the terminal.

To more easily use uv, you can also enable autocompletion in your shell via an included script within uv. There are instructions
on how to do this for various shells [on uv's home site](https://docs.astral.sh/uv/getting-started/installation/#shell-autocompletion).
For example, if you are running bash you would run `echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc`
in your terminal.

The first time you run `uv venv`, the correct version of python and all dependencies will be downloaded
and installed into a python virtual environment.

## Token Files

Many of scripts in the project rely on token files that are not hosted on github for security reasons. You will need to
contact an administrator for access to these.
