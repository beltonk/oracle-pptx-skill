#!/usr/bin/env python3
"""Insert icons into PowerPoint slides based on icon specifications in JSON.

Usage:
    python insert-icons.py <input.pptx> <icons.json> <output.pptx>
    
Icons JSON format:
{
  "slide-1": {
    "icon": "RMIL_Database-and-AI_GenAI-Agents_Air_RGB.svg",
    "position": {"left": 11.0, "top": 1.2, "width": 1.0, "height": 1.0}
  }
}

For dark themes, use _Air_RGB.svg icons (light/white).
For light themes, use _Bark_RGB.svg icons (dark).
"""

import sys
import json
import tempfile
import subprocess
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches

def svg_to_png(svg_path, png_path, size=300):
    """Convert SVG to PNG using available methods"""
    try:
        import cairosvg
        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(png_path),
            output_width=size,
            output_height=size,
            background_color='transparent'
        )
        return True
    except ImportError:
        pass
    
    try:
        result = subprocess.run(
            ['rsvg-convert', '-w', str(size), '-h', str(size), 
             '-f', 'png', '-o', str(png_path), str(svg_path)],
            capture_output=True,
            timeout=10
        )
        if result.returncode == 0 and png_path.exists():
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    
    try:
        from svglib.svglib import svg2rlg
        from reportlab.graphics import renderPM
        drawing = svg2rlg(svg_path)
        if drawing:
            renderPM.drawToFile(drawing, str(png_path), fmt='PNG')
            return True
    except ImportError:
        pass
    
    print(f"  ⚠️  Warning: No SVG converter available")
    print("     Install: pip install cairosvg")
    print("     Or: brew install librsvg (macOS)")
    return False

def detect_theme_from_template(prs):
    """Detect if template is dark or light theme"""
    # Check background color of first slide
    try:
        if prs.slides:
            slide = prs.slides[0]
            if hasattr(slide.background, 'fill'):
                fill = slide.background.fill
                if hasattr(fill, 'fore_color') and hasattr(fill.fore_color, 'rgb'):
                    rgb = fill.fore_color.rgb
                    # Dark if RGB values are low
                    brightness = (rgb[0] + rgb[1] + rgb[2]) / 3
                    return 'dark' if brightness < 128 else 'light'
    except:
        pass
    return 'dark'  # Default to dark

def insert_icons(input_pptx, icons_json_path, output_pptx):
    """Insert icons based on JSON specifications"""
    
    with open(icons_json_path, 'r') as f:
        icon_specs = json.load(f)
    
    prs = Presentation(input_pptx)
    
    # Detect theme
    theme = detect_theme_from_template(prs)
    
    # Determine icon directory
    if theme == 'dark':
        icons_dir = Path(__file__).parent.parent / "resources" / "icons" / "light-theme"
        print(f"  📋 Detected dark theme, using light-colored (_Air_RGB) icons")
    else:
        icons_dir = Path(__file__).parent.parent / "resources" / "icons" / "dark-theme"
        print(f"  📋 Detected light theme, using dark-colored (_Bark_RGB) icons")
    
    inserted = 0
    skipped = 0
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        for slide_key, spec in icon_specs.items():
            slide_idx = int(slide_key.split('-')[1])
            
            if slide_idx >= len(prs.slides):
                print(f"  ⚠️  Slide {slide_idx} not found")
                skipped += 1
                continue
            
            slide = prs.slides[slide_idx]
            icon_file = spec.get('icon')
            position = spec.get('position', {})
            
            if not icon_file:
                skipped += 1
                continue
            
            # Auto-switch to correct theme variant
            if theme == 'dark' and '_Bark_' in icon_file:
                icon_file = icon_file.replace('_Bark_', '_Air_')
            elif theme == 'light' and '_Air_' in icon_file:
                icon_file = icon_file.replace('_Air_', '_Bark_')
            
            svg_path = icons_dir / icon_file
            if not svg_path.exists():
                print(f"  ❌ Icon not found: {icon_file}")
                skipped += 1
                continue
            
            # Convert SVG to PNG
            png_path = temp_path / f"icon_{slide_idx}.png"
            if not svg_to_png(svg_path, png_path, 300):
                skipped += 1
                continue
            
            # Insert icon - send to back layer
            try:
                left = Inches(position.get('left', 11.0))
                top = Inches(position.get('top', 1.2))
                width = Inches(position.get('width', 1.0))
                height = Inches(position.get('height', 1.0))
                
                pic = slide.shapes.add_picture(
                    str(png_path),
                    left, top,
                    width=width, height=height
                )
                
                # Send icon to back (behind text)
                slide.shapes._spTree.remove(pic._element)
                slide.shapes._spTree.insert(2, pic._element)
                
                inserted += 1
                print(f"  ✓ Slide {slide_idx}: {icon_file}")
            except Exception as e:
                print(f"  ❌ Failed on slide {slide_idx}: {e}")
                skipped += 1
        
        prs.save(output_pptx)
    
    print(f"\n✅ Icon insertion complete:")
    print(f"   Inserted: {inserted}")
    print(f"   Skipped: {skipped}")
    print(f"   Output: {output_pptx}")

def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    
    input_pptx = Path(sys.argv[1])
    icons_json = Path(sys.argv[2])
    output_pptx = Path(sys.argv[3])
    
    if not input_pptx.exists():
        print(f"Error: Input file not found: {input_pptx}")
        sys.exit(1)
    
    if not icons_json.exists():
        print(f"Error: Icons JSON not found: {icons_json}")
        sys.exit(1)
    
    print(f"🎨 Inserting icons with proper positioning...\n")
    
    try:
        insert_icons(str(input_pptx), str(icons_json), str(output_pptx))
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
