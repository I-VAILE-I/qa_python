import random

from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    @pytest.mark.parametrize(
        "first_book,second_book",
        [
            ('Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'),
            ('Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби')
        ]
    )
    def test_add_new_book_add_two_books(
            self,
            first_book: str,
            second_book: str
    ):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book(first_book)
        collector.add_new_book(second_book)

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_dont_add_book_twice(
            self,
    ):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_dont_add_book_with_empty_name(
            self,
    ):
        collector = BooksCollector()
        collector.add_new_book('')

        assert len(collector.get_books_genre()) == 0

    @pytest.mark.xfail
    def test_add_new_book_dont_add_book_with_space_in_name(
            self,
    ):
        collector = BooksCollector()
        collector.add_new_book(' ')

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_dont_add_book_with_too_long_name(
            self,
    ):
        collector = BooksCollector()
        collector.add_new_book('01234567890123456789012345678901234567891')

        assert len(collector.get_books_genre()) == 0

    def test_get_book_genre_get_genre_to_added_book(
            self,
    ):
        first_book = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(first_book)

        assert collector.get_book_genre(name=first_book) == ''

    def test_get_book_genre_get_genre_to_not_added_book(
            self,
    ):
        first_book = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()

        assert collector.get_book_genre(name=first_book) is None

    def test_set_book_genre_set_random_genre_one_book(
            self,
    ):
        first_book = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        collector.add_new_book(first_book)
        gener = collector.genre[random.randint(0, 4)]
        collector.set_book_genre(name=first_book, genre=gener)

        assert collector.get_book_genre(name=first_book) == gener

    @pytest.mark.parametrize(
        "first_book,second_book,genre",
        [
            ('Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить', 'Ужасы'),
            ('Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби', 'Фантастика')
        ]
    )
    def test_set_book_genre_set_genre_two_books(
            self,
            first_book: str,
            second_book: str,
            genre: str
    ):
        collector = BooksCollector()
        collector.add_new_book(first_book)
        collector.add_new_book(second_book)
        collector.set_book_genre(name=first_book, genre=genre)
        collector.set_book_genre(name=second_book, genre=genre)

        assert len(collector.get_books_genre().values()) == 2

    def test_set_book_genre_set_genre_to_not_added_book(
            self,
    ):
        first_book = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        gener = collector.genre[random.randint(0, 4)]
        collector.set_book_genre(name=first_book, genre=gener)

        assert collector.get_book_genre(name=first_book) is None

    @pytest.mark.parametrize(
        "first_book,second_book,genre",
        [
            ('Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить', 'Ужасы'),
            ('Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби', 'Фантастика')
        ]
    )
    def test_get_books_with_specific_genre_two_books_with_one_genre(
            self,
            first_book: str,
            second_book: str,
            genre: str
    ):
        collector = BooksCollector()
        collector.add_new_book(first_book)
        collector.add_new_book(second_book)
        collector.set_book_genre(name=first_book, genre=genre)
        collector.set_book_genre(name=second_book, genre=genre)

        assert len(collector.get_books_with_specific_genre(genre)) == 2

    def test_get_books_with_specific_genre_book_with_not_added_genre(
            self,
    ):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre(name='Гордость и предубеждение и зомби', genre='Ужасы')

        assert len(collector.get_books_with_specific_genre('Фантастика')) == 0

    @pytest.mark.parametrize(
        "first_book,second_book,first_genre,second_genre",
        [
            ('Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить', 'Ужасы', 'Фантастика'),
            ('Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби', 'Фантастика', 'Ужасы')
        ]
    )
    def test_get_books_for_children_two_books_with_one_adult_genre(
            self,
            first_book: str,
            second_book: str,
            first_genre: str,
            second_genre: str
    ):
        collector = BooksCollector()
        collector.add_new_book(first_book)
        collector.add_new_book(second_book)
        collector.set_book_genre(name=first_book, genre=first_genre)
        collector.set_book_genre(name=second_book, genre=second_genre)

        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_add_one_book(
            self,
    ):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_dont_add_one_book_twice(
            self,
    ):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_one_book(
            self,
    ):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert len(collector.get_list_of_favorites_books()) == 0
