# tripadvisor-web-crawler

The web crawler was written in Python for [tripadvisor](https://www.tripadvisor.com/). This non-profit project is used to practice ETL(Extract, transform, load) for people who want to learn basic data engineer skills. 

The web crawler of Tripadvisor, the overall project include following parts:

1. Get URLs for input place name(e.g. bellevue) and related sections (e.g. things_to_do)

## Installation

Follow these steps to use the web crawler:

- Download Chromedrive from [here](https://chromedriver.chromium.org/).
- Install Python virtual environments:

```
$ python3 -m pip3 install --user virtualenv
```

- Clone all remote branches in Git:

```
$ git clone https://github.com/weikunhan/tripadvisor-web-crawler.git
$ cd tripadvisor-web-crawler
$ git branch -a
```

- Install Python packages from requirements file, either using pip, conda or virtualenv:

```
$ virtualenv ./env
$ source ./env/bin/activate
$ pip3 install -r requirements.txt
```

## Configuration

The [config.json](./config.json) file allows to set:

1. the Chromedrive setup
2. the timeout and retry for web crawler
3. the API info
4. the header for outpu csv
5. the directory to store output csv, as well as their filenames
6. the directory to store temp files
7. the section information

## Usage

The web crawler has x parameters:

- `-q`, `--place_name`: crawling tartget place informaiton based on a string query.
- `-s`, `--section_name`: crawling urls of section based on the search result for one place.

The following show each part run examples and instructions.

### Part 1

Generate file to recored the top-30 things_to_do URLs bellevue city 

```
$ source ./env/bin/activate 
$ python main.py -q bellevue -s things_to_do
```

If you want to practice this part, you need to do:

```
$ git checkout practice-part-1
```

If you want to show answer for all parts, you need to do:

```
$ git checkout master
```

## Note

Python >= 3.6 is required.

## License

[MIT License](./LICENSE)


