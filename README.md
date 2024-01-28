# qa_python

Были реализованы:
test_add_new_book_add_two_books - проверка на возможность добавления двух книг
test_add_new_book_dont_add_book_twice - проверка на то, что книга с одним названием не добавится дважды
test_add_new_book_dont_add_book_with_empty_name - проверка на выставленную валидацию, не добавляет книгу с пустым именем
test_add_new_book_dont_add_book_with_space_in_name - проверка на добавление имени с пробелом в названии, нкжна доработка
test_add_new_book_dont_add_book_with_too_long_name - проверка на выставленную валидацию, не добавляет книгу с длинным названием в 41 символ и более
test_get_book_genre_get_genre_to_added_book - получаем жанр к книге, которой не добавили жанр
test_get_book_genre_get_genre_to_not_added_book - проверяем что не добавит жанр к не добавленной книге
test_set_book_genre_set_random_genre_one_book - добавялем рандомный жанр к книге
test_set_book_genre_set_genre_two_books - добавялем одинаковый жанр к разным книгам, проверяем жанр
test_set_book_genre_set_genre_to_not_added_book - получаем жанр у не добавленной книги
test_get_books_with_specific_genre_two_books_with_one_genre - получаем названия книг по жанру
test_get_books_with_specific_genre_book_with_not_added_genre - проверяем вывод если не добавить жанр книге
test_get_books_for_children_two_books_with_one_adult_genre - добавляем книгу с взрослым жанром и детским жанром, проверяем вывод 1 книги
test_add_book_in_favorites_add_one_book - проверяем добавление книги в любимые
test_add_book_in_favorites_dont_add_one_book_twice - проверяем что книга дважды не добавляется в любимые
test_delete_book_from_favorites_delete_one_book - проверяем что книга удаляется из списка любимых