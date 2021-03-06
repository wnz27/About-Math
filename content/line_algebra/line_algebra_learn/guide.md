<!--
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2020-03-26 23:10:17
 * @LastEditTime: 2020-03-26 23:10:42
 * @FilePath: /Coding-Daily/content/Python数据相关/line_algebra_learn/guide.md
 * @description: type some description
 -->
# 线性代数学习笔记

## 什么是向量 
两个视角：
- 几何：有向线段
- 现实：数据点

### 向量运算的基本性质
- 加法交换律
- 加法结合律
- 向量数量乘法满足分配率
  - k(向量a + 向量b) = k向量a + k向量b
  - (k + c)向量a = k向量a + c向量a
  - (kc)向量a = k(c向量a)
  - 1向量a = 向量a
### 零向量
**从推导出一个性质出发**：对任意一个向量u， 都存在一个向量0， 满足：`向量u + 向量0 = 向量u` 我们称这样的一个向量，为0向量

这个0向量没有箭头，0向量长度随研究对象的维度决定。

### 负向量
对任意一个向量u，都存在一个向量-u，满足：`向量u + 向量-u = 0向量`

### 向量长度
模长

单位向量， 只关心方向

根据向量u求出u的单位向量的过程：归一化， 规范化（normalize）

**标准单位向量（Standard Unit Vector）**：只由0，1组成的单位向量。指向坐标轴正方向。

二维空间有两个标准单位向量，三维空间有三个标准单位向量，n维空间中有n个标准单位向量。

### 向量相乘
两个向量相乘，结果是一个数。
更严格的说法：两个向量的**点乘**， 两个向量的**内积**
向量u * 向量v = |向量u| * |向量v| * cosO
向量u * 向量v = x1*x2 + y1*y2 = |向量u| * |向量v| * cosO

- 用投影解读向量点乘，把方向不同的方向利用投影到同一个方向做乘法
- 也可以投影到x，y轴来看和理解

## [向量类源码实现](./playLA/Vector.py)
