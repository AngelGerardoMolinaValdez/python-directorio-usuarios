from typing import Optional
import os
import sqlite3
from errors.connection import DataBaseFileNotExist


class UsersInformation:
    path : str
    connection : object
    cursor : object


    @classmethod
    def start(cls, name) -> Optional[Exception]:
        path = os.path.join(
            os.path.dirname(__file__), "database", name)

        if not os.path.exists(path):
            return DataBaseFileNotExist()

        cls.path = path

        cls.connection = sqlite3.connect(path)
        cls.cursor = cls.connection.cursor()


    @classmethod
    def close(cls) -> None:
        cls.connection.close()


    def _save(self) -> None:
        UsersInformation.connection.commit()


    def get(self, get_by : str = None) -> None:
        if get_by is None:
            UsersInformation.cursor.execute(
                'SELECT * FROM users')

        elif get_by.isdigit():
            UsersInformation.cursor.execute(
                'SELECT * FROM users WHERE id = ?', get_by)

        else:
            UsersInformation.cursor.execute(
                f"SELECT * FROM users WHERE name LIKE '%{get_by.upper()}%'")
        
        return UsersInformation.cursor.fetchall()


    def update(self, user_id : str, name : str,  phone : str, email : str, address : str) -> None:
        UsersInformation.cursor.execute(
            'UPDATE users SET name = ?, phone = ?, email = ?, address = ? WHERE id = ?',
            (name.upper(),  phone, email, address, user_id)
        )
        self._save()



    def delete(self, user_id : str) -> None:
        UsersInformation.cursor.execute(
            f"DELETE FROM users WHERE id = '{user_id}'")
        self._save()


    def create(self, name : str,  phone : str, email : str, address : str) -> None:
        UsersInformation.cursor.execute("""
            INSERT INTO users(name, phone, email, address)
            VALUES (?, ?, ?, ?)""",
            (name.upper(),  phone, email, address))
        self._save()
