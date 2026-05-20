from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN", None)
ADMINS = list(env.str("ADMINS").split(","))

if not TOKEN:
    raise Exception("TOKEN sozlanmagan")
