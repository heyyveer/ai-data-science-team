import re

file_path = r"c:\Users\Asus\Documents\GitHub\ai-data-science-team\apps\ai-pipeline-studio-app\app.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Match use_container_width=True (case-insensitive for True just in case)
pattern = r"\buse_container_width\s*=\s*[Tt]rue\b"

matches = re.findall(pattern, content)
print(f"Found {len(matches)} occurrences of use_container_width=True")

if len(matches) > 0:
    new_content, count = re.subn(pattern, 'width="stretch"', content)
    print(f"Replaced {count} occurrences.")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("app.py successfully updated and saved.")
else:
    print("No occurrences found.")
