import os

# Table of Contents
table_of_contents = [
    "Introduction to Computer Networking",
    "Networking Basics",
    "Networking Protocols",
    "TCP/IP Fundamentals",
    "Network Devices",
    "Local Area Networks (LAN)",
    "Wide Area Networks (WAN)",
    "Network Security",
    "Troubleshooting Networks",
    "Resources"
]

# Content for each README.md
readme_content = """# {topic}

This directory covers the topic of {topic}. It contains resources and materials to help you learn and understand the fundamentals of {topic} in computer networking.

Feel free to explore the content in this directory to enhance your knowledge about {topic} in computer networking.

Happy learning! 🚀
"""

# Function to create directories and README.md
def create_directories_and_readme(table_of_contents):
    for item in table_of_contents:
        directory_name = item.lower().replace(" ", "_")
        try:
            os.makedirs(directory_name, exist_ok=True)  # Create parent directories if they don't exist
            print(f"Directory '{directory_name}' created.")
        except Exception as e:
            print(f"Error creating directory '{directory_name}': {e}")
        
        # Create README.md inside the directory
        readme_file_path = os.path.join(directory_name, "README.md")
        with open(readme_file_path, "w") as readme_file:
            readme_file.write(readme_content.format(topic=item))

            print(f"README.md created for '{item}'.")

if __name__ == "__main__":
    create_directories_and_readme(table_of_contents)

