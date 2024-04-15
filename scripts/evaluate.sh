#python3 evaluate.py --model ORIG_STG2 --experiment 1k_adam_trueWD \
#	--loadPath ORIG_STG2_1k_adam_trueWD\
#	--chunkSize 32 --batchSize 32 \
#	--gpu 4
#python3 evaluate.py --model ORIG_STG1 --experiment 1k_adam_trueWD \
#	--loadPath ORIG_STG1_1k_adam_trueWD\
#	--chunkSize 32 --batchSize 32 \
#	--gpu 3

##Thingi10k dataset
#python3 evaluate.py --model ORIG_STG1 --experiment lc_thingi10k_2 \
#	--loadPath ORIG_STG1_lc_thingi10k\
#	--chunkSize 32 --batchSize 32 \
#	--gpu 3 \
#	--path render/output \
#  --category thingi10k
#
##Thingi10k dataset
#python3 evaluate.py --model ORIG_STG2 --experiment lc_thingi10k_2_best \
#	--loadPath ORIG_STG2_lc_thingi10k_2\
#	--chunkSize 32 --batchSize 32 \
#	--gpu 3 \
#	--path render/output \
#  --category thingi10k

#Thingi10k dataset
#python3 evaluate.py --model ORIG_STG2 --experiment lc_thingi10k_2_100e \
#	--loadPath ORIG_STG2_lc_thingi10k_2\
#	--chunkSize 32 --batchSize 32 \
#	--gpu 3 \
#	--path render/output \
#  --category thingi10k \
#  --loadEpoch 100

#python3 evaluate.py --model ORIG_STG2 --experiment lc_thingi10k_2_300e \
#	--loadPath ORIG_STG2_lc_thingi10k_2\
#	--chunkSize 32 --batchSize 32 \
#	--gpu 3 \
#	--path render/output \
#  --category thingi10k \
#  --loadEpoch 300

##evaluate chairs from thingi10k with shapenet weights
#python3 evaluate.py --model ORIG_STG2 --experiment 1k_adam_trueWD_thingi10k_chairs \
#	--loadPath ORIG_STG2_1k_adam_trueWD\
#	--chunkSize 32 --batchSize 32 \
#	--gpu 3 \
#	--path render/output \
#  --category thingi10k

#evaluate chairs from thingi10k with shapenet weights
python3 evaluate.py --model ORIG_STG2 --experiment adrienThingi10k \
	--loadPath ORIG_STG2_adrienThingi10k\
	--chunkSize 32 --batchSize 32 \
	--gpu 3 \
	--path render/output \
  --category thingi10k

#change loadpat to the path of the model you want to evaluate

