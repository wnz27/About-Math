# -*- coding: utf-8 -*-
# @UpdateTime    : 2020/6/21 17:13
# @File    : vector_test.py
import unittest
from content.线性代数.线性代数学习.playLA.Vector import Vector
import os


class Helper(unittest.TestCase):
    def _eq(self, item1, item2):
        return self.assertEquals(item1, item2)


class TestVector(Helper):
    def testVectorAssociativeLaw(self):
        """
        测试向量结合律
        """
        vec = Vector([2, 5])
        vec2 = Vector([8, 1])
        k = 2
        res1 = k * vec2 + k * vec
        res2 = k * (vec + vec2)
        self._eq(res1[0], res2[0])
        self._eq(res1[1], res2[1])

    def testZeroVector(self):
        """
        测试0向量
        """
        vec = Vector([3, 4, 5])
        l = len(vec)
        zero_vec = Vector([0] * l)
        new_vec = zero_vec + vec
        self._eq(new_vec[0], vec[0])
        self._eq(new_vec[1], vec[1])
        self._eq(new_vec[2], vec[2])

    def testNegativeVector(self):
        """
        测试负向量
        """
        vec = Vector([6, 38, 95])
        l = len(vec)
        neg_vec = -1 * vec
        new_vec = neg_vec + vec
        self._eq(new_vec[0], 0)
        self._eq(new_vec[1], 0)
        self._eq(new_vec[2], 0)

    def testNorm(self):
        vec = Vector([2, 2, 2, 2])
        vec2 = Vector([3, 3, 3, 3])
        self._eq(vec.norm(), 4)
        self._eq(vec2.norm(), 6)
        vec3 = Vector([0] * 3)
        self._eq(vec3.norm(), 0)

