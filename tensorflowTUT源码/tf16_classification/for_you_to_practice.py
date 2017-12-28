 

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
# number 1 to 10 data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

def add_layer(inputs, in_size, out_size, activation_function=None, ):
    # add one more layer and return the output of this layer
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, )
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b, )
    return outputs

def  compute_accuracy(v_xs, v_ys):
    global prediction

    y_pre = sess.run(prediction,feed_dict={xs:v_xs}) #这是预测的结果

    correct_prediction=tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result = sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result



# define placeholder for inputs to network
xs = tf.placeholder(tf.float32,shape=[None,784])
ys = tf.placeholder(tf.float32,shape=[None,10])

# add output layer
prediction = add_layer(xs,784,10,activation_function=tf.nn.softmax())

# the error between prediction and real data 这是关键的
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),reduction_indices=[1]))


train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)



sess = tf.Session()
# important step
sess.run(tf.initialize_all_variables())

for i in range(1000):
    x_batch,y_batch = mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={xs:x_batch,ys:y_batch}) #模型的训练是不需要返回结果的

    if i % 50 == 0:

        print(compute_accuracy(
            mnist.test.images, mnist.test.labels))



'''
深度学习思路：
1.构建深度学习网络 add_layer
2.然后对这些，prediction 求出对数损失函数
3.对损失函数使用梯度下降 train_step

4.启动sess.run(init) 运行上面我们构建的这些架构，进行初始化
5.书写for循环进行训练  我们可以选择训练很多次 
    for xxx：
        batch_xs, batch_ys = mnist.train.next_batch(100)
        每次使用
        sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys}) #这是训练
        compute_accuracy() 这是predict 外层循环训练次数到达50次的时候我们就进行

'''





