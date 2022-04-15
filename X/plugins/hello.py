from . import *

@BaseClient.on(X_cmd(pattern="Hi"))
async def _(aman):
    if aman.fwd_from:
        return
    try:
        await aman.edit(chat_id, "Hello! My Friend")
    except:
        await aman.delete()
        await BaaseClient.send_message(chat_id, "Hello! My Friend")
