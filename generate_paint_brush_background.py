from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import random
import math

# Dimensions for high-res paint brush background
width, height = 800, 900
img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Theme colors (matching website palette):
# #FF6B00 (Primary Orange), #FF8C38 (Warm Orange), #FFB693 (Peach Accent), #E05300 (Deep Orange)
colors = [
    (255, 107, 0, 220),   # Vibrant primary orange
    (255, 140, 56, 180),  # Warm apricot orange
    (224, 83, 0, 200),    # Deep crimson orange
    (255, 182, 147, 140), # Soft peach highlight
]

center_x, center_y = width // 2, height // 2 - 20

# Draw main organic brush stroke shapes
def draw_brush_stroke(draw, start, end, width_start, width_end, color, num_bristles=40):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.hypot(dx, dy)
    angle = math.atan2(dy, dx)
    
    steps = int(length)
    for i in range(steps):
        t = i / float(steps)
        # Add random noise/bristle jitter
        curr_x = start[0] + dx * t + math.sin(t * math.pi * 3) * 15
        curr_y = start[1] + dy * t + math.cos(t * math.pi * 2) * 10
        
        curr_w = width_start + (width_end - width_start) * (1.0 - math.pow(t - 0.5, 2) * 3)
        
        # Draw multiple bristle tracks for realistic paint texture
        for b in range(num_bristles):
            offset_r = (random.random() - 0.5) * curr_w
            bx = curr_x + offset_r * math.cos(angle + math.pi/2)
            by = curr_y + offset_r * math.sin(angle + math.pi/2)
            
            b_size = random.uniform(2, 6)
            bristle_alpha = int(color[3] * random.uniform(0.3, 0.9))
            bristle_color = (color[0], color[1], color[2], bristle_alpha)
            
            draw.ellipse([bx - b_size, by - b_size, bx + b_size, by + b_size], fill=bristle_color)

# Layer 1: Wide diagonal background sweep
draw_brush_stroke(draw, (center_x - 220, center_y - 250), (center_x + 200, center_y + 220), 240, 280, colors[2], num_bristles=60)

# Layer 2: Main vibrant orange stroke
draw_brush_stroke(draw, (center_x - 180, center_y - 180), (center_x + 180, center_y + 180), 280, 320, colors[0], num_bristles=80)

# Layer 3: Secondary accent stroke
draw_brush_stroke(draw, (center_x + 150, center_y - 200), (center_x - 160, center_y + 160), 200, 240, colors[1], num_bristles=50)

# Layer 4: Peach highlight stroke
draw_brush_stroke(draw, (center_x - 100, center_y - 120), (center_x + 120, center_y + 100), 160, 200, colors[3], num_bristles=40)

# Layer 5: Paint splatters and droplets along edges
for _ in range(120):
    angle = random.uniform(0, math.pi * 2)
    dist = random.uniform(180, 360)
    sx = center_x + math.cos(angle) * dist
    sy = center_y + math.sin(angle) * dist
    
    radius = random.uniform(3, 14)
    color = random.choice(colors)
    draw.ellipse([sx - radius, sy - radius, sx + radius, sy + radius], fill=color)

# Smooth blur for realistic paint blending
img_blurred = img.filter(ImageFilter.GaussianBlur(radius=3))

# Save brush stroke texture PNG
img_blurred.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/brush_stroke_bg.png')

print("Successfully generated paint brush background image: assets/brush_stroke_bg.png!")
