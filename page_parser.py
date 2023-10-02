import aiohttp
import asyncio
from os import getenv

from re import escape, split
from dotenv import load_dotenv


load_dotenv()


async def requestAndProcess():  # arguably not the best decision to do two things in one function, but "it has to be this way"
    async with aiohttp.ClientSession() as session:
        async with session.get(getenv('url')) as response:
            if response.status == 200:
                html = await response.text()
            else:
                print("Error while loading the page")
                return None

    '''
    You would rightfully ask: what the HELL do these two lines do?
    Honestly, I have small to zero understanding of how does it do that.
    All I know and care about - the two lines below transform whatever mess if left after initial scraping
    of RSS data into usable anecdote string.
    '''
    sep = ['"\\', '\\"']  # special symbols to remove anecdote markdowns
    text_list = split('|'.join(map(escape, sep)), html)
    anecdote_string = text_list[1]
    anecdote_string = anecdote_string.replace("<br>", ' ')

    return anecdote_string
