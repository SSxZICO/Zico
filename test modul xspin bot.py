# meta developer: @gde_zico
import random
from datetime import timedelta
import asyncio
import time
from telethon import events

from telethon import functions
from telethon.tl.types import Message

from .. import loader, utils


@loader.tds
class FarmMonacoMod(loader.Module):
    """Модуль для автоматического фарминга в игровом боте @xSpinBot самое удобное для клана можете активировать и поспать а в это время бюмодул будет активен. Кодер @gde_zico"""

    strings = {"name": "xSpinBot module by ssxzico"}

    def __init__(self):
        self.tasks = []

    async def b_run(self, client):
        while True:
            await client.send_message('@kordistongderbdd', "!б 5000")
            await asyncio.sleep(4)

    @loader.unrestricted
    @loader.ratelimit
    async def farm2cmd(self, message):
        """Запустить автоматический фарминг в боте"""
        if self.tasks:
            return await message.edit("Автоматический игра уже запущен. Кодер @gde_zico")
        await message.edit("Автоматический игра запущен. Кодер @gde_zico")
        client = message.client
        self.tasks = [asyncio.create_task(self.b_run(client))]

    @loader.unrestricted
    @loader.ratelimit
    async def stop2cmd(self, message):
        """Остановить автоматический фарминг в боте"""
        if not self.tasks:
            return await message.edit("Автоматический игра не запущен. Кодер @gde_zico")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Автоматический игра остановлен. Кодер @gde_zico")