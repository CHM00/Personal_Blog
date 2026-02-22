# AI面试手撕

## RMSNorm归一化

RMSNorm归一化：**目前大模型采用的归一化方法，相比LayerNorm，省略了均值和方差的计算**，提高了计算效率，也没有偏差。 
$$
y = \gamma \cdot \frac{x}{\sqrt{\frac{1}{n}\sum^{n}_{i=1}x^2 + \epsilon}}
$$

```python
import torch

class RMS_Norm(torch.nn.Module):
    def __init__(self, dim:int, eps:float=1e-5):
        super().__init__()
        self.eps = eps
        self.weight = torch.nn.Parameter(torch.ones(dim))


    def _norm(self, x):
# torch.rsqrt()是计算平方根的倒数, x.pow(2)是针对输入的每一个元素平方, mean(-1,keepdim=True)对最后一维求均值相当于计算每个特征向量的 RMS（均方根），因为[batch_size, seq_len, hidden_dim]→ 最后一维是hidden_dim，实际上也是embedding的维度
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)

    def forward(self, x):
        return self.weight * self._norm(x.float()).type_as(x)
```



## 对输入的英文句子进行简单的词频统计（东方通信公司）

python的输入函数`input()`, 括号中的文字是提示语，可以省略；**但是无论在控制台输入数字、字母，都会以字符串的形式输入；**

类型转换：把输入的字符串变成想要的输入；可以使用强制类型转换：`int(), float()`; 可以考虑使用`try-except`捕获异常，友好提示用户；

 map() 会根据提供的函数对指定序列做映射。第一个参数是函数，第二参数是可迭代对象，可以针对可迭代对象调用函数

`a,b = map(int, input().split())`, `list1 = list(map(int, input().split()))`

```python
'''
    使用python编写一个函数，实现对输入的英文句子进行简单的词频统计（忽略大小写，忽略标点符号），返回次数最多的前3个单词及其出现次数
'''

import re
from collections import Counter

def word_frequency(sentence):
    '''
    对输入的英文句子进行简单的词频统计（忽略大小写，忽略标点符号），返回次数最多的前3个单词及其出现次数
    :param sentence: 输入的英文句子
    :return: 次数最多的前3个单词及其出现次数
    '''
    # 全部转换为小写字母
    sentence = sentence.lower()
    # 正则表达式去掉无关字符，比如标点符号,re.sub()函数的用法，用于替换字符串中匹配正则模式的子串; 根据正则表达式匹配目标字符串中的子串，并用指定内容替换这些子串
    # \w 表示匹配任意的字母，数字以及下划线，等价于[a-zA-Z0-9_], \s表示匹配所有空白符,包括空格、制表符、换行符等
    sentence= re.sub(r"[^\w\s]"," ", sentence)

    # 按照空格分割字符串
    # word = sentence.split(' ')  # 这里只使用空格字符作为分隔符，而不是空白符，不能分割制表符等，而且当有连续多个空格时，会产生空字符串元素
    word = sentence.split()
    print(word)
    # 统计单词出现的次数,collection库中Counter用于计数，其中的most_common()方法用于返回counter中n个最大数目的元素，返回一个列表，每个元素是一个元组，元组的第一个元素是单词，第二个元素是出现次数
    word = Counter(word).most_common(3)
    print(word)
    for w in word:
        print(w[0], w[1])

if __name__ == '__main__':
    sentence = input("请输入字符串: ").strip()
    print(sentence)
    word_frequency(sentence)
```



## ==带掩码的多头自注意力机制==

思想：多头是通过分割实现的，把`[batch_size, seq_len, hidden_size]` 通过`torch.view()`拆分开的，形成`[batch_size, seq_len, num_heads, hidden_dim]`, 这是可以交换，为后续的attention_score打基础，其中`permute(0, 2, 1, 3)`以及`transpose(1,2)`交换；计算完成分数之后需要拼接



```python
import torch
import numpy as np

class MaskMultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, heads: int, hidden_size: int):
        super().__init__()
        self.heads = heads
        self.hidden_size = hidden_size
        self.hidden_dim = hidden_size // heads  # // 表示地板除，先除后取整, / 表示除法, 不管是不是整数，最后都是float类型
        assert hidden_size == heads * self.hidden_dim

    def _softmax(self, x):
        # 为什么要减去最大值? 为了数值的稳定，因为指数运算可能会超所inf, 减去最大值之后，所有值小于0，确保exp(x)在0-1之间
        # torch.max(x, dim=-1, keepdim=True)[0] 表示在最后一个维度上取最大值, 并保持维度不变
        # np.max(x, dim=-1, keepdim=True) 表示在最后一个维度上取最大值, 并保持维度不变
        # 两者的不同地方在于torch.max()返回的是（最大值，索引）, np.max()返回的是最大值
        expx = torch.exp(x- torch.max(x, dim=-1, keepdim=True)[0])
        return expx / torch.sum(expx, dim=-1, keepdim=True)  # 针对K进行softmax

    def forward(self, Q, K, V, mask, W):
        batch_size, seq_len, _ = Q.shape
        Q = torch.tensor(Q, dtype=torch.float32)
        K = torch.tensor(K, dtype=torch.float32)
        V = torch.tensor(V, dtype=torch.float32)
        W = torch.tensor(W, dtype=torch.float32)
        mask =torch.tensor(mask, dtype=torch.bool)

        Q = Q.view(batch_size, seq_len, self.heads, self.hidden_dim)
        K = K.view(batch_size, seq_len, self.heads, self.hidden_dim)
        V = V.view(batch_size, seq_len, self.heads, self.hidden_dim)

        attention_score = torch.matmul(Q, K.transpose(2, 3)) / torch.sqrt(torch.tensor(self.hidden_dim))

        # 掩码操作
        attention_score = attention_score.masked_fill(mask == True, float("-inf"))
        attention_score = self._softmax(attention_score)

        # 上下文向量
        output = torch.matmul(attention_score, V)
        output = output.permute(0, 2, 1, 3)
        # 将多头注意力的输出重塑回原始形状
        output = output.contiguous()  # 确保内存的连续性
        output = output.view(batch_size, seq_len, self.hidden_size)  # 重塑张量形状，reshape和view都是可以的
        output = torch.matmul(output, W)
        return output


# 输入参数
# input = input().split(";")
example_input = (
        "2",
        "[[[1.0,2.0],[3.0,4.0]],[[5.0,6.0],[7.0,8.0]]]",
        "[[[1.0,1.0],[1.0,1.0]],[[1.0,1.0],[1.0,1.0]]]",
        "[[[0.5,0.5],[0.5,0.5]],[[0.5,0.5],[0.5,0.5]]]",
        "[[1.0,0.0],[0.0,1.0]]"
    )
input = example_input
num_heads = int(input[0])

# eval能够处理任意深度的嵌套结构
Q = np.array(eval(input[1].strip()))
K = np.array(eval(input[2].strip()))
V = np.array(eval(input[3].strip()))
W_o = np.array(eval(input[4].strip()))

batch_size, seq_len, hidden_size = Q.shape
# np.ones(seq_len, seq_len)是全1矩阵
# np.triu(matrix, k=1)保留主对角线上方（k=1）的元素, k=0会包含对角线
# astype(bool), 转换为bool类型
mask = np.triu(np.ones((seq_len, seq_len)), k=1).astype(bool)
print(mask)
mask = np.broadcast_to(mask, (batch_size, num_heads, seq_len, seq_len))
print(mask)
# @在numpy中等于np.matmul(), 表示矩阵乘法; 在torch中等于torch.matmul(), 表示矩阵的乘积
mask_attention = MaskMultiHeadSelfAttention(num_heads, hidden_size)
output = mask_attention(Q, K, V, mask=mask, W=torch.tensor(W_o))
print(output)

```



## 带KV Cache的掩码自注意力机制

题目：支持缓存已计算过的**Key**和**Value**张量，处理超过缓存容量的溢出逻辑

实现：在自回归逻辑中，KV Cache的正确行为是：

​	① 首次调用：缓存为空，处理整个初始序列

​	② 后续调用：每次只处理一个新的token，使用缓存的历史KV，只沿着序列维度拼接，即增加**$seq\_len$**

注意：**为什么要掩码矩阵，主要是对注意力分数做掩码操作**，因此最后是`attention_score..masked_fill(mask==0, float(’-inf‘))`



```python
import torch
import math

class KVCacheAttention(torch.nn.Module):
    def __init__(self, d_model, n_heads, seq_len_max, use_cache=True):
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_head = d_model // n_heads

        # 线性变化
        self.query = torch.nn.Linear(d_model, d_model)
        self.key = torch.nn.Linear(d_model, d_model)
        self.value = torch.nn.Linear(d_model, d_model)
        self.out = torch.nn.Linear(d_model, d_model)

        # KV Cache中的最大长度
        self.max_seq_len = seq_len_max

        self.Cache_K = None
        self.Cache_V = None

        self.use_cache = use_cache

    def softmax(self, x):
        expx = torch.exp(x)
        return expx / torch.sum(expx, dim=-1, keepdim=True)

    def get_cache_size(self):
        """获取当前缓存大小"""
        if self.Cache_K is None:
            return 0
        return self.Cache_K.size(1)  # 序列长度维度

    def clear_cache(self):
        """清空KV缓存"""
        self.Cache_K = None
        self.Cache_V = None
        # self.max_seq_len = 0

    def forward(self, x, mask=False):
        batch, seq_len, _ = x.shape

        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)

        if self.use_cache and self.Cache_K is not None:
            K = torch.cat([self.Cache_K, K], dim=1)
            V = torch.cat([self.Cache_V, V], dim=1)

            # 缓存截断
            if self.max_seq_len < K.shape[1]:
                K = K[:, -self.max_seq_len:]
                V = V[:, -self.max_seq_len:]

            # 更新缓存
            self.Cache_K = K
            self.Cache_V = V

        else:
            self.Cache_K = K
            self.Cache_V = V

        Q = Q.view(batch, seq_len, self.n_heads, self.d_head).permute(0, 2, 1, 3)
        K = K.view(batch, -1, self.n_heads, self.d_head).permute(0, 2, 1, 3)
        V = V.view(batch, -1, self.n_heads, self.d_head).permute(0, 2, 1, 3)

        # 注意力分数  (batch, heads, seq_len, total_len)
        attention_score = torch.matmul(Q, K.transpose(2, 3)) / math.sqrt(self.d_model)

        # 掩码矩阵
        if mask:
            total_len = attention_score.shape[-1]
            mask_matrix = torch.tril(torch.ones(seq_len, total_len))
            mask_matrix = mask_matrix.view(1, 1, seq_len, total_len)
            # mask_matrix = mask_matrix.masked_fill(mask_matrix==0, float('-inf'))
            attention_score = attention_score.masked_fill(mask_matrix == 0, float('-inf'))

        # 掩码之后进行softmax计算 (batch, heads, seq_len, total_len)
        attention_score = self.softmax(attention_score)

        # 计算输出 V=(batch, heads, total_len, self.d_head)  output=(batch, seq_len, self.d_model)
        output = torch.matmul(attention_score, V)
        output = output.permute(0, 2, 1, 3).contiguous().view(batch, seq_len, self.d_model)
        output = self.out(output)
        return output


if __name__ =='__main__':
    x = torch.randn(32, 54, 768)
    d_model = 768
    heads = 8
    seq_len_max = 6
    kv_cache_attention = KVCacheAttention(d_model, heads, seq_len_max)

    # 第一次调用时，mask为True，会初始化KVCache
    output = kv_cache_attention(x, mask=True)
    print(f"输入形状: {x.shape}")
    print(f"输出形状: {output.shape}")
    print(f"缓存大小: {kv_cache_attention.get_cache_size()}")

    # 第二次调用时，mask为True，会使用KVCache
    x2 = torch.randn(32, 1, 768)
    output = kv_cache_attention(x2, mask=True)
    print(f"输入形状: {x2.shape}")
    print(f"输出形状: {output.shape}")
    print(f"缓存大小: {kv_cache_attention.get_cache_size()}")


    print("\n=== 测试缓存溢出处理 ===")
    # 模拟多次推理，测试缓存溢出
    kv_cache_attention.clear_cache()
    print(f"缓存大小: {kv_cache_attention.get_cache_size()}")
    for i in range(seq_len_max + 10):  # 超过最大长度
        x_step = torch.randn(32, 1, d_model)
        output_step = kv_cache_attention(x_step, mask=True)
        if (i + 1) % 1 == 0:
            print(f"步数 {i + 1}: 缓存大小 = {kv_cache_attention.get_cache_size()}")

```



## K-Means

**K-MEANS**算法是一种**基于欧式距离的聚类算法**, 其基本思想是**将数据点分为K个簇**,  每个簇的中心是该簇中所有数据点的均值。
算法步骤:
1、选择初始化的K个样本作为初始聚类中心
2、针对数据集中的每个样本xi, 计算它到k个聚类中心的距离, 并将其分到距离最小的聚类中心所对应的类中
3、针对每个类别a_i, 重新计算它的聚类中心a_i,即属于该类的所有样本的质心，**也就是均值**
4、重复上面的2，3步骤，直到达到某个中止条件(迭代次数、最小误差变化等)

重点：

（1）如何随机选择初始的K个样本：**np.random.choice(X.shape[0], self.k, replace=False)**, 从索引$0->X.shape[0]-1$中随机选取self.k个样本，返回选择的索引，生成最新的质心

（2）为每个点分配给最近的聚类中心，因此要初始化k个空聚类中心

（3）计算每个特征与中间特征的距离，使用np.linalg.norm()去计算**两个特征之间的欧式距离** , 然后使用**np.argmin()**函数找到其中距离最小的索引，即使它所属的聚类中心， 并将其加入到聚类中心

（4）计算新的聚类中心, **对这个类别中的所有样本计算均值**作为新的聚类中心，利用np.mean(cluster, axis=0);沿着行的方向（对每个特征维度计算均值）

（5）判断是否小于最小误差变化，如果小于的话，说明两次聚类结果相差不大，到达收敛条件。

```python
# 实现K-MEANS算法, 基于欧式距离的聚类算法
'''
    K-MEANS算法是一种基于欧式距离的聚类算法, 其基本思想是将数据点分为K个簇, 每个簇的中心是该簇中所有数据点的均值。
    算法步骤:
    1、选择初始化的K个样本作为初始聚类中心
    2、针对数据集中的每个样本xi, 计算它到k个聚类中心的距离, 并将其分到距离最小的聚类中心所对应的类中
    3、针对每个类别a_i, 重新计算它的聚类中心a_i,即属于该类的所有样本的质心，也就是均值
    4、重复上面的2，3步骤，直到达到某个中止条件(迭代次数、最小误差变化等)
'''

import numpy as np

class KMeans:
    def __init__(self, k:int, max_iters:int, atol:float=1e-4):
        self.k = k
        self.max_iters = max_iters
        self.atol = atol

    # 训练拟合过程
    def fit(self, X):
        if self.k > X.shape[0]:
            self.k = X.shape[0]
            print(f"k值大于样本数量, 已将k值调整为{self.k}")
        # 随机选择k个样本作为初始化聚类中心
        indices = np.random.choice(X.shape[0], self.k, replace=False) # 从0到X.shape[0]-1的索引范围中随机选取self.k个不重复的索引（replace=False）, 结果indices是一个包含K个随机索引的数组
        # 使用这些随机索引从数组中选取初始的聚类中心样本
        centroids = X[indices]

        # 为每个点分配给最近的聚类中心
        for _ in range(self.max_iters):
            # 提供多个类别
            clusters = [[] for _ in range(self.k)]
            for feature in X:
                # 单个点与单个中心的距离
                distance = [np.linalg.norm(feature - centroid) for centroid in centroids]  # 用于计算特征向量与聚类中心之间的欧式距离, np.linalg.norm()用于计算向量的范数，默认是L2范数，先平方后开根号
                # 等价于：np.sqrt(np.sum((a-b)**2))
                # 找到最近的聚类中心
                close_cluster = np.argmin(distance)  # 返回距离最小的索引, 即所属的聚类中心
                clusters[close_cluster].append(feature)  # 将该点加入到最近的聚类中心所属的类别中
            # 计算新的质点, np.mean()用于计算计算每个类别的均值，对当前簇中所有数据点计算均值, axis=0表示对列进行计算（沿着行的方向）, 即对每个特征维度计算均值
            new_centroids = []
            for i, cluster in enumerate(clusters):
                if len(cluster) > 0:
                    new_centroids.append(np.mean(cluster, axis=0))
                else:
                    new_centroids.append(X[np.random.randint(0, X.shape[0])])
            # new_centroids = np.array([np.mean(cluster, axis=0) for cluster in clusters if cluster])

            # 检查质心是否变化, np.allclose(a, b, atol=tolerance)函数, 比较两个数组是否在指定容差范围内近似相等
            if np.allclose(centroids, new_centroids, atol=self.atol):
                break
            centroids = new_centroids
        self.centroids = centroids

    # 预测新数据点所属的聚类中心
    def predict(self, X):
        y_pred = [np.argmin([np.linalg.norm(centroid - x) for centroid in self.centroids]) for x in X]
        return np.array(y_pred)


def test_new_data_prediction():
    # 训练数据
    train_data = np.array([[1, 2], [1, 4], [4, 1], [4, 3]])

    # 新数据
    new_data = np.array([[0, 0], [5, 5], [2, 3]])

    kmeans = KMeans(k=2, max_iters=5)
    kmeans.fit(train_data)
    labels = kmeans.predict(new_data)

    # 验证预测结果合理性
    assert len(labels) == len(new_data)
    assert set(labels).issubset({0, 1})  # 标签应在0和1之间

test_new_data_prediction()

```



## KNN (K-Nearest Neighbors) k-近邻算法，是一个分类算法

KNN是监督学习算法，首先需要给定一组n维特征的数据点和对应的类别标签，使用KNN对新样本进行分类。对于一个新样本，计算它与所有训练样本的距离，选出最近的K个邻居，看这K个邻居中哪个类别最多，预测为哪个类别。一般使用欧式距离做度量。

KNN中使用到了torch中的几个函数，torch.bicount()函数，用于统计每个元素出现的次数，它的索引值就是标签值，它的torch.argmax()函数返回最大值对应的索引值；torch.argsort()函数是对张量进行排序，默认是升序排列；

这里使用的torch方法

```python
import torch
import numpy as np
class KNN:
    def __init__(self, k):
        self.k = k
        self.X = None
        self.y = None

    def train(self, X, y):
        self.X = X
        self.y = y

    def predict(self, T):
        # 计算每个点到所有点的距离
        y_preds = []
        for t in T:
            # 计算每个特征所属类别
            print(self.X)
            print(self.y)
            print(torch.sum((self.X - t)**2, dim=1))
            print(torch.sum((self.X - t)**2, dim=0))

            distance = torch.sqrt(torch.sum((self.X - t)**2, dim=1))
            print(distance)
            # 查找每个特征的最近的3个点, 默认是升序排列
            k_nearest_indices = torch.argsort(distance)[:self.k]
            print(k_nearest_indices)
            # 获取每个的标签
            k_nearest_labels = self.y[k_nearest_indices]
            print(k_nearest_labels)

            # 计数,找到里面最大的
            output = torch.bincount(k_nearest_labels)
            print(torch.bincount(k_nearest_labels))
            print(output)
            print(output.argmax())
            # torch.bicount()函数是专门用于统计非负整数出现频率的函数, 它的核心逻辑是输入一个1维的非负整数张量, 输出是一维的张量,其中它的索引就是它的标签,索引位置对应的值就是该标签出现的次数。
            # torch.argmax()函数用于找到张量中最大值所在索引,返回最大值所在索引;
            y_pred = torch.bincount(k_nearest_labels).argmax()
            print(y_pred)
            y_preds.append(y_pred.item())  # item()是将单个元素的张量转换为python原生的标量值;

        return y_preds
def test_knn_basic():
    """基础功能测试"""
    # X = torch.tensor([[1.0, 0], [2.0, 0], [3.0, 0], [4.0, 0]])
    X = torch.tensor([[2.0, 0], [1.0, 0], [3.0, 0], [4.0, 0]])
    y = torch.tensor([2, 2, 3, 3])
    knn = KNN(k=3)
    knn.train(X, y)
    y_pred = knn.predict(torch.tensor([[1.1, 0]]))
    print(y_pred)

if __name__ == '__main__':
    test_knn_basic()
```

**numpy方法**

使用numpy的方法利用collections中的Counter计数，并使用most_common返回出现次数最多的元素，返回的是一个列表，列表中是元组；

```python
import numpy as np
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for x in X_test:
            # 计算每个测试点到所有训练点的欧氏距离
            distances = np.sqrt(np.sum((self.X_train - x) ** 2, axis=1))
            # 找到距离最小的 k 个索引
            nearest_indices = np.argsort(distances)[:self.k]
            # 获取这 k 个邻居的标签
            nearest_labels = self.y_train[nearest_indices]
            # 投票决定最终类别
            print(Counter(nearest_labels).most_common(1))
            most_common = Counter(nearest_labels).most_common(1)[0][0]
            predictions.append(most_common)
        return np.array(predictions)

def test_knn_basic():
    """基础功能测试"""
    # X = torch.tensor([[1.0, 0], [2.0, 0], [3.0, 0], [4.0, 0]])
    X = np.array([[2.0, 0], [1.0, 0], [3.0, 0], [4.0, 0]])
    y = np.array([2, 2, 3, 3])
    knn = KNN(k=3)
    knn.fit(X, y)
    y_pred = knn.predict(np.array([[1.1, 0]]))
    print(y_pred)

if __name__ == '__main__':
    test_knn_basic()
```



## 实现LoRA微调模块

题目要求: ① 支持冻结原始模型参数  ② 使用低秩矩阵分解 ③ 提供适配器前向传播

实现：**相对来说比较简单**，重点关注：**如何冻结预训练参数权重**，使用`self.W.requires_grad_(False)`冻结权重

第二个关注点：需要针对**低秩矩阵初始化**, $self.lora\_A$ 与 $self.lora\_B$ 处理, `nn.init.kaiming_uniform_()`,`nn.init.zeros()`;

```python
import torch
from torch import nn
import math

class LoRALayer(nn.Module):
    def __init__(self, rank, in_feature, out_feature, alpha, freeze_base=True):
        '''
        :param rank: 低秩矩阵的秩
        :param in_feature: 输入的特征维度
        :param out_feature: 输出的特征维度
        :param alpha 缩放因子初始值, 用于控制低秩适配器的影响程度
        :param freeze_base: 是否冻结预训练模型的权重  # freeze 冻结
        '''
        super().__init__()
        self.rank = rank

        # 预训练权重冻结
        self.W = nn.Linear(in_feature, out_feature, bias=False)

        # 可学习的低秩矩阵
        self.lora_A = nn.Linear(in_feature, rank)
        self.lora_B = nn.Linear(rank, out_feature)
        
        # 初始化低秩矩阵
        nn.init.kaiming_uniform_(self.lora_A.weight, a=math.sqrt(5))  # 这里使用的a是math.sqrt(5),
        nn.init.zeros_(self.lora_B.weight)

        if freeze_base:
            # 冻结预训练权重参数
            self.W.requires_grad_(False)
        # alpha是可学习的参数, 用于控制低秩适配器对原始模型的影响程度, 训练过程中自动调整
        self.alpha = nn.Parameter(torch.tensor(alpha, dtype=torch.float32))
        # self.alpha = self.alpha / self.rank

    def forward(self, x):
        base_output = self.W(x)

        # 低秩矩阵输出
        lora_output = self.lora_B(self.lora_A(x))
        lora_output = lora_output * self.alpha
        output = lora_output + base_output
        return output

if __name__ == '__main__':
    '''
        针对输入x的不同形状, 有不同的含义, 适用于Transformer中不同的层
        x:(batch, dim) 表示输入的批量数据, 每个样本的特征维度为dim, 适用于全连接层和FFN层
        x:(batch, seq, dim) 表示输入的批量数据, 每个样本的特征维度为dim, 适用于处理序列数据, 比如Transformer中的token嵌入层
        x:(batch, head, seq, dim) 表示输入的批量数据, 每个样本的特征维度为dim, 适用于多头注意力层
    '''
    x = torch.randn(32, 768)
    lora_layer = LoRALayer(rank=4, in_feature=768, out_feature=768, alpha=1.0)
    output = lora_layer(x)
    print(output.shape)
```



## 实现Transformer绝对位置编码Position Embedding

**torch.arange() 用于生成一维张量**，**unsqueeze()用于增加维度**。

**div_term就是为位置编码的每一维，分配一个不同的变化速度**，**让模型既能看清大概位置，也能分清相邻位置**。

```python
import torch
import torch.nn as nn
import math

class PositionalEncoding(nn.Module):
    def __init__(self, max_len, d_model):
        super(PositionalEncoding, self).__init__()
        # 初始化一个位置编码的矩阵，维度是[max_len, d_model]
        self.pe = torch.zeros(max_len, d_model)
        self.base = 10000.0

        # Shape: (max_len, 1)
        position = torch.arange(0, max_len, 1, dtype=torch.float)
        print(position.shape)
        position = position.unsqueeze(1)
        print(position.shape)

        # Shape: (dim_model // 2,  )  计算的是频率项div_term
        div_term = torch.exp(torch.arange(0, d_model, 2, dtype=torch.float) * -(math.log(self.base) / d_model))
        print(div_term.shape)

        # 计算sin、cos位置编码
        self.pe[:, 0::2] = torch.sin(position * div_term)
        self.pe[:, 1::2] = torch.cos(position * div_term)

        self.pe = self.pe.unsqueeze_(0)  # Shape: (1, max_len, d_model)

    def forward(self, x):
        """
        Args:
            x: Tensor, shape [batch_size, seq_len, embedding_dim]
        Returns:
            Tensor: Positional Encoding
        """
        return self.pe[:, :x.size(1)]
```



## 旋转位置编码RoPE



