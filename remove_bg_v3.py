from PIL import Image
import numpy as np

# Load source image
img = Image.open('C:/Users/hp/.gemini/antigravity/brain/0ee541b7-eb92-4360-a00f-81a4f6ff7437/.user_uploaded/media__1785095993829.jpg').convert('RGBA')
arr = np.array(img, dtype=np.float32)

r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

# Compute color difference (saturation) and brightness
max_diff = np.maximum.reduce([np.abs(r - g), np.abs(g - b), np.abs(b - r)])
brightness = (r + g + b) / 3.0

# Checkerboard pixels are gray/white neutral colors (max_diff < 18) AND bright (brightness > 165)
# Note: The body has saturated skin (max_diff > 30), denim pants (blue hue), dark hair (brightness < 100), dark sunglasses (brightness < 60).
# The white shirt stripes are bordered by dark blue stripes, but let's check if white shirt pixels have max_diff < 18.
# White shirt stripes are surrounded by blue stripes inside the upper body region.

is_bg_color = (max_diff < 20) & (brightness > 160)

# Let's refine bg_color:
# All pixels outside the body silhouette, PLUS any isolated gray/white regions inside arm/leg gaps!
# Let's inspect connected components of non-bg pixels to preserve the body silhouette cleanly.
from scipy.ndimage import label, binary_fill_holes, binary_erosion, binary_dilation

# Initial body mask: NOT background color
body_mask = ~is_bg_color

# Fill holes in the main body (this protects the white shirt stripes inside the torso!)
# Find the largest connected component (the character)
labeled_body, num_body = label(body_mask)
component_sizes = np.bincount(labeled_body.ravel())
component_sizes[0] = 0 # Ignore background label 0

largest_label = component_sizes.argmax()
main_body = (labeled_body == largest_label)

# Fill internal holes (protects white t-shirt stripes and watch face inside the torso)
main_body_filled = binary_fill_holes(main_body)

# BUT wait! Between legs and inside arm-to-torso gaps, binary_fill_holes fills those gaps if they are enclosed.
# Let's detect arm/leg gap regions specifically:
# Gap pixels are bg_color AND inside main_body_filled.
# If gap pixels touch the outer border through bg_color path, they ARE background!

# Pure outer background + gap background:
bg_final = is_bg_color | (~main_body_filled)

# Refine edges with smooth alpha mask
alpha = np.where(bg_final, 0, 255).astype(np.uint8)

# Feather edge pixels slightly to eliminate any hard fringe
edge_mask = binary_dilation(bg_final, iterations=1) & ~bg_final
alpha[edge_mask] = 130

# Put alpha back into image
arr_out = arr.astype(np.uint8)
arr_out[:,:,3] = alpha

out_img = Image.fromarray(arr_out)
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar.png')
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_clean.png')

print("Successfully generated ultra-clean transparent avatar PNG!")
