
import pandas as pd
from pandas.errors import ParserError

from utils import find_project_root

"""
Pandas and SQL are both capable of similar things, but you'll find that they are
also better at different things. Pandas is usually better for dealing with smaller
datasets since it's not optimized like a database, and if it's used on a larger
dataset it's usually to use the miles of extra flexibility you get from using it
within a full fledged interpreted language to clean it for processing within a
more heavily resourced database. SQL gives you granular control over not just how
you transform the data, but the manner in which you do so. This allows you to, with
experience, optimize a query for your exact use case and reduce resource use or
increase speed or both.

This is largely how we use it, and I'm moving us even further in that direction as
our systems mature. To that end we're going to learn enough pandas to make you
dangerous and then get into SQL. This will have the secondary benefit of giving me a
reason to dig further into SQL optimization, which I have paid attention to in the
past, but our data throughput hasn't been high enough to make truly necessary yet.
====================================================================================

The core of pandas consists of the DataFrame and Series objects. You'll find that
while thereare operations suitable for other things, a pandas operation will almost
always beeither acting on one of these objects or a method of one in practice. In
additionto the convenience of having an object built to hold tabular and array data
and all of the built-in methods that go with them, what makes DataFrames and Series
(and the arrays from the numpy library they're built out of) is that they are heavily
optimized by using C-based code under the hood to perform operations on the entire
dataset at once. The operation `df = df + 5` on a table called df filled with
integers will look at the dtype (datatype) of each column, see that they're all
numbers, and then add 5 to all elements at the same time.

Strictly speaking, there are more optimized libraries that use multiprocessing
these days, but pandas is sufficient for cleaning data and getting it into BigQuery.

Usually when we're working with pandas we're working with a table of data in some
form, and there are a number of different formats the constructor for a dataframe
will accept. Press enter to advance each print statement in the terminal.
"""

columns = ["a", "b", "c"]
list_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
columns = pd.Index(columns)
df = pd.DataFrame(data=list_lists, columns=columns)
print(df)
input()

dict_lists = {col: list_lists[i] for i, col in enumerate(columns)}
# [
#   "a": [1, 2, 3],
#   "b": [4, 5, 6],
#   "c": [7, 8, 9]
# ]
df = pd.DataFrame(dict_lists)
print(df)
input()

series_list = [pd.Series(list_lists[i], name=col) for i, col in enumerate(columns)]
#
#   "a": [1, 2, 3], name = a
#   "b": [4, 5, 6], name = b
#   "c": [7, 8, 9], name = c
#
df = pd.DataFrame(series_list)
print(df)
input()
# Whoops, what happened there?
df = pd.concat(series_list, axis=1)
print(df)
input()
# Oh, there it is

path = find_project_root() / "example_files" / "session_3.csv"
df = pd.read_csv(path)
print(df)
input()

"""
There are a lot of other ways to make dataframes, mostly from other file types
(notably excel, html, and zip files containing them for our purposes) but the
ones we will use most are, by far, lists of dictionaries (#2) and read_csv.
read_csv is very powerful with a lot of different keyword arguments you can use
to open a variety of different formats of files and even urls, I recommend pulling
up the docs every time you need to use it until you're comfortable with it.

====================================================================================

Once you have the data in a dataframe you have a great deal of control over it.
"""

path = find_project_root() / "example_files" / "test_data.csv"
df = pd.read_csv(path)
print(df.head(10).to_markdown())  # Get just the first x rows
print(df.dtypes)  # Print datatypes for all columns

input()

df = df.rename(columns={"timestamp_canvassed": "timestamp"})  # Rename parts of an index
# Notice how I specified columns above, rows have labels just like columns
# Generally they default to numbered rows unless you change it yourself

# Also note above that I had to assign the result of the rename function back to the
# dataframe. Most pandas functions do not touch the original dataframe (referred to as
# modifying in-place) but instead return a copy of the dataframe, which must then be
# assigned to the variable.

df["crm_id"] = df["crm_id"].astype(str) #  Cast a datatype to another datatype
# The above can throw an exception if it fails to cast anything easily, only
# use this to convert to a less restrictive data type (like from integer to string above)
# or make sure you've throughly cleaned the data

# You can apply functions to series, and a dataframe's columns are stored as series
def from_bq_timestamp(s: pd.Series) -> pd.Series:
    # if s.str.endswith(" UTC").all():  # Pandas' strip functions doesn't just strip the
    #     s = s.str.rstrip(" UTC")
    try:
        s = pd.to_datetime(s, format="%Y-%m-%d %H:%M:%S.%f UTC", utc=True)  # Convert string to time object
    except (ParserError, ValueError):
        pass  # If it fails to convert, do nothing.
    return s

new = df.apply(from_bq_timestamp)  # Apply function to all columns
df["timestamp"] = from_bq_timestamp(df.loc[:, "timestamp"])  # Apply to columns individually
df["time_added"] = from_bq_timestamp(df.loc[:, "time_added"])
print(new.head(10))

input()

print(df.head(10))  # Same result in this case
print(df.dtypes)  # Note the changed dtypes
print(df.describe())  # Free stats!

input()

df[["project_code", "state"]] = df["instance_name"].str.extract(r"^(\d+)(\D+)$", expand=True)  # Regex operations are built in
print(new.head(10))
print(df.head(10))

# df = df.drop(columns=["instance_name"])
# df_mask = ~(df["survey_question"].isna())
# df = df[df_mask]
# print(df.reset_index())

df = df.groupby(["list", "survey_question"])["survey_response"].count()
print(df)
