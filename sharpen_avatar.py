from PIL import Image, ImageFilter, ImageEnhance
import numpy as np

# Load source avatar PNG
img_path = 'C:/Users/hp/.gemini/antigravity/brain/0ee541b7-eb92-4360-a00f-81a4f6ff7437/.user_uploaded/media__1785098493846.png'
img = Image.open(img_path).convert('RGBA')

# Separate RGB and Alpha
r, g, b, a = img.split()
rgb = Image.merge('RGB', (r, g, b))

# Apply unsharp mask for crisp realistic detail enhancement
sharpened_rgb = rgb.filter(ImageFilter.UnsharpMask(radius=1.8, percent=180, threshold=2))

# Enhance contrast and sharpness slightly
enhancer = ImageEnhance.Contrast(sharpened_rgb)
sharpened_rgb = enhancer.enhance(1.08)

sharp_detail = ImageEnhance.Sharpness(sharpened_rgb).enhance(1.4)

# Re-combine RGB with smooth alpha channel
final_img = Image.merge('RGBA', (sharp_detail.split()[0], sharp_detail.split()[1], sharp_detail.split()[2], a))

# Save enhanced ultra-sharp avatar
final_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_hd.png')
final_img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/mayank_avatar_final.png')

print("Successfully generated ultra-sharp HD avatar image!")
