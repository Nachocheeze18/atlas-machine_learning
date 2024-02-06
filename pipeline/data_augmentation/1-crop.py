import tensorflow as tf

def crop_image(image, size):
    """
    Performs a random crop of an image.

    Args:
        image (tf.Tensor): A 3D TensorFlow tensor containing the image to crop.
        size (tuple): A tuple containing the size of the crop in the format (height, width, channels).

    Returns:
        tf.Tensor: The cropped image.
    """
    # Extracting dimensions of the image and the crop size
    image_height, image_width, _ = image.shape
    crop_height, crop_width, _ = size

    # Calculating the maximum allowable coordinates for the top-left corner of the crop
    max_x = image_width - crop_width
    max_y = image_height - crop_height

    # Generating random coordinates for the top-left corner of the crop
    offset_x = tf.random.uniform((), maxval=max_x, dtype=tf.int32)
    offset_y = tf.random.uniform((), maxval=max_y, dtype=tf.int32)

    # Cropping the image using tf.image.crop_to_bounding_box
    cropped_image = tf.image.crop_to_bounding_box(image, offset_y, offset_x, crop_height, crop_width)

    return cropped_image
