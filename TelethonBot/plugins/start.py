# By < @xditya >
# // @BotzHub //
from .. import RyoStar
from telethon import events, Button

@RyoStar.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("SHARE [ANH EM](https://halotravel.vn/wp-content/uploads/2020/07/thach_trangg_101029297_573874646879779_1794923475739360981_n.jpg) VÀI NHÓM NGON 🐰❤❤!\n\n• t.me/joinchat/yzw782riS9s1Njll \n\n• t.me/joinchat/p5yntuuOIOoxMDE9 \n\n• t.me/congdongnang",
                    buttons=[
                        [Button.url("NHÓM CỦA NẮNG ❤", url="https://t.me/nhomcuanang"),Button.url("KÊNH CỦA NẮNG 🌞",url="https://t.me/kenhcuanang")],
                        [Button.url("XEM VIDEO HOT TẠI ĐÂY 🔞",url="https://t.me/Hoahoantu_bot?startgroup=start")]
                    ])
