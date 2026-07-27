from PIL import Image
import numpy as np
from scipy.ndimage import label, binary_dilation

# Open source image
img = Image.open('C:/Users/hp/.gemini/antigravity/brain/0ee541b7-eb92-4360-a00f-81a4f6ff7437/.user_uploaded/media__1785095993829.jpg').convert('RGBA')
arr = np.array(img)

r, g, b = arr[:,:,0].astype(float), arr[:,:,1].astype(float), arr[:,:,2].astype(float)

# The background checkerboard consists of neutral white and light-gray tiles.
# Characteristics:
# 1. Color variance (diff between R, G, B) is extremely small (< 12)
# 2. Brightness is high (> 180) or light gray (> 190)

color_diff = np.maximum.reduce([np.abs(r - g), np.abs(g - b), np.abs(b - r)])
brightness = (r + g + b) / 3.0

bg_mask = (color_diff < 15) & (brightness > 175)

# Border connected component extraction:
# We only flood-fill background connected to the outer border of the image
# so inside-body whites (like shirt stripes or glasses highlights) stay intact!
border_seed = np.zeros(bg_mask.shape, dtype=bool)
border_seed[0, :] = bg_mask[0, :]
border_seed[-1, :] = bg_mask[-1, :]
border_seed[:, 0] = bg_mask[:, 0]
border_seed[:, -1] = bg_mask[:, -1]

# Expand border seed slightly inwards from edges
border_seed[:30, :] |= bg_mask[:30, :]
border_seed[-30:, :] |= bg_mask[-30:, :]
border_seed[:, :30] |= bg_mask[:, :30]
border_seed[:, -30:] |= bg_mask[:, -30:]

labeled, num_features = label(bg_mask)
border_labels = set(labeled[border_seed])
if 0 in border_labels:
    border_labels.remove(0)

is_bg = np.isin(labeled, list(border_labels))

# Set background pixels alpha = 0 (completely transparent)
arr[is_bg, 3] = 0

# Alpha feathering for smooth edge transition without halo
edge_mask = binary_dilation(is_bg, iterations=1) & ~is_bg
arr[edge_mask, 3] = 120

out_img = Image.fromarray(arr)
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar.png')
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_clean.png')
print("Successfully processed clean transparent avatar PNG!")
