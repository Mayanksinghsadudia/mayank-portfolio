from PIL import Image
import numpy as np
from scipy.ndimage import label, binary_fill_holes, binary_dilation

# Open source PNG
img_path = 'C:/Users/hp/.gemini/antigravity/brain/0ee541b7-eb92-4360-a00f-81a4f6ff7437/.user_uploaded/media__1785097641564.png'
img = Image.open(img_path).convert('RGBA')
arr = np.array(img, dtype=np.uint8)

r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]

# Pure color difference & brightness threshold for outer background
brightness = (r.astype(float) + g.astype(float) + b.astype(float)) / 3.0
color_diff = np.maximum.reduce([np.abs(r.astype(float) - g.astype(float)), 
                                np.abs(g.astype(float) - b.astype(float)), 
                                np.abs(b.astype(float) - r.astype(float))])

# Any pixel that is bright white/light gray OR already low alpha OR low saturation light color
bg_mask = (a < 100) | ((brightness > 170) & (color_diff < 30))

# Flood fill outer background starting from all image borders
border_seed = np.zeros(bg_mask.shape, dtype=bool)
border_seed[0, :] = True
border_seed[-1, :] = True
border_seed[:, 0] = True
border_seed[:, -1] = True

labeled, num_features = label(bg_mask)
border_labels = set(labeled[border_seed])
if 0 in border_labels:
    border_labels.remove(0)

is_outer_bg = np.isin(labeled, list(border_labels))

# Also erode character edges by 1px to strip any leftover white halo pixels
halo = binary_dilation(is_outer_bg, iterations=2) & (brightness > 160)
is_outer_bg |= halo

# Set alpha to 0 for all background & halo pixels
arr_out = arr.copy()
arr_out[is_outer_bg, 3] = 0

out_img = Image.fromarray(arr_out)
# Save with NEW file name to break browser cache completely!
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_v2.png')
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar.png')

print("Generated clean transparent avatar assets: mayank_avatar_v2.png!")
