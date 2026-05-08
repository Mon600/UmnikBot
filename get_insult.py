import uuid

from googletrans import Translator

from async_httpx_client import get_async_client


async def get_insult() -> str | None:
    client = await get_async_client()
    headers = {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0',
    }
    response = await client.get(
        'https://evilinsult.com/generate_insult.php',
        params={
            'lang': 'ru',
            'type': 'json',
            'cache_bust': str(uuid.uuid4())
        },
        headers=headers
    )
    if response.status_code == 200:
        r_json = response.json()
        return r_json['insult']
    else:
        return None