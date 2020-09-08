# DL-Telegram-by-file-attachment
[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)   

This tool automatically download a file (document) from a Telegram channel based on terms to search on.

The [service used to get Telegram content](https://tg.i-c-a.su/) has a RPM limit of 15 requests per minute but the script can check if the file is already present and not download it again.

## Installation 

Just copy and rename `config-sample.ini` to `config.ini` and set as you need.  
Run `downloader.py` to execute the tool.