from PIL import Image, ImageFilter
import numpy as np

# Load user's brush swatch image
img_path = 'C:/Users/hp/.gemini/antigravity/brain/0ee541b7-eb92-4360-a00f-81a4f6ff7437/.user_uploaded/media__1785107195037.jpg'
img = Image.open(img_path).convert('RGBA')
arr = np.array(img, dtype=np.float32)

r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

# Calculate paint stroke density / opacity from whiteness
whiteness = np.minimum.reduce([r, g, b])
stroke_density = np.clip((255.0 - whiteness) / 255.0, 0, 1.0)

# Target website template colors:
# Primary Orange Accent: RGB (255, 107, 0)
# Deep Accent: RGB (224, 83, 0)
# Warm Highlight: RGB (255, 150, 60)

# Recolor the paint stroke according to shading density to match website theme #FF6B00
new_r = stroke_density * 255.0
new_g = stroke_density * 107.0 + (1.0 - stroke_density) * 30.0
new_b = stroke_density * 0.0

# Calculate smooth alpha channel
alpha = np.clip(stroke_density * 280.0, 0, 255)

# Outer white background removal
is_pure_white = (r > 232) & (g > 232) & (b > 232)
alpha[is_pure_white] = 0

arr_out = np.zeros_like(arr)
arr_out[:,:,0] = np.clip(new_r, 0, 255)
arr_out[:,:,1] = np.clip(new_g, 0, 255)
arr_out[:,:,2] = np.clip(new_b, 0, 255)
arr_out[:,:,3] = alpha

out_img = Image.fromarray(arr_out.astype(np.uint8))

# Save recolored & edge-feathered paint brush stroke
out_path = 'C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_brush_stroke_theme.png'
out_img.save(out_path)

print("Successfully recolored and feathered user brush stroke image to match #FF6B00 website theme!")
