from PIL import Image, ImageDraw, ImageFilter
import math, random

# Dimensions for high-res paint brush stroke asset
width, height = 900, 1000
img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Theme colors (matching website palette):
# #FF6B00 (Vibrant Primary Orange), #FF8C38 (Warm Orange), #FFB693 (Peach Accent), #D04500 (Deep Crimson Red-Orange)
colors = [
    (255, 107, 0, 255),   # Primary vibrant orange
    (255, 140, 56, 230),  # Warm apricot orange
    (210, 65, 0, 240),    # Deep crimson orange
    (255, 190, 150, 200), # Soft peach highlight
]

center_x, center_y = width // 2, height // 2

def draw_thick_brush(draw, start, end, start_w, end_w, color, bristles=90):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    length = math.hypot(dx, dy)
    angle = math.atan2(dy, dx)
    
    steps = int(length * 1.5)
    for i in range(steps):
        t = i / float(steps)
        # Organic wave curvature
        cx = start[0] + dx * t + math.sin(t * math.pi * 2) * 25
        cy = start[1] + dy * t + math.cos(t * math.pi * 1.5) * 15
        
        cw = start_w + (end_w - start_w) * (1.0 - math.pow(t - 0.5, 2) * 2.8)
        
        for b in range(bristles):
            offset_r = (random.random() - 0.5) * cw
            bx = cx + offset_r * math.cos(angle + math.pi/2)
            by = cy + offset_r * math.sin(angle + math.pi/2)
            
            b_size = random.uniform(4, 12)
            alpha = int(color[3] * random.uniform(0.5, 1.0))
            b_color = (color[0], color[1], color[2], alpha)
            
            draw.ellipse([bx - b_size, by - b_size, bx + b_size, by + b_size], fill=b_color)

# Layer 1: Wide dark crimson stroke sweep
draw_thick_brush(draw, (150, 180), (750, 820), 320, 380, colors[2], bristles=120)

# Layer 2: Main vibrant orange stroke
draw_thick_brush(draw, (180, 220), (720, 780), 380, 440, colors[0], bristles=140)

# Layer 3: Secondary energetic cross-stroke
draw_thick_brush(draw, (750, 220), (160, 750), 300, 360, colors[1], bristles=100)

# Layer 4: Warm peach light highlight stroke
draw_thick_brush(draw, (280, 280), (620, 680), 220, 280, colors[3], bristles=80)

# Layer 5: Paint splatters and droplets
for _ in range(160):
    angle = random.uniform(0, math.pi * 2)
    dist = random.uniform(220, 420)
    sx = center_x + math.cos(angle) * dist
    sy = center_y + math.sin(angle) * dist
    
    radius = random.uniform(5, 22)
    color = random.choice(colors)
    draw.ellipse([sx - radius, sy - radius, sx + radius, sy + radius], fill=color)

# Save crisp high-res brush stroke asset
img.save('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/brush_stroke_bg.png')
print("Generated bold, vibrant paint brush background: assets/brush_stroke_bg.png!")
