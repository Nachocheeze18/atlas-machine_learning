import tensorflow as tf

def change_brightness(image, max_delta):
    # Generate a random brightness factor within the specified range
    delta = tf.random.uniform([], -max_delta, max_delta)
    
    # Apply brightness adjustment
    adjusted_image = tf.image.adjust_brightness(image, delta)
    
    return adjusted_image
