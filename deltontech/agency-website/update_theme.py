import os
import glob
import re

html_files = glob.glob(r'c:\Users\dell\Desktop\myweb\agency-website\*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Logo Text "DELTON TECHNOLOGIES" tracking and clean up any inline styles
    content = re.sub(
        r'<span class="([^"]*)tracking-tight([^"]*) text-\[#FDFFF5\] leading-none([^"]*)"(?:\s*style="[^"]*")?\s*>\s*DELTON\s+TECHNOLOGIES\s*</span>',
        r'<span class="\1tracking-[0.15em]\2 text-[#FDFFF5] leading-none\3">DELTON TECHNOLOGIES</span>',
        content,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
    )

    # 2. Update Slogan layout - replace entire <span> wrapping the slogan with flex justify-between.
    content = re.sub(
        r'<span\s+class="([^"]*?)text-\[#FDFFF5\]/80\s+uppercase\s+leading-none([^"]*)">\s*HERE\s+IS\s+YOUR\s+SOLUTION\s+PARTNER\s*</span>',
        r'<span class="\1text-[#FDFFF5]/80 uppercase leading-none w-full flex justify-between font-medium">\n            <span>HERE</span><span>IS</span><span>YOUR</span><span>SOLUTION</span><span>PARTNER</span>\n          </span>',
        content,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
    )
    # if slogan has newlines (due to formatting)
    content = re.sub(
        r'<span\s+class="([^"]*?)text-\[#FDFFF5\]/80\s+uppercase\s+leading-none([^"]*)">\s*HERE\s*\n\s*IS\s+YOUR\s+SOLUTION\s+PARTNER\s*</span>',
        r'<span class="\1text-[#FDFFF5]/80 uppercase leading-none w-full flex justify-between font-medium">\n            <span>HERE</span><span>IS</span><span>YOUR</span><span>SOLUTION</span><span>PARTNER</span>\n          </span>',
        content,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
    )

    # 3. Update "Get Started" buttons
    content = re.sub(
        r'bg-primary (hover:bg-primary/90 rounded-full[^\"]*)"([^>]*)>\s*Get\s*Started\s*</a>',
        r'bg-[#FDFFF5] text-dark hover:bg-white rounded-full text-sm font-medium transition-transform hover:scale-105 shadow-[0_0_15px_rgba(253,255,245,0.4)]"\2>Get Started</a>',
        content,
        flags=re.IGNORECASE | re.MULTILINE
    )
    

    # 4. Update "Start Your Project" button in index.html hero
    content = re.sub(
        r'bg-primary (rounded-full font-medium text-lg text-center[^\"]*)"([^>]*)>\s*Start\s*\n\s*Your\s*Project\s*</a>',
        r'bg-[#FDFFF5] text-dark \1 shadow-[0_0_20px_rgba(253,255,245,0.4)]"\2>Start Your Project</a>',
        content,
        flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files.")
