#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/17 PM4:30
# @Author  : Shiloh Leung
# @Site    : 
# @File    : ml_ncp.py
# @Software: PyCharm Community Edition


from tensorD.dataproc.reader import TensorReader
import tensorflow as tf
from tensorD.factorization.env import Environment
from tensorD.dataproc.provider import Provider
from tensorD.factorization.ncp import NCP_BCU
from tensorD.demo.DataGenerator import *

if __name__ == '__main__':
    full_shape = [943, 1682, 31]
    base = TensorReader('/root/tensorD_f/data_out_tmp/u1.base.csv')
    base.read(full_shape=full_shape)
    with tf.Session() as sess:
        rating_tensor = sess.run(base.full_data)
    data_provider = Provider()
    data_provider.full_tensor = lambda: rating_tensor
    env = Environment(data_provider, summary_path='/tmp/ncp_ml')
    ncp = NCP_BCU(env)
    args = NCP_BCU.NCP_Args(rank=20, validation_internal=1)
    ncp.build_model(args)
    loss_hist = ncp.train(100)
    out_path = '/root/tensorD_f/data_out_tmp/python_out/ncp_ml_20.txt'
    with open(out_path, 'w') as out:
        for loss in loss_hist:
            out.write('%.6f\n' % loss)
