from typing import Optional
import typer
import json
import cv2
import numpy as np
from PIL import ImageColor
import pytesseract
from pytesseract import Output
import sys
import os
import string
import time
from importlib import resources

app = typer.Typer()


@app.callback()
def callback():
    """
    Censor It
    """

@app.command()
def add(word: str):
    """
    Adds a censor word.
    """
    f = resources.open_text("censor_it", "data.json")

    data = json.load(f)
    if word not in data["censor_words"]:
        data["censor_words"].append(word)
        with resources.path("censor_it", "data.json") as f:
            json.dump(data, open(f, "w"), indent = 4)
        typer.echo(f"Added {word} to the censor list.")
    else:
        typer.echo(f"{word} is already in censor list.")

@app.command()
def remove(word: str):
    """
    Removes a censor word.
    """
    f = resources.open_text("censor_it", "data.json")
    data = json.load(f)
    if word not in data["censor_words"]:
        typer.echo(f"{word} not in the censor list.")
    else:
        data["censor_words"].remove(word)
        with resources.path("censor_it", "data.json") as f:
            json.dump(data, open(f, "w"), indent = 4)
        typer.echo(f"Removed {word} from the censor list.")

@app.command()
def clear():
    """
    Clears all the censor words.
    """
    f = resources.open_text("censor_it", "data.json")

    data = json.load(f)
    num_of_words = len(data["censor_words"])
    data["censor_words"] = []
    typer.echo(f"Cleared {num_of_words} words from censor list.")
    with resources.path("censor_it", "data.json") as f:
            json.dump(data, open(f, "w"), indent = 4)


@app.command()
def censor_words():
    """
    Prints all censor words.
    """
    f = resources.open_text("censor_it", "data.json")
    data = json.load(f)
    for word in data["censor_words"]:
        typer.echo(word)

@app.command()
def image(path: str, censor_all: bool = typer.Option(False, "--censor-all", "--all", "-a"), min_conf: Optional[float] = typer.Option(1.0, "--min-conf", "--conf", "-m"), bar_color: Optional[str] = typer.Option(None, "--bar-color", "--color", "-b")):
    """
    Censor the words in an image or a directory of images.
    """
    if not os.path.exists("./censor-it-output"):
        os.makedirs("./censor-it-output")

    if censor_all:
        cens_all = True # if set to true all words will be censored
        cens_words = []
        typer.echo("Censoring all words in image(s).")
    else:
        typer.echo("Censoring words in image(s) using censor words.")
        cens_all = False
        f = resources.open_text("censor_it", "data.json")
        data = json.load(f)
        cens_words =  set(data["censor_words"]) # words that will be censored

    num_words = 0 # total num of words
    num_cens = 0 # num of words censored
    rgb = None
    imgs = [] # contains all images
    blur = True

    if min_conf < 0:
        min_conf = 0
    elif min_conf > 1:
        min_conf = 1

    try:
        if bar_color:
            blur = False
            rgb = list(ImageColor.getcolor(bar_color, "RGB"))
            rgb.reverse()
    except:
        typer.echo("Error: Please correctly format --bar-color using hex .e.g. \"#FF0000\".")
        sys.exit(1)

    # checks if provided path is a dir or a file
    if os.path.isfile(path):
        try:
            img = cv2.imread(path, cv2.IMREAD_COLOR)
            t = time.strftime("%H-%M-%S", time.localtime())
            imgs.append([img, f"./censor-it-output/{t}-{os.path.basename(path)}"])
        except:
                typer.echo(f"Couldn't open {file}.")
                sys.exit(1)

    elif os.path.isdir(path):
        for file in os.listdir(path):
            if os.path.isfile(f"{path}/{file}"):
                img = cv2.imread(f"{path}/{file}", cv2.IMREAD_COLOR)
                if type(img) == type(None):
                    typer.echo(f"Couldn't read {file}")
                    continue
                t = time.strftime("%H-%M-%S", time.localtime())
                imgs.append([img, f"./censor-it-output/{t}-{file}"])
    else:
        # error when trying to get file or dir EXIT
        typer.echo("Error: Please provide a path to a file or directory.")
        sys.exit(1)

    for img, f in imgs:
        typer.echo(f"Censoring {f}")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pytesseract.image_to_data(img_rgb, output_type=Output.DICT) # detects words in images

        for i in range(len(results["text"])):

            x = results["left"][i]
            y = results["top"][i]
            w = results["width"][i]
            h = results["height"][i]

            text = results["text"][i]
            conf = float(results["conf"][i])

            if conf > min_conf:
                num_words += 1
                text = text.strip(string.punctuation).lower() # cleaning text by removing leading/trailing punctuation and setting to lowercase
                styled_text = typer.style(text, fg=typer.colors.RED, bold=True)
                # censors according to arg provided by the user
                if blur:
                    cens = img[y:y+h, x:x+w] # dimensions of the word
                    cens = cv2.GaussianBlur(cens, (23, 23), 30)
                else:
                    cens = np.full([h, w, 3], rgb) # an array full of 255s

                if cens_all:
                    img[y:y+cens.shape[0], x:x+cens.shape[1]] = cens
                    num_cens += 1
                    typer.echo(f"Censored {styled_text}")
                elif text in cens_words:
                    img[y:y+cens.shape[0], x:x+cens.shape[1]] = cens
                    num_cens += 1
                    typer.echo(f"Censored {styled_text}")
        
        cv2.imwrite(f, img)

    typer.echo("Complete!")