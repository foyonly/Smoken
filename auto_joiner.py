import time
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import (
    FloodWaitError, 
    UserDeactivatedBanError, 
    UsernameInvalidError, 
    ChannelInvalidError, 
    UserNotMutualContactError
)
import os

# Fill these with your Telegram API details
api_id = '25323871'
api_hash = '5b0348b25dc3983f656859b008686fb7'
session_file = 'group_joiner_session'  # This will save the session

# Load group links from file
group_links_file = 'group_links.txt'  # File where group links are stored (each link on a new line)

def load_group_links(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

# Login or reuse old session
def login():
    if os.path.exists(f"{session_file}.session"):
        client = TelegramClient(session_file, api_id, api_hash)
    else:
        client = TelegramClient(session_file, api_id, api_hash)
        client.start()  # One-time login will prompt only once
    return client

# Main function to join the groups
def join_groups(client, group_links):
    for link in group_links:
        try:
            print(f"Joining group: {link}")
            client(JoinChannelRequest(link))  # Attempt to join the group
            print(f"Successfully joined group: {link}")
            
            # Delay between joining groups (to avoid rate-limiting)
            time.sleep(5)  # 5 seconds between each request (adjust if needed)

        except ChannelInvalidError:
            print(f"Error: Group link invalid -> {link}")

        except UsernameInvalidError:
            print(f"Error: Username not found -> {link}")

        except FloodWaitError as e:
            print(f"Flood wait error, retry after {e.seconds} seconds")
            time.sleep(e.seconds)  # Sleep for the required flood wait duration

        except UserNotMutualContactError:
            print(f"Error: Mutual contact not found for joining -> {link}")

        except UserDeactivatedBanError:
            print(f"Error: Your account is banned or deactivated")

        except Exception as e:
            print(f"Unexpected error occurred: {str(e)}")

# Program starts here
if __name__ == "__main__":
    try:
        # Login using session
        client = login()
        client.connect()

        if not client.is_user_authorized():
            print("First time login, please provide credentials:")
            client.start()

        # Load group links
        group_links = load_group_links(group_links_file)

        if group_links:
            # Join the groups
            join_groups(client, group_links)
        else:
            print("No group links found in the file.")

    except Exception as e:
        print(f"Login failed or other error occurred: {str(e)}")

    finally:
        # Clean up
        client.disconnect()
