# By < @xditya >
# // @BotzHub //
from .. import RyoStar
from telethon import events, Button

@RyoStar.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("EVENT GROUP LIVE FREE\n!❤🤒😭🎀🤨😍🐰❤!\n\nNữ Sinh - IDOL - Đủ Thể Loại - 2K => 2k3 - SOME - MÓC BƯỚM - GIAO LƯU - NHÀ NGHỈ 🤟\n\n♯ Xem hướng dẫn: [BẤM VÀO ĐÂY](http://bit.ly/3dYTXJr)\n\nCó Bán Vé Vip LIVE ZALO 🤘 ༻@Ryo_Star༺",
                    buttons=[
                        [Button.url("ıllıllı BẤM NÚT PHÍA DƯỚI ıllıllı", url="http://t.me/hoptacxa0")],
[Button.url("PHÒNG LIVE MỐC BÍM SỐ 1 🎬 ",url="http://bit.ly/3u34kRW")],
                        [Button.url("PHÒNG LIVE ẸT ẸT SOME SỐ 2 🎬",url="http://bit.ly/3sWInCE")],
[Button.url("PHÒNG LIVE TÂM SỰ SỐ 3 🎬",url="http://bit.ly/3x2JVhW")],
[Button.url("SÉT KÈO IDOL CALL UY TÍN🔞",url="http://t.me/joinchat/HFMeDVI4K_czMjBl")]
                    ])
