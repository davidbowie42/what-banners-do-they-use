# What banners do they use

__What banners do they use__ is a script for checking what cookie banners a list of websites use.

## Installation

- Clone this repository
- Make sure you are using Python 3.9 or above

## Usage

Place a csv file named `domains.csv` containing the domains of the websites you want to have checked in the same directory as main.py  

Sample input:

```csv
duckduckgo.com
cookiebot.com
clickskeks.at
```

Executing `python3 main.py` will create a file `output.csv` with the following contents:

|Domain|Banner|
|---|---|
|duckduckgo.com|unknown|
|cookiebot.com|cookiebot|
|clickskeks.at|clickskeks|

## State of the project

Currently the project is in its early stages and only supports two cookie banner providers, namely Cookiebot and clickskeks.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
