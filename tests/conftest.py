import sys
import pathlib

root = pathlib.Path.cwd()

sys.path.append(str(root))
sys.path.append(str(root) + "/bot")

pytest_plugins = ('pytest_asyncio',)