from . import *

async def restart(event):
    await eor(
        event,
        f"✅ **Restarted UserBot X** \n**Type** `{HANDLER}ping` **after 1 minute to check if I am working !**",
    )
    try:
        os.system(print("Restarted - X!"))
        
    except:
        rest = "Restarted - X"
        x = None
        if x is not None:
            os.system(f"print({rest})"
    await bash("pkill python3 && python3 -m userbot")


@BaseClient.on(X_cmd(pattern="restart"))
async def re(user):
    if user.fwd_from:
        return
    event = await eor(user, "Restarting UserBot X ...")
    await restart(event)
