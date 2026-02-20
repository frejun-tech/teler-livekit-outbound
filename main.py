import asyncio
from config import settings
from livekit_service import LiveKitService


async def main():
    service = LiveKitService(settings)
    await service.dispatch_call()


if __name__ == "__main__":
    asyncio.run(main())