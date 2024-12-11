import time

int_dir = 'out'
out_dir = 'out'
eval_interval = 5000
eval_iters = 200
wandb_log = False # feel free to turn on
wandb_project = 'gpt2finetune'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'amazon'
init_from = 'resume' # this is the smallest GPT-2 model, good for google colab

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

batch_size = 16
gradient_accumulation_steps = 32
max_iters = 500000

# finetune at constant LR
learning_rate = 2e-5
decay_lr = False

iter_num = 0
best_val_loss = 1e9

