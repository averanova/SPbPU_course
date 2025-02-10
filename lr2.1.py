if __name__ == "__main__":
    # Write your solution here
    class Countries:
        """Базовый класс, описывающий страну"""

        def __init__(self, name: str, population_size: int):
            """Инициализация страны с её названием и численностью населения"""

            self._name = name  # Название страны, защищен для предотвращения несанкционированного изменения
            self._population_size = population_size  # Численность населения, защищен для предотвращения несанкционированного изменения

        def __str__(self) -> str:
            """Возвращает строковое представление страны"""

            return f'Страна {self._name}, численность населения: {self._population_size}'

        def __repr__(self) -> str:
            """Возвращает строковое представление для откладки"""

            return f'Countries(name = {self._name!r}, population_size = {self._population_size!r})'

        def language(self) -> str:
            """Метод перегружен в дочерних классах так как страна может иметь один или несколько официальных языков"""

            raise NotImplementedError("Метод реализован в дочерних классах")

    class Japan(Countries):
        """Дочерний класс, который представляет Японию"""

        def __init__(self, name: str, population_size: int):
            """Инициализация Японии с её именем и численностью населения"""

            super().__init__(name, population_size)

        def __str__(self) -> str:
            """Возвращает строковое представление Японии"""

            return f'Страна {self._name}, численность населения: {self._population_size}'

        def __repr__(self) -> str:
            """Возвращает строковое представление для откладки"""

            return f'Japan(name = {self._name!r}, population_size = {self._population_size!r})'

        def language(self) -> str:
            """Возвращает официальный язык Японии"""
            return "Японский"

        class Canada(Countries):
            """Дочерний класс, который представляет Канаду"""

            def __init__(self, name: str, population_size: int):
                """Инициализация Канады с её именем и численностью населения"""

                super().__init__(name, population_size)

            def __str__(self) -> str:
                """Возвращает строковое представление Японии"""

                return f'Страна {self._name}, численность населения: {self._population_size}'

            def __repr__(self) -> str:
                """Возвращает строковое представление Канады для откладки"""

                return f'Canada(name = {self._name!r}, population_size = {self._population_size!r})'

            def language(self) -> str:
                """Возвращает официальные языки Канады"""
                return "Английский и Французский"

    pass
