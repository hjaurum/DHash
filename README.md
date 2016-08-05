# DHash
Image comparing with dHash algorithm.

##Function
####1. 获得图片的dHash值：
```python
hash = DHash.calculate_hash(image)
```

####2. 计算两张图片间的汉明距离：
```python
hash = DHash.hamming_distance(image1, image2)
```

####3. 计算两个dHash值间的汉明距离：
```python
hash = DHash.hamming_distance(dHash1, dHash2)
```


#### dHash算法实现详解：
http://www.jianshu.com/p/193f0089b7a2
