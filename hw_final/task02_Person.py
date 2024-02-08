import logging
import argparse

FORMAT = '{levelname} - {asctime}. В модуле "{name}" в строке {lineno:03d}, функция "{funcName}()," ' \
         'в {created} секунд, записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', filename="logErrorsPerson", level=logging.NOTSET, encoding="utf-8")
logger = logging.getLogger(__name__)


class InvalidNameError(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class InvalidAgeError(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self._age = age
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        logger.info(f"added age by 1 -- Person({self.full_name()})")
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        if (len(last_name) == 0) or (len(first_name) == 0) or (len(last_name) == 0):
            message = f"Invalid last_name, first_name or patronymic. It should be a non-empty string."
            logger.error(message)
            raise InvalidNameError(message)
        if age < 0 or type(age) is not int:
            message = f"Invalid age: {age}. Age should be a positive integer."
            logger.error(message)
            raise InvalidAgeError(message)
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary
        logger.info(f"initialized the object -- Person({self.full_name()} ({self.position})")

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


def parser():
    new_parser = argparse.ArgumentParser(description='Сreates a Person and calculates its perimeter and area')
    new_parser.add_argument('-last_name', metavar='last_name', type=str, help='enter last_name to create Person',
                            default="No last_name")
    new_parser.add_argument('-first_name', metavar='first_name', type=str, help='enter first_name to create Person',
                            default="No first_name")
    new_parser.add_argument('-patronymic', metavar='patronymic', type=str, help='enter patronymic to create Person',
                            default="No patronymic")
    new_parser.add_argument('-age', metavar='age', type=int, help='enter age to create Person',
                            default=1)
    new_parser.add_argument('-position', metavar='position', type=str, help='enter position to create Employee',
                            default="Intern")
    new_parser.add_argument('-salary', metavar='salary', type=int, help='enter salary to create Employee',
                            default=1)
    args = new_parser.parse_args()
    emp = Employee(args.last_name, args.first_name, args.patronymic, args.age, args.position, args.salary)
    print(f"Employee - {emp.__str__()}, age - {emp.get_age()}, salary - {emp.salary}")


if __name__ == '__main__':
    emp1 = Employee("Ivanov", "Ivan", "Ivanovich", 30, "Manager", 50000)
    emp1.birthday()
    parser()
