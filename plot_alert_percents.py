#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., .5+height, '%.1f'%height,
                ha='center', va='bottom')



pf_dev_warn = [16.78, 3.23, 0.01]
pf_dev_crit = [6.71, 0.65, 0.01]

pf_dst_warn = [22.82, 29.03, 82.67]
pf_dst_crit = [0.00, 0.00, 4.00]

zl_dev_warn = [25.87, 39.35, 16.67]
zl_dev_crit = [11.19, 25.99, 2.78]

zl_dst_warn = [0.01, 0.01, 22.22]
zl_dst_crit = [0.01, 0.01, 2.78]




N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars



fig = plt.figure()

ax = fig.add_subplot(121)
rects_warn = ax.bar(ind, pf_dev_warn, width, color='y')
rects_crit = ax.bar(ind+width, pf_dev_crit, width, color='r')
ax.set_ylabel('% of Run Incurred')
ax.set_title('Path Deviation Alerts')
ax.grid(True)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Earth', 'Monolith', 'Control') )
ax.legend( (rects_warn[0], rects_crit[0]), ('Warning', 'Critical'), 'upper right' )
autolabel(rects_warn)
autolabel(rects_crit)

ax = fig.add_subplot(122)
rects_warn = ax.bar(ind, pf_dst_warn, width, color='y')
rects_crit = ax.bar(ind+width, pf_dst_crit, width, color='r')
ax.set_ylabel('% of Run Incurred')
ax.set_title('Following Distance Alerts')
ax.grid(True)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Earth', 'Monolith', 'Control') )
ax.legend( (rects_warn[0], rects_crit[0]), ('Warning', 'Critical'), 'upper left' )
autolabel(rects_warn)
autolabel(rects_crit)

plt.savefig('./figs/precision_following_alert_percents.png', format='png')



fig = plt.figure()

ax = fig.add_subplot(121)
rects_warn = ax.bar(ind, zl_dev_warn, width, color='y')
rects_crit = ax.bar(ind+width, zl_dev_crit, width, color='r')
ax.set_ylabel('% Incurred')
ax.set_title('Path Deviation Alerts')
ax.grid(True)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Earth', 'Monolith', 'Control') )
plt.ylim((0,45))
ax.legend( (rects_warn[0], rects_crit[0]), ('Warning', 'Critical'), 'upper right' )
autolabel(rects_warn)
autolabel(rects_crit)

ax = fig.add_subplot(122)
rects_warn = ax.bar(ind, zl_dst_warn, width, color='y')
rects_crit = ax.bar(ind+width, zl_dst_crit, width, color='r')
ax.set_ylabel('% Incurred')
ax.set_title('Following Distance Alerts')
ax.grid(True)
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Earth', 'Monolith', 'Control') )
ax.legend( (rects_warn[0], rects_crit[0]), ('Warning', 'Critical'), 'upper left' )
autolabel(rects_warn)
autolabel(rects_crit)

plt.savefig('./figs/zero_landmark_alert_percents.png', format='png')




plt.show()

