from PIL import Image
import numpy as np
from scipy.ndimage import label, binary_fill_holes, binary_dilation

# Open the PNG image
img_path = 'C:/Users/hp/.gemini/antigravity/brain/0ee541b7-eb92-4360-a00f-81a4f6ff7437/.user_uploaded/media__1785097641564.png'
img = Image.open(img_path).convert('RGBA')
arr = np.array(img, dtype=np.uint8)

r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]

# Identify white/light-gray background and halo pixels:
# 1. Any pixel with alpha == 0 is already background
# 2. Any pixel with R > 210 and G > 210 and B > 210 (high brightness, white/light gray)
# 3. Any pixel with low color variance and brightness > 200

brightness = (r.astype(float) + g.astype(float) + b.astype(float)) / 3.0
color_diff = np.maximum.reduce([np.abs(r.astype(float) - g.astype(float)), 
                                np.abs(g.astype(float) - b.astype(float)), 
                                np.abs(b.astype(float) - r.astype(float))])

is_white_bg = (a == 0) | ((brightness > 200) & (color_diff < 20))

# Flood fill from image borders to only remove background connected to outer edges
border_seed = np.zeros(is_white_bg.shape, dtype=bool)
border_seed[0, :] = is_white_bg[0, :]
border_seed[-1, :] = is_white_bg[-1, :]
border_seed[:, 0] = is_white_bg[:, 0]
border_seed[:, -1] = is_white_bg[:, -1]

# Expand border seed
border_seed[:10, :] |= is_white_bg[:10, :]
border_seed[-10:, :] |= is_white_bg[-10:, :]
border_seed[:, :10] |= is_white_bg[:, :10]
border_seed[:, -10:] |= is_white_bg[:, -10:]

labeled, num_features = label(is_white_bg)
border_labels = set(labeled[border_seed])
if 0 in border_labels:
    border_labels.remove(0)

is_outer_bg = np.isin(labeled, list(border_labels))

# Also strip any remaining white fringe pixels along the boundary of outer background!
fringe = binary_dilation(is_outer_bg, iterations=2) & ((brightness > 190) & (color_diff < 25))
is_outer_bg |= fringe

# Set alpha to 0 for all background & fringe pixels
arr_out = arr.copy()
arr_out[is_outer_bg, 3] = 0

out_img = Image.fromarray(arr_out)
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar.png')
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_clean.png')

print("Perfect background removal completed!")
print("Remaining white pixels with alpha > 0:", np.sum((arr_out[:,:,3] > 0) & (arr_out[:,:,0] > 230) & (arr_out[:,:,1] > 230) & (arr_out[:,:,2] > 230)))
