from typing import Optional, List, Dict, Any
from datetime import datetime


class SocialMediaAccount:
    """
    Базовый класс для аккаунта в социальной сети.

    Attributes:
        _username (str): Логин пользователя (инкапсулирован для защиты от прямого изменения)
        _email (str): Электронная почта пользователя (инкапсулирована)
        full_name (str): Полное имя пользователя
        registration_date (datetime): Дата регистрации
        is_active (bool): Статус активности аккаунта
        _friends_count (int): Количество друзей (инкапсулирован для контролируемого доступа)
    """

    def __init__(self, username: str, email: str, full_name: str) -> None:
        """
        Инициализация аккаунта в социальной сети.

        Args:
            username: Уникальный логин пользователя
            email: Электронная почта пользователя
            full_name: Полное имя пользователя
        """
        self._username = username
        self._email = self._validate_email(email)
        self.full_name = full_name
        self.registration_date = datetime.now()
        self.is_active = True
        self._friends_count = 0
        self._posts: List[Dict[str, Any]] = []  # Список постов пользователя

    @staticmethod
    def _validate_email(email: str) -> str:
        """
        Статический метод для валидации email.

        Args:
            email: Электронная почта для проверки

        Returns:
            Валидный email

        Raises:
            ValueError: Если email не содержит символа '@'
        """
        if '@' not in email:
            raise ValueError("Некорректный формат email")
        return email

    @property
    def username(self) -> str:
        """Геттер для username (только чтение)."""
        return self._username

    @property
    def email(self) -> str:
        """Геттер для email (только чтение)."""
        return self._email

    @property
    def friends_count(self) -> int:
        """Геттер для количества друзей."""
        return self._friends_count

    @friends_count.setter
    def friends_count(self, value: int) -> None:
        """Сеттер для количества друзей с валидацией."""
        if value < 0:
            raise ValueError("Количество друзей не может быть отрицательным")
        self._friends_count = value

    def create_post(self, content: str, is_public: bool = True) -> Dict[str, Any]:
        """
        Создание нового поста.

        Args:
            content: Текст поста
            is_public: Флаг публичности поста

        Returns:
            Словарь с информацией о созданном посте
        """
        post = {
            'id': len(self._posts) + 1,
            'content': content,
            'created_at': datetime.now(),
            'is_public': is_public,
            'likes': 0,
            'comments': []
        }
        self._posts.append(post)
        return post

    def get_posts(self, public_only: bool = False) -> List[Dict[str, Any]]:
        """
        Получение постов пользователя.

        Args:
            public_only: Если True, возвращаются только публичные посты

        Returns:
            Список постов пользователя
        """
        if public_only:
            return [post for post in self._posts if post['is_public']]
        return self._posts

    def add_friend(self) -> None:
        """Добавление нового друга."""
        self._friends_count += 1

    def remove_friend(self) -> None:
        """Удаление друга."""
        if self._friends_count > 0:
            self._friends_count -= 1

    def deactivate_account(self) -> None:
        """Деактивация аккаунта."""
        self.is_active = False

    def get_account_age_days(self) -> int:
        """
        Получение возраста аккаунта в днях.

        Returns:
            Количество дней с момента регистрации
        """
        delta = datetime.now() - self.registration_date
        return delta.days

    def __str__(self) -> str:
        """Строковое представление для пользователя."""
        status = "активен" if self.is_active else "неактивен"
        return f"Аккаунт {self._username} ({self.full_name}). Статус: {status}"

    def __repr__(self) -> str:
        """Строковое представление для разработчика."""
        return (f"SocialMediaAccount(username={self._username!r}, "
                f"email={self._email!r}, full_name={self.full_name!r})")


class VKAccount(SocialMediaAccount):
    """
    Класс для аккаунта ВКонтакте, наследующий от SocialMediaAccount.

    Добавляет специфичные для ВК атрибуты и методы.

    Attributes:
        vk_id (int): Уникальный ID ВКонтакте
        city (Optional[str]): Город пользователя
        university (Optional[str]): Университет пользователя
        _music_list (List[str]): Список любимой музыки (инкапсулирован)
        _stories (List[Dict]): Список историй (инкапсулирован)
        has_vk_pay (bool): Наличие VK Pay
    """

    def __init__(self, username: str, email: str, full_name: str,
                 vk_id: int, city: Optional[str] = None) -> None:
        """
        Инициализация аккаунта ВКонтакте.

        Args:
            username: Логин пользователя
            email: Электронная почта
            full_name: Полное имя
            vk_id: Уникальный ID ВКонтакте
            city: Город пользователя (опционально)
        """
        # Наследуем конструктор базового класса
        super().__init__(username, email, full_name)

        # Добавляем специфичные атрибуты для ВК
        self.vk_id = vk_id
        self.city = city
        self.university: Optional[str] = None
        self._music_list: List[str] = []  # Инкапсулирован для контроля добавления музыки
        self._stories: List[Dict[str, Any]] = []  # Инкапсулирован, т.к. истории временные
        self.has_vk_pay = False
        self._secret_chats: List[str] = []  # Приватные чаты (полная инкапсуляция)

    def add_music(self, track_name: str, artist: str) -> None:
        """
        Добавление трека в список любимой музыки.

        Args:
            track_name: Название трека
            artist: Исполнитель
        """
        music_entry = f"{artist} - {track_name}"
        if music_entry not in self._music_list:
            self._music_list.append(music_entry)

    def get_music_list(self) -> List[str]:
        """
        Получение списка любимой музыки.

        Returns:
            Копия списка музыки (для защиты исходных данных)
        """
        return self._music_list.copy()

    def create_story(self, content: str, duration_hours: int = 24) -> Dict[str, Any]:
        """
        Создание истории (специфичный метод для ВК).

        Args:
            content: Содержимое истории
            duration_hours: Длительность отображения истории в часах

        Returns:
            Словарь с информацией о созданной истории
        """
        story = {
            'id': len(self._stories) + 1,
            'content': content,
            'created_at': datetime.now(),
            'expires_at': datetime.now().timestamp() + duration_hours * 3600
        }
        self._stories.append(story)
        return story

    def get_active_stories(self) -> List[Dict[str, Any]]:
        """
        Получение активных историй.

        Returns:
            Список историй, которые еще не истекли
        """
        current_time = datetime.now().timestamp()
        return [story for story in self._stories if story['expires_at'] > current_time]

    # ПЕРЕГРУЗКА метода create_post из базового класса
    def create_post(self, content: str, is_public: bool = True,
                    allow_comments: bool = True, allow_reposts: bool = True) -> Dict[str, Any]:
        """
        Перегрузка метода create_post с добавлением специфичных для ВК параметров.

        Причина перегрузки: В ВКонтакте есть дополнительные настройки поста,
        которых нет в базовом классе (комментарии, репосты).

        Args:
            content: Текст поста
            is_public: Флаг публичности поста
            allow_comments: Разрешить комментарии
            allow_reposts: Разрешить репосты

        Returns:
            Словарь с информацией о созданном посте
        """
        post = super().create_post(content, is_public)
        # Добавляем специфичные для ВК поля
        post['allow_comments'] = allow_comments
        post['allow_reposts'] = allow_reposts
        post['vk_specific'] = True
        return post

    # НАСЛЕДОВАНИЕ метода add_friend из базового класса
    # (используется без изменений, поэтому явно не переопределяется)

    def enable_vk_pay(self) -> None:
        """Активация VK Pay."""
        self.has_vk_pay = True

    def _add_secret_chat(self, chat_id: str) -> None:
        """
        Приватный метод для добавления приватного чата.

        Инкапсулирован, так как доступ к приватным чатам должен быть
        строго контролируемым.

        Args:
            chat_id: ID приватного чата
        """
        if chat_id not in self._secret_chats:
            self._secret_chats.append(chat_id)

    def send_money_vk_pay(self, amount: float, recipient: 'VKAccount') -> bool:
        """
        Перевод денег через VK Pay (специфичный метод для ВК).

        Args:
            amount: Сумма перевода
            recipient: Получатель

        Returns:
            True если перевод успешен, False в противном случае

        Raises:
            ValueError: Если сумма отрицательная или получатель не имеет VK Pay
        """
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")
        if not self.has_vk_pay or not recipient.has_vk_pay:
            raise ValueError("У одного из пользователей не активирован VK Pay")

        # Здесь была бы логика реального перевода
        print(f"Перевод {amount} руб. от {self.username} к {recipient.username}")
        return True

    def __str__(self) -> str:
        """Перегрузка строкового представления с добавлением информации о ВК."""
        base_str = super().__str__()
        city_info = f", Город: {self.city}" if self.city else ""
        return f"{base_str} (ВКонтакте, ID: {self.vk_id}{city_info})"

    def __repr__(self) -> str:
        """Перегрузка repr с добавлением специфичных атрибутов ВК."""
        return (f"VKAccount(username={self.username!r}, email={self.email!r}, "
                f"full_name={self.full_name!r}, vk_id={self.vk_id}, city={self.city!r})")


# Пример использования классов
def demonstrate_inheritance():
    """Демонстрация работы наследования."""

    print("=== Демонстрация наследования ===\n")

    # Создаем базовый аккаунт
    print("1. Создание базового аккаунта:")
    basic_account = SocialMediaAccount(
        username="ivan_petrov",
        email="ivan@example.com",
        full_name="Иван Петров"
    )
    print(f"   {basic_account}")
    print(f"   Repr: {repr(basic_account)}")

    # Создаем пост через базовый метод
    post1 = basic_account.create_post("Мой первый пост!")
    print(f"   Создан пост: {post1['content'][:30]}...")
    print(f"   Количество друзей: {basic_account.friends_count}")

    # Добавляем друзей
    basic_account.add_friend()
    basic_account.add_friend()
    print(f"   После добавления друзей: {basic_account.friends_count}")

    print("\n" + "=" * 50 + "\n")

    # Создаем аккаунт ВКонтакте
    print("2. Создание аккаунта ВКонтакте:")
    vk_account = VKAccount(
        username="anna_smith",
        email="anna@example.com",
        full_name="Анна Смит",
        vk_id=123456789,
        city="Москва"
    )
    print(f"   {vk_account}")
    print(f"   Repr: {repr(vk_account)}")

    # Используем унаследованный метод
    print("\n3. Использование унаследованного метода add_friend():")
    vk_account.add_friend()
    vk_account.add_friend()
    vk_account.add_friend()
    print(f"   Количество друзей ВК: {vk_account.friends_count}")

    # Используем перегруженный метод
    print("\n4. Использование перегруженного метода create_post():")
    vk_post = vk_account.create_post(
        content="Привет из ВКонтакте!",
        is_public=True,
        allow_comments=True,
        allow_reposts=False
    )
    print(f"   Создан пост ВК: {vk_post['content']}")
    print(f"   Разрешены комментарии: {vk_post['allow_comments']}")
    print(f"   Разрешены репосты: {vk_post['allow_reposts']}")

    # Используем специфичные методы ВК
    print("\n5. Использование специфичных методов ВК:")
    vk_account.add_music("Bohemian Rhapsody", "Queen")
    vk_account.add_music("Smells Like Teen Spirit", "Nirvana")
    print(f"   Любимая музыка: {vk_account.get_music_list()}")

    # Создаем историю и сразу используем её
    created_story = vk_account.create_story("Мой день в парке!", 12)
    active_stories_count = len(vk_account.get_active_stories())
    print(f"   Создана история '{created_story['content'][:15]}...' на {12} часов")
    print(f"   Активных историй: {active_stories_count}")

    # Активируем VK Pay
    vk_account.enable_vk_pay()
    print(f"   VK Pay активирован: {vk_account.has_vk_pay}")

    print("\n6. Проверка полиморфизма:")
    accounts = [basic_account, vk_account]

    for i, account in enumerate(accounts, 1):
        print(f"   {i}. {account}")
        # Вызов полиморфного метода
        account.create_post(f"Тестовый пост {i}")
        print(f"   Количество постов: {len(account.get_posts())}")

    print("\n" + "=" * 50)
    print("Демонстрация завершена успешно!")


# Дополнительная демонстрация валидации
def demonstrate_validation():
    """Демонстрация валидации данных."""
    print("\n=== Демонстрация валидации данных ===")

    # Проверка некорректного email без сохранения переменной
    print("1. Проверка валидации email:")
    try:
        # Некорректный email - не сохраняем объект, так как он не создастся
        SocialMediaAccount(
            username="test_user",
            email="invalid-email",  # Нет символа '@'
            full_name="Тестовый Пользователь"
        )
        print("   Ошибка: объект создался с некорректным email!")
    except ValueError as e:
        print(f"   Успешно: {e}")

    # Проверка валидации через сеттер
    print("\n2. Проверка валидации количества друзей:")
    account = SocialMediaAccount("user1", "user1@example.com", "Пользователь 1")
    try:
        account.friends_count = -5  # Должно вызвать ошибку
        print("   Ошибка: установлено отрицательное количество друзей!")
    except ValueError as e:
        print(f"   Успешно: {e}")

    # Успешная установка корректного значения
    account.friends_count = 10
    print(f"   Корректное значение установлено: {account.friends_count} друзей")

    print("\nВалидация работает корректно!")


# Демонстрация работы с приватными атрибутами
def demonstrate_encapsulation():
    """Демонстрация принципа инкапсуляции."""
    print("\n=== Демонстрация инкапсуляции ===")

    vk_account = VKAccount("demo_user", "demo@example.com", "Демо Пользователь", 999999, "Санкт-Петербург")

    print("1. Попытка прямого доступа к приватным атрибутам:")
    try:
        # Попытка доступа к приватному атрибуту (работает, но не рекомендуется)
        print(f"   Приватный email (не рекомендуется): {vk_account._email}")
    except AttributeError:
        print("   Не удалось получить доступ к приватному атрибуту")

    print("\n2. Использование геттеров:")
    print(f"   Email через свойство: {vk_account.email}")
    print(f"   Username через свойство: {vk_account.username}")

    print("\n3. Проверка, что свойства только для чтения:")
    try:
        vk_account.username = "новый_логин"  # Должно вызвать ошибку
    except AttributeError as e:
        print(f"   Успешно защищено от изменения: {type(e).__name__}")

    print("\nИнкапсуляция работает корректно!")


if __name__ == "__main__":
    demonstrate_inheritance()
    demonstrate_validation()
    demonstrate_encapsulation()