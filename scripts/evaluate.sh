python3 evaluate.py --model ORIG_STG2 --experiment 1k_adam_trueWD \
	--loadPath ORIG_STG2_1k_adam_trueWD\
	--chunkSize 32 --batchSize 32 \
	--gpu 4

# python3 evaluate.py --model ORIG_STG2 --experiment sgd_trueWD_restart_cont1 \
# 	--loadPath ORIG_STG2_sgd_trueWD_restart_cont1 \
# 	--chunkSize 32 --batchSize 32 \
# 	--gpu 0

#change loadpat to the path of the model you want to evaluate