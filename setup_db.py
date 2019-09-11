from db import init_db
from tortoise import run_async, Tortoise


async def setup_db():
    await init_db()
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    run_async(setup_db())
