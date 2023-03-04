class Node:
    """Класс для представления узла с данными"""

    def __init__(self, data: dict) -> None:
        """Узел инициализируется словарем с данными"""
        self.data = data
        self.left = None
        self.right = None

