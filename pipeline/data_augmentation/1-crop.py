#!/usr/bin/env python3
import tensorflow as tf

def crop_image(image, size):
    """Performs a random crop of an image."""
    image_height, image_width, _ = image.shape
    crop_height, crop_width, _ = size
    max_x = image_width - crop_width
    max_y = image_height - crop_height
    offset_x = tf.random.uniform((), maxval=max_x, dtype=tf.int32)
    offset_y = tf.random.uniform((), maxval=max_y, dtype=tf.int32)
    cropped_image = tf.image.crop_to_bounding_box(image, offset_y, offset_x, crop_height, crop_width)

    return cropped_image
