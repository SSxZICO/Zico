# meta developer: @gde_zico
import asyncio
from telethon import events
from .. import loader, utils


@loader.tds
class FarmMonacoMod(loader.Module):
    """Модуль для фарминга @xSpinBot в указанном чате или теме.
    Запуск:
    - Для обычного чата: .farm2 [chat_id]
    - Для темы: .farm2 [chat_id] [topic_id]"""

    strings = {"name": "xSpinBot module by ssxzico"}

    def __init__(self):
        self.tasks = []
        self.chat_id = None
        self.topic_id = None

    async def b_run(self, client):
        while True:
            try:
                if self.topic_id:
                    await client.send_message(self.chat_id, "!б 5000", reply_to=self.topic_id)
                else:
                    await client.send_message(self.chat_id, "!б 5000")
                await asyncio.sleep(4)
            except Exception as e:
                print(f"Ошибка отправки: {e}")
                await asyncio.sleep(10)

    @loader.unrestricted
    @loader.ratelimit
    async def farm2cmd(self, message):
        """Запустить автофарминг: .farm2 [chat_id] [topic_id (необязательно)]"""
        args = utils.get_args(message)

        if len(args) < 1:
            await message.edit("❗️ Использование: <code>.farm2 [chat_id] [topic_id]</code>")
            return

        try:
            self.chat_id = int(args[0])
            self.topic_id = int(args[1]) if len(args) > 1 else None
        except ValueError:
            await message.edit("❗️ Chat ID и Topic ID должны быть числами.")
            return

        if self.tasks:
            await message.edit("⚠️ Фарм уже запущен.")
            return

        await message.edit("✅ Автофарминг запущен.")
        self.tasks = [asyncio.create_task(self.b_run(message.client))]

    @loader.unrestricted
    @loader.ratelimit
    async def stop2cmd(self, message):
        """Остановить фарминг: .stop2"""
        if not self.tasks:
            await message.edit("⛔️ Автофарминг не запущен.")
            return

        for task in self.tasks:
            task.cancel()
        self.tasks.clear()
        await message.edit("🛑 Автофарминг остановлен.")
