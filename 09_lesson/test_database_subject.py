from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:320@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_add_subject():
    # Тест на добавление предмета
    test_subject_title = "Geometry"
    test_subject_id = 17

    with db.connect() as connection:
        # Добавляем тестовый предмет
        connection.execute(
            text("""
            INSERT INTO subject (subject_title, subject_id)
            VALUES (:subject, :subject_id)
            """),
            {"subject": test_subject_title, "subject_id": test_subject_id}
        )

        # Проверяем, что предмет добавился
        result = connection.execute(
            text("SELECT * FROM subject WHERE subject_title = :subject"),
            {"subject": test_subject_title}
        )
        rows = result.fetchall()

        assert len(rows) == 1, f"Expected 1 subject, got {len(rows)}"
        assert rows[0].subject_title == test_subject_title
        assert rows[0].subject_id == test_subject_id

        # Очищаем тестовые данные
        connection.execute(
            text("DELETE FROM subject WHERE subject_title = :subject"),
            {"subject": test_subject_title}
        )


def test_update_subject():
    # Тест на изменение предмета
    original_title = "Geometry"
    new_title = "Music"
    test_subject_id = 17

    with db.connect() as connection:
        # Добавляем тестовый предмет
        connection.execute(
            text("""
            INSERT INTO subject (subject_title, subject_id)
            VALUES (:subject, :subject_id)
            """),
            {"subject": original_title, "subject_id": test_subject_id}
        )

        # Обновляем название предмета
        connection.execute(
            text("""
            UPDATE subject
            SET subject_title = :new_title WHERE subject_id = :subject_id
            """),
            {"new_title": new_title, "subject_id": test_subject_id}
        )

        # Проверяем, что старое название больше не существует
        result_old = connection.execute(
            text("SELECT * FROM subject WHERE subject_title = :subject"),
            {"subject": original_title}
        )
        rows_old = result_old.fetchall()
        assert len(rows_old) == 0, f"Old title '{original_title}' still exists"

        # Проверяем, что новое название появилось
        result_new = connection.execute(
            text("SELECT * FROM subject WHERE subject_title = :subject"),
            {"subject": new_title}
        )
        rows_new = result_new.fetchall()

        assert len(rows_new) == 1, (
            f"Expected 1 subject with new title, got {len(rows_new)}"
        )
        assert rows_new[0].subject_title == new_title
        assert rows_new[0].subject_id == test_subject_id

        # Очищаем тестовые данные
        connection.execute(
            text("DELETE FROM subject WHERE subject_id = :subject_id"),
            {"subject_id": test_subject_id}
        )


def test_delete_subject():
    # Тест на удаление предмета
    test_subject_title = "Psychology"
    test_subject_id = 17

    with db.connect() as connection:
        # Добавляем тестовый предмет
        connection.execute(
            text("""
            INSERT INTO subject (subject_title, subject_id)
            VALUES (:subject, :subject_id)
            """),
            {"subject": test_subject_title, "subject_id": test_subject_id}
        )

        # Проверяем, что предмет добавился
        result = connection.execute(
            text("SELECT * FROM subject WHERE subject_title = :subject"),
            {"subject": test_subject_title}
        )
        rows = result.fetchall()

        assert len(rows) == 1, f"Expected 1 subject, got {len(rows)}"
        assert rows[0].subject_title == test_subject_title
        assert rows[0].subject_id == test_subject_id

        # Очищаем тестовые данные
        connection.execute(
            text("DELETE FROM subject WHERE subject_title = :subject"),
            {"subject": test_subject_title}
        )
