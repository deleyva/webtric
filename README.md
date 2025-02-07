# webtric
## _One python script to scrape many typical websites_

## Features

- Parsing of sites with table-like or tile-like structures
- Initial data preprocessing

## Installation

Pulse-Selenium requires Python3.7+ and [Selenium Chrome Driver](https://chromedriver.chromium.org/downloads) to be installed.

Create virtual environment and install requirements.txt

```sh
./scripts/quotes.sh ./outputs/quotes local
```
or

```sh
./scripts/quotes.sh ./outputs/quotes remote
```

## Docker

It can also be used through Docker
```sh
export APP=./scripts/quotes.sh
docker-compose up
```

## Jupyter
Run http://localhost:8888/lab?token=webtric to access internal filesystem and read scraped files 

Here is a good example on how to do it:
```python
import pandas as pd
from os import listdir
from os.path import isfile, join

VOLUME = "/home/webtric"
files = [f for f in listdir(VOLUME) if isfile(join(VOLUME, f))]

print('List of all parsed files')
print('\n'.join(files))

df = pd.read_csv(join(VOLUME, files[-1]))
df.head()
```
