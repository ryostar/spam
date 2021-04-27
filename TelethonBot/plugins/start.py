# By < @xditya >
# // @BotzHub //
from .. import RyoStar
from telethon import events, Button

@RyoStar.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("SHARE ANH EM VÀI NHÓM NGON 🐰❤❤! \n\n 1️⃣ t.me/joinchat/yzw782riS9s1Njll \n 2️⃣ t.me/joinchat/p5yntuuOIOoxMDE9",
                    buttons=[
                        [Button.url("NHÓM CỦA NẮNG ❤", url="https://t.me/nhomcuanang")],
                        [Button.url("KÊNH CỦA NẮNG 🌞",url="https://t.me/kenhcuanang")]
                    ])

@RyoStar.on(events.NewMessage(incoming=True, pattern="start"))
async def start(event):
    await event.reply("SHARE ANH EM 2 GROUP NGON 🐰❤❤!",
                    buttons=[
                        [Button.url("NHÓM CỦA NẮNG ❤", url="https://t.me/nhomcuanang")],
                        [Button.url("KÊNH CỦA NẮNG 🌞",url="https://t.me/kenhcuanang")]
                    ])

@RyoStar.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")
