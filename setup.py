from distutils.core import setup

setup(
    name='GamesBot',
    version = '1.0',
    description = 'A Discord bot for gaming news',
    author = 'John Wolf',
    author_email = 'johnmwolf34@gmail.com',
    url = 'https://github.com/JWolf34/GamesBot',
    packages = ['discord', 'asyncio'],
    py_modules=['GamesBot', 'RedditGamesScraper']

)
