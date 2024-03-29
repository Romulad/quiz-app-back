import sqlite3

from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE']
        )
        g.db.execute('PRAGMA foreign_keys=ON')

    return g.db

def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()
    
    
