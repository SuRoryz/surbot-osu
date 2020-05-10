import sqlite3
import os


# Executor class. Uses for creating sql-query
class Executor:
    def __init__(self):
        pass

    @staticmethod
    def select(to: str, frm: str, where: str = None, order: str = None) -> str:
        sql = f"select {to} from {frm}"

        if where:
            sql += f" where {where}"

        if order:
            sql += f" order by {order}"

        return sql

    @staticmethod
    def insert(into: str, columns: tuple, values: tuple):
        sql = f"insert into {into} {columns} values {values}"

        return sql

    @staticmethod
    def delete(frm: str, where: str = None):
        sql = f"delete from {frm}"

        if where:
            sql += f" where {where}"

        return sql

    @staticmethod
    def update(to: str, to_set: str, where: str = None):
        sql = f"update {to} set {to_set}"

        if where:
            sql += f" where {where}"

        return sql

    @staticmethod
    def execute(db, sql):
        db = sqlite3.connect(db)
        cur = db.cursor()

        cur.execute(sql)
        db.commit()
        res = cur.fetchall()

        cur.close()
        db.close()

        return res


# Language class. Uses to set/get languages to/from database
class Language:
    def __init__(self, name: str):

        self.db_name: str = "lang.db"
        self.name: str = name

        if not(os.path.exists(self.db_name)):
            db = sqlite3.connect(self.db_name)
            cur = db.cursor()

            try:
                cur.execute("CREATE TABLE lang (name, lang)")
                db.commit()
            finally:
                cur.close()
                db.close()

    # Executing sql-query. Actually, you can use Executor.execute for this
    def execute(self, sql: str) -> tuple:
        db = sqlite3.connect(self.db_name)
        cur = db.cursor()

        cur.execute(sql)
        db.commit()
        res = cur.fetchall()

        cur.close()
        db.close()

        return res

    # Check for existing in db
    def exists(self) -> None:
        try:
            if self.execute(Executor.select("name", "lang", f"name='{self.name}'")):
                return True
        except:
            return False
        return False

    # Inserts into db a new user
    def insert_language(self, language: str) -> None:
        self.execute(Executor.insert("lang", ("name", "lang"), (self.name, language)))

    # Sets new language for user
    def set_language(self, language: str) -> None:
        self.execute(Executor.update("lang", f"lang='{language}'", f"name='{self.name}'"))

    # Gets current language for user
    def get_language(self) -> str:
        lang = self.execute(Executor.select("lang", "lang", f"name='{self.name}'"))[0]
        return lang[0]
