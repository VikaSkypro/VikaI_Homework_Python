# Описание класса и методов
import requests
from faker import Faker

# Переменные с авторизацией и пользователем my_headers и user



class ProjectsApi:

    # Инициализация
    def __init__(self, url) -> None:
        self.faker = Faker()
        self.url = url

    # Получить список проектов
    def get_projects(self, params_to_add=None):
        projects = requests.get(
            self.url + '/api-v2/projects',
            headers=my_headers,
            params=params_to_add
        )
        projects_json = projects.json()
        return projects_json, projects.status_code

    # Создать проект
    def create_random_project(self):
        project = {
            "title": self.faker.company(),
            "users": user
        }
        create_project = requests.post(
            self.url + '/api-v2/projects',
            json=project,
            headers=my_headers
        )
        return create_project.json(), create_project.status_code, project

    def create_project(self, title, users=None):
        project = {
            "title": title,
            "users": users
        }
        create_project = requests.post(
            self.url + '/api-v2/projects',
            json=project,
            headers=my_headers
        )
        return create_project.json()

    def get_project_id(self, id):
        resp = requests.get(
            self.url + '/api-v2/projects/' + str(id),
            headers=my_headers
        )
        return resp.json(), resp.status_code

    # Изменение/удаление проекта
    def edit_project(self, create_new_id, new_title, deleted=False):
        # Вызываем словарь и кладем в него описание
        project = {
            "deleted": deleted,
            "title": new_title,
            "users": user
        }

        # Метод отправляет запрос по URL, передает заголовки и тело
        resp = requests.put(
            self.url + '/api-v2/projects/' + str(create_new_id),
            headers=my_headers,
            json=project
        )

        # Результат вернется в JSON
        response_json = resp.json()
        return response_json, resp.status_code
