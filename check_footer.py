import glob

html_files = glob.glob('*.html')

missing = []
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        if 'datenschutzerklaerung.html' not in content:
            missing.append(f)

print("Files missing datenschutzerklaerung link:")
for f in missing:
    print(f"  {f}")
print(f"\nTotal: {len(missing)} files")
