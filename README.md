# Инструкция по запуску тестов для формирования отчета Allure.
1. Перейти в директорию с тестами.
2. Запустить тесты и указать путь к каталогу результатов тестирования:
   ```
   pytest --alluredir allure-result
   ```
   или
   ```
   python -m pytest --alluredir allure-result
   ```
   В директории с тестами появится папка ***allure-result***. Там сохранятся отчеты о тестах.
3. Следующая команда запускает Allure и конвертирует результаты теста в отчет:
   ```
   allure serve allure-result
   ```
   
4. В командной строке нажать ```Ctrl+C -> Y``` - это завершает работу утилиты.
5. _Allure Report_ — это утилита. Она обрабатывает результаты тестирования и создает HTML-отчет.
   Allure умеет генерировать отчет в файл — его можно выгружать. 

   Для этого используется команда:
   ```
   allure generate allure-result 
   ```
   где, allure-result это название папки.

   Результат выгрузится в папку ***allure-report***.
6. В файле __index.html__ хранится результат отчета, его можно запускать с помощью команды:
   ```
   allure open allure-report
   ```
   Если вы отправите папку allure-report коллеге, то он сможет открывать этой командой результаты у себя на компьютере.
