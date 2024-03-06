import polyscope as ps
import scipy
mat_import = scipy.io.loadmat("C:\\Users\\tiwyl\\PycharmProjects\\pytorch-3d-point-cloud-generation\\results\\ORIG_STG2_adam_nohup_100_evaluate\\108238b535eb293cd79b19c7c4f0e293.mat")
mat = mat_import["pointcloud"]
# Initialize polyscope
ps.init()

### Register a point cloud
# `my_points` is a Nx3 numpy array
for i in range(24):
    ps.register_point_cloud("my points"+str(i), mat[i][0])

ps.show()
#ps.screenshot()