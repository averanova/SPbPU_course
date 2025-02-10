import doctest
class Cinema:

    def __init__(self, name: str, address: str):
        """
        Создание и подготовка к работе объекта "Кинотеатр"

        :param name: Название кинотеатра
        :param address: адрес кинотеатра

        Примеры:
        >>> cinema = Cinema("А113", "г. Иваново, ул. 8 Марта, д. 32") #Инициализация экземпляра класса
        """
        self.name = name
        self.address = address
        if not isinstance(name, str):
            raise TypeError("Название кинотеатра должно быть типа str")
        if not isinstance(address, str):
            raise TypeError("Адрес должен быть типа str")

    def list_movies(self) -> list:
        """
        Метод для отображения списка всех фильмов кинотеатра
        :return: список фильмов кинотеатра

        Пример:
        >>> cinema = Cinema("А113", "г. Иваново, ул. 8 Марта, д. 32")
        >>> cinema.list_movies()
        """
        ...

    def add_movie(self, movie: str) -> None:
        """
        Метод для добавления фильма в список фильмов кинотеатра
        :param movie: Название добавляемого фильма
        :return: None

        Примеры:
        >>>cinema = Cinema("А113", "г. Иваново, ул. 8 Марта, д. 32")
        >>>cinema.add_movie("Соник")
        """
        ...

class Car:
    def __init__(self, brand: str, model: str, year: int, mileage:int):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: марка автомобиля
        :param model: модель автомобиля
        :param year: год выпуска автомобиля
        :param mileage: пробег автомобиля

        Примеры:
        >>> car1 = Car("Toyota", "Supra", 2019, 10481) #Инициализация экземпляра класса
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        if year < 0:
            raise ValueError("Год выпуска не может быть отрицательным числом")
        if mileage < 0:
            raise ValueError("Пробег не может быть отрицательным числом")

    def drive(self, distance: int) -> int:
        """
        Метод для увеличения пробега при поездке
        :param distance: расстояние, которое проехал автомобиль
        :return: текущий пробег автомобиля (mileage + distance)

        Примеры:
        >>> car1 = Car("Toyota", "Supra", 2019, 10481)
        >>> car1.drive(250)
        """
        ...

    def refuel(self, liters: int) -> str:
        """
        Метод, описывающий заправку автомобиля

        :param liters:количество литров топлива
        :return: сообщение о заправке автомобиля

        Пример:
        >>> car1 = Car("Toyota", "Supra", 2019, 10481)
        >>> car1.refuel(10)
        """
        return f'Автомобиль {self.brand} {self.model} заправлен на {liters} л.'

class Country:
    def __init__(self, name: str, population: int, area:float):
        """
        Создание и подготовка к работе объекта "Страна"

        :param name: название страны
        :param population: численность населения страны
        :param area: площадь страны км^2.

        Пример:
        >>> Norway = Country("Норвегия", 5550203, 385207)
        """
        self.name = name
        self.population = population
        self.area = area
        if not isinstance(population, int):
            raise TypeError("Численность населения должна быть целым числом")
        if population < 0:
            raise ValueError("Численность населения не может быть отрицательной")
        if area < 0:
            raise TypeError("Площадь не может быть отрицательной")

    def capital(self, cap: str) -> str:
        """
        Метод, возвращающий столицу страны
        :param cap: название столицы страны
        :return: столица страны

        Пример:
        >>> Norway = Country("Норвегия", 5550203, 385207)
        >>> Norway.capital("Осло")
        """
        ...

    def density(self) -> float:
        """
        Метод, который расчитывает плотность населения страны (число жителей на км^2)
        :return: плотность населения (population/area)
        >>> Norway = Country("Норвегия", 5550203, 385207)
        >>>Norway.density()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    Norway = Country("Норвегия", 5550203, 385207)
    print(Norway)
    pass
