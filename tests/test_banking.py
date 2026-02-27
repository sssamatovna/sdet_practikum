import allure
from pages.manager_page import ManagerPage
from pages.customers_page import CustomersPage
from utils import random_data
from utils.customer_helper import find_customer_delete

@allure.feature("Banking Project - Customer Management")
class TestBanking:

    @allure.title("Создание клиента с помощью сгенерированных данных")
    @allure.story("TC-001: Создание клиента")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_customer(self, driver, base_url):
        manager_page = ManagerPage(driver, base_url)
        customers_page = CustomersPage(driver, base_url)
        manager_page.open()

        # 1. Генерация данных
        post_code = random_data.generate_post_code()
        first_name = random_data.generate_first_name(post_code)
        last_name = "Sdet"

        with allure.step(f"Данные: {first_name}, {last_name}, {post_code}"):
            manager_page.go_to_add_customer()
            alert_text = manager_page.add_customer(first_name, last_name, post_code)

            assert "Customer added successfully" in alert_text, f"Ожидался успешный alert, но получен: {alert_text}"

            manager_page.go_to_customers_list()
            names = customers_page.get_all_first_names()

            assert first_name in names, f"Клиент '{first_name}' не найден в списке после добавления."

    @allure.title("Проверка сортировки клиентов по имени")
    @allure.story("TC-002: Сортировка клиентов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_customers(self, driver, base_url, create_test_customers):
        manager_page = ManagerPage(driver, base_url)
        customers_page = CustomersPage(driver, base_url)
        manager_page.open()

        manager_page.go_to_customers_list()

        # 1. Подготовка списка для сравнения.
        # Сортируем сгенерированные имена A-Z, чтобы получить ожидаемые списки
        # test_names = ['Cxkud', 'Negksjmlr', 'Vnymopf']
        test_names_asc = sorted(create_test_customers)
        test_names_desc = sorted(create_test_customers, reverse=True)

        # 2. Клик 1: Ожидаем Z-A (как показал предыдущий запуск)
        with allure.step("Проверка сортировки Z-A (Первый клик)"):
            customers_page.sort_by_first_name()
            names_after_sort = customers_page.get_all_first_names()

            # Фильтруем, чтобы получить только наши 3 имени в порядке, как их отсортировала UI
            test_names_after = [name for name in names_after_sort if name in create_test_customers]

            # Утверждение, что порядок соответствует Z-A
            assert test_names_after == test_names_desc, (
                f"Первый клик не привел к сортировке Z-A. Ожидалось: {test_names_desc}, Получено: {test_names_after}"
            )

        # 3. Клик 2: Ожидаем A-Z
        with allure.step("Проверка сортировки A-Z (Второй клик)"):
            customers_page.sort_by_first_name()  # Второй клик
            names_after_sort = customers_page.get_all_first_names()

            # Фильтруем, чтобы проверить только наши 3 имени
            test_names_after = [name for name in names_after_sort if name in create_test_customers]

            # Утверждение, что порядок соответствует A-Z
            assert test_names_after == test_names_asc, (
                f"Второй клик не привел к сортировке A-Z. Ожидалось: {test_names_asc}, Получено: {test_names_after}"
            )

    @allure.title("Удаление клиента с длиной имени, ближайшей к среднему значению")
    @allure.story("TC-003: Удаление клиента")
    @allure.severity(allure.severity_level.NORMAL)
    def test_delete_customer(self, driver, base_url, create_test_customers):
        manager_page = ManagerPage(driver, base_url)
        customers_page = CustomersPage(driver, base_url)
        manager_page.open()

        manager_page.go_to_customers_list()

        with allure.step("Считать все имена таблицы и выбрать цель"):
            names = customers_page.get_all_first_names()
            # Берем только тестовые имена
            target_names = [name for name in names if name in create_test_customers]
            target = find_customer_delete(target_names)
            assert target, "Не удалось выбрать цель для удаления"

        with allure.step(f"Удалить клиента {target}"):
            customers_page.delete_by_first_name(target)

        # Правка №2: Добавлено сообщение об ошибке
        with allure.step("Проверить, что клиент исчез из таблицы (без поиска)"):
            names_after = customers_page.get_all_first_names()
            assert target not in names_after, f"ОШИБКА: Клиент '{target}' не был удален из таблицы. Текущие имена: {names_after}"
