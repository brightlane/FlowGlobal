from datetime import date
import random

affiliate_url = "https://manychat.partnerlinks.io/nwkkk7vkps17"

topics = [
    "Instagram DM automation",
    "chatbot funnels",
    "WhatsApp marketing automation",
    "AI customer engagement",
    "sales automation systems"
]

topic = random.choice(topics)
today = date.today()

posts = {
    "x": f"🚀 {topic.title()} is changing how businesses grow in 2026.\n\nAutomate leads, sales & messaging with chatbots.\n👉 {affiliate_url}",

    "linkedin": f"""
📊 {topic.title()} is transforming digital marketing in 2026.

Businesses are using automation to:
- generate leads faster
- reduce manual messaging
- scale customer engagement

Learn more: {affiliate_url}
""",

    "facebook": f"""
🔥 New automation strategy: {topic}

Businesses are scaling faster using chatbot systems.

Start here 👉 {affiliate_url}
"""
}

with open(f"social-{today}.txt", "w") as f:
    for platform, text in posts.items():
        f.write(f"\n--- {platform.upper()} ---\n{text}\n")

print("Social posts generated")
