import asyncio
import json

from googletrans import Translator
import httpx

from async_httpx_client import get_async_client


async def get_fact() -> str | None:
    client = await get_async_client()
    r = await client.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en")
    if r.status_code == 200:
        translator = Translator()
        r_json = r.json()
        res = await translator.translate(r_json["text"], dest='ru')
        return res.text
    else:
        return None


if __name__ == '__main__':
    asyncio.run(get_fact())