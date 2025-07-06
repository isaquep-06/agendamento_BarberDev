from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Cria o banco SQLite (você pode trocar para PostgreSQL ou MySQL se quiser)
engine = create_engine('sqlite:///barberdev.db')
Session = sessionmaker(bind=engine)
session = Session()

# Cria as tabelas
Base.metadata.create_all(engine)
