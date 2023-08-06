import sqlite3
from pathlib import Path
from typing import Any, Optional, cast

from . import AbstractStorage


class Sqlite3(AbstractStorage):
    def __init__(self, path: Path = Path('http_intercept.db')):
        super().__init__(path)
        self._connection: Optional[sqlite3.Connection] = None
        self._cursor: Optional[sqlite3.Cursor] = None

    def exists(self) -> bool:
        return self._path.exists()

    def __enter__(self) -> 'Sqlite3':
        if self.exists():
            self._connection = sqlite3.connect(self._path)
            self._cursor = self._connection.cursor()
        else:
            self._connection = sqlite3.connect(self._path)

            self._cursor = self._connection.cursor()
            self._cursor.execute(
                "CREATE TABLE file(file_name PRIMARY KEY, data BLOB)")
            self._connection.commit()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        assert self._connection  # TOOD: ask in stakoverflow
        self._connection.close()

    def __setitem__(self, key: str, value: bytes) -> None:
        assert self._connection
        assert self._cursor

        super().__setitem__(key, value)

        self._cursor.execute(
            "INSERT INTO file values (?, ?)", (key, value)
        )
        self._connection.commit()

    def __getitem__(self, key: str) -> bytes:
        assert self._connection
        assert self._cursor
        self._cursor.execute(
            "SELECT data FROM file WHERE file_name = (?)", (key, )
        )
        res = self._cursor.fetchone()
        if not res:
            raise KeyError(f'No data for key {key!r}')

        return res and cast(bytes, res[0])

    def __contains__(self, key: str) -> bool:
        assert self._cursor

        self._cursor.execute(
            "SELECT count(1) FROM file WHERE file_name = (?)", (key, )
        )
        return bool(self._cursor.fetchone()[0])
