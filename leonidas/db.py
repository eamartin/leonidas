from sqlalchemy import (Table, Column, Boolean, DateTime, String, MetaData,
                        create_engine)

metadata = MetaData()
snatches = Table('snatches', metadata,
    Column('info_hash', String(20)),
    Column('user_token', String(32)),
    Column('time', DateTime)
)
status = Table('status', metadata,
    Column('info_hash', String(20)),
    Column('user_token', String(32)),
    Column('peer_id', String),
    Column('ip', String),
    Column('port', String),
    Column('time', DateTime),
    Column('complete', Boolean)
)

def create_tables(config):
    engine = create_engine(config['database'], echo=config.get('debug', False))
    metadata.create_all(engine)
