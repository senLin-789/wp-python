from dao.Database import Database


class UserDao(Database):
    def __init__(self) -> None:
        super(UserDao, self).__init__()

    def get_users(self, page, limit):
        cursor = self.connection.cursor()
        sql = f"select * from user limit {(int(page)-1)*int(limit)},{limit}"
        print(sql)
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows
