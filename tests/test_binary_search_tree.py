import pytest

from src.binary_search_tree import BinarySearchTree


def test_bst_empty():
    """В пустом дереве root ссылается на None."""
    bst = BinarySearchTree()
    assert bst.root is None


def test_bst_insert_root(bst):
    """При добавлении единственного узла он хранится в root."""
    assert bst.root.data == {'id': 40}


def test_bst_insert_left(bst):
    """Добавляем первый элемент слева."""
    bst.insert({'id': 30})
    assert bst.root.left.data == {'id': 30}


def test_bst_insert_right(bst):
    """Добавляем первый элемент справа."""
    bst.insert({'id': 50})
    assert bst.root.right.data == {'id': 50}


def test_bst_insert_left_left(bst):
    """Добавляем два элемента слева."""
    bst.insert({'id': 30})
    bst.insert({'id': 25})
    assert bst.root.left.left.data == {'id': 25}


def test_bst_insert_right_right(bst):
    """Добавляем два элемента справа."""
    bst.insert({'id': 50})
    bst.insert({'id': 60})
    assert bst.root.right.right.data == {'id': 60}


def test_bst_search_empty():
    """Поиск в пустом дереве возращает None."""
    bst = BinarySearchTree()
    assert bst.search(444) is None


@pytest.mark.parametrize('post_id, post_data', [(40, {'id': 40}),
                                                (30, {'id': 30}),
                                                (25, {'id': 25}),
                                                (35, {'id': 35}),
                                                (50, {'id': 50}),
                                                (45, {'id': 45}),
                                                (60, {'id': 60})])
def test_bst_search_root(bst_full, post_id, post_data):
    """Ищем пост в вершине дерева."""
    assert bst_full.search(post_id) == post_data

