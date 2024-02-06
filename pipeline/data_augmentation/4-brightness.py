#!/usr/bin/env python3
import tensorflow as tf

def change_brightness(image, max_delta):
    """randomly changes the brightness of an image"""
    delta = tf.random.uniform([], -max_delta, max_delta)
    adjusted_image = tf.image.adjust_brightness(image, delta)
    
    return adjusted_image
