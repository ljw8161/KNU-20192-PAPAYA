import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_data = np.array([
    [-76.453, -447.421], [-105.868, -565.096], [-73.156, -565.096], [-31.25, -565.096],
    [-27.448, -107.012], [-57.366, -107.0127], [-123.945, -155.269], [-108.32, -155.269],
    [-74.303, -152.6431], [-9.132,	-148.8228], [-65.242, -135.668], [-125.23, -178.7888],
    [-11.704, -112.1245], [-40.403, -156.5552], [69.134, -148.811], [222.33, -95.2559],
    [-129.208, -122.652], [-135.659, -122.652], [-164.4233, -182.69], [-170.894, -155.254],
    [-138.314, -105.6955], [-147.46, -152.726], [-80.8207, -93.871], [-178.779, -168.329],
    [-75.7686, -88.7266], [-168.427, -169.697], [-126.609, -133.084], [-178.7337, -152.6774],
    [-146.1274, -110.9347], [-142.177, -87.3863], [-155.263, -153.989], [-148.6936, -180.0173],
    [-157.915, -134.4031], [-139.676, -138.341], [-134.3762, -169.719], [-113.559, -148.735],
    [-83.5149, -104.4039], [-152.692, -177.436]
], dtype=np.float32)
y_data = np.array([
    [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [0, 1], [1, 0], [1, 0],
    [1, 0], [1, 0], [1, 0], [1, 0],
    [1, 0], [1, 0], [1, 0], [1, 0],
    [1, 0], [1, 0], [1, 0], [1, 0],
    [1, 0], [1, 0], [1, 0], [1, 0], [1, 0], [1, 0]
], dtype=np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_uniform([2, 10], -1., 1.))
W2 = tf.Variable(tf.random_uniform([10, 2], -1., 1.))

b1 = tf.Variable(tf.zeros([10]))
b2 = tf.Variable(tf.zeros([2]))

L1 = tf.add(tf.matmul(X, W1), b1)
L1 = tf.nn.relu(L1)

model = tf.add(tf.matmul(L1, W2), b2)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=model))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_op = optimizer.minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(1000):
    sess.run(train_op, feed_dict={X: x_data, Y: y_data})
    if (step + 1) % 100 == 0:
        print(step + 1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))

prediction = tf.argmax(model, 1)
target = tf.argmax(Y, 1)
print('predicted :', sess.run(prediction, feed_dict={X: x_data}))
print('realtime :', sess.run(target, feed_dict={Y: y_data}))

is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('accuracy: ', sess.run(accuracy * 100, feed_dict={X: x_data, Y: y_data}))
