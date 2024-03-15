import polyscope as ps
import scipy

mat_import = scipy.io.loadmat("C:\\Users\\tiwyl\\PycharmProjects\\pytorch-3d-point-cloud-generation\\results\\ORIG_STG2_1k_adam_trueWD\\108238b535eb293cd79b19c7c4f0e293.mat")

mat = mat_import["pointcloud"]
# Initialize polyscope
ps.init()


# Set the up and front directions
ps.set_up_dir("z_up")
#ps.set_screenshot_extension(".jpg")

### Register a point cloud
# `my_points` is a Nx3 numpy array
for i in range(24):
    ps.register_point_cloud("my points"+str(i), mat[i][0])
    ps.show()
    #ps.scr  eenshot("my points"+str(i),True)
    ps.remove_point_cloud("my points"+str(i))
#ps.register_point_cloud("my points"+str(4), mat[7][0])
#ps.show()

#ps.screenshot()