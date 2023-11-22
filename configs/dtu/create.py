# Define the list of values
values = [
    "scan24",
    "scan37",
    "scan40",
    "scan55",
    "scan63",
    "scan65",
    "scan69",
    "scan83",
    "scan97",
    "scan105",
    "scan106",
    "scan110",
    "scan114",
    "scan118",
    "scan122",
]
views = [
    "35 2 30",
    "35 2 30",
    "35 2 30",
    "35 2 30",
    "35 2 30",
    "35 2 30",
    "35 2 30",
    "21 26 33",
    "21 26 33",
    "21 26 33",
    "21 26 33",
    "21 26 33",
    "21 26 33",
    "21 26 33",
    "21 26 33",
]
n_views = [3]

# Loop through the list of values
for n in n_views:
    for i, value in enumerate(values):
        # Create a filename based on the value
        filename = f"{value}-{n}v.gin"

        # Define the content of the file, replacing a placeholder with the value
        content = f' \
 # DTU \n \
# DTU settings\n \
Config.data_dir = "data/dtu/Rectified/"\n \
Config.dtu_mask_path = "data/dtu/submission_data/idrmasks"\n \
Config.checkpoint_dir = "out/dtu/{value}-{n}v"\n \
Config.dtu_scan = "{value}"\n \
Config.dtu_split_type = "zerorf"\n \
Config.dataset_loader = "dtu"\n \
Config.white_background = False\n \
Config.near = 0.5\n \
Config.far = 3.5\n \
Config.factor = 4\n \
Config.render_factor = 4\n \
MLP.density_noise = 1.\n \
\n \
Config.n_input_views = 3\n \
Config.max_steps = 43945\n \
\n \
Config.lr_init = 0.002\n \
Config.lr_final = 0.00002\n \
Config.lr_delay_steps = 512\n \
Config.lr_delay_mult = 0.01\n \
Config.grad_max_norm = 0.1\n \
Config.grad_max_val = 0.1\n \
\n \
Config.anneal_nearfar = True\n \
Config.anneal_nearfar_steps = 256\n \
Config.anneal_nearfar_perc = 0.5\n \
\n \
Config.depth_tvnorm_loss_mult = 0.1\n \
Config.depth_tvnorm_decay = True\n \
Config.depth_tvnorm_maxstep = 512\n \
Config.depth_tvnorm_loss_mult_start = 400.0\n \
Config.depth_tvnorm_loss_mult_end = 0.1\n \
\n \
Config.flow_loss_mult = 0.0\n \
Config.depth_tvnorm_mask_weight = 1.0\n \
'
        # Create and write to the file
        with open(filename, "w") as file:
            file.write(content)

