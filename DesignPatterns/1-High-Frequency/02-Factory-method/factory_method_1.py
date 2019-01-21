#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
from enum import Enum, auto
from typing import List


class DbMode(Enum):
    STANDALONE: int = auto()
    NETWORKING: int = auto()


class DataObject(metaclass=ABCMeta):
    # 戻り値となるクラスを DataObject クラスを1継承しているものと入れ替えれば
    # Client クラス側は DataObject.create() を呼び出すだけでよく、変更後の影響範囲は少ない

    def __init__(self) -> None:
        pass

    @staticmethod
    def create(db_type: DbMode):
        if db_type == DbMode.STANDALONE:
            return FileDataObject()
        if db_type == DbMode.NETWORKING:
            return DbDataObject()

    @abstractmethod
    def fetch_data_object(self, id_num: int) -> str:
        pass


class FileDataObject(DataObject):

    def __init__(self) -> None:
        self.data_list: List[str] = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.data_list.append(line)

    def fetch_data_object(self, id_num: int) -> str:
        return self.data_list[id_num]


class DbDataObject(DataObject):
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self) -> None:
        # DBへの接続手続きなど
        pass

    def fetch_data_object(self, id_num: int) -> str:
        pass


class Client:
    def __init__(self) -> None:
        self.data_object: DataObject = DataObject.create(DbMode.STANDALONE)

    def operating(self, id_num: int) -> str:
        person: str = self.data_object.fetch_data_object(id_num)
        return person


if __name__ == '__main__':

    client: Client = Client()

    i: int = 0
    while True:
        try:
            print(client.operating(i), end="")
            i += 1
        except IndexError:
            break

    row: str = client.operating(1)
    print("\n")
    print(row)
