# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['censor_this']

package_data = \
{'': ['*']}

install_requires = \
['opencv-python>=4.6.0.66,<5.0.0.0',
 'pytesseract>=0.3.10,<0.4.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['censor-this = censor_this.main:app']}

setup_kwargs = {
    'name': 'censor-this',
    'version': '0.1.1',
    'description': 'A command line tool to censor words in an image.',
    'long_description': '# censor-this\n<a href="https://pypi.org/project/censor-this/"><img src="https://shields.io/static/v1?label=PyPi&message=censor-this&color=yellow"/></a><br/>\ncensor-this is a Python command line tool that allows you to censor words in an image.\n\n## Installation\nInstall Tesseract https://github.com/tesseract-ocr/tessdoc/blob/main/Installation.md#introduction\n```bash\npip install censor-this\n```\n\n## Commands\n### add\n```bash\ncensor-this add [word]\n```\n\nAdds a "censor word".\n\n#### Args\nword - The "censor word" that will be added. <font color="red">[required]</font>\n\n### remove\n```bash\ncensor-this remove [word]\n```\n\nRemoves a "censor word".\n\n#### Args\nword - The censor word that will be removed. <font color="red">[required]</font>\n\n### clear\n```bash\ncensor-this clear\n```\nRemoves all "censor words".\n\n### censor-words\n```bash\ncensor-this censor-words\n```\n\nPrints all "censor words".\n\n### image\n```bash\ncensor-this image [path]\n```\n\nCensors all "censor words" from an image or directory of images with blur, then outputs the results to *./censor-this-output*.\n\n#### Args\npath - The path to the image/directory. [example: this/is/the/path/to/the/image.png] <font color="red">[required]</font> <br />\n--censor-all | --all | -a -  Censor all words in an image. <font color="orange">[example: --censor-all]</font> <br />\n--min-conf | --conf | -m - The minimum confidence that will be required for a word to be censored. <font color="orange">[example: --min-conf=40.0]</font> <font color="aqua"> [default: 90.0]</font> <font color="green">**FLOAT**</font> <br />\n--bar-color | --color | -c - The color the censor bar will be.  When not present censor bar will default to blur.  Must be in ***hex*** format. <font color="orange">[example: --bar-color=#FFA200 ]</font> <font color="aqua">[default: None]</font> <font color="green">**TEXT**</font> <br />\n\n## Example\n1. Add words that you want to censor.\n```bash\ncensor-this add best # adding best to censor words\ncensor-this add worst # adding worst to censor words\ncensor-this add age # adding age to censor words\ncensor-this add foolishness # adding foolishness to censor words\n```\n2. Censor the words in the image.\n```bash\ncensor-this ./imgs/example.png --bar-color=\\#FFA200\n```\n3. Retrieve output from *./censor-this-output*.',
    'author': 'Colbe Roberson',
    'author_email': 'cgr28@njit.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
