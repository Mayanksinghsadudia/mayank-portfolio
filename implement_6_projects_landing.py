import os
import re

# Load index.html
with open('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add hidden styling for cards beyond top 6
# Mark the first 6 cards without hidden class, and cards 7-29 with class 'project-card-extra'
pattern_card = r'(<div class="project-card"[^>]*>)'

cards = re.findall(pattern_card, html)
print(f"Total project cards found in index.html: {len(cards)}")

# Update index.html to add class 'project-card-extra' to cards beyond index 5 (card 7 to 29)
card_counter = 0

def card_replacer(match):
    global card_counter
    card_counter += 1
    full_tag = match.group(1)
    if card_counter > 6:
        if 'class="project-card' in full_tag:
            return full_tag.replace('class="project-card', 'class="project-card project-card-extra"')
    return full_tag

new_html = re.sub(pattern_card, card_replacer, html)

# Add "View All Projects (29)" button right after the projects-grid </div>
button_html = '''        <!-- View All Projects Button -->
        <div style="text-align: center; margin-top: 40px;" id="view-all-container">
          <button id="view-all-projects-btn" class="btn-primary" style="padding: 14px 32px; font-size: 14px; letter-spacing: 1px; cursor: pointer; display: inline-flex; align-items: center; gap: 10px;">
            <span class="material-symbols-outlined">grid_view</span>
            View All Projects (29)
          </button>
        </div>'''

grid_end_pattern = r'(</div>\s*</div>\s*</section>\s*<!-- 04 CONTACT SECTION -->)'
grid_end_replacement = button_html + '\n\n' + r'\1'

new_html_with_btn = re.sub(grid_end_pattern, grid_end_replacement, new_html)

with open('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html_with_btn)

print("SUCCESS: Updated index.html with 6 initial projects on landing page and 'View All Projects (29)' button!")
