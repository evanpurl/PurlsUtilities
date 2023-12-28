import os

import aiomysql
from aiomysql import Error
from dotenv import load_dotenv

load_dotenv()


async def create_pool():
    try:
        pool = await aiomysql.create_pool(host=os.getenv('host'), port=int(os.getenv('port')),
                                          user=os.getenv('user'), password=os.getenv('password'),
                                          db=os.getenv('db'))

        return pool
    except Exception or Error as e:
        print(f"Create Pool: {e}")


async def create_table(pool, mysql, data):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(mysql, data)
                await conn.commit()
                await cur.close()
    except Error or Exception as e:
        print(f"Create Table: {e}")


async def create_unique_index(pool, mysql, data):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(mysql, data)
                await conn.commit()
                await cur.close()
    except Error or Exception as e:
        print(f"createuniqueindex: {e}")


async def run(pool, mysql):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(mysql)
                await conn.commit()
        pool.close()
        await pool.wait_closed()
    except Exception or Error as e:
        print(e)


async def get(pool, mysql):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(mysql)
                result = await cur.fetchone()
        if not result:
            return 0
        if len(result) == 0:
            return 0
        return result[0]
    except Exception or Error as e:
        print(f"Get: {e}")
