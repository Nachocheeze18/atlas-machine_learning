import tensorflow as tf

def change_hue(image, delta):
    # Convert image to float32
    image_float = tf.image.convert_image_dtype(image, tf.float32)

    # Convert image to HSV color space
    hsv_image = tf.image.rgb_to_hsv(image_float)

    # Extract hue, saturation, and value channels
    hue, saturation, value = tf.split(hsv_image, 3, axis=-1)

    # Adjust hue
    hue = (hue + delta) % 1.0

    # Merge the channels back together
    hsv_image = tf.concat([hue, saturation, value], axis=-1)

    # Convert back to RGB color space
    rgb_image = tf.image.hsv_to_rgb(hsv_image)

    # Convert back to the original data type
    rgb_image = tf.image.convert_image_dtype(rgb_image, tf.uint8)

    return rgb_image
