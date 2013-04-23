#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy, scipy.stats


pf_dev = [
    sio.loadmat('/home/rgcofield/devel/lfviz_ws/matlab/parsed/earth/precision_following_dev.mat')['dev'].T[0],
    sio.loadmat('/home/rgcofield/devel/lfviz_ws/matlab/parsed/monolith/precision_following_dev.mat')['dev'].T[0],
    sio.loadmat('/home/rgcofield/devel/lfviz_ws/matlab/parsed/control/precision_following_dev.mat')['dev'].T[0]
]
pf_dev_mean = [0.87, 0.47, 0.21];
pf_dev_std = [1.226411, 0.624184, 0.263980];

pmf = [scipy.stats.binom.pmf(d,100,0.1) for d in pf_dev]
fig = []
for n in range(3):
    fig.append(plt.figure())
    ax = fig[n].add_subplot(111)
    plt.plot(pf_dev[n], pmf[n])



zl_dev = [
    sio.loadmat('/home/rgcofield/devel/lfviz_ws/matlab/parsed/earth/zero_landmark_dev.mat')['dev'].T[0],
    sio.loadmat('/home/rgcofield/devel/lfviz_ws/matlab/parsed/monolith/zero_landmark_dev.mat')['dev'].T[0],
    sio.loadmat('/home/rgcofield/devel/lfviz_ws/matlab/parsed/control/zero_landmark_dev.mat')['dev'].T[0]
]
zl_dev_mean = [2.74, 3.68, 0.73];
zl_dev_std = [4.145173, 5.665256, 1.035379];

pmf = [scipy.stats.binom.pmf(d,100,0.1) for d in zl_dev]
fig = []
for n in range(3):
    fig.append(plt.figure())
    ax = fig[n].add_subplot(111)
    plt.plot(zl_dev[n], pmf[n])




plt.show()