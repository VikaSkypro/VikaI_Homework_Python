import pytest
from SubjectPage import SubjectPage


# Фикстура для управления соединением с базой данных и транзакциями
@pytest.fixture(scope="function")
def db_connection():
    db_connection_string = "postgresql://postgres:123gavgav@localhost:5432/skypro"
    subject_page = SubjectPage(db_connection_string)
    yield subject_page


# Тест добавления предмета
def test_insert_subject(db_connection):
    subject_page = db_connection

    # Находим максимальный subject_id
    max_subject_id = subject_page.get_max_subject_id()
    new_subject_id = (
        max_subject_id + 1 if max_subject_id is not None else 1
    )  # Устанавливаем новый id

    # Выполняем вставку
    inserted_row, rowcount = subject_page.insert_subject(
        new_subject_id, "music"
    )
    print(f"Добавлен предмет с ID {new_subject_id}: {inserted_row}")
    assert rowcount == 1, "Предмет не добавлен в таблицу."

    # Проверяем, что предмет создан
    assert subject_page.subject_exists(
        new_subject_id
    ), "Предмет не существует после добавления."
    print(f"Предмет с ID {new_subject_id} успешно найден после добавления.")

    # Удаляем предмет
    deleted_row, delete_count = subject_page.delete_subject(new_subject_id)
    print(f"Удален предмет с ID {new_subject_id}: {deleted_row}")
    assert delete_count == 1, "Предмет не был удален корректно."

    # Проверяем, что предмет больше не существует
    assert not subject_page.subject_exists(
        new_subject_id
    ), "Предмет все еще существует в базе данных."
    print(f"Предмет с ID {new_subject_id} успешно удален.")


# Тест обновления предмета
def test_update_subject(db_connection):
    subject_page = db_connection

    # Находим максимальный subject_id
    max_subject_id = subject_page.get_max_subject_id()
    new_subject_id = (
        max_subject_id + 1 if max_subject_id is not None else 1
    )  # Устанавливаем новый id

    # Вставляем предмет
    subject_page.insert_subject(new_subject_id, "music")
    print(f"Добавлен предмет с ID {new_subject_id} для обновления.")

    # Обновляем название предмета
    new_title = "music_updated"
    updated_row = subject_page.update_subject(new_subject_id, new_title)
    print(f"Обновлен предмет с ID {new_subject_id}:"
          f" новое название - {new_title}")

    # Проверяем, что обновленный предмет не None
    assert updated_row is not None, "Предмет с указанным ID не найден."
    # Проверяем, что новое название совпадает
    assert (
        updated_row["subject_title"] == new_title
    ), (f"Ожидалось название '{new_title}', "
        f"но получено '{updated_row['subject_title']}'")

    # Удаляем созданный предмет
    deleted_row, delete_count = subject_page.delete_subject(new_subject_id)
    print(f"Удален предмет с ID {new_subject_id} после обновления.")
    assert delete_count == 1, "Созданный предмет не был удален корректно."
    # Проверяем, что предмет больше не существует
    assert not subject_page.subject_exists(
        new_subject_id
    ), "Созданный предмет все еще существует в базе данных."
    print(f"Предмет с ID {new_subject_id} успешно удален после обновления.")


# Тест удаления предмета
def test_delete_subject(db_connection):
    subject_page = db_connection

    # Находим максимальный subject_id
    max_subject_id = subject_page.get_max_subject_id()
    new_subject_id = (
        max_subject_id + 1 if max_subject_id is not None else 1
    )  # Устанавливаем новый id

    # Вставляем предмет
    subject_page.insert_subject(new_subject_id, "music")
    print(f"Добавлен предмет с ID {new_subject_id} для удаления.")

    # Удаляем предмет
    deleted_row, delete_count = subject_page.delete_subject(new_subject_id)
    print(f"Удален предмет с ID {new_subject_id}: {deleted_row}")
    assert delete_count == 1, "Предмет не был удален корректно."

    # Проверяем, что предмет больше не существует
    assert not subject_page.subject_exists(
        new_subject_id
    ), "Предмет все еще существует в базе данных."
    print(f"Предмет с ID {new_subject_id} успешно удален в тесте удаления.")
