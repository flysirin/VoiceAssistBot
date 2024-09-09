# Voice Assist Bot

This is a telegram bot that allows you to chat with ChatGPT 3.5, takes audio and decrypts it into text.

## Environs
`OPENAI_API_KEY` - key from OpenAi   
`BOT_TOKEN `  - key from Telegram  
`ADMIN_IDS`   - your Telegram ID  
`WEBHOOK_URL`  - Refers to the URL where the Telegram bot will send updates  

#### This bot use `ffmpeg` for decode audio and video to mp3
`FFMPEG_BINARY_WINDOWS = f"services/ffmpeg_windows/ffmpeg.exe"`  
`FFMPEG_BINARY_LINUX = f"services/ffmpeg_linux/ffmpeg"`  


### Docker `python:3.10.11-alpine3.17`
`Docker` - light standard config with webhook and `curl` request
`Dockerfile_polling_http_sever` - light 'polling' configuration for Google Cloud with health check
