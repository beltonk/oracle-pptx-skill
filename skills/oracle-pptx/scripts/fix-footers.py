#!/usr/bin/env python3
"""
Fix footer display in Oracle PowerPoint presentations.

Footers are controlled by XML attributes in presentation.xml and slide*.xml files,
not by placeholder content. This script enables footer display programmatically.
"""

import sys
import zipfile
import os
from pathlib import Path
from lxml import etree

def fix_footers(pptx_path: Path):
    """Enable footers on all slides by modifying XML attributes."""
    
    if not pptx_path.exists():
        print(f"Error: File not found: {pptx_path}")
        return False
    
    # Create temp directory
    temp_dir = pptx_path.parent / f"_temp_{pptx_path.stem}"
    temp_dir.mkdir(exist_ok=True)
    
    try:
        # Extract PPTX
        with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        slides_dir = temp_dir / "ppt" / "slides"
        if not slides_dir.exists():
            print(f"Error: No slides directory found")
            return False
        
        # Fix each slide
        slide_files = sorted(slides_dir.glob("slide*.xml"))
        fixed_count = 0
        
        for slide_file in slide_files:
            tree = etree.parse(str(slide_file))
            root = tree.getroot()
            
            # Find commonSlideData element
            ns = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'}
            csd = root.find('.//p:cSld', ns)
            
            if csd is not None:
                # Check if showMasterSp attribute exists
                show_master = csd.get('showMasterSp')
                
                if show_master != '1':
                    # Set to '1' to show master elements (including footer)
                    csd.set('showMasterSp', '1')
                    tree.write(str(slide_file), xml_declaration=True, encoding='UTF-8', standalone=True)
                    fixed_count += 1
        
        print(f"✅ Fixed footers on {fixed_count} slides")
        
        # Repackage PPTX
        output_path = pptx_path.parent / f"{pptx_path.stem}-fixed.pptx"
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root_dir, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = Path(root_dir) / file
                    arcname = file_path.relative_to(temp_dir)
                    zipf.write(file_path, arcname)
        
        print(f"✅ Saved fixed presentation: {output_path}")
        return True
        
    finally:
        # Cleanup
        import shutil
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix-footers.py <presentation.pptx>")
        sys.exit(1)
    
    pptx_path = Path(sys.argv[1])
    success = fix_footers(pptx_path)
    sys.exit(0 if success else 1)
