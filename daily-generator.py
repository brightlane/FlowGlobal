from datetime import date
import random

affiliate_url = "https://manychat.partnerlinks.io/nwkkk7vkps17"

topics = [
    "Instagram DM automation for business growth",
    "chatbot funnels for lead generation",
    "WhatsApp marketing automation strategies",
    "AI chatbot marketing systems",
    "sales automation with ManyChat",
    "customer engagement automation funnels"
]

keyword = random.choice(topics)
today = date.today()

title = f"{keyword.title()} - Daily Automation Guide {today}"

description = f"Learn how {keyword} helps businesses scale using chatbot automation systems like ManyChat."

content = f"""
<h1>{title}</h1>

<p>Businesses today rely heavily on automation systems to manage customer communication and generate leads efficiently.</p>

<h2>Why This Matters</h2>
<p>{keyword} is one of the fastest growing strategies in digital marketing because it reduces manual work and increases conversion rates.</p>

<h2>How ManyChat Helps</h2>
<p>ManyChat allows you to build automated chatbot funnels that capture leads, respond instantly, and guide users toward conversion.</p>

<p><a href="{affiliate_url}">👉 Start with ManyChat Automation</a></p>

<h2>Use Cases</h2>
<ul>
<li>Instagram DM funnels</li>
<li>WhatsApp customer automation</li>
<li>Facebook Messenger marketing</li>
<li>E-commerce lead generation</li>
</ul>

<h2>Strategy Tip</h2>
<p>Always segment your audience and personalize chatbot flows for higher engagement and conversion rates.</p>

<h2>Final CTA</h2>
<p><a href="{affiliate_url}">👉 Launch Your Automation System with ManyChat</a></p>
"""

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="ManyChat, chatbot automation, marketing funnels, AI business tools">
</head>

<body>
{content}
</body>
</html>
"""

filename = f"blog-{today}.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(html)

print("Generated:", filename)
