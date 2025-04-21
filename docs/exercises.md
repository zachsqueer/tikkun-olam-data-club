# Exercises

## Set 1

1. Go to the [Kaggle API documentation](https://github.com/Kaggle/kaggle-api/blob/main/docs/KaggleApi.md)
and make a [Kaggle](https://www.kaggle.com) account. On your profile page you will be able to make an api
key, do so and place it in you .env folder. Your goal is to download [this file](https://www.kaggle.com/datasets/towhid121/netflix-life-impact-dataset-nlid).
Note the following:
    - This api uses basic auth and your api token will just have a username and password in it. The syntax for using this with the `requests` module is `requests.get(url, auth=(username, password))` where your key is the
    password.
    - The "user slug" and "dataset slug" can both be obtained from the page for the file, it is difficult to find
    from the API
    - The result of this api call will be the raw file data, not a json object. The "content" attribute of the Response object you get from your request can be used to access this data, and you can write it to disk
    using a similar construct to that used to write the google token to file.
    - Python's default text encoding is "whatever the current user's OS defaults are", which means that
    using the default encoding reduces compatibility and causes errors. When opening a file, it's important to set the "encoding" parameter, which is almost always "utf-8". Additionally, data sent over a network is often encoded as a stream of bytes, such as the data received for the csv files output by the Kaggle API. bytes objects like these have a .decode() method which can be passed an encoding (such as "utf-8") to decode it into a python string. 

2. Once you have the file downloaded, read [this short pandas tutorial](https://pandas.pydata.org/docs/user_guide/10min.html) and read the csv into a dataframe. Eliminate all rows from the dataframe except
those for movies released before 2016, and then print their titles.

3. Use the framework we developed to read [this spreadsheet](https://docs.google.com/spreadsheets/d/1dpW9eEg7dduk_7ztguU7NYbtqp44KiLgY_4zvHGBsTg/edit?gid=1902408398#gid=1902408398) into memory and then
make it into a dataframe. Confirm that they contain the same data.