# By < @xditya >
# // @BotzHub //
from .. import RyoStar
from telethon import events, Button

@RyoStar.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("👌❤❤😢🤖❤\nTẢI APP XEM LIVE MIỄN PHÍ\n📜❤🤒😭🤨😍🐰❤!\n\n• Tải app [HOTLIVE32.COM](HOTLIVE32.COM)\n• Tải app [MMLIVE](mm636.vip)\n• Tải app [QQLIVE](http://WWW.QQL849.COM) \n\n CHỈ CẦN NẠP 20K LÀ VÔ ĐƯỢC PHÒNG VIP BAO PHÊ ❤❤❤🔞🔞",
                    buttons=[
                        [Button.url("Tải ngay HOTLIVE32.COM ❤", url="hotlive32.com")],
[Button.url("Tải ngay MM636.VIP 🔞",url="mm636.vip")],
                        [Button.url("Tải ngay QQL849.COM 🔞",url="QQL849.COM")]
                    ])
