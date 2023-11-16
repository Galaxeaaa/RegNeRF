# Define the list of values
values = ["stone", "pumpkin2", "fabric_toy", "potato", "pine", "fabric_mushroom", "fabric_cow", "fabric_birthday_cake"]
ids = ["04", "27", "29", "39", "40", "44", "50", "62"]
n_views = [6]

# Loop through the list of values
for n in n_views:
    for i, value in enumerate(values):
        # Create a filename based on the value
        filename = f"{value}-{n}v.gin"

        # Define the content of the file, replacing a placeholder with the value
        content = f' \
 # Oppo \n \
 Config.data_dir = "./data/openillumination/lighting_patterns/obj_{ids[i]}_{value}/output"\n \
 Config.checkpoint_dir = "out/oppo/{value}-{n}v" \n \
 Config.dataset_loader = "oppo" \n \
 Config.white_background = True \n \
 Config.factor = 8\n \
 Config.render_factor = 0 \n \
 Config.near = 0.5 \n \
 Config.far = 1.5 \n \
 MipNerfModel.ray_shape = "cylinder" \n \
 MLP.density_noise = 1. \n \
 \n \
 Config.n_input_views = {n}\n \
 Config.hardcode_views = True \n \
 Config.max_steps = 100000 \n \
 \n \
 Config.lr_init = 0.002 \n \
 Config.lr_final = 0.00002 \n \
 Config.lr_delay_steps = 512 \n \
 Config.lr_delay_mult = 0.01 \n \
 Config.grad_max_norm = 0.1 \n \
 Config.grad_max_val = 0.1 \n \
 \n \
 Config.anneal_nearfar = True \n \
 Config.anneal_nearfar_steps = 512 \n \
 Config.anneal_nearfar_perc = 0.0001 \n \
 Config.anneal_mid_perc = 1.0 \n \
 \n \
 Config.depth_tvnorm_loss_mult = 0.1 \n \
 Config.depth_tvnorm_decay = True \n \
 Config.depth_tvnorm_maxstep = 512 \n \
 Config.depth_tvnorm_loss_mult_start = 400.0 \n \
 Config.depth_tvnorm_loss_mult_end = 0.1 \n \
 \n \
 Config.flow_loss_mult = 0.0 \n \
'
        # Create and write to the file
        with open(filename, "w") as file:
            file.write(content)

