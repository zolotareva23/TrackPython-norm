import doctest
from abc import ABC, abstractmethod


class ConstructionMaterial(ABC):
    """
    Абстрактный класс для представления строительных материалов
    """

    def __init__(self, name: str, density: float, price_per_kg: float):
        """
        Создание и подготовка к работе объекта "Строительный материал"

        :param name: Название материала
        :param density: Плотность материала в кг/м³
        :param price_per_kg: Цена за килограмм материала в рублях

        Примеры:
        >>> material = ConcreteMaterial("Бетон", 2400, 2.5)  # используем конкретную реализацию
        >>> material.name
        'Бетон'
        >>> material.density
        2400.0
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if len(name.strip()) == 0:
            raise ValueError("Название не может быть пустой строкой")
        self.name = name

        if not isinstance(density, (int, float)):
            raise TypeError("Плотность должна быть типа int или float")
        if density <= 0:
            raise ValueError("Плотность должна быть положительным числом")
        self.density = float(density)

        if not isinstance(price_per_kg, (int, float)):
            raise TypeError("Цена за кг должна быть типа int или float")
        if price_per_kg < 0:
            raise ValueError("Цена за кг не может быть отрицательной")
        self.price_per_kg = float(price_per_kg)

    @abstractmethod
    def calculate_weight(self, volume: float) -> float:
        """
        Расчет веса материала для заданного объема

        :param volume: Объем материала в м³
        :return: Вес материала в кг

        :raise ValueError: Если объем не положительный

        Примеры:
        >>> concrete = ConcreteMaterial("Бетон М400", 2400, 2.5)
        >>> concrete.calculate_weight(5)
        12000.0
        >>> concrete.calculate_weight(0)
        Traceback (most recent call last):
        ...
        ValueError: Объем должен быть положительным
        """
        ...

    @abstractmethod
    def calculate_cost(self, volume: float) -> float:
        """
        Расчет стоимости материала для заданного объема

        :param volume: Объем материала в м³
        :return: Стоимость в рублях

        :raise ValueError: Если объем не положительный

        Примеры:
        >>> concrete = ConcreteMaterial("Бетон М400", 2400, 2.5)
        >>> concrete.calculate_cost(5)
        30000.0
        >>> concrete.calculate_cost(-1)
        Traceback (most recent call last):
        ...
        ValueError: Объем должен быть положительным
        """
        ...

    @abstractmethod
    def get_material_category(self) -> str:
        """
        Получение категории материала

        :return: Категория материала ("вяжущее", "заполнитель", "отделочный", "арматура")

        Примеры:
        >>> concrete = ConcreteMaterial("Бетон М400", 2400, 2.5)
        >>> concrete.get_material_category()
        'вяжущее'
        """
        ...


class Stock(ABC):
    """
    Абстрактный класс для представления акций компаний
    """

    def __init__(self, ticker: str, company_name: str, current_price: float):
        """
        Создание и подготовка к работе объекта "Акция"

        :param ticker: Биржевой тикер акции
        :param company_name: Название компании-эмитента
        :param current_price: Текущая цена акции в рублях

        Примеры:
        >>> stock = CommonStock("SBER", "Сбербанк", 300.0)  # используем конкретную реализацию
        >>> stock.ticker
        'SBER'
        >>> stock.current_price
        300.0
        """
        if not isinstance(ticker, str):
            raise TypeError("Тикер должен быть строкой")
        if len(ticker.strip()) == 0:
            raise ValueError("Тикер не может быть пустой строкой")
        self.ticker = ticker.upper()

        if not isinstance(company_name, str):
            raise TypeError("Название компании должно быть строкой")
        if len(company_name.strip()) == 0:
            raise ValueError("Название компании не может быть пустой строкой")
        self.company_name = company_name

        if not isinstance(current_price, (int, float)):
            raise TypeError("Цена акции должна быть типа int или float")
        if current_price <= 0:
            raise ValueError("Цена акции должна быть положительным числом")
        self.current_price = float(current_price)

        self.quantity_owned = 0

    @abstractmethod
    def calculate_dividend_yield(self, dividend_per_share: float) -> float:
        """
        Расчет дивидендной доходности акции

        :param dividend_per_share: Дивиденд на одну акцию в рублях
        :return: Дивидендная доходность в процентах

        :raise ValueError: Если дивиденд отрицательный

        Примеры:
        >>> stock = CommonStock("SBER", "Сбербанк", 300.0)
        >>> stock.calculate_dividend_yield(15.0)
        5.0
        >>> stock.calculate_dividend_yield(-5.0)
        Traceback (most recent call last):
        ...
        ValueError: Дивиденд не может быть отрицательным
        """
        ...

    @abstractmethod
    def calculate_profit(self, purchase_price: float, quantity: int) -> float:
        """
        Расчет прибыли от инвестиции в акции

        :param purchase_price: Цена покупки акции в рублях
        :param quantity: Количество акций
        :return: Прибыль в рублях

        :raise ValueError: Если цена покупки не положительная или количество не положительное

        Примеры:
        >>> stock = CommonStock("SBER", "Сбербанк", 300.0)
        >>> stock.calculate_profit(250.0, 10)
        500.0
        >>> stock.calculate_profit(0, 10)
        Traceback (most recent call last):
        ...
        ValueError: Цена покупки должна быть положительной
        """
        ...

    @abstractmethod
    def get_sector(self) -> str:
        """
        Получение сектора экономики компании

        :return: Сектор экономики ("финансы", "технологии", "энергетика", "потребительские товары")

        Примеры:
        >>> stock = CommonStock("SBER", "Сбербанк", 300.0)
        >>> stock.get_sector()
        'финансы'
        """
        ...

    def buy(self, price: float, quantity: int) -> None:
        """
        Покупка акций

        :param price: Цена покупки за одну акцию
        :param quantity: Количество акций для покупки

        :raise ValueError: Если цена или количество не положительные

        Примеры:
        >>> stock = CommonStock("SBER", "Сбербанк", 300.0)
        >>> stock.buy(280.0, 100)
        >>> stock.quantity_owned
        100
        >>> stock.buy(-10, 5)
        Traceback (most recent call last):
        ...
        ValueError: Цена должна быть положительной
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть типа int или float")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")

        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть типа int")
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")

        self.quantity_owned += quantity


class BankAccount(ABC):
    """
    Абстрактный класс для представления банковских счетов
    """

    def __init__(self, account_number: str, owner_name: str, initial_balance: float):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер счета
        :param owner_name: Имя владельца счета
        :param initial_balance: Начальный баланс счета в рублях

        Примеры:
        >>> account = SavingsAccount("40817810099910004312", "Иванов Иван", 10000.0)  # конкретная реализация
        >>> account.account_number
        '40817810099910004312'
        >>> account.balance
        10000.0
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть строкой")
        if len(account_number.strip()) == 0:
            raise ValueError("Номер счета не может быть пустой строкой")
        if not account_number.isdigit():
            raise ValueError("Номер счета должен содержать только цифры")
        self.account_number = account_number

        if not isinstance(owner_name, str):
            raise TypeError("Имя владельца должно быть строкой")
        if len(owner_name.strip()) == 0:
            raise ValueError("Имя владельца не может быть пустой строкой")
        self.owner_name = owner_name

        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Начальный баланс должен быть типа int или float")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.balance = float(initial_balance)

    @abstractmethod
    def calculate_interest(self, days: int, annual_rate: float) -> float:
        """
        Расчет начисленных процентов за период

        :param days: Количество дней для расчета процентов
        :param annual_rate: Годовая процентная ставка
        :return: Сумма начисленных процентов в рублях

        :raise ValueError: Если количество дней не положительное или ставка отрицательная

        Примеры:
        >>> account = SavingsAccount("40817810099910004312", "Иванов Иван", 10000.0)
        >>> account.calculate_interest(30, 5.0)
        41.0958904109589
        >>> account.calculate_interest(-10, 5.0)
        Traceback (most recent call last):
        ...
        ValueError: Количество дней должно быть положительным
        """
        ...

    @abstractmethod
    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета

        :param amount: Сумма для снятия в рублях
        :return: Фактически снятая сумма

        :raise ValueError: Если сумма для снятия не положительная
        :raise ValueError: Если недостаточно средств на счете

        Примеры:
        >>> account = SavingsAccount("40817810099910004312", "Иванов Иван", 10000.0)
        >>> account.withdraw(5000.0)
        5000.0
        >>> account.withdraw(15000.0)
        Traceback (most recent call last):
        ...
        ValueError: Недостаточно средств на счете
        """
        ...

    @abstractmethod
    def get_account_type(self) -> str:
        """
        Получение типа банковского счета

        :return: Тип счета ("расчетный", "депозит", "кредитный", "сберегательный")

        Примеры:
        >>> account = SavingsAccount("40817810099910004312", "Иванов Иван", 10000.0)
        >>> account.get_account_type()
        'сберегательный'
        """
        ...

    def deposit(self, amount: float) -> None:
        """
        Внесение денег на счет

        :param amount: Сумма для внесения в рублях

        :raise ValueError: Если сумма для внесения не положительная

        Примеры:
        >>> account = SavingsAccount("40817810099910004312", "Иванов Иван", 10000.0)
        >>> account.deposit(5000.0)
        >>> account.balance
        15000.0
        >>> account.deposit(-1000.0)
        Traceback (most recent call last):
        ...
        ValueError: Сумма для внесения должна быть положительной
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма для внесения должна быть положительной")

        self.balance += float(amount)


# Конкретные реализации для демонстрации
class ConcreteMaterial(ConstructionMaterial):
    """Конкретная реализация для бетонного материала"""

    def calculate_weight(self, volume: float) -> float:
        """Расчет веса бетона"""
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем должен быть положительным")
        volume_float = float(volume)
        return self.density * volume_float

    def calculate_cost(self, volume: float) -> float:
        """Расчет стоимости бетона"""
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if volume <= 0:
            raise ValueError("Объем должен быть положительным")
        volume_float = float(volume)
        weight = self.calculate_weight(volume_float)
        return weight * self.price_per_kg

    def get_material_category(self) -> str:
        """Получение категории бетона"""
        return "вяжущее"


class CommonStock(Stock):
    """Конкретная реализация для обыкновенных акций"""

    def calculate_dividend_yield(self, dividend_per_share: float) -> float:
        """Расчет дивидендной доходности"""
        if not isinstance(dividend_per_share, (int, float)):
            raise TypeError("Дивиденд должен быть типа int или float")
        if dividend_per_share < 0:
            raise ValueError("Дивиденд не может быть отрицательным")

        if self.current_price == 0:
            raise ValueError("Цена акции не может быть нулевой")

        dividend_float = float(dividend_per_share)
        return (dividend_float / self.current_price) * 100

    def calculate_profit(self, purchase_price: float, quantity: int) -> float:
        """Расчет прибыли от инвестиции"""
        if not isinstance(purchase_price, (int, float)):
            raise TypeError("Цена покупки должна быть типа int или float")
        if purchase_price <= 0:
            raise ValueError("Цена покупки должна быть положительной")

        if not isinstance(quantity, int):
            raise TypeError("Количество должно быть типа int")
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")

        purchase_price_float = float(purchase_price)
        return (self.current_price - purchase_price_float) * quantity

    def get_sector(self) -> str:
        """Получение сектора компании"""
        if "банк" in self.company_name.lower():
            return "финансы"
        elif "нефть" in self.company_name.lower() or "газ" in self.company_name.lower():
            return "энергетика"
        else:
            return "разное"


class SavingsAccount(BankAccount):
    """Конкретная реализация для сберегательного счета"""

    def calculate_interest(self, days: int, annual_rate: float) -> float:
        """Расчет начисленных процентов"""
        if not isinstance(days, int):
            raise TypeError("Количество дней должно быть типа int")
        if days <= 0:
            raise ValueError("Количество дней должно быть положительным")

        if not isinstance(annual_rate, (int, float)):
            raise TypeError("Годовая ставка должна быть типа int или float")
        if annual_rate < 0:
            raise ValueError("Годовая ставка не может быть отрицательной")

        annual_rate_float = float(annual_rate)
        return self.balance * (annual_rate_float / 100) * (days / 365)

    def withdraw(self, amount: float) -> float:
        """Снятие денег со сберегательного счета"""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть типа int или float")
        if amount <= 0:
            raise ValueError("Сумма для снятия должна быть положительной")

        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")

        amount_float = float(amount)
        self.balance -= amount_float
        return amount_float

    def get_account_type(self) -> str:
        """Получение типа счета"""
        return "сберегательный"


if __name__ == "__main__":
    # Тестирование примеров, которые находятся в документации
    doctest.testmod()

    # Демонстрация работы с конкретными реализациями
    print("=== Демонстрация работы 3 абстрактных классов ===")

    # 1. Строительные материалы
    print("\n1. Строительные материалы:")
    concrete = ConcreteMaterial("Бетон М400", 2400, 2.5)
    print(f"Материал: {concrete.name}")
    print(f"Вес 2.5 м³: {concrete.calculate_weight(2.5)} кг")
    print(f"Стоимость 2.5 м³: {concrete.calculate_cost(2.5)} руб")
    print(f"Категория: {concrete.get_material_category()}")

    # 2. Акции
    print("\n2. Акции:")
    sber_stock = CommonStock("SBER", "Сбербанк", 320.50)
    sber_stock.buy(300.0, 100)
    print(f"Акция: {sber_stock.company_name} ({sber_stock.ticker})")
    print(f"Дивидендная доходность (дивиденд 20 руб): {sber_stock.calculate_dividend_yield(20):.2f}%")
    print(f"Прибыль от 100 акций купленных по 300 руб: {sber_stock.calculate_profit(300.0, 100)} руб")
    print(f"Сектор: {sber_stock.get_sector()}")
    print(f"Акций в наличии: {sber_stock.quantity_owned}")

    # 3. Банковские счета
    print("\n3. Банковские счета:")
    savings = SavingsAccount("40817810123456789012", "Петров Петр", 50000.0)
    print(f"Счет №: {savings.account_number}")
    print(f"Владелец: {savings.owner_name}")
    print(f"Текущий баланс: {savings.balance} руб")
    print(f"Проценты за 90 дней при ставке 6%: {savings.calculate_interest(90, 6.0):.2f} руб")
    print(f"Тип счета: {savings.get_account_type()}")

    # Операции со счетом
    savings.deposit(15000.0)
    print(f"Баланс после внесения 15000 руб: {savings.balance} руб")

    withdrawn = savings.withdraw(20000.0)
    print(f"Снято: {withdrawn} руб")
    print(f"Баланс после снятия: {savings.balance} руб")