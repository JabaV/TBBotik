import asyncio
import sqlite3


# get resources by quality
async def grbq(rarity: int) -> list:
    con = sqlite3.connect('BD/Lich.db')
    cursor = con.cursor()
    cursor.execute(f'select * from Resources where Rarity = {rarity}')
    a = cursor.fetchall()
    return a


async def grbqr(rarity: int) -> list:
    con = sqlite3.connect('BD/Lich.db')
    cursor = con.cursor()
    cursor.execute(f'select * from Resources where Rarity != {rarity}')
    a = cursor.fetchall()
    return a


async def gra() -> list:
    con = sqlite3.connect('BD/Lich.db')
    cursor = con.cursor()
    cursor.execute(f'select * from Resources')
    a = cursor.fetchall()
    return a


async def gibq(rarity: int) -> list:
    con = sqlite3.connect('BD/Lich.db')
    cursor = con.cursor()
    cursor.execute(f'select * from Ingredients where Rarity = {rarity} and IsDerivative = 0')
    a = cursor.fetchall()
    return a


async def get_shop(name: str) -> tuple:
    con = sqlite3.connect('../BD/Lich.db')
    cursor = con.cursor()
    cursor.execute(f'select File_Desc, Image from Shops where Name = {name}')
    a = cursor.fetchall()
    return a[0]
