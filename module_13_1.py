import asyncio


async def start_strongman(name, power):

    print(f'Силач {name} начал соревнования.')
    ball = 1
    while 5 >= ball:
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {ball} шар')
        ball += 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():

    player_1 = asyncio.create_task(start_strongman('Pasha', 3))
    player_2 = asyncio.create_task(start_strongman('Denis', 4))
    player_3 = asyncio.create_task(start_strongman('Apollon', 5))

    await player_1
    await player_2
    await player_3


asyncio.run(start_tournament())
