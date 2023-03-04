from src.node import Node


class BinarySearchTree:
    """Класс для представления структуры бинарного дерева."""

    def __init__(self) -> None:
        """Дерево инициализируется пустым."""
        self.__root = None

    @property
    def root(self):
        return self.__root

    def insert(self, data: dict) -> None:
        """Добавляем данные в структуру дерева."""
        if self.__root is None:
            self.__root = Node(data)
        else:
            self._insert_recursive(self.__root, data)

    def _insert_recursive(self, node: Node, data: dict) -> None:
        """Рекурсивно ищем куда добавить новый узел в дереве."""
        if data['id'] < node.data['id']:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)

        if data['id'] > node.data['id']:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

    def search(self, post_id: int) -> dict | None:
        """Ищем по id пост и возвращаем словарь с его данными."""
        if self.__root is None:
            return None
        else:
            return self._search_recursive(self.__root, post_id)

    def _search_recursive(self, node: Node, post_id: int) -> dict | None:
        """Рекурсивно ищем и возвращаем словарь с данными."""
        if post_id == node.data['id']:
            return node.data

        if post_id < node.data['id'] and node.left is not None:
            return self._search_recursive(node.left, post_id)

        if post_id > node.data['id'] and node.right is not None:
            return self._search_recursive(node.right, post_id)

