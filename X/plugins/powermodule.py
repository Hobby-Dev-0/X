
from . import *

async def restart(event):
    await eor(
        event,
        f"✅ **Restarted ᴀɴᴅᴇɴᴄᴇɴᴛᴏ** \n**Type** `{hl}ping` **after 1 minute to check if I am working !**",
    )
    await bash("pkill python3 && python3 -m userbot")


@BaseClient.on(X_cmd(pattern="restart"))
async def re(user):
    if user.fwd_from:
        return
    event = await eor(user, "Restarting Dynos ...")
    await restart(event)
