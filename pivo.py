from .. import loader
from asyncio import sleep
@loader.tds
class pivoMod(loader.Module):
	strings = {"name": "pivo"}
	@loader.owner
	async def pivocmd(self, message):
		for _ in range(10):
			for pivo in ['Го', 'пить', 'ПИВО', 'вкусное', 'Львовское)', '🍺']:
				await message.edit(pivo)
				await sleep(0.07)