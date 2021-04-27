# By < @xditya >
# // @BotzHub //
from .. import RyoStar
from telethon import events, Button

@RyoStar.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("SHARE ANH EM 2 GROUP NGON 🐰❤❤!",
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/nhomcuanang")],
                        [Button.inline("Inline Button",data="https://t.me/kenhcuanang")]
                    ])

@RyoStar.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")
