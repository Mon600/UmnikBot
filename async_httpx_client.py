from httpx import AsyncClient


async def get_async_client() -> AsyncClient:
    return AsyncClient(timeout=10.0, follow_redirects=True)