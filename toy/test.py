###   https://github.com/yongyehuang/Tensorflow-Tutorial


from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import warnings
warnings.filterwarnings('ignore')  # 不打印 warning 

import numpy as np
import tensorflow as tf

# 设置按需使用GPU
config = tf.ConfigProto()
#config.gpu_options.allow_growth = False
sess = tf.Session(config=config)

# 用tensorflow 导入数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('../data/MNIST_data', one_hot=False, source_url='http://yann.lecun.com/exdb/mnist/')

print('training data shape ', mnist.train.images.shape)
print('training label shape ', mnist.train.labels.shape)

# 权值初始化
def weight_variable(shape):
    # 用正态分布来初始化权值
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    # 本例中用relu激活函数，所以用一个很小的正偏置较好
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


# input_layer
X_input = tf.placeholder(tf.float32, [None, 784])
y_input = tf.placeholder(tf.int64, [None])  # 不使用 one-hot 

# FC1
W_fc1 = weight_variable([784, 1024])
b_fc1 = bias_variable([1024])
h_fc1 = tf.nn.relu(tf.matmul(X_input, W_fc1) + b_fc1)

# FC2
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
# y_pre = tf.nn.softmax(tf.matmul(h_fc1, W_fc2) + b_fc2)
logits = tf.matmul(h_fc1, W_fc2) + b_fc2

print(logits)

# 1.损失函数：cross_entropy
# 如果label是 one-hot 的话要换一下损失函数，参考：https://blog.csdn.net/tz_zs/article/details/76086457
cross_entropy = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y_input, logits=logits)) 
# 2.优化函数：AdamOptimizer, 优化速度要比 GradientOptimizer 快很多
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 3.预测结果评估
#　预测值中最大值（１）即分类结果，是否等于原始标签中的（１）的位置。argmax()取最大值所在的下标
correct_prediction = tf.equal(tf.argmax(logits, 1), y_input)  
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 开始运行
sess.run(tf.global_variables_initializer())
# 这大概迭代了不到 10 个 epoch， 训练准确率已经达到了0.98
for i in range(5000):
    X_batch, y_batch = mnist.train.next_batch(batch_size=100)
    cost, acc,  _ = sess.run([cross_entropy, accuracy, train_step], feed_dict={X_input: X_batch, y_input: y_batch})
    if (i+1) % 500 == 0:
        test_cost, test_acc = sess.run([cross_entropy, accuracy], feed_dict={X_input: mnist.test.images, y_input: mnist.test.labels})
        print("step {}, train cost={:.6f}, acc={:.6f}; test cost={:.6f}, acc={:.6f}".format(i+1, cost, acc, test_cost, test_acc))