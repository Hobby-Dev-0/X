
   
from asyncio import sleep

from telethon.errors import rpcbaseerrors

from . import *

lg_id = -100


@BaseClient.on(X_cmd(pattern="del$"))
async def delete_it(safai):
    msg_src = await safai.get_reply_message()
    if safai.reply_to_msg_id:
        try:
            await msg_src.delete()
            await safai.delete()
        except rpcbaseerrors.BadRequestError:
            pass


@BaseClient.on(X_cmd(pattern=r"purge"))
async def fastpurger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "**Fast Purge Completed!** \nPurged `" + str(count) + "` messages.",
    )

    await purg.client.send_message(
        lg_id, "#PURGE\n\nPurged `" + str(count) + "` messages."
    )
    await sleep(2)
    await done.delete()


@BaseClient.on(X_cmd(pattern=r"purgeme"))
async def purgeme(delme):
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "**Self Purge Complete!** Purged  `" + str(count) + "`  messages.",
    )
    await delme.client.send_message(
        lg_id, "#PURGE \nSelf Purged  `" + str(count) + "`  messages."
    )
    await sleep(2)
    i = 1
    await smsg.delete()


@BaseClient.on(X_cmd(pattern=r"sd"))
async def selfdestruct(destroy):
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    await destroy.client.send_message(
        lg_id,
        f"#SELF_DESTRUCT \n\nSelf Destruct message query done successfully!\n\n**SD Msg :**  `{text}`",
    )

