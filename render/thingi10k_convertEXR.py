import os,sys,time
import numpy as np
import scipy.io
import OpenEXR
import array,Imath

THINGI10KPATH = os.path.abspath("./output/8_depth_fixed/")
#CATEGORY = sys.argv[-4]
#MODEL_LIST = sys.argv[-3]
#RESOLUTION = int(sys.argv[-2])
RESOLUTION = 128
#FIXED = int(sys.argv[-1])
FIXED = 8
N = 100

def readEXR(fname,RESOLUTION):
	channel_list = ["B","G","R"]
	file = OpenEXR.InputFile(fname)
	dw = file.header()["dataWindow"]
	height,width = RESOLUTION,RESOLUTION
	FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)
	vectors = [np.array(array.array("f",file.channel(c,FLOAT))) for c in channel_list]
	depth = vectors[0].reshape([height,width])
	return depth

#listFile = open(MODEL_LIST)
#listFile = [f for f in os.listdir(THINGI10KPATH) if os.path.isfile(os.path.join(THINGI10KPATH, f))]
listDepthFolders = [os.path.join(dirpath) for dirpath, dirnames, files in os.walk(THINGI10KPATH)]

#remove parent directory
listDepthFolders = listDepthFolders[1:]
for folder in listDepthFolders:
	#MODEL = folder.strip()
	#model_folder = folder.split()
	#print(model_folder)
	timeStart = time.time()
	model_folder_name = os.path.basename(folder)

	print(folder)
	print(model_folder_name)

	# # arbitrary views
	# Z = []
	# depth_path = "output/{1}_depth/exr_{0}".format(MODEL,CATEGORY)
	# for i in range(N):
	# 	depth = readEXR("{0}/{1}.exr".format(depth_path,i),RESOLUTION)
	# 	depth[np.isinf(depth)] = 0
	# 	Z.append(depth)
	# trans_path = "{0}/trans.mat".format(depth_path)
	# trans = scipy.io.loadmat(trans_path)["trans"]
	# mat_path = "output/{1}_depth/{0}.mat".format(MODEL,CATEGORY)
	# scipy.io.savemat(mat_path,{
	# 	"Z": np.stack(Z),
	# 	"trans": trans,
	# })
	# os.system("rm -rf {0}".format(depth_path))

	# fixed views
	Z = []
	#depth_path = "output/{1}_depth_fixed/exr_{0}".format(MODEL,FIXED)

	for i in range(FIXED):
		depth = readEXR("{0}/{1}.exr".format(folder,i),RESOLUTION)
		depth[np.isinf(depth)] = 0
		Z.append(depth)
	mat_path = "output/{0}_depth_fixed_mat/{1}.mat".format(FIXED,model_folder_name)
	scipy.io.savemat(mat_path,{
		"Z": np.stack(Z),
	})
	#os.system("rm -rf {0}".format(depth_path))

	print("{1} done, time={0:.4f} sec".format(time.time()-timeStart,model_folder_name))