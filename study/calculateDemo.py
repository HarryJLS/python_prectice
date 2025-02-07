import numpy as np
import matplotlib.pyplot as plt

x = np.array([4,3,3,4,2,2,0,1,2,5,1,2,5,1,3])
y = np.array([8,6,6,7,4,4,2,4,5,9,3,4,8,3,6])
# 获取样本的数量
m = len(x)
# x增加一列1
x = np.c_[np.ones([m, 1]), x]
print(x.shape)
#为了后续的维度对应，y也做维度变化
y = y.reshape(15, 1)
print(y.shape)

#theta的值是随机获取
theta = np.zeros([2,1])
print(theta)

#超参数alpha 学习率 步长
alpha = 0.01
#迭代次数
m_iter = 1000
#定义一个数组，存储所有的代价数据
cost = np.zeros(m_iter)
for i in range(m_iter):
    y_hat = x.dot(theta)#求预测值
    error = y_hat - y#求误差值
    cost_val = 1/(2*m) * error.T.dot(error)#求代价值
    cost[i] = cost_val#记录代价值
    delta_theta = 1 / m * x.T.dot(error)#求导数
    theta = theta - alpha*delta_theta#更新参数
print(theta)

#使用图形进行演示
plt.scatter(x[:,1], y, c='blue')
plt.plot(x[:,1], x.dot(theta), c='r-')
plt.show()

#代价值展示
plt.plot(cost)
plt.show()






#
# if __name__ == '__main__':