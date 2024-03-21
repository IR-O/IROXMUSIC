import logging
from motor.motor_asyncio import AsyncIOMotorClient

async def main():
    # Connect to MongoDB
    client = AsyncIOMotorClient("mongodb://username:password@host:port")
    db = client.my_database
    collection = db.my_collection

    # Use the logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    # Perform some database operations
    await collection.insert_one({"name": "John Doe"})
    result = await collection.find_one({"name": "John Doe"})
    logger.debug(f"Found document: {result}")

if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
