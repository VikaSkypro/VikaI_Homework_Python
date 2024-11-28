from ProjectsApi import ProjectsApi

api = ProjectsApi("https://ru.yougile.com")


# Получить список проектов
def test_get_project():
    # создаем проект
    created_project, status_code_create, _ = (
        api.create_random_project()
    )  # Теперь распаковываем только нужные значения
    created_id = created_project["id"]
    # получаем список
    body, status_code = api.get_projects()
    # Проверка, что полученное тело ответа является словарем
    assert isinstance(body, dict), "Ожидался словарь, но получен другой тип."
    # проверяем, что кол-во проектов в content совпадает с count из paging
    assert len(body["content"]) == body["paging"]["count"]
    # print(len(body['content']))
    # Получение удаленных проектов
    body2, status_code2 = api.get_projects(
        params_to_add={"includeDeleted": "true"}
    )  # true пишется строчными.
    assert isinstance(body2, dict), "Ожидался словарь, но получен другой тип."
    # проверка, что активных проектов меньше чем всех(вкл удаленные)
    assert len(body2["content"]) > len(body["content"])

    assert status_code == 200
    assert status_code2 == 200
    # Удаляем созданный проект, что бы не переполнить limit
    edit_response, edit_status_code = api.edit_project(
        created_id, new_title="deleted", deleted=True
    )
    assert (
        edit_status_code == 200
    ), f"Не удалось удалить проект. Код статуса: {edit_status_code}. Ответ: {edit_response}"


# Проверка добавления нового проекта
def test_add_project():
    body, _ = api.get_projects()
    len_before = len(body["content"])

    result, status_code, created_project = api.create_random_project()
    new_id = result["id"]

    body, _ = api.get_projects()
    len_after = len(body["content"])
    assert len_after - len_before == 1
    assert body["content"][-1]["id"] == str(new_id)
    assert body["content"][-1]["title"] == created_project["title"]
    assert body["content"][-1]["users"] == created_project["users"]
    # print(project)
    # print(
    #    f"Количество проектов до добавления: {len_before}, после добавления: {len_after}"
    #)

    # Удаляем созданный проект, что бы не переполнить limit
    edit_response, edit_status_code = api.edit_project(
        new_id, new_title="deleted", deleted=True
    )
    assert (
        edit_status_code == 200
    ), f"Не удалось удалить проект. Код статуса: {edit_status_code}. Ответ: {edit_response}"


# Создание проекта без заполнения названия проекта
def test_neg_add_project():
    global result
    title = ""  # Пустое название проекта
    try:
        result = api.create_project(title)
        assert (
            result["statusCode"] == 400
        ), f"Ожидается статус - код: 400, получен: {result['statusCode']}"
        expected_message = ["title should not be empty"]
        assert (
            result["message"] == expected_message
        ), f"Ожидается сообщение: {expected_message}, получено: {result['message']}"

    except Exception as e:
        print(f"Получено исключение: {e}")


# Получение информации о проекте по id
def test_get_one_project():
    # создаем проект
    result, status_code, created_project = api.create_random_project()
    new_id = result["id"]
    # получаем проект по id
    project_data, project_status_code = api.get_project_id(new_id)

    # Проверяем, что id и статус-код правильные
    assert project_data["id"] == str(new_id)
    assert project_status_code == 200

    # Проверяем, что title присутствует в данных проекта
    assert "title" in project_data, f"Response data: {project_data}"
    assert project_data["title"] == created_project["title"]

    # Удаляем созданный проект, что бы не переполнить limit
    edit_response, edit_status_code = api.edit_project(
        new_id, new_title="deleted", deleted=True
    )
    assert (
        edit_status_code == 200
    ), f"Не удалось удалить проект. Код статуса: {edit_status_code}. Ответ: {edit_response}"


def test_neg_get_project():
    # Используем несуществующий id
    non_existent_id = 999999

    # Получаем проект по указанному id
    project_data, project_status_code = api.get_project_id(non_existent_id)

    # Проверяем статус-код на наличие 429
    if project_status_code == 429:
        assert (
            project_status_code == 429
        ), f"Слишком много запросов: {project_status_code}. Убедитесь, что лимит не превышен."

    # Проверяем, что статус-код 404 (не найдено)
    assert (
        project_status_code == 404
    ), f"Непредвиденный status code: {project_status_code}"
    assert (
        project_data.get("message") == "Проект не найден"
    ), f"Непредвиденное сообщение: {project_data}"
    assert (
        project_data.get("error") == "Not Found"
    ), f"Непредвиденная ошибка: {project_data}"


# редактирование проекта
def test_edit_project():
    result, status_code, created_project = api.create_random_project()
    new_id = result["id"]
    assert status_code == 201
    assert "id" in result, f"проект не создан: {result}"

    create_new_id = result["id"]
    # print("создан проект:", result)

    result_check, status_code_check = api.get_project_id(create_new_id)
    assert (
        status_code_check == 200
    ), f"Проект с ID {create_new_id} не найден. Ответ: {result_check}"

    new_title = "Новое название"

    edited, edit_status_code = api.edit_project(create_new_id, new_title)
    assert edit_status_code == 200

    result_after_edit, status_code_after_edit = api.get_project_id(create_new_id)
    assert status_code_after_edit == 200
    assert result_after_edit["title"] == new_title

    # Удаляем созданный проект, что бы не переполнить limit
    edit_response, edit_status_code = api.edit_project(
        new_id, new_title="deleted", deleted=True
    )
    assert (
        edit_status_code == 200
    ), f"Не удалось удалить проект. Код статуса: {edit_status_code}. Ответ: {edit_response}"


# Редактирование проекта с указанием пустого title
def test_neg_edit_project():
    # создаем проект
    created_project, status_code_create, _ = api.create_random_project()
    created_id = created_project["id"]

    # Пытаемся редактировать проект с пустым полем title
    edit_response, edit_status_code = api.edit_project(
        created_id, new_title="", deleted=False
    )

    # Проверка, что статус - код равен 400 (Bad Request)
    assert (
        edit_status_code == 400
    ), f"Ожидался статус 400, но получили: {edit_status_code}. Ответ: {edit_response}"

    # Проверка, что сообщение об ошибке указывает на отсутствие title
    assert "title should not be empty" in edit_response.get(
        "message", []
    ), f"Неожиданное сообщение об ошибке: {edit_response}"

    # Удаляем созданный проект, что бы не переполнить limit
    edit_response, edit_status_code = api.edit_project(
        created_id, new_title="deleted", deleted=True
    )
    assert (
        edit_status_code == 200
    ), f"Не удалось удалить проект. Код статуса: {edit_status_code}. Ответ: {edit_response}"
