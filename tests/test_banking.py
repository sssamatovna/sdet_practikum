import pytest
import allure

from sdet_practikum.settings import DEFAULT_LAST_NAME
from sdet_practikum.pages.manager_page import ManagerPage
from sdet_practikum.utils.random_data import generate_customer_data
from sdet_practikum.utils.customer_helper import find_customer_delete

@allure.title("Создание клиента: Post Code -> First Name")
@allure.story("Создание клиента")
def test_add_customer(driver, base_url):
    page = ManagerPage(driver, base_url)

    with allure.step("Открыть менеджер и форму Add Customer"):
        page.open()
        page.click_add_customer_button()

    with allure.step("Сгенерировать валидные данные"):
        first_name, post_code = generate_customer_data()  # 10 цифр -> 5 букв
        last_name = DEFAULT_LAST_NAME

    with allure.step("Заполнить и отправить форму"):
        page.fill_customer_form(first_name, last_name, post_code)
        page.submit_customer_form()
        alert_text = page.accept_alert()
        assert "Customer added successfully" in alert_text

    with allure.step("Перейти в Customers и проверить последнюю строку"):
        page.go_to_customers_tab()
        row = page.get_last_row_data()
        assert row["first_name"] == first_name
        assert row["last_name"] == last_name
        assert row["post_code"] == post_code

@allure.title("Сортировка клиентов по First Name")
@allure.story("Сортировка клиентов")
@pytest.mark.usefixtures("create_three_customers")
def test_sort_customers_by_firstname(driver, base_url):
    page = ManagerPage(driver, base_url)
    page.open()
    page.go_to_customers_tab()

    with allure.step("Клик по заголовку 'First Name' — сортировка ASC"):
        page.sort_by_first_name()
        asc = page.get_all_first_names()
        assert asc == sorted(asc), "Ожидалась сортировка по возрастанию"

    with allure.step("Клик ещё раз — сортировка DESC"):
        page.sort_by_first_name()
        desc = page.get_all_first_names()
        assert desc == sorted(desc, reverse=True), "Ожидалась сортировка по убыванию"

@allure.title("Удаление клиента с длиной имени, ближайшей к среднему значению")
@allure.story("Удаление клиента")
@pytest.mark.usefixtures("create_three_customers")
def test_delete_customer(driver, base_url):
    page = ManagerPage(driver, base_url)
    page.open()
    page.go_to_customers_tab()

    with allure.step("Считать все имена таблицы и выбрать цель"):
        names = page.get_all_first_names()
        target = find_customer_delete(names)
        assert target, "Не удалось выбрать цель для удаления"

    with allure.step(f"Удалить клиента {target}"):
        page.delete_by_first_name(target)

    with allure.step("Проверить, что клиент исчез из таблицы (без поиска)"):
        names_after = page.get_all_first_names()
        assert target not in names_after