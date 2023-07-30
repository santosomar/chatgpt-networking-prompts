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

# Function to create directories
def create_directories(table_of_contents):
    for item in table_of_contents:
        directory_name = item.lower().replace(" ", "_")
        try:
            os.mkdir(directory_name)
            print(f"Directory '{directory_name}' created.")
        except FileExistsError:
            print(f"Directory '{directory_name}' already exists.")
        except Exception as e:
            print(f"Error creating directory '{directory_name}': {e}")

if __name__ == "__main__":
    create_directories(table_of_contents)

