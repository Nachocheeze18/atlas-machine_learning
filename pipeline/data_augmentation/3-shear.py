#!/usr/bin/env python3
import tensorflow as tf
from tensorflow.image import transform

def shear_image(image, intensity):
    """randomly shears an image"""
    shear_x = tf.random.uniform([], -intensity, intensity)
    shear_y = tf.random.uniform([], -intensity, intensity)
    transform_matrix = tf.convert_to_tensor([[1.0, shear_x, 0.0],
                                             [shear_y, 1.0, 0.0]])
    sheared_image = transform(image, transform_matrix)

    return sheared_image
