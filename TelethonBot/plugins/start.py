# By < @xditya >
# // @BotzHub //
from .. import RyoStar
from telethon import events, Button

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

@RyoStar.on(events.NewMessage(pattern='hello'))
                async def on_greeting(event):
                    '''Greets someone'''
                    await event.reply('Hi')

                for callback, event in client.list_event_handlers():
                    print(id(callback), type(event))
        """
        return [(callback, event) for event, callback in self._event_builders] 
