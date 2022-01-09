import numpy as np

from pyvox.models import Vox
from pyvox.writer import VoxWriter

a = np.linalg.norm(np.mgrid[-5:5:10j, -5:5:10j, -5:5:10j], axis=0) < 4
print(a)

vox = Vox.from_dense(a)
print(vox)

VoxWriter('test1.vox', vox).write()
