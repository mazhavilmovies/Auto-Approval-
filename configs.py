from os import getenv

class Config:
    API_ID = int(getenv("API_ID", "21419016"))
    API_HASH = getenv("API_HASH", "79198e1eb4cfd0f771a89d83b9144e7e")
    BOT_TOKEN = getenv("BOT_TOKEN", "8195734162:AAEDqrvuIgVqnPqEJ4yiDcwtMUW9K8lM3mQ")
    
    # Your Force Subscribe Channel Id
    CHID = int(getenv("CHID", "-1002674451609"))  # Make the bot admin in this channel
    
    # Bot owners (use space-separated user IDs in env)
    SUDO = list(map(int, getenv("SUDO", "1933114137").split()))
    
    # MongoDB connection URI
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://kentkouhali5l_db_user:gFvGsyASnQPu9rDZ@cluster0.m9xgtlr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

cfg = Config()
