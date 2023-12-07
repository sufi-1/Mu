import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
# للنشر المحلي
if os.path.exists(".env"):
    load_dotenv(".env")
# الفارات
API_ID = 27703508
API_HASH = 4cb84dd9cd3c3ee0bdb5c720fcfb7dba
SESSION = "AgGmuNQAfE_nD0lmghrMjufYbhg7eaHSkTz6F3Kfhsx5kbdR4kbZygwP8fibvDa559FjnFHUlohFaqPU0GOdiNGr2ThkCUHDZPgVz9RZa8YKiv9GrsmgQqjudBRPRZ4mFFGP3qGN9dOo-B6bR8ODuolrQ2vOrwzK4bSyD9V2JhOAnRqCD9PnlaqlyrAagEUIq1Cs_roe_N2N-xTIMm_QT93_qBd_XnneZMa3uui4i4b5F35ZXdFME8YPp8c8TtzVXuOWlCAywYobhevwRGSbVT5tF2-yAmBRXMrebltn0GGzoaohBbhqaDGaebYNy-dXjtUZu4X0o6jl1DuqetJFfrs2UbLVQAAAAAGEUw3xAA"
HNDLR = "."
SUDO_USERS = 6515002865
contact_filter = filters.create(    lambda _, __, message: (message.from_user and message.from_user.is_contact)    or message.outgoing)
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicTelethon"))
call_py = PyTgCalls(bot)
