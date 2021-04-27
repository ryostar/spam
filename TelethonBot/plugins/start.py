# By < @xditya >
# // @BotzHub //
from .. import RyoStar
from telethon import events, Button

@RyoStar.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("SHARE ANH EM VÀI NHÓM NGON 🐰❤❤!\n\n• t.me/joinchat/yzw782riS9s1Njll \n\n• t.me/joinchat/p5yntuuOIOoxMDE9 \n\n• t.me/congdongnang",
                    buttons=[
                        [Button.url("NHÓM CỦA NẮNG ❤", url="https://t.me/nhomcuanang"),Button.url("KÊNH CỦA NẮNG 🌞",url="https://t.me/kenhcuanang")],
                        [Button.url("XEM VIDEO HOT TẠI ĐÂY 🔞",url="https://t.me/ditmemay_bot?startgroup=start")]
                    ])

@RyoStar.on(events.NewMessage(incoming=True, pattern="start"))
async def start(event):
    await event.reply("SHARE ANH EM 2 GROUP NGON 🐰❤❤!",
                    buttons=[
                        [Button.url("NHÓM CỦA NẮNG ❤", url="https://t.me/nhomcuanang"),Button.url("NHÓM CỦA NẮNG ❤", url="https://t.me/nhomcuanang")],
                        [Button.url("KÊNH CỦA NẮNG 🌞",url="https://t.me/kenhcuanang")]
                    ])

@RyoStar.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")
