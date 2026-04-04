import os
import glob

files = glob.glob("*.html")
# don't modify ecommerce-development.html since it already has it
if "ecommerce-development.html" in files:
    files.remove("ecommerce-development.html")

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Navbar
    target1_hover = '<a href="web-design.html" class="px-4 py-3 hover:bg-white/10 text-sm border-b border-white/5">Web Design</a>'
    target1_active = '<a href="web-design.html" class="px-4 py-3 bg-white/10 text-sm border-b border-white/5">Web Design</a>'
    
    repl1_hover = target1_hover + '\n            <a href="ecommerce-development.html" class="px-4 py-3 hover:bg-white/10 text-sm border-b border-white/5">E-commerce Development</a>'
    repl1_active = target1_active + '\n            <a href="ecommerce-development.html" class="px-4 py-3 hover:bg-white/10 text-sm border-b border-white/5">E-commerce Development</a>'
    
    if target1_hover in content:
        content = content.replace(target1_hover, repl1_hover)
    elif target1_active in content:
        content = content.replace(target1_active, repl1_active)
        
    # Footer
    target2 = '<li><a href="web-design.html" class="hover:text-primary transition-colors">Web Design</a></li>'
    repl2 = target2 + '\n            <li><a href="ecommerce-development.html" class="hover:text-primary transition-colors">E-commerce Development</a></li>'
    
    if target2 in content:
        content = content.replace(target2, repl2)
        
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Updated navbars and footers successfully.")
