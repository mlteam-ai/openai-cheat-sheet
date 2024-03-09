import os

# Directory containing the HTML files
html_dir = './docs'  # Adjust the path as needed
html_files = [f for f in os.listdir(html_dir) if f.endswith('.html') and f != 'index.html']

# Start of the HTML index file
index_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of HTML Files</title>
</head>
<body>
    <h1>Index of HTML Files</h1>
    <ul>
'''

# Add links to all HTML files
for filename in html_files:
    path = os.path.join(html_dir, filename)
    index_content += f'        <li><a href="{filename}">{filename}</a></li>\n'

# End of the HTML index file
index_content += '''
    </ul>
</body>
</html>
'''

# Write the index file
with open(os.path.join(html_dir, 'index.html'), 'w') as index_file:
    index_file.write(index_content)
