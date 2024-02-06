import tensorflow as tf

def flip_image(image):
    """Flip the image horizontally"""
    flipped_image = tf.image.flip_left_right(image)
    return flipped_image
