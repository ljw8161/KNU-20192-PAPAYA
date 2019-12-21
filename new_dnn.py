import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_data = np.array([
    [866.401, 288.412, 839.019, 317.874, 821.422, 364.88, 946.654, 472.661, 1072.1, 306.125, 1058.41, 327.672, 1054.51, 321.759, 1025.11, 523.591],
    [888.054, 288.446, 901.681, 313.972, 868.405, 339.452, 917.354, 507.857, 889.986, 288.379, 901.648, 312.018, 868.379, 339.438, 915.46, 509.819],
    [891.881, 286.523, 899.812, 313.955, 868.434, 337.53, 915.421, 507.971, 888.01, 288.378, 899.719, 312.02, 868.369, 339.433, 915.404, 507.955],
    [1197.44, 292.4, 1230.93, 319.763, 1201.51, 411.925, 1256.31, 523.552, 886.059, 268.887, 882.071, 296.31, 870.387, 380.591, 868.343, 480.561],
    [915.304, 276.711, 911.525, 304.206, 897.74, 306.094, 919.352, 509.95, 917.317, 274.889, 915.349, 304.153, 897.752, 304.136, 919.308, 509.933],
    [713.628, 288.538, 727.241, 308.135, 684.217, 327.671, 776.266, 482.473, 868.282, 302.174, 854.724, 321.847, 776.347, 319.883, 815.46, 511.846],
    [850.736, 296.319, 838.941, 321.839, 886.125, 407.991, 790.075, 505.873, 850.704, 315.924, 803.706, 337.481, 776.332, 339.469, 742.922, 494.212],
    [954.611, 272.722, 917.321, 294.396, 931.06, 335.53, 917.317, 478.443, 952.607, 270.827, 917.308, 294.395, 964.329, 364.874, 917.471, 478.443],
    [776.342, 304.138, 760.553, 317.845, 768.459, 349.25, 723.367, 468.755, 744.914, 284.565, 727.226, 300.213, 762.583, 335.595, 727.245, 476.658],
    [944.762, 261.072, 952.652, 290.38, 917.406, 339.403, 917.474, 478.498, 936.978, 259.089, 901.709, 290.378, 917.47, 335.518, 919.319, 478.458],
    [774.252, 304.222, 742.972, 306.096, 768.461, 347.264, 727.264, 474.59, 725.395, 274.843, 699.953, 300.257, 745.017, 325.734, 725.409, 476.654],
    [789.938, 270.898, 758.744, 290.556, 776.334, 319.834, 717.589, 466.769, 870.277, 304.077, 860.577, 319.827, 819.402, 272.892, 897.796, 478.586],
    [776.394, 396.233, 805.735, 427.558, 821.39, 492.205, 768.505, 586.171, 805.734, 398.112, 809.644, 427.6, 823.451, 492.248, 817.492, 564.696],
    [809.596, 396.272, 774.357, 419.784, 829.185, 492.176, 772.427, 584.266, 819.349, 392.349, 821.446, 421.695, 836.935, 484.432, 774.308, 572.596],
    [870.277, 304.077, 860.577, 319.827, 819.402, 272.892, 897.796, 478.586, 872.33, 294.387, 883.961, 333.469, 821.405, 382.571, 899.781, 478.578],
    [837.008, 382.425, 840.987, 411.875, 854.772, 470.72, 821.321, 558.912, 837.092, 380.606, 846.841, 411.876, 856.667, 470.676, 819.438, 558.833],
    [774.259, 306.185, 799.795, 323.734, 772.368, 353.157, 743.001, 458.914, 919.307, 292.386, 917.294, 319.88, 885.959, 339.449, 913.428, 490.269],
    [856.702, 364.827, 823.274, 388.429, 882.05, 447.217, 837.102, 539.208, 864.463, 366.751, 870.271, 390.346, 882.107, 447.205, 870.446, 525.495],
    [919.307, 292.386, 917.294, 319.88, 885.959, 339.449, 913.428, 490.269, 764.547, 351.241, 744.99, 341.423, 744.952, 398.202, 819.34, 458.938],
    [884.067, 355.096, 886.069, 384.434, 899.752, 443.285, 874.307, 521.574, 884.148, 353.24, 852.669, 382.455, 903.654, 435.419, 854.603, 509.955],
    [838.924, 308.122, 827.224, 335.484, 811.596, 343.366, 897.751, 509.85, 815.479, 308.104, 776.248, 337.507, 740.983, 345.298, 885.96, 507.886],
    [886.059, 268.887, 882.071, 296.31, 870.387, 380.591, 868.343, 480.561, 899.816, 272.748, 888.064, 304.106, 886.073, 382.609, 886.082, 494.143],
    [460.853, 121.936, 474.564, 137.621, 449.161, 178.849, 451.081, 225.733, 462.913, 120.041, 478.45, 135.738, 492.217, 166.992, 464.836, 227.696],
    [476.572, 120.015, 462.882, 137.646, 462.823, 178.844, 492.309, 235.603, 478.601, 120.076, 490.302, 137.686, 466.779, 178.77, 496.228, 229.708],
    [507.832, 123.908, 494.255, 145.432, 494.148, 180.731, 478.592, 225.731, 511.846, 120.035, 505.931, 139.625, 505.976, 178.786, 494.218, 225.73],
    [541.321, 122.016, 533.391, 141.565, 543.203, 178.84, 572.568, 227.746, 552.97, 123.896, 541.216, 145.434, 543.223, 180.733, 523.536, 229.801],
    [554.91, 125.893, 549.082, 143.465, 554.936, 178.84, 523.667, 227.859, 570.509, 121.983, 555.027, 139.613, 554.996, 180.684, 582.369, 231.72],
    [588.177, 180.655, 619.532, 239.5, 604.009, 123.895, 596.038, 141.59, 588.32, 180.81, 584.287, 229.764],
    [617.588, 125.9, 607.856, 147.358, 605.842, 182.687, 633.392, 241.446, 619.618, 131.654, 617.631, 147.349, 617.626, 182.664, 635.182, 241.426],
    [666.594, 131.688, 662.604, 147.385, 666.674, 186.584, 635.282, 239.474, 682.266, 131.751, 666.669, 147.461, 672.464, 188.57, 695.996, 243.391],
    [680.22, 131.763, 670.53, 147.478, 674.414, 192.487, 648.96, 243.509, 686.219, 131.706, 680.294, 147.391, 680.214, 190.504, 696.012, 243.397],
    [729.318, 133.755, 742.972, 149.367, 713.702, 194.514, 698.031, 241.412, 742.913, 133.773, 729.214, 151.371, 727.316, 196.352, 766.489, 257.189],
    [915.368, 241.444, 886.09, 259.175, 831.152, 304.108, 960.412, 398.272, 931.107, 274.774, 897.762, 288.579, 829.248, 313.989, 1015.36, 337.491],
    [1226.85, 321.769, 1262.27, 351.14, 1201.48, 319.911, 1201.45, 527.579, 1242.62, 331.585, 1230.82, 351.2, 1209.29, 343.35, 1154.49, 519.651],
    [729.3, 272.789, 758.629, 296.347, 694.024, 304.211, 803.689, 466.762, 715.629, 278.703, 695.945, 300.198, 692.054, 290.552, 762.636, 460.799],
    [1107.43, 300.273, 1150.41, 337.563, 1036.91, 349.173, 1025.13, 494.151, 839.012, 294.356, 827.278, 317.904, 886.044, 341.394, 872.395, 492.31],
    [707.763, 325.717, 727.271, 327.651, 680.294, 351.213, 713.625, 466.816, 711.73, 298.299, 744.905, 308.124, 692.024, 337.417, 715.639, 476.469],
    [784.128, 310.011, 774.347, 339.431, 682.329, 349.144, 852.743, 525.489, 727.406, 288.576, 703.792, 306.195, 695.938, 335.502, 727.274, 474.538],
    [729.389, 288.574, 696.002, 300.256, 668.64, 319.838, 743.055, 490.298, 758.618, 304.213, 760.671, 337.537, 725.306, 415.8, 760.674, 521.661],
    [772.392, 323.776, 788.021, 351.126, 827.218, 413.882, 760.689, 523.619, 713.734, 286.513, 729.404, 306.03, 703.797, 343.357, 709.725, 462.911],
    [1121.13, 321.793, 1074.19, 335.569, 1074.07, 366.786, 1132.87, 523.667, 921.341, 274.836, 915.316, 292.42, 974.166, 333.559, 905.648, 425.62],
    [921.341, 274.836, 915.316, 292.42, 974.166, 333.559, 905.648, 425.62, 1087.72, 319.868, 1072.11, 339.486, 1042.76, 323.791, 1168.14, 509.878]

], dtype=np.float32)
y_data = np.array([
    [0, 1],
    [1, 0],
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1],
    [0, 1],
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1],
    [0, 1],
    [1, 0],
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1],
    [1, 0],
    [0, 1],
    [0, 1]
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1],
    [0, 1]
], dtype=np.float32)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_uniform([16, 20], -1., 1.))
W2 = tf.Variable(tf.random_uniform([20, 2], -1., 1.))

b1 = tf.Variable(tf.zeros([20]))
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