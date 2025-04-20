# Usage

The easiest way to get started with running our projects is via the `tolam` command line tool. Once you
have installed uv and run `uv venv` the project will automatically build the tool. activate the virtual
environment from the `tikkun-olam-data-club` root folder by entering `. ./.venv/Scripts/activate` and then
enter `tolam` into the terminal as well as any command line arguments necessary. This will automatically
run the `main()` function in the file at `src/cli/run.py`. This is the only entry point that is usable
via this tool.

## Running Scripts as Modules

It is important to note that because of the project's structure, scripts must be run as 
modules. So instead of moving to the `/src/cli/` directory and 
using `uv run run.py` to launch the `run.py` script, you would remain in the root 
folder in the terminal and instead run `uv run -m cli.run`. 

Breaking down this syntax:

* We've added the `-m` flag to the `uv run` command, which will prime the interpreter to look for
a module
* We've given the interpreter a path to the file we want to run starting from the root folder,
`src`, using `.` as a directory separator instead of `/`.
* We've omitted the .py extension on the `run.py` file

Using this syntax you can run any file in the project from the `src/` folder.

## Unhosted Token Folders

Many scripts have a need for sensitive data like login information. This data is generally stored in token
files in a folder named `.env` within src. This folder is excluded from github,
so during setup you will need to create the folder before either placing the correct token file in it or
creating your own as appropriate.

Not all versions of Windows will allow you to easily create a folder starting with a dot. If you run into
problems, opening the folder in vscode should allow you to create the folder via its explorer window.
