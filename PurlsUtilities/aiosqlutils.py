import os

import aiomysql
from aiomysql import Error
from dotenv import load_dotenv

load_dotenv()


async def aiomysql_create_pool():
    """ Creates pool using credentials in .env file (host, port, user, password, db)
    :return: pool
    """
    try:
        pool = await aiomysql.create_pool(host=os.getenv('host'), port=int(os.getenv('port')),
                                          user=os.getenv('user'), password=os.getenv('password'),
                                          db=os.getenv('db'))

        return pool
    except Exception or Error as e:
        print(f"aiomysql Create Pool: {e}")


async def aiomysql_create_table(pool, mysql, data):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(mysql, data)
                await conn.commit()
                await cur.close()
    except Error or Exception as e:
        print(f"aiomysql Create Table: {e}")


async def aiomysql_create_unique_index(pool, mysql, data):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(mysql, data)
                await conn.commit()
                await cur.close()
    except Error or Exception as e:
        print(f"aiomysql createuniqueindex: {e}")


async def aiomysql_run(pool, mysql):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(mysql)
                await conn.commit()
        pool.close()
        await pool.wait_closed()
    except Exception or Error as e:
        print(f"aiomysql run: {e}")


async def aiomysql_get(pool, mysql):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(mysql)
                result = await cur.fetchall()
        if not result:
            return 0
        if len(result) == 0:
            return 0
        return result
    except Exception or Error as e:
        print(f"aiomysql get: {e}")
