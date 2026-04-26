import os

# Define the affiliate URL
affiliate_url = "https://manychat.partnerlinks.io/nwkkk7vkps17"

# Define the directory containing your HTML blog files
directory = './your-website-folder'

# Function to update links in the HTML blog file
def update_affiliate_links(file_path, affiliate_url):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace placeholder with the actual affiliate link
        content = content.replace("https://manychat.partnerlinks.io/YOUR_AFFILIATE_ID", affiliate_url)

        # You can also add any other replacement rules for your blog content here
        # For example, updating CTAs or other references to ManyChat with your affiliate link
        
        # Save the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Affiliate link updated in: {file_path}")
    
    except Exception as e:
        print(f"Error updating file {file_path}: {e}")

# Loop through all HTML files in the specified directory
def process_blog_files():
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            update_affiliate_links(file_path, affiliate_url)

# Run the script to update all blog files
if __name__ == "__main__":
    process_blog_files()
