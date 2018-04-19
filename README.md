# DHash
Image comparing with dHash algorithm.
使用dHash算法实现图片对比、相似图片查重。

## dHash简介
dHash算法属于感知哈希算法，用于图片相似度对比。

感知哈希算法目前有：

1. aHash：平均值哈希，速度快，但准确率较低。
2. pHash：感知哈希，准确率高，但速度较慢。
3. `dHash：差异值哈希，速度快，且准确率高。`

## Function
#### 1. 获得图片的dHash值：
```python
hash = DHash.calculate_hash(image)
```

#### 2. 计算两张图片间的汉明距离：
```python
hamming_distance = DHash.hamming_distance(image1, image2)
```

#### 3. 计算两个dHash值间的汉明距离：
```python
hamming_distance = DHash.hamming_distance(dHash1, dHash2)
```


#### dHash算法实现详解：
http://www.jianshu.com/p/193f0089b7a2
