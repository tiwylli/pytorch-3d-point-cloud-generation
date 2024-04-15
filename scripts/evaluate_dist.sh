
python3 evaluate_dist.py --model ORIG_STG2 --experiment 1k_adam_trueWD \
	--loadPath ORIG_STG2_1k_adam_trueWD \
	--chunkSize 32 --batchSize 32 \
	--gpu 2

# python evaluate_dist.py --model ORIG_STG2 --experiment sgd_trueWD_restart_cont1 \
# 	--loadPath ORIG_STG2_sgd_trueWD_restart_cont1 \
# 	--chunkSize 32 --batchSize 32 \
# 	--gpu 1

# python evaluate_dist.py --model ORIG_STG2 --experiment orig_tf \
# 	--loadPath "~/3D-point-cloud-generation/results_0/orig-ft_it100000" \
# 	--chunkSize 32 --batchSize 32 \
# 	--gpu 1
