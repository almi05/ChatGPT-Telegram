import openai
import telegram
import os

openai.api_key = "<your OpenAI API key>"
bot = telegram.Bot(token="<your Telegram bot token>")

# Handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat_id, text="Hello! I am a Telegram bot powered by ChatGPT. Send me a message and I will try to respond.")

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def respond(message):
    # Use ChatGPT to generate a response to the message
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Send the response as a message
    bot.send_message(chat_id=message.chat_id, text=response.text)

# Run the bot
bot.polling()
