# DL-Telegram-by-file-attachment
[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)   

This tool automatically download a file (document) from a Telegram channel based on terms to search on.

The [service used to get Telegram content](https://tg.i-c-a.su/) has a RPM limit of 15 requests per minute but the script can check if the file is already present and not download it again.

## Installation & Use

Make sure to have Python3 installed on your system: you can follow the instruction to get it [straight from the Python website](https://wiki.python.org/moin/BeginnersGuide/Download).

Clone this repository and rename `config-sample.ini` to `config.ini` then open the renamed file and change the configuration as you wish.

The parameters you can set are:
- `name` is the channel name you want to download from (only the name, not the whole URL)
- `pages` is the number of pages to search for documents to download
- `filter` allows you to filter the file type to download
- `download` is the folder where the downloads are stored

To use the tool simply run `downloader.py`.