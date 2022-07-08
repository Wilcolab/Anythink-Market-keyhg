print('Please fill the seeds file')

import asyncio
from sqlalchemy import create_engine
from app.core.config import get_app_settings
from app.db.repositories.users import UsersRepository
from app.db.repositories.items import ItemsRepository

# async def seed():
#     SETTINGS = get_app_settings()
#     DATABASE_URL = SETTINGS.database_url.replace("postgres://", "postgresql://")
#     engine = create_engine(DATABASE_URL)
#     with engine.connect() as conn:
#         users_repo = UsersRepository(conn)
#         user = await users_repo.get_user_by_username(username='andrei_test')
#         items_repo = ItemsRepository(conn)
#         item = await items_repo.create_items(
#             slug='123',
#             title='123',
#             description='123',
#             body='123',
#             seller=user,
#         )

# asyncio.run(seed())
    
# users_repo = UsersRepository(conn)
# users_repo.create_user(username= 'aaa', email= 'bbb', password='ccc')

SETTINGS = get_app_settings()
DATABASE_URL = SETTINGS.database_url.replace("postgres://", "postgresql://")
engine = create_engine(DATABASE_URL)
for i in range(100):
    engine.execute("INSERT INTO users (username, email, salt) VALUES ('abc%s', 'abc%s@email.com', 'abc')" % (i, i))
    engine.execute("INSERT INTO items (slug, title, description, body, seller_id) VALUES ('%s123', '123', '123', 123, 1)" % (i))
    engine.execute("INSERT INTO comments (body, seller_id, item_id) VALUES ('123', 1, 1)")


# INITIAL_DATA = {
#       'users': [
#             {
#                   'username': 'superuser',
#                   'email': 'superuser@example.com',
#             },
#             {
#                   'username': 'admin',
#                   'email': 'admin@example.com',
#             }
#       ],
# }

# # This method receives a table, a connection and inserts data to that table.
# def initialize_table(target, connection, **kw):
#     tablename = str(target)
#     if tablename in INITIAL_DATA and len(INITIAL_DATA[tablename]) > 0:
#         connection.execute(target.insert(), INITIAL_DATA[tablename])

# # In main.py
# from sqlalchemy import event
# from app.models.domain.users import User
# from fastapi import FastAPI

# # I set up this event before table creation
# event.listen(User.__table__, 'after_create', initialize_table)

# app = FastAPI()

# initialize_table(User.__table__)

# # ....

# # This will create the DB schema and trigger the "after_create" event
# @app.on_event("startup")
# def configure():
#     Base.metadata.create_all(bind=engine)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)