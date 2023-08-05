# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pfd']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.5,<3.0']

entry_points = \
{'console_scripts': ['paralleldownload = pfd.paralleldownloadcli:start',
                     'pfd = pfd.paralleldownloadcli:start']}

setup_kwargs = {
    'name': 'pfd',
    'version': '0.5.2',
    'description': 'Parallel Fast Downloader',
    'long_description': '# pfd - Parallel fast downloader\n#### Download large number of files extremely fast.\n\n\nA Python Package for Fast Parallel Download of Multiple Files.\nIt\'s Simple, easy and extremely fast since it uses, all the cores in your CPU to spin separate process for parallel download.\n`pfd` uses `requests` as its only dependency, which is almost always present in all python environment.\n\n\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pfd?style=for-the-badge)\n\n### Python Package Index Badges\n\n[![PyPI](https://img.shields.io/pypi/v/pfd?style=for-the-badge&color=gree&logo=pypi)](https://pypi.org/project/batchimage/)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/pfd?label=Downloads&style=for-the-badge)\n![PyPI - Status](https://img.shields.io/pypi/status/pfd?label=Status&style=for-the-badge)\n![PyPI - Format](https://img.shields.io/pypi/format/pfd?label=Format&style=for-the-badge)\n\n\n### Github Badges\n\n![GitHub last commit](https://img.shields.io/github/last-commit/insumanth/pfd?style=for-the-badge)\n![GitHub commit activity](https://img.shields.io/github/commit-activity/y/insumanth/pfd?style=for-the-badge)\n![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/insumanth/pfd?style=for-the-badge)\n![Lines of code](https://img.shields.io/tokei/lines/github/insumanth/pfd?style=for-the-badge)\n\n\n\n------------------\n## Python Package Index Install \n\n```\npip install pfd\n```\n-------------------\n\n### Usage:\n\n**Basic example:**\n```shell\n$ pfd input_url_file.txt\n```\n* It downloads the files using the urls in the file. Each url in a line.\n* The downloaded files is stored in current directory.\n* Uses number of process equal to number of CPU Cores in the machine.\n\n**Getting help, info, version and example:**\n```shell\n$ pfd [-h | -i | -v | -eg]\n```\n* These options will just print text and exits.\n  * `-h ` Prints the help message.\n  * `-i ` Prints information aboout the package.\n  * `-v ` Prints current version of the package.\n  * `-eg` Prints few example of how to use the this cli.\n\nSpecify save directory:\n```shell\n$ pfd input_url_file.txt downloads_directory\n```\n* The downloaded files is stored in `downloads_directory` directory.\n* You can provide absolute or relative paths for both url file and save directory.\n\n**Use N Processes**:\n```shell\n$ pfd input_url_file.txt -p 17\n```\n* Uses 17 processes to download files.\n* Default is equal to the number of cpu core count in the machine.\n\n\n**File names:**\n\n```shell\n$ pfd input_url_file.txt [-u | -n | -a]\n```\n\n* By default, it searches for the file name in the response. If found, it will use this name. Else it will use a uuid string as file name. [Yet to be implemented]\n  * `-u` All downloaded files will be named as uuid strings `[eg: 5b71113f-43be-40f5-b267-9b93919196aa.jpg]`\n  * `-n` All downloaded files will be named as sequential numbers `[eg: 017.jpg]`\n  * `-a` All downloaded files will be named as sequential lowercase english alphabets `[eg: exy.jpg]`\n* If extension is needed, they have to be manually provided.\n\n\n**Specify Extension**\n```shell\n$ pfd input_url_file.txt -e png\n```\n* Uses the provided extension in file names.\n* `.` (dot) is optional.\n* If extension is needed, they must be provided when using `[-u | -n | -a]` .\n\n\n\n------------------\n\n#### Description\n\nDo you want to download thousands of files at once but can\'t wait for sequential download? \n\nToday\'s machines have multiple CPU cores.\nMost entry level machines have 4 Cores while higher end machines have around 8 Cores, \nSome desktop processor even have 16 - 32 Cores.\nBut using just one Core for downloading files is not the best approach if you have hundreds or thousands of files to download.\n\nThe rapid shift towards cloud technologies provide massive processing power, GigaBit network and faster writes to disk.\nBy properly making use of this processing power, bandwidth, memory and IO, we can make our life a bit easier.\n\n`pfd` is one of such package.\nIt is a cli tool used to download thousands of files in short time.\nIt achieves it by spinning seperate process per CPU core and downloading parallely.\n\n\nImagine a Machine with 24 Core CPU and Gigabit Network.\nThe process to download 1000 files, and it takes 1 second to fetch each file,\n\n##### Sequential download\n\nPython Interpreter does the following steps.\n\nMake request  ➜ open a file ➜ save the content to the file\n\nAfter it is done, Python Interpreter repeats the steps 1000 times sequentially.\n\n\n\nIt takes `1000 files` `x` `1 Second` = `1000 Seconds` or `~17 Minutes` to download all files.\n\n`➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜`\n \n##### Parallel download\n\n28 Python Interpreter is spun up in all of 28 cores (one per core by default).\n\nEach Python Interpreter does the following steps.\n\nMake request  ➜ open a file ➜ save the content to the file\n\nAfter it is done, Each Python Interpreter repeats the steps 42 times (1000 files / 24 process).\n\n\nIt takes `(1000 files` `/` `24 Processes)` `x` `1 Second` = `42 Seconds` or `~1 Minutes` to download all files.\n\n```\n➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜\n➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜\n➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜\n[.. 19 more processes ..]\n➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜\n➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜ .. ➜➜➜\n```\n\n**Note:** This is just a logical comparison.\nThe time is not a real world example, many factors affects the download speeed.\nThere will be a slight overhead in setting up the process and collecting the work.\nSo, it will not download all in under a minute.\nThe Overhead should be negligable with higher input.\n\n\n\n\n\n-----------------\n![Made With Python](https://forthebadge.com/images/badges/made-with-python.svg)\n![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)\n\n<!--\n<img src="https://forthebadge.com/images/badges/works-on-my-machine.svg" alt="works-on-my-machine" width="500" height="100">\n-->\n',
    'author': 'Sumanth',
    'author_email': 'sumanthreddystar@gmail.com',
    'maintainer': 'Sumanth',
    'maintainer_email': 'sumanthreddystar@gmail.com',
    'url': 'https://pypi.org/project/pfd/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
