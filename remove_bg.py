from PIL import Image
import numpy as np

img = Image.open('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar.png').convert('RGBA')
arr = np.array(img)

# The checkerboard grid consists of white (approx 245-255) and gray (approx 200-220) tiles with low saturation.
# Let's inspect R, G, B channels and variance
r, g, b = arr[:,:,0].astype(float), arr[:,:,1].astype(float), arr[:,:,2].astype(float)

# Saturation / color difference
color_diff = np.abs(r - g) + np.abs(g - b) + np.abs(b - r)

# Background checkerboard is neutral gray/white (color_diff < 15) AND bright (brightness > 180)
# Except for parts of white stripes on t-shirt which are enclosed inside the body contour!

brightness = (r + g + b) / 3.0
bg_candidate = (color_diff < 15) & (brightness > 180)

# Flood fill from image borders (top, left, right, bottom margins) to only remove background connected to edges!
from scipy.ndimage import binary_fill_holes, label

# Mark border background pixels
border_mask = np.zeros(bg_candidate.shape, dtype=bool)
border_mask[0, :] = bg_candidate[0, :]
border_mask[-1, :] = bg_candidate[-1, :]
border_mask[:, 0] = bg_candidate[:, 0]
border_mask[:, -1] = bg_candidate[:, -1]

# Also top 5% and bottom 5% and left/right 5%
border_mask[:50, :] |= bg_candidate[:50, :]
border_mask[-50:, :] |= bg_candidate[-50:, :]
border_mask[:, :50] |= bg_candidate[:, :50]
border_mask[:, -50:] |= bg_candidate[:, -50:]

# Connected components of bg_candidate that touch the border_mask
labeled, num_features = label(bg_candidate)
border_labels = set(labeled[border_mask])
if 0 in border_labels:
    border_labels.remove(0)

is_bg = np.isin(labeled, list(border_labels))

# Set background pixels to transparent alpha=0
arr[is_bg, 3] = 0

# Smooth anti-aliased edge transition
# Expand background slightly for clean edges
from scipy.ndimage import binary_dilation
edge_mask = binary_dilation(is_bg, iterations=1) & ~is_bg
arr[edge_mask, 3] = 128

out_img = Image.fromarray(arr)
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_transparent.png')
print("Successfully generated transparent avatar PNG!")
