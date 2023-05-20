""" Module docstring"""

from flask import Flask, request
import tensorflow as tf

app = Flask("Image classifier")
resnet = tf.keras.applications.ResNet101()


if __name__ == "__main__":
    app.run(port=1675)
    input()
