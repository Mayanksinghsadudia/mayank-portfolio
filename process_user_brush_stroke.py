from PIL import Image
import numpy as np

img_path = 'C:/Users/hp/.gemini/antigravity/brain/0ee541b7-eb92-4360-a00f-81a4f6ff7437/.user_uploaded/media__1785107195037.jpg'
img = Image.open(img_path).convert('RGBA')
arr = np.array(img, dtype=np.float32)

r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

# White background removal calculation:
# Pure white (255, 255, 255) -> Alpha 0
# Pure paint color -> Alpha 255

brightness = (r + g + b) / 3.0
whiteness = np.minimum.reduce([r, g, b])

# Calculate alpha: 255 - whiteness, boosted for paint opacity
alpha = np.clip((255.0 - whiteness) * 2.2, 0, 255)

# For outer background where whiteness > 240, force alpha = 0
is_pure_white = (r > 238) & (g > 238) & (b > 238)
alpha[is_pure_white] = 0

arr_out = arr.copy()
arr_out[:,:,3] = alpha

out_img = Image.fromarray(arr_out.astype(np.uint8))

# Save output transparent brush stroke asset
out_path_1 = 'C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_brush_stroke.png'
out_path_2 = 'C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/brush_stroke_bg.png'

out_img.save(out_path_1)
out_img.save(out_path_2)

print(f"Successfully processed user brush stroke image with clean white background removal!")
