import pytest
import allure
from settings import DEFAULT_LAST_NAME
from pages.manager_page import ManagerPage
from tests.utils import generate_customer_data
from tests.utils import find_customer_delete

@allure.title("Тест1. Успешное создание клиента")
@allure.description("Создание и проверка нового клиента")
@allure.story("Создание клиента")
def test_add_customer(driver, base_url):
    manager_page = ManagerPage(driver, base_url)

    manager_page.open()

    manager_page.click_add_customer_button()

    first_name, post_code = generate_customer_data()
    last_name = DEFAULT_LAST_NAME

    manager_page.fill_customer_form(first_name, last_name, post_code)
    manager_page.submit_customer_form()

    alert_text = manager_page.accept_alert()
    with allure.step("Проверить, что данные в таблице соответствуют ожидаемым"):
        customer_data = manager_page.get_customer_data_from_row()

        assert customer_data["first_name"] == first_name
        assert customer_data["last_name"] == last_name
        assert customer_data["post_code"] == post_code

@allure.title("Tест2. Сортировка клиентов по имени")
@allure.feature("Клиенты")
@allure.story("Сортировка")
@pytest.mark.usefixtures("create_three_customers")
def test_sort_customers_by_first_name(driver, base_url):
    """
    Проверяет корректность сортировки на наборе свежесозданных данных.
    Фикстура 'create_three_customers' подготавливает 3 новых клиента.
    """
    manager_page = ManagerPage(driver, base_url)

    with allure.step("Открыть вкладку 'Customers'"):
        manager_page.go_to_customers_tab()

    original_names = manager_page.get_customer_first_names()

    with allure.step("Отсортировать по убыванию (Z-A) и проверить"):
        manager_page.sort_by_first_name()
        sorted_names_desc = manager_page.get_customer_first_names()
        assert sorted_names_desc == sorted(
            original_names, reverse=True
        ), "Сортировка по убыванию не работает"

    with allure.step("Отсортировать по возрастанию (A-Z) и проверить"):
        manager_page.sort_by_first_name()
        sorted_names_asc = manager_page.get_customer_first_names()
        assert sorted_names_asc == sorted(
            original_names
        ), "Сортировка по возрастанию не работает"


@allure.title("Tест3. Удаление клиента по алгоритму")
@allure.story("Удаление")
@pytest.mark.usefixtures("create_three_customers")
def test_delete_customer(driver, base_url):
    """
    Проверяет удаление клиента, имя которого имеет длину,
    ближайшую к средней арифметической длине всех имен.
    Фикстура 'create_three_customers' подготавливает 3 новых клиента.
    """
    manager_page = ManagerPage(driver, base_url)

    with allure.step("Открыть вкладку 'Customers'"):
        manager_page.go_to_customers_tab()

    with allure.step("Найти клиента для удаления по алгоритму"):
        all_names = manager_page.get_customer_first_names()

        name_to_delete = find_customer_delete(all_names)

    with allure.step(
        f"Удалить клиента '{name_to_delete}' и проверить результат"
    ):  # noqa: E501
        manager_page.delete_customer(name_to_delete)

        remaining_names = manager_page.get_customer_first_names()

        assert (
            name_to_delete not in remaining_names
        ), f"Клиент '{name_to_delete}' все еще в таблице"
        assert (
            len(remaining_names) == len(all_names) - 1
        ), "Количество клиентов не уменьшилось на 1"