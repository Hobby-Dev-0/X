
from . import *

async def restart(rstart):
    await eor(
        rstart,
        f"✅ **Restarted UserBot X** \n**Type** `{HANDLER}ping` **after 1 minute to check if I am working !**",
    )
    await print("restarted X")
    await bash("pkill python3 && python3 -m userbot")


@BaseClient.on(X_cmd(pattern="restart"))
async def re(user):
    if user.fwd_from:
        return
    event = await eor(user, "Restarting UserBot X ...")
    await restart(rstart)
