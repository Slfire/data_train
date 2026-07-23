import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DB = os.getenv("db_url")

df = pd.read_csv("projets\data\steam_games.csv")
print(df)