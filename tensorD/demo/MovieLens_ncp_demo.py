#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/4 PM8:41
# @Author  : Shiloh Leung
# @Site    : 
# @File    : MovieLens_ncp_demo.py
# @Software: PyCharm Community Edition

from tensorD.dataproc.reader import TensorReader
import tensorflow as tf
from tensorD.factorization.env import Environment
from tensorD.dataproc.provider import Provider
from tensorD.factorization.ncp import NCP_BCU
from tensorD.loss import *

if __name__ == '__main__':
    full_shape = [600, 1500, 30] #[671, 9066, 262]
    # Train on *.base.csv
    print('=========Train=========')
    base = TensorReader('random_data.csv') #('new_ratings_all.csv')
    base.read(full_shape=full_shape)
    with tf.Session() as sess:
        rating_tensor = sess.run(base.full_data)
    data_provider = Provider()
    data_provider.full_tensor = lambda: rating_tensor
    env = Environment(data_provider, summary_path='/tmp/ncp_demo')
    ncp = NCP_BCU(env)
    args = NCP_BCU.NCP_Args(rank=20, validation_internal=3)
    ncp.build_model(args)
    ncp.train(100)
    print('Training ends.\n\n\n')

    # Test on *.test.csv
    # print('=========Test=========')
    # test = TensorReader('movielens-100k/u1.test.csv')
    # test.read(full_shape=full_shape)
    # full = tf.constant(ncp.full, dtype=tf.float64)
    # rmse_op = rmse_ignore_zero(test.full_data, full)
    # with tf.Session() as sess:
    #     rmse = sess.run(rmse_op)
    # print('RMSE on u1.test.csv :  %.5f' % rmse)






