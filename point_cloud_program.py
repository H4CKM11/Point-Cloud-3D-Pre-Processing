# -*- coding: utf-8 -*-
"""
Spyder Editor

@Author: Eduardo Martinez
"""

import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits import mplot3d

file_path_PC = "F:/Programming/Computer Vision/Point_Cloud_Proccesor/data/sample.xyz"
point_cloud = np.loadtxt(file_path_PC, skiprows=1, max_rows=10000)
xyz = point_cloud[:, 0:3]
rgb = point_cloud[:, 3:6]

mean_Z = np.mean(point_cloud, axis=0)[2]
spatial_query = point_cloud[abs(point_cloud[:,2] - mean_Z)<1]

# ax = plt.axes(projection = '3d')
# ax.scatter(xyz[:,0],xyz[:,1],xyz[:,2], c=rgb/255, s=0.01)
# plt.show()

# np.savetxt("F:/Programming/Computer Vision/Point_Cloud_Proccesor/data/sample_filtered.xyz", spatial_query, delimiter=";", fmt='%1.3f')