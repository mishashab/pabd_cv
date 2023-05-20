""" Module docstring"""

from flask import Flask, request
import tensorflow as tf

app = Flask("Image classifier")
resnet = tf.keras.applications.ResNet101()

with open('../data/imgnet_cats_ru.txt', encoding='utf-8') as f:
    cats = f.readlines()

cats_ru = [s.rstrip() for s in cats]


@app.route("/")
def home():
    """function docstring"""
    return "Home page"


if __name__ == "__main__":
    app.run(port=1675)
    input()
