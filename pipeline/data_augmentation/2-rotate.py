import tensorflow as tf

def rotate_image(image):
    # Transpose the image tensor
    transposed_image = tf.transpose(image, perm=[1, 0, 2])
    # Reverse the rows of the transposed image tensor
    rotated_image = tf.reverse(transposed_image, axis=[1])
    return rotated_image
