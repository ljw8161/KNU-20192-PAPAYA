import tensorflow as tf
import numpy as np

x_data = np.array([[5.38], [5.85], [7.73], [18.2], [5.85], [5.34], [7.72], [18.08], [3.90], [1.87], [1.25], [1.43], [2.05], [16.30], [2.08], [1.43], [9.58], [3.87], [1.11], [0.91], [0.76], [1.03], [1.16], [0.94], [1.17], [1.01], [1.05], [0.85], [0.76], [0.61], [0.99], [1.21], [0.85], [0.99], [1.26], [1.31], [1.25], [1.16]], dtype=np.float32)
y_data = np.array([[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]], dtype=np.float32)

X = tf.placeholder(tf.float32, [None, 1], name='x-input')
Y = tf.placeholder(tf.float32, [None, 1], name='y-input')

W = tf.Variable(tf.random_normal([1,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 - hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    # Initialize TensorFlow variables
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        sess.run(train, feed_dict={X: x_data, Y: y_data})
        
        if step % 100 == 0:
            print(step, sess.run(cost, feed_dict={X: x_data, Y: y_data}), sess.run(W))

    # Accuracy report
    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)