import tensorflow as tf
print("hello")
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))