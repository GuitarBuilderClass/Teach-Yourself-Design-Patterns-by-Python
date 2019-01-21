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

    @abstractmethod
    def fetch_data_object(self, num: int) -> str:
        pass


class FileDataObject(DataObject):

    def __init__(self) -> None:
        self.data_list: List[str] = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.data_list.append(line)

    def fetch_data_object(self, row_num: int) -> str:
        return self.data_list[row_num]


class DbDataObject(DataObject):
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self) -> None:
        # DBへの接続手続きなど
        pass

    def fetch_data_object(self, id_num: int) -> str:
        #
        pass


class DataObjectFactory:
    def __init__(self, db_type: DbMode) -> None:
        self._db_type: DbMode = db_type

    def create(self):
        if self._db_type == DbMode.STANDALONE:
            return FileDataObject()
        if self._db_type == DbMode.NETWORKING:
            return DbDataObject()


class Client:
    def __init__(self) -> None:
        # あとでFileDataObjectからDbDataObjectへ変更するときは
        # ここで呼び出すクラスを変更すればよいという目論見

        # ただし、Clientを呼び出すたびにFileDataObjectクラスが生成される
        self.factory: DataObjectFactory = DataObjectFactory(DbMode.STANDALONE)
        self.data_object: DataObject = self.factory.create()

    def operating(self, id_num: int) -> str:
        person: str = self.data_object.fetch_data_object(id_num)
        return person


if __name__ == '__main__':

    factory: DataObjectFactory = DataObjectFactory(DbMode.STANDALONE)
    client: DataObject = factory.create()

    i = 0
    while True:
        try:
            print(client.fetch_data_object(i), end="")
            i += 1
        except IndexError:
            break

    client2: DataObject = factory.create()
    row = client.fetch_data_object(1)
    print("\n")
    print(row)
