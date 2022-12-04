import os
import openai
from dotenv import load_dotenv
from pyrogram import Client, filters, types, enums
import asyncio


load_dotenv()
STRING_SESSION = os.environ.get("STRING_SESSION")
openai.api_key = os.environ.get("OPENAI_API_KEY")
# Initializing telegram app
app = Client("my_bot", session_string=STRING_SESSION)


def make_request(prompt: str) -> str:
    """request maker

    Args:
        prompt (str): the question which will be answered by AI

    Returns:
        str: The AI answer
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


@app.on_message(filters.command(['start']))
async def start(client: Client, message: types.Message):
    """Start message"""
    await message.reply_text(
        "This is an Ai Chat bot, created using OpenAi APi\n"
        "Send a question and the AI bot will reply")


@app.on_message(filters.private & filters.text)
async def getting_question(client: Client, message: types.Message):
    """Getting the question from user"""
    question = message.text
    my_message = await message.reply_text("getting the answer ...", quote=True)
    # pushing task to the event loop
    asyncio.create_task(handeling_query(my_message, question))


async def handeling_query(my_message: types.Message, query: str):
    # convert make_request function to thread, this way the event loop won't be blocked
    answer = await asyncio.to_thread(make_request, query)
    try:
        await my_message.edit(answer, parse_mode=enums.ParseMode.DISABLED)
    except Exception as err:
        await my_message.edit(str(err), True)


# Running the app
app.run()
