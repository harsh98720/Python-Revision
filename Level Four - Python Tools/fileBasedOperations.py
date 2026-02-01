with open('Level Four - Python Tools/content.txt', 'r') as f:
    content = f.readlines()

# Empty check
if not content:
    print("Empty Content")
else:
    print(content)

# Line count
line_count = len(content)
print("Line count:", line_count)

# Word count (RIGHT WAY)
word_count = 0
for line in content:
    word_count += len(line.split())

print("Word count:", word_count)
