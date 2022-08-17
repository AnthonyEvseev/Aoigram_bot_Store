from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

# Заберем токен нашего бота (прописать в файле ".env")
BOT_TOKEN = env.str("BOT_TOKEN")

# Заберем данные для подключения к базе данных (юзер, пароль, название бд) - тоже прописать в файле ".env"
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")

admins = [
    env.str("ADMIN_ID"),
]

ip = env.str("IP")

# Ссылка подключения к базе данных
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}"
aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}