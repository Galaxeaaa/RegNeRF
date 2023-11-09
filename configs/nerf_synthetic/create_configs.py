# Define the list of values
values = ["chair", "drums", "ficus", "hotdog", "lego", "materials", "mic", "ship"]
n_views = [4, 6]

# Loop through the list of values
for n in n_views:
    for value in values:
        # Create a filename based on the value
        filename = f"{value}{n}.gin"
        
        # Define the content of the file, replacing a placeholder with the value
        content = f" \
# Blender \n \
Config.data_dir = \"./data/nerf_synthetic\" \n \
Config.blender_scene = \"{value}\" \n \
Config.checkpoint_dir = \"out/nerf_synthetic/{value}{n}\" \n \
Config.dataset_loader = 'blender' \n \
Config.white_background = True \n \
Config.factor = 0 \n \
Config.render_factor = 0 \n \
Config.near = 0 \n \
Config.far = 1 \n \
MipNerfModel.ray_shape = 'cylinder' \n \
MLP.density_noise = 1. \n \
\n \
Config.n_input_views = 4 \n \
Config.hardcode_views = True \n \
Config.max_steps = 139535 \n \
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
"
        
        # Create and write to the file
        with open(filename, "w") as file:
            file.write(content)
