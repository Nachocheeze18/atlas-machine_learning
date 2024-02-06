#!/usr/bin/env python3
import tensorflow as tf

def change_hue(image, delta):
    """changes the hue of an image"""
    image_float = tf.image.convert_image_dtype(image, tf.float32)

    hsv_image = tf.image.rgb_to_hsv(image_float)

    hue, saturation, value = tf.split(hsv_image, 3, axis=-1)

    hue = (hue + delta) % 1.0

    hsv_image = tf.concat([hue, saturation, value], axis=-1)

    rgb_image = tf.image.hsv_to_rgb(hsv_image)

    rgb_image = tf.image.convert_image_dtype(rgb_image, tf.uint8)

    return rgb_image
