import subprocess

# Get the current arrangement from displayplacer:
dp_list_output = subprocess.run(['displayplacer', 'list'], capture_output=True, text=True)
dp_current_confg = dp_list_output.stdout.split("\n")[-2]
splitoput = dp_current_confg.split('"')[1::2]

# Split out configs for current orientation
current_logical_config_left = ''
current_logical_config_center = ''
current_logical_config_right = ''
current_logical_config_mbp = ''

for x in splitoput:
    if x.endswith('origin:(-7680,-458) degree:0'):
        current_logical_config_left = x
    elif x.endswith('origin:(-5120,-458) degree:0'):
        current_logical_config_center = x
    elif x.endswith('origin:(-2560,-458) degree:0'):
        current_logical_config_right = x
    elif x.endswith('origin:(0,0) degree:0'):
        current_logical_config_mbp = x
    else:
        raise Exception("Current display orientation isn't as expected. Exiting.")

target_config_left = current_logical_config_left.replace('(-7680,-458)','(-2560,-458)')
target_config_center = current_logical_config_center
target_config_right = current_logical_config_right.replace('(-2560,-458)','(-7680,-458)')
target_config_mbp = current_logical_config_mbp

subprocess.run(['displayplacer', target_config_left, target_config_center, target_config_right, target_config_mbp], text=True)