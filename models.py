from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Agendamento(Base):
    __tablename__ = 'agendamentos'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    data = Column(Date, nullable=False)
    horario = Column(String, nullable=False)
    unidade = Column(String, nullable=False)
