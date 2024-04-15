import polyscope as ps
import scipy

# Load a point cloud from a .mat file in results/ORIG_STG2_lc_thingi10k



#mat_import = scipy.io.loadmat("C:\\Users\\tiwyl\\PycharmProjects\\pytorch-3d-point-cloud-generation\\results\\ORIG_STG1_1k_adam_trueWD\\108238b535eb293cd79b19c7c4f0e293.mat")
mat_import = scipy.io.loadmat("C:\\Users\\tiwyl\\PycharmProjects\\pytorch-3d-point-cloud-generation\\results\\ORIG_STG2_adrienThingi10k\\exr_1158264.mat")

mat = mat_import["pointcloud"]
# Initialize polyscope
ps.init()


# Set the up and front directions
ps.set_up_dir("z_up")
ps.set_screenshot_extension(".jpg")
#ps.look_at((0., 0., 0.5), (1., 1., 1.))
### Register a point cloud
# `my_points` is a Nx3 numpy array
for i in range(24):
    ps.register_point_cloud("my points"+str(i), mat[i][0])
    ps.show()
    #ps.screenshot("my points"+str(i)+".jpg",True)
    ps.remove_point_cloud("my points"+str(i))
#ps.register_point_cloud("my points"+str(4), mat[7][0])
#ps.show()

#ps.screenshot()