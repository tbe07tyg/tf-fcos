import tensorflow as tf
from tensorflow.keras.layers import Layer, InputSpec


class ScaleLayer(Layer):

    def __init__(self, init_value=1.0, **kwargs):
        super(ScaleLayer, self).__init__(**kwargs)
        self.init_value = init_value

    def build(self, input_shape):
        shape = [1] * len(input_shape)
        self.scale = self.add_weight(
            shape=shape,
            initializer=tf.keras.initializers.Constant(self.init_value),
            name='scale')

    def call(self, inputs):
        outputs = self.scale * inputs
        return outputs

