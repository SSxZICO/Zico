# meta developer: @gde_zico
import asyncio
from .. import loader, utils

@loader.tds
class FarmMonacoMod(loader.Module):
    """Автофарминг модуль для @xSpinBot. Автор: @gde_zico"""

    strings = {"name": "xSpinBotFarm"}

    def __init__(self):
        self.tasks = []
        self.running_chat_id = None

    async def b_run(self, client, chat_id):
        while True:
            try:
                await client.send_message(chat_id, "!б 5000")
                await asyncio.sleep(4)
            except Exception as e:
                print(f"[Farm] Error: {e}")
                await client.send_message(chat_id, f"⚠️ Xatolik: {e}")
                await asyncio.sleep(10)

    @loader.unrestricted
    @loader.ratelimit
    async def farm2cmd(self, message):
        """Ishga tushurish: .farm2 [chat_id]"""
        args = utils.get_args(message)

        if self.tasks:
            return await message.edit("⛔️ Farming allaqachon ishlamoqda. To‘xtatish uchun: .stop2")

        if not args:
            return await message.edit("❗️Iltimos, chat ID kiriting. Masalan: <code>.farm2 -1001234567890</code>")

        chat_id = args[0]

        try:
            chat_id = int(chat_id)
        except ValueError:
            return await message.edit("❗️Chat ID raqam bo‘lishi kerak. Masalan: <code>.farm2 -1001234567890</code>")

        await message.edit(f"✅ Farming boshlandi.\nChat ID: <code>{chat_id}</code>\nKod: @gde_zico")
        self.running_chat_id = chat_id
        client = message.client
        self.tasks = [asyncio.create_task(self.b_run(client, chat_id))]

    @loader.unrestricted
    @loader.ratelimit
    async def stop2cmd(self, message):
        """To‘xtatish: .stop2"""
        if not self.tasks:
            return await message.edit("ℹ️ Hozirda hech qanday farming ishlamayapti.")

        for task in self.tasks:
            task.cancel()

        self.tasks = []
        cid = self.running_chat_id or "Noma'lum"
        self.running_chat_id = None

        await message.edit(f"🛑 Farming to‘xtatildi.\nChat ID: <code>{cid}</code>\nKod: @gde_zico")
