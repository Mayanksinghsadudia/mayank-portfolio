from PIL import Image
import numpy as np

# Load transparent avatar image
img_path = 'C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_v2.png'
img = Image.open(img_path).convert('RGBA')
arr = np.array(img, dtype=np.float32)

height, width = arr.shape[0], arr.shape[1]

r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]

# T-shirt bounding box in relative coordinates:
# Vertical: y from 21% to 48% of total height
# Horizontal: x from 28% to 72% of total width

y_min, y_max = int(height * 0.21), int(height * 0.48)
x_min, x_max = int(width * 0.28), int(width * 0.72)

# Create t-shirt mask
tshirt_mask = np.zeros((height, width), dtype=bool)
tshirt_mask[y_min:y_max, x_min:x_max] = (a[y_min:y_max, x_min:x_max] > 100)

# Exclude skin color from t-shirt mask (neck and arms)
# Skin has warm tone: R > G + 12 and R > B + 25
is_skin = (r > g + 12) & (r > b + 25) & (r > 100) & (b < 160)
tshirt_mask &= ~is_skin

# Exclude watch / wrist bands (very dark black on wrists)
is_black_strap = (r < 50) & (g < 50) & (b < 50)
tshirt_mask[int(height*0.41):, :] &= ~is_black_strap[int(height*0.41):, :]

# Calculate luminance / shading from original t-shirt pixels
luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0

# Target brown color palette:
# Rich warm brown: Base RGB = (125, 75, 45) -> Hex #7D4B2D
new_r = np.clip(luminance * 180.0 + 20.0, 0, 255)
new_g = np.clip(luminance * 110.0 + 10.0, 0, 255)
new_b = np.clip(luminance * 70.0 + 5.0, 0, 255)

# Apply brown color to t-shirt mask
arr_out = arr.copy()
arr_out[:,:,0] = np.where(tshirt_mask, new_r, arr[:,:,0])
arr_out[:,:,1] = np.where(tshirt_mask, new_g, arr[:,:,1])
arr_out[:,:,2] = np.where(tshirt_mask, new_b, arr[:,:,2])

out_img = Image.fromarray(arr_out.astype(np.uint8))
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_v3.png')
out_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_v2.png')

print("Successfully changed t-shirt color to brown!")
