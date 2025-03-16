from PIL import Image
import numpy as np
from tqdm import tqdm
import os, json

# read video list from video_cut.json
with open('./data/GTA/video_cut.json', 'r') as f:
    video_cut = json.load(f)
video_list = list(video_cut.keys())

for video_id in tqdm(video_list):
    # if video_id not in ['fbi_2_mcs_2', 'fam_6_mcs_1', 'fbi_1_ext', 'family_4_mcs_2', 'low_fun_int', 'maude_mcs_1', 'sol_1_mcs_1_concat', 'fin_c_ext']:
    #     continue
    dir_name = f'./data/GTA/psg4d_gta/visible/{video_id}'
    file_list = [filename.strip('.npy') for filename in sorted(os.listdir(dir_name))]
    video_cut_start = video_cut[video_id][0]
    video_cut_end = video_cut[video_id][1]
    for file_id in tqdm(file_list):
        # read generated mask
        mask_pth = os.path.join('./data/background_masks', video_id, file_id + '.bmp')
        background_mask = Image.open(mask_pth)
        background_mask = np.array(background_mask, dtype=np.uint16)
        background_mask[background_mask != 0] = background_mask[background_mask != 0] + 1000
        # read existing mask
        vis_pth = os.path.join(dir_name, file_id + '.npy')
        foreground_mask = np.load(vis_pth)
        # merge mask
        final_mask = foreground_mask.copy()
        final_mask[foreground_mask == 0] = background_mask[foreground_mask == 0]
        # save mask
        os.makedirs(f'./data/GTA/psg4d_gta/masks/{video_id}', exist_ok=True)
        save_pth = os.path.join(f'./data/GTA/psg4d_gta/masks/{video_id}/{file_id}.npy')
        np.save(save_pth, final_mask)
