# 🔄 Discord Status Rotator

## 📖 Overview

Koma4k Status Rotator is a simple Python script that automates the rotation of your Discord custom status, emojis, and online presence.
It provides an efficient solution for maintaining a dynamic and engaging Discord profile.

## ✨ Key Features

- 🔁 Automated custom status message rotation
- 🎭 Systematic emoji cycling
- <img src="statuses/online.png" width="16" height="16"> <img src="statuses/idle.png" width="16" height="16"> <img src="statuses/dnd.png" width="16" height="16"> Intelligent presence status rotation (online, idle, do not disturb)
- ⏱️ Customizable rotation speed
- 🧼 Optional console clearing for enhanced readability
- 🔐 Secure token management
- 📊 Real-time console logging

## 🛠️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/koma4k0/koma4k-status-rotator.git
   ```
2. Navigate to the project directory:
   ```
   cd koma4k-status-rotator
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

1. Configure `config.json` with your Discord token and preferences:
   ```json
   {
     "token": "YOUR_DISCORD_TOKEN",
     "status_sequence": ["online", "idle", "dnd"],
     "clear_enabled": true,
     "clear_interval": 15,
     "speed_rotator": 5
   }
   ```
2. Populate `text.txt` with desired status messages (one per line).
3. Populate `emojis.txt` with desired emojis (one per line, format: `emoji_name:emoji_id` for custom emojis).

## 🚀 Usage

Run the script:
```
python main.py
```

## 📊 Logging

The application offers detailed logging in the console, including:
- ⏰ Precise timestamps of status alterations
- 👤 Current username (with masked token)
- 💬 Updated status message
- 😃 Active emoji
- <img src="statuses/online.png" width="16" height="16"> Current presence status

## ⚠️ Legal Disclaimer

Please be advised that the use of this script may potentially violate Discord's Terms of Service. Utilization is at the user's own risk. Koma4k disclaims any responsibility for consequences resulting from its use.
