import tensorflow as tf
from tensorflow.image import transform

def shear_image(image, intensity):
    # Randomly generate shearing angles
    shear_x = tf.random.uniform([], -intensity, intensity)
    shear_y = tf.random.uniform([], -intensity, intensity)
    
    # Define transformation matrix for shearing
    transform_matrix = tf.convert_to_tensor([[1.0, shear_x, 0.0],
                                             [shear_y, 1.0, 0.0]])

    # Apply affine transformation to the image
    sheared_image = transform(image, transform_matrix)

    return sheared_image
