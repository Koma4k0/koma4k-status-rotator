import requests as rq
import time as tm
import json as js
import os
import logging
from colorama import init as c, Fore as cl
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class koma4k_status_rotator:
    def __init__(self, d):
        self.token = d.get("token")
        self.clear_enabled = d.get("clear_enabled", False)
        self.clear_interval = d.get("clear_interval", 60)
        self.speed_rotator = d.get("speed_rotator", 5)
        self.status_sequence = d.get("status_sequence", [])
        self.status_index = 0
        self.emoji_index = 0
        self.messages = self.load_file("text.txt")
        self.emojis = self.load_file("emojis.txt")

    @staticmethod
    def load_file(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines()]
        except Exception as e:
            logging.error(f"Error loading file {file_name}: {e}")
            return []

    async def fetch_user_data(self):
        headers = {'Authorization': self.token}
        try:
            response = rq.get("https://discord.com/api/v10/users/@me", headers=headers)
            response.raise_for_status()
            user_data = response.json()
            return user_data.get("username", "Unknown User"), True
        except rq.RequestException as e:
            logging.error(f"Failed to fetch user data: {e}")
            return "Invalid token", False

    async def update_status(self, msg, emoji_name, emoji_id, status):
        headers = {'Authorization': self.token}
        try:
            user_settings = rq.get("https://discord.com/api/v10/users/@me/settings", headers=headers).json()
            custom_status = {
                "text": msg,
                "emoji_name": emoji_name,
                "emoji_id": emoji_id
            }
            payload = {
                "custom_status": custom_status,
                "activities": user_settings.get("activities", []),
                "status": status
            }
            rq.patch("https://discord.com/api/v10/users/@me/settings", headers=headers, json=payload)
        except rq.RequestException as e:
            logging.error(f"Failed to update status: {e}")

    @staticmethod
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def format_text(text, color):
        return f"{color}{text}{cl.RESET}"

    async def run(self):
        c()  # Initialize colorama
        while True:
            username, valid_token = await self.fetch_user_data()
            current_status = self.status_sequence[self.status_index % len(self.status_sequence)]
            msg = self.messages[self.status_index % len(self.messages)]
            ts = self.format_text(tm.strftime("%I:%M %p:"), cl.MAGENTA)

            token_color = cl.GREEN if valid_token else cl.RED
            masked_token = f"{self.token[:6]}******"
            colored_token = self.format_text(f"{masked_token} | {username}", token_color)
            colored_status = self.format_text(msg, cl.CYAN)

            emoji_data = self.emojis[self.emoji_index % len(self.emojis)].split(":")
            emoji_name, emoji_id = emoji_data[0], emoji_data[1] if len(emoji_data) == 2 else None

            logging.info(f"{ts} Status changed: {colored_token}. New status: {colored_status}. | Emoji: ({emoji_name}) | Status: {current_status}")
            await self.update_status(msg, emoji_name, emoji_id, current_status)

            self.status_index += 1
            self.emoji_index += 1

            await asyncio.sleep(self.speed_rotator)
            if self.clear_enabled and self.status_index % self.clear_interval == 0:
                self.clear_console()

if __name__ == "__main__":
    try:
        with open("config.json", "r") as config_file:
            config = js.load(config_file)
    except FileNotFoundError:
        logging.error("Configuration file not found.")
        exit(1)
    except js.JSONDecodeError:
        logging.error("Error decoding JSON from the configuration file.")
        exit(1)

    koma4k_ = koma4k_status_rotator(config)
    asyncio.run(koma4k_.run())
