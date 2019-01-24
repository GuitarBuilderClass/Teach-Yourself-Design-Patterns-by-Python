#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
from enum import Enum, auto
from typing import List

# パターン1はファイルからDBへ切り替えが予定されていることが分かっている場合の設計で
# クライアント側のコードに影響を与えないことを大切にしている
# パターン2ではクライアント側からどのクラスを呼び出すか切り替えられる設計を目指す


class DBMode(Enum):
    STANDALONE: int = auto()  # ファイルからの読み書き
    NETWORKING: int = auto()  # DB からの読み書き


class DataObject(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @staticmethod
    def create() -> object:
        return FileDataObject()

    @abstractmethod
    def fetch_data_object(self, id_num: int) -> str:
        pass


class FileDataObject(DataObject):

    def __init__(self) -> None:
        super().__init__()
        self.data_list: List[str] = list()

        with open('test.csv', 'r') as f:
            for line in f:
                self.data_list.append(line)

    def fetch_data_object(self, id_num) -> str:
        return self.data_list[id_num]


class DBDataObject(DataObject):
    """未実装クラスだが、将来的に FileDataObject と差し替える予定"""

    def __init__(self) -> None:
        # DBへの接続手続きなど
        super().__init__()

    def fetch_data_object(self, id_num: int) -> str:
        pass


class DataObjectFactory:
    # オブジェクト生成の責任を負う
    # create 時にどのクラスを呼び出すか1度決めてしまえば、以後は毎回クラスを指定する必要がなくなる

    @staticmethod
    def create(data_type: DBMode):
        if data_type == DBMode.STANDALONE:
            return FileDataObject()
        if data_type == DBMode.NETWORKING:
            return DBDataObject()


class Client:

    def __init__(self) -> None:
        self.factory = DataObjectFactory()

        # ここで DbMode を指定する
        self.data_object = self.factory.create(DBMode.STANDALONE)


if __name__ == '__main__':
    client: DataObject = Client().data_object

    i: int = 0
    while True:
        try:
            print(client.fetch_data_object(i), end="")
            i += 1
        except IndexError:
            break

    row: str = client.fetch_data_object(2)
    print("\n")
    print(row)
