import tensorflow as tf
import numpy as np
def add_layer(layoutname,inputs,in_size,out_size,activatuib_funaction=None,):
    with tf.name_scope(layoutname):
        with tf.name_scope('weights'):
            Weights=tf.Variable(tf.random_normal([in_size,out_size]),name='W')
        with tf.name_scope('biases'):
            biases=tf.Variable(tf.zeros([1,out_size])+0.1,name='b')
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b=tf.add(tf.matmul(inputs,Weights),biases)

        if activatuib_funaction is None:
            outputs=Wx_plus_b
        else :
            outputs=activatuib_funaction(Wx_plus_b)
        return outputs
x_data=np.linspace(-1,1,300)[:,np.newaxis]
noise=np.random.normal(0,0.09,x_data.shape)
y_data=np.square(x_data)-0.05+noise
with tf.name_scope('inputs'):
    xs=tf.placeholder(tf.float32,[None,1],name="x_in")
    ys=tf.placeholder(tf.float32,[None,1],name="y_in")
l1=add_layer("first_layer",xs,1,10,activatuib_funaction=tf.nn.relu)
prediction =add_layer('second_layout',l1,10,1,activatuib_funaction=None)
with tf.name_scope('loss'):
    loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
with tf.name_scope('train'):
    train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.global_variables_initializer()

with tf.Session() as sess:
    writer=tf.summary.FileWriter("logs/",sess.graph)
    sess.run(init)

#作者：Jcme丶Ls
#链接：https://www.jianshu.com/p/b0a29c3f8c33
#來源：简书
#简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。