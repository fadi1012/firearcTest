import aiosqlite


async def init_db():
    db = await aiosqlite.connect("./test.db")
    cursor = await db.cursor()

    # Create the database tables
    await cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            body TEXT
        )
    ''')

    # Add a dummy article to the database
    await cursor.execute('''
        INSERT INTO articles (title, description, body)
        VALUES (?, ?, ?)
    ''', ("Dummy Title", "Dummy Desc", "Dummy Body"))

    await db.commit()
    await db.close()


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_db())
