import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_data = np.array([
    [76.17, 511.54], [80.81, 509.32], [41.73, 586.4], [581.6, 48.84],
    [440.84, 58.81], [448.54, 17.57], [640.86, 40.71], [44.5, 599.37],
    [30.09, 410.76], [66.47, 463.56], [642.99, 48.99], [26.26, 597.65],
    [43.15, 520.2], [41.07, 627.89], [407.11, 32.6], [408.17, 29.22],
    [37.67, 645.49], [21.96, 486.83], [45.63, 32.98], [32.44, 37.41],
    [43.75, 26.26], [29.5, 43.87], [32.09, 41.49], [54.91, 52.36],
    [39.6, 47.18], [40.71, 49.67], [40.69, 40.6], [42.35, 39.76],
    [53.2, 43.78], [32.09, 41.49], [70.49, 55.35], [53.32, 41.2]
           //두 프레임간 어깨-주먹 피타고라스
], dtype=np.float32)
y_data = np.array([
    [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [0, 1], [0, 1], [0, 1],
    [0, 1], [0, 1], [1, 0], [1, 0],
    [1, 0], [1, 0], [1, 0], [1, 0],
    [1, 0], [1, 0], [1, 0], [1, 0],
    [1, 0], [1, 0], [1, 0], [1, 0]
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