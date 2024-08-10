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
    """Модуль для автоматического фарминга в игровом боте @xSpinBot самое удобное для клана можете активировать и поспать а в это время бюмодул будет активен"""

    strings = {"name": "code of xSpinBot by ssxzico"}

    def __init__(self):
        self.tasks = []

    async def b_run(self, client):
        while True:
            await client.send_message('https://t.me/+aLV58fXwlCBmN2Zk', "!б 5000")
            await asyncio.sleep(4)

  #  async def p_run(self, client):
      #  while True:
           # await client.send_message('@xSpinBot', "!бизвывод")
          #  await asyncio.sleep(1920)

  #  async def l_run(self, client):
      #  while True:
           # await client.send_message('@xSpinBot', "!бизактив")
          #  await asyncio.sleep(1220)

    #async def t_run(self, client):
      #  while True:
           # await client.send_message('@xSpinBot', "!банквывод 1000000")
          #  await asyncio.sleep(1420)

#*    async def a_run(self, client):
     #   while True:
          #  await client.send_message('@xSpinBot', "!б 5000")
          #  await asyncio.sleep(1680)

    @loader.unrestricted
    @loader.ratelimit
    async def farm1cmd(self, message):
        """Запустить автоматический фарминг в боте"""
        if self.tasks:
            return await message.edit("Автоматический фарминг уже запущен.")
        await message.edit("Автоматический фарминг запущен.")
        client = message.client
        self.tasks = [asyncio.create_task(self.b_run(client))]  #, asyncio.create_task(self.l_run(client)), asyncio.create_task(self.t_run(client)), asyncio.create_task(self.a_run(client))]

    @loader.unrestricted
    @loader.ratelimit
    async def stop1cmd(self, message):
        """Остановить автоматический фарминг в боте"""
        if not self.tasks:
            return await message.edit("Автоматический фарминг не запущен.")
        for task in self.tasks:
            task.cancel()
        self.tasks = []
        await message.edit("Автоматический фарминг остановлен.")