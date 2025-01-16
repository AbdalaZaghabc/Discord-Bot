# Discord Music Bot 🎵

A Python-based music bot for Discord that plays high-quality audio in voice channels. This bot integrates multiple libraries to fetch and stream music from YouTube, ensuring smooth and reliable performance. Created since my friends and I wanted a free bot that plays music when asked.

The prefix is a '.' For example: ".play Yellow Coldplay"

## Features
- Plays music directly from YouTube.
- Supports a wide range of audio formats.
- Provides seamless integration with Discord voice channels.
- Lightweight and efficient design.

## Technologies Used
- **[discord.py](https://github.com/Rapptz/discord.py)**: A Python wrapper for the Discord API.
- **[PyNaCl](https://github.com/pyca/pynacl)**: Used for voice support in Discord.
- **[youtube-search-python (ytsearch)](https://github.com/alexmercerind/youtube-search-python)**: Enables YouTube search functionality.
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: Fetches and processes audio from YouTube links.
- **[FFmpeg](https://ffmpeg.org/)**: Handles audio encoding and streaming.

## Environment Variables
The bot relies on environment variables for secure configuration. The path to ffempg has to be explicit in the environment variables of your windodws system.
