from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker


class SubjectPage:
    def __init__(self, db_connection_string):
        self.engine = create_engine(db_connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def get_max_subject_id(self):
        session = self.Session()  # Создаем новую сессию
        try:
            max_id_sql = text("SELECT MAX(subject_id) FROM subject")
            max_id_result = session.execute(max_id_sql)
            return max_id_result.scalar()  # Получаем максимальный subject_id
        finally:
            session.close()  # Закрываем сессию

    def insert_subject(self, new_subject_id, new_subject_title):
        insert_sql = text(
            "INSERT INTO subject(subject_id, subject_title) VALUES (:new_subject_id, :new_subject_title) RETURNING *"
        )
        session = self.Session()  # Создаем новую сессию
        try:
            result = session.execute(
                insert_sql,
                {
                    "new_subject_id": new_subject_id,
                    "new_subject_title": new_subject_title,
                },
            )
            session.commit()  # Фиксируем изменения
            return (
                result.fetchone(),
                result.rowcount,
            )  # Возвращаем первую вставленную строку
        finally:
            session.close()  # Закрываем сессию

    def update_subject(self, subject_id, new_title):
        sql = text(
            "UPDATE subject SET subject_title = :new_subject_title WHERE subject_id = :subject_id RETURNING *"
        )
        session = self.Session()  # Создаем новую сессию
        try:
            result = session.execute(
                sql, {"new_subject_title": new_title, "subject_id": subject_id}
            )
            updated_row = result.fetchone()
            session.commit()  # Фиксируем изменения
            return (
                updated_row._mapping if updated_row else None
            )  # Возвращаем результаты как словарь
        finally:
            session.close()  # Закрываем сессию

    def delete_subject(self, subject_id):
        sql = text(
            "DELETE FROM subject WHERE subject_id = :subject_id RETURNING *"
        )
        session = self.Session()  # Создаем новую сессию
        try:
            result = session.execute(sql, {"subject_id": subject_id})
            deleted_row = result.fetchone()
            session.commit()  # Фиксируем изменения
            return deleted_row, (
                1 if deleted_row else 0
            )  # Возвращаем удаленную запись и количество затронутых строк
        finally:
            session.close()  # Закрываем сессию

    def subject_exists(self, subject_id):
        check_sql = text(
            "SELECT * FROM subject WHERE subject_id = :subject_id"
        )
        session = self.Session()  # Создаем новую сессию
        try:
            check_result = session.execute(
                check_sql, {"subject_id": subject_id}
            )
            return check_result.fetchone() is not None
        finally:
            session.close()  # Закрываем сессию
