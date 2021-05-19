
import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)#0到2π区间100等分
y = np.sin(x) #函数sinx

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#一个FIGURE图形生成一行两列两个子图，后面一个1表示当前激活第一个子图。
plt.title(r'$f(x)=sin(x)$') #标题为$f(x)=sin(x)$
plt.plot(x, y)#展示x，y数据
#plt.show()

x1 = [t*0.375*np.pi for t in x]
y1 = np.sin(x1) #函数sinx1
plt.subplot(1,2,2)#一个FIGURE图形生成一行两列两个子图，后面一个1表示当前激活第二个子图。
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$
plt.plot(x1, y1)#展示x1，y1数据
plt.show()#显示++++++