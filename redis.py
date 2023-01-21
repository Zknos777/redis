import redis.asyncio as redis
import asyncio

async def s():
    connection = redis.Redis()
    print(f"Ping successful: {await connection.ping()}")
    await connection.close()
    
asyncio.run(s())