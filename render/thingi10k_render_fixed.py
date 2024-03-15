# usage: blender blank.blend -b -P render_fixed.py -- SHAPENETPATH CATEGORY MODEL_LIST RESOLUTION FIXED
# blender blank.blend -b -P thingi10k_render_fixed.py -- 128 8

# 1. launch next 2 lines of code in blender python interpreter
import pip
#pip.main(['install', 'tqdm', '--user'])
import sys
# 2. watch blender's python path in console output at this moment
# 3. insert the path to packages_path below and uncomment
packages_path = "C:\\Users\\tiwyl\\AppData\\Roaming\\Python\\Python39\\Scripts" + "\\..\\site-packages" # the path you see in console
# 4. uncomment the next code and launch script in blender interpreter again
sys.path.insert(0, packages_path )
#import tqdm
# use installed packages here
import os,sys,time
import bpy
from bpy import context, ops
import numpy as np
import shutil
import scipy.io

curpath = os.path.abspath(os.path.dirname("."))
sys.path.insert(0,curpath)
import util


# redirect output to log file
logfile = "./tmp/blender_render.log"
errors_log = "./tmp/blender_render_errors.log"
max_dim = .75
#SHAPENETPATH = sys.argv[-5]
THINGI10KPATH = os.path.abspath("../Thingi10k/raw_meshes/")
BUFFERPATH = os.path.abspath("./buffer/")
#CATEGORY = sys.argv[-4]
#MODEL_LIST = sys.argv[-3]
RESOLUTION = int(sys.argv[-2])
FIXED = int(sys.argv[-1])

scene,camera,fo = util.setupBlender(BUFFERPATH,RESOLUTION)
camPosAll = util.getFixedViews(FIXED)


#listFile = open(MODEL_LIST)
# Get a list of all files in the directory
#todo listfile truncated if some files already process (in case of crash)
listFile = [f for f in os.listdir(THINGI10KPATH) if os.path.isfile(os.path.join(THINGI10KPATH, f))]

for line in listFile:
	MODEL = line.strip()
	timeStart = time.time()
	trans = []

	depth_path = "output/{1}_depth_fixed/exr_{0}".format(MODEL.strip(".stl"),FIXED)
	if not os.path.isdir(depth_path):
		os.makedirs(depth_path)

	# # suppress output
	# open(logfile,"a").close()
	# old = os.dup(1)
	# sys.stdout.flush()
	# os.close(1)
	# os.open(logfile,os.O_WRONLY)

	#shape_file = "{2}/{0}/{1}/models/model_normalized.obj".format(CATEGORY,MODEL,SHAPENETPATH)THINGI10KPATH
	shape_file = os.path.join(THINGI10KPATH,MODEL)
	#bpy.ops.import_scene.obj(filepath=shape_file)


	#todo trycatch the import to not crash if error, log it to file
	try:
		bpy.ops.import_mesh.stl(filepath=shape_file)
	except Exception as e:
		with open(errors_log, "a") as f:
			f.write(f"Error importing {shape_file}: {str(e)}\n")
		continue
	#################
	mesh = context.selected_objects[0]
	for obj in bpy.context.selected_objects:  # deselect EVERYTHING
		obj.select_set(False)
	mesh.select_set(state=True)  # ok now just select our mesh
	bpy.context.view_layer.objects.active = mesh

	ops.object.origin_set(type='GEOMETRY_ORIGIN')
	util.scaleMesh(mesh, max_dim)
	#bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)
	####
	#time.sleep(300)
	for m in bpy.data.materials:
		m.use_shadeless = True

	for i in range(FIXED):
		theta = 0
		camPos = camPosAll[i]
		q1 = util.camPosToQuaternion(camPos)
		q2 = util.camRotQuaternion(camPos,theta)
		q = util.quaternionProduct(q2,q1)

		util.setCameraExtrinsics(camera,camPos,q)
		q_extr,t_extr = util.cameraExtrinsicMatrix(q,camPos)

		# # for ShapeNetCore.v2 all the objects are rotated 90 degrees
		# # comment out this block if ShapeNetCore.v1 is used
		# if i==0:
		# 	for o in bpy.data.objects:
		# 		if o==camera: o.select = False
		# 		else: o.select = True
		# 	bpy.ops.transform.rotate(value=-np.pi/2,axis=(0,0,1))

		bpy.ops.render.render(write_still=False)

		shutil.copyfile("{0}/Depth0001.exr".format(fo.base_path),
						"{0}/{1}.exr".format(depth_path,i))
		trans.append(np.array(q_extr))

	# # show output
	# os.close(1)
	# os.dup(old)
	# os.close(old)

	# clean up
	for o in bpy.data.objects:
		if o==camera: continue
		o.select_set(True)
	bpy.ops.object.delete()
	for m in bpy.data.meshes:
		bpy.data.meshes.remove(m)
	for m in bpy.data.materials:
	    m.user_clear()
	    bpy.data.materials.remove(m)

	print("{1} done, time={0:.4f} sec".format(time.time()-timeStart,MODEL))
	#exit(0)

trans = np.array(trans,dtype=np.float32)
np.save("output/trans_fuse{0}.npy".format(FIXED),trans)





