#!/usr/bin/env python3
"""Insert icons into PowerPoint slides based on icon specifications in JSON.

Usage:
    python insert-icons.py <input.pptx> <icons.json> <output.pptx>
    
Icons JSON format:
{
  "slide-1": {
    "icon": "RMIL_Database-and-AI_GenAI-Agents_Bark_RGB.svg",
    "position": {"left": 10.5, "top": 1.5, "width": 1.0, "height": 1.0}
  },
  "slide-5": {
    "icon": "RMIL_Business_Analytics_Bark_RGB.svg",
    "position": {"left": 0.5, "top": 1.2, "width": 1.2, "height": 1.2}
  }
}

Note: SVG files will be converted to PNG for PowerPoint compatibility.
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
        # Try cairosvg first (best quality)
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
        # Try using rsvg-convert (if available on system)
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
        # Try svglib + reportlab
        from svglib.svglib import svg2rlg
        from reportlab.graphics import renderPM
        drawing = svg2rlg(svg_path)
        if drawing:
            renderPM.drawToFile(drawing, str(png_path), fmt='PNG')
            return True
    except ImportError:
        pass
    
    print(f"  ⚠️  Warning: No SVG converter available, skipping {svg_path.name}")
    print("     Install cairosvg: pip install cairosvg")
    print("     Or install librsvg: brew install librsvg (macOS)")
    return False

def insert_icons(input_pptx, icons_json_path, output_pptx):
    """Insert icons based on JSON specifications"""
    
    # Load icon specifications
    with open(icons_json_path, 'r') as f:
        icon_specs = json.load(f)
    
    prs = Presentation(input_pptx)
    icons_dir = Path(__file__).parent.parent / "resources" / "icons" / "dark-theme"
    
    inserted = 0
    skipped = 0
    
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        for slide_key, spec in icon_specs.items():
            # Parse slide index
            slide_idx = int(slide_key.split('-')[1])
            
            if slide_idx >= len(prs.slides):
                print(f"  ⚠️  Slide {slide_idx} not found, skipping")
                skipped += 1
                continue
            
            slide = prs.slides[slide_idx]
            icon_file = spec.get('icon')
            position = spec.get('position', {})
            
            if not icon_file:
                print(f"  ⚠️  No icon specified for {slide_key}, skipping")
                skipped += 1
                continue
            
            svg_path = icons_dir / icon_file
            if not svg_path.exists():
                print(f"  ❌ Icon not found: {icon_file}")
                skipped += 1
                continue
            
            # Convert SVG to PNG
            png_path = temp_path / f"icon_{slide_idx}.png"
            if not svg_to_png(svg_path, png_path):
                skipped += 1
                continue
            
            # Insert icon
            try:
                left = Inches(position.get('left', 10.5))
                top = Inches(position.get('top', 1.5))
                width = Inches(position.get('width', 1.0))
                height = Inches(position.get('height', 1.0))
                
                slide.shapes.add_picture(
                    str(png_path),
                    left, top,
                    width=width, height=height
                )
                inserted += 1
                print(f"  ✓ Slide {slide_idx}: {icon_file}")
            except Exception as e:
                print(f"  ❌ Failed to insert icon on slide {slide_idx}: {e}")
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
    
    print(f"🎨 Inserting icons from specifications...\n")
    
    try:
        insert_icons(str(input_pptx), str(icons_json), str(output_pptx))
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
