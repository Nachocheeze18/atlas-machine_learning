#!/usr/bin/env python3
import tensorflow as tf

def rotate_image(image):
    """rotates an image by 90 degrees counter-clockwise"""
    transposed_image = tf.transpose(image, perm=[1, 0, 2])
    rotated_image = tf.reverse(transposed_image, axis=[1])
    return rotated_image
