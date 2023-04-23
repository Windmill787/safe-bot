# Parser telegram bot
Tracks multiple channels messages then looks for matches and duplicates message to bot<br>
No ads, no spam, no bot messages, just relevant messages

# Instruction
1. Set environment variables: BOT_KEY, API_ID, API_HASH. BOT_KEY - your telegram bot key, which will send you messages. API_ID - telegram api id. API_HASH - telegram api hash.
2. Execute "python main.py channel1,channel2 word1,word2". This will request your telegram credentials to confirm that is you. And also generate session_name.session file, so you will authenticate yourself only once
3. Now you will receive message from your bot, every time message with needed words appear in needed channels

After session_name.session file is generated you can also run docker compose, which will copy your session to container, so you don't need to auth.<br>
If you run docker compose don't forget to create ".env" file and set environment variables inside. Take a look to .env.example