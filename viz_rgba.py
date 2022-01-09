import math
import sys
import coloredlogs
from pyvox.parser import VoxParser
from pyvox.writer import VoxWriter

# coloredlogs.install(level='DEBUG')

m = VoxParser(sys.argv[1]).parse()
n=m

# print(m.palette)

print(len(m.models[0].voxels))
img = m.to_dense()

VoxWriter('explode/head.vox', n).write()
# print(img)
# print(img.shape)

# import matplotlib.pyplot as plt
# import numpy as np

# s = math.ceil(math.sqrt(img.shape[0]))
# print('size', img.shape, s)
# f, arr = plt.subplots(s,s)
# for i, slc in enumerate(img):
#     arr[i//s, i%s].imshow(img[i])
# for a in range(i+1, s*s):
#     arr[a//s, a%s].imshow(np.zeros(img.shape[1:3]))

# plt.show()
