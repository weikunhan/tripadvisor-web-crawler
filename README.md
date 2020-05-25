# tripadvisor-web-crawler

The web crawler was written in Python for [tripadvisor](https://www.tripadvisor.com/). This non-profit project is used to practice ETL(Extract, transform, load) for people who want to learn basic data engineer skills. 

Scraper of Tripadvisor reviews, parametric by date and language. The script allows to scrape:

1. 
2. 
3. 

## Installation

Follow these steps to use the web crawler:

- Download Chromedrive from [here](https://chromedriver.chromium.org/).
- Install Python virtual environments:

```
$ python3 -m pip3 install --user virtualenv
```

- Install Python packages from requirements file, either using pip, conda or virtualenv:

```
$ cd tripadvisor-web-crawler
$ virtualenv ./venv
$ source ./venv/bin/activate
$ pip3 install -r requirements.txt
```

## Configuration

The [config.json](./config.json) file allows to set:

1. the Chromedrive setup
2. the header for outpu csv
3. the directory to store output csv, as well as their filenames
4. the timeout and retry for web crawler
5. the API info
6. the directory to store temp files

## Usage

The scraper has 5 parameters:
- `--i`: input file, containing a list of Tripadvisor urls that point to first page of reviews.
- `--lang`: language code to filter reviews.
**Note**: only "select all languages" click is implemented.
- `--N`: number of reviews to scrape.
- `--q`: string query to scrape url places.
- `--place`: boolean value to scrape place metadata instead of reviews.

Some examples:

- `python scraper.py --q amsterdam`: generates the _urls.txt_ file with the top-30 POIs of amsterdam
- `python scraper.py --place 1`: generates a csv file containing metadata of places present in _urls.txt_
- `python scraper.py`: generates a csv file containing reviews of places present in _urls.txt_



## Note

Python >= 3.6 is required.

## License

[MIT License](./LICENSE)


