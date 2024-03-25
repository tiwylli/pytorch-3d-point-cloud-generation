import os,sys,time
import numpy as np
import scipy.io
import OpenEXR
import array,Imath
from scipy import ndimage

THINGI10KPATH = os.path.abspath("./output/8_rgb_fixed/")
#CATEGORY = sys.argv[-4]
#MODEL_LIST = sys.argv[-3]
#RESOLUTION = int(sys.argv[-2])
RESOLUTION = 128
#RESOLUTION = 128
#FIXED = int(sys.argv[-1])
FIXED = 8
N = 100


def readEXR(filename):
	"""Read color data from EXR image file.
    Parameters
    ----------
    filename : str
        File path.

    Returns
    -------
    img : RGB or RGBA image in float32 format. Each color channel
          lies within the interval [0, 1].
          Color conversion from linear RGB to standard RGB is performed
          internally. See https://en.wikipedia.org/wiki/SRGB#The_forward_transformation_(CIE_XYZ_to_sRGB)
          for more information.

    """

	exrfile = OpenEXR.InputFile(filename)
	header = exrfile.header()

	dw = header['dataWindow']
	isize = (dw.max.y - dw.min.y + 1, dw.max.x - dw.min.x + 1)

	channelData = dict()

	# convert all channels in the image to numpy arrays
	for c in header['channels']:
		C = exrfile.channel(c, Imath.PixelType(Imath.PixelType.FLOAT))
		C = np.frombuffer(C, dtype=np.float32)
		C = np.reshape(C, isize)

		channelData[c] = C

	# Only use RGB channels
	colorChannels = ['R', 'G', 'B']
	img = np.concatenate([channelData[c][..., np.newaxis] for c in colorChannels], axis=2)

	# Calculate start and end indices
	start_index = img.shape[0] // 4
	end_index = img.shape[0] - start_index

	# Slice the array
	resized_img = img[start_index:end_index, start_index:end_index, :]
	img = resized_img
	# linear to standard RGB
	img[..., :3] = np.where(img[..., :3] <= 0.0031308,
							12.92 * img[..., :3],
							1.055 * np.power(img[..., :3], 1 / 2.4) - 0.055)

	# sanitize image to be in range [0, 1]
	#img = np.where(img < 0.0, 0.0, np.where(img > 1.0, 1, img))

	return img







# def readEXR(fname,RESOLUTION):
# 	channel_list = ["B","G","R"]
# 	file = OpenEXR.InputFile(fname)
# 	dw = file.header()["dataWindow"]
# 	height,width = RESOLUTION,RESOLUTION
# 	FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)
# 	vectors = [np.array(array.array("f",file.channel(c,FLOAT))) for c in channel_list]
# 	depth = vectors[0].reshape([height,width])
# 	return depth

#listFile = open(MODEL_LIST)
#listFile = [f for f in os.listdir(THINGI10KPATH) if os.path.isfile(os.path.join(THINGI10KPATH, f))]
listRGBFolders = [os.path.join(dirpath) for dirpath, dirnames, files in os.walk(THINGI10KPATH)]

#remove parent directory
listRGBFolders = listRGBFolders[1:]
for folder in listRGBFolders:
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
	images = []
	#depth_path = "output/{1}_depth_fixed/exr_{0}".format(MODEL,FIXED)

	for i in range(FIXED):
		rgb = readEXR("{0}/{1}.exr".format(folder,i))
		images.append(rgb)

	images_array = np.array(images)
	# Save the numpy array to a .npy file
	np.save("output/thingi10k_inputRGB/{0}.npy".format(model_folder_name), images_array)


	print("{1} done, time={0:.4f} sec".format(time.time()-timeStart,model_folder_name))