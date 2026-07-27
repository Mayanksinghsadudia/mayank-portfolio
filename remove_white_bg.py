from PIL import Image
import numpy as np
from scipy.ndimage import label, binary_fill_holes, binary_dilation

# Open the new white background avatar image
img_path = 'C:/Users/hp/.gemini/antigravity/brain/0ee541b7-eb92-4360-a00f-81a4f6ff7437/.user_uploaded/media__1785097389463.jpg'
img = Image.open(img_path).convert('RGBA')
arr = np.array(img, dtype=np.float32)

r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

brightness = (r + g + b) / 3.0
color_diff = np.maximum.reduce([np.abs(r - g), np.abs(g - b), np.abs(b - r)])

# White & light floor shadow background pixels:
# High brightness (> 215) AND low color difference (< 15)
bg_mask = (brightness > 215) & (color_diff < 15)

# Border connected component extraction:
border_seed = np.zeros(bg_mask.shape, dtype=bool)
border_seed[0, :] = bg_mask[0, :]
border_seed[-1, :] = bg_mask[-1, :]
border_seed[:, 0] = bg_mask[:, 0]
border_seed[:, -1] = bg_mask[:, -1]

labeled, num_features = label(bg_mask)
border_labels = set(labeled[border_seed])
if 0 in border_labels:
    border_labels.remove(0)

is_outer_bg = np.isin(labeled, list(border_labels))

# Set alpha to 0 for outer background
alpha = np.where(is_outer_bg, 0, 255).astype(np.uint8)

# Subtle anti-aliasing edge blending
edge_mask = binary_dilation(is_outer_bg, iterations=1) & ~is_outer_bg
alpha[edge_mask] = 140

arr_out = arr.astype(np.uint8)
arr_out[:,:,3] = alpha

out_img = Image.fromarray(arr_out)
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar.png')
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_transparent.png')

print("White background successfully removed! Transparent PNG saved.")
