
   
import os
from . import *

ver = "0.1"
X = os.system("python --version") or "3.10.2"

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = (
    os.environ.get("ALIVE_PIC")
    or "https://te.legra.ph/file/2183fc07f904d2d0cae40.png"
)
pm_caption = "➥ **X:** `ONLINE`\n\n"
pm_caption += "➥ **ѕуѕтємѕ ѕтαтѕ**\n"
pm_caption += "➥ **тєℓєтнση νєяѕιση:** `1.24.0` \n"
pm_caption += f"➥ **ρутнση:** `{X}` \n"
pm_caption += "➥ **∂αтαвαѕє ѕтαтυѕ:**  `Functional`\n"
pm_caption += "➥ **¢υяяєηт вяαη¢н** : `master`\n"
pm_caption += f"➥ **νєяѕιση** : `{ver}`\n"
pm_caption += f"➥ **му вσѕѕ** : {DEFAULTUSER} \n"
pm_caption += f"➥ **ℓι¢єηѕє** : [𝘎𝘕𝘜 𝘈𝘧𝘧𝘦𝘳𝘰 𝘎𝘦𝘯𝘦𝘳𝘢𝘭 𝘗𝘶𝘣𝘭𝘪𝘤 𝘓𝘪𝘤𝘦𝘯𝘴𝘦 𝘷3.0](https://github.com/Hobby-Dev-0/X/blob/X/LICENSE/)\n"
pm_caption += "➥ **¢σρуяιgнт** : By [Aman Pandey](https://github.com/Hobby-Dev-0/)\n"


# only Owner Can Use it
@BaseClient.on(X_cmd(pattern="alive$"))
async def _(event):
    await event.get_chat()
    await event.delete()
    await BaseClient.send_file(event.chat_id, PM_IMG, caption=pm_caption)
