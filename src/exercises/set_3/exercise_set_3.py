"""
To add a dependency like pandas to your environment when using uv, even if you add it
into the virtual envirnoment properly it won't be recorded in your pyproject.toml or
your uv.lock files. You can add it to the pyproject.toml file manually which will add
it to your uv.lock file on your next run or sync, but it's infinitely easier to just
add it as

    uv add pandas

from your terminal. However, when I add it as part of my environment to create this
exercise set, it will be added to the pyproject.toml file, so you shouldn't even have
to do this as pandas will be installed when you run a file. I just wanted to demonstrate
how convenient uv is making package management behind the scenes.
"""
