import os

folder = "blogs"

files = sorted(os.listdir(folder), reverse=True)

links = ""

for f in files:
    links += f'<li><a href="blogs/{f}">{f}</a></li>\n'

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>Daily Blogs</title>
</head>
<body>

<h1>Daily SEO Blogs</h1>

<ul>
{links}
</ul>

<p><a href="https://manychat.partnerlinks.io/nwkkk7vkps17">Try ManyChat</a></p>

</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html)

print("Index updated")
