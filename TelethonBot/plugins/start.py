# By < @xditya >
# // @BotzHub //
from .. import RyoStar
from telethon import events, Button

public static InlineKeyboardMarkup TestInlineKeyboard { get; } = new InlineKeyboardMarkup           
    {
        InlineKeyboard = new []{new[] {new InlineKeyboardButton("Text1","Data1"), new InlineKeyboardButton("text1","data2")} }
    };

@RyoStar.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("SHARE ANH EM VÀI NHÓM NGON 🐰❤❤!\n\n• t.me/joinchat/yzw782riS9s1Njll \n\n• t.me/joinchat/p5yntuuOIOoxMDE9 \n\n• t.me/congdongnang",
                    buttons=[
                        [Button.url("NHÓM CỦA NẮNG ❤", url="https://t.me/nhomcuanang"),Button.url("KÊNH CỦA NẮNG 🌞",url="https://t.me/kenhcuanang")],
                        [Button.url("XEM VIDEO HOT TẠI ĐÂY 🔞",url="https://t.me/Hoahoantu_bot?startgroup=start")]
                    ])

# @RyoStar.on(events.callbackquery.CallbackQuery(data="example"))
# async def ex(event):
#    await event.edit("You clicked a button!")
