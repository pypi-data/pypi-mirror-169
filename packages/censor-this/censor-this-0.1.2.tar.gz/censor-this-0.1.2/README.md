# censor-this
<a href="https://pypi.org/project/censor-this/"><img src="https://shields.io/static/v1?label=PyPi&message=censor-this&color=yellow"/></a>
<a href="https://github.com/cgr28/censor-this"><img src="https://shields.io/static/v1?label=GitHub&message=censor-this&color=blue" /></a><br />
censor-this is a Python command line tool that allows you to censor words in an image.

## Installation
Install Tesseract https://github.com/tesseract-ocr/tessdoc/blob/main/Installation.md#introduction
```bash
pip install censor-this
```

## Commands
### add
```bash
censor-this add [word]
```

Adds a "censor word".

#### Args
- word - The "censor word" that will be added. <br /> **[required]**

### remove
```bash
censor-this remove [word]
```

Removes a ***censor word***.

#### Args
- word - The ***censor word*** that will be removed. <br /> **[required]**

### clear
```bash
censor-this clear
```
Removes all ***censor words***.

### censor-words
```bash
censor-this censor-words
```

Prints all ***censor words***.

### image
```bash
censor-this image [path]
```

Censors all ***censor words*** from an image or directory of images with blur, then outputs the results to *./censor-this-output*.

#### Args
- path - The path to the image/directory. <br /> **[example: this/is/the/path/to/the/image.png] [required]** <br />
- --censor-all | --all | -a -  Censor all words in an image. <br /> **[example: --censor-all]** <br />
- --min-conf | --conf | -m - The minimum confidence that will be required for a word to be censored. <br /> **[example: --min-conf=40.0] [default: 90.0] FLOAT** <br />
- --bar-color | --color | -c - The color the censor bar will be.  When not present censor bar will default to blur.  Must be in ***hex*** format. <br /> **[example: --bar-color=#FFA200 ] [default: None] TEXT**

## Example
<img src="https://github.com/cgr28/censor-this/blob/main/imgs/example.png" />

1. Add words that you want to censor.
```bash
censor-this add best # adding best to censor words
censor-this add worst # adding worst to censor words
censor-this add age # adding age to censor words
censor-this add foolishness # adding foolishness to censor words
```

2. Censor the words in the image.
```bash
censor-this image ./imgs/example.png --bar-color=#FFA200
```
3. Retrieve output from *./censor-this-output*.

<img src="https://github.com/cgr28/censor-this/blob/main/imgs/censored-example.png" />
