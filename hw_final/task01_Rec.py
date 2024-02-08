import logging
import argparse

FORMAT = '{levelname} - {asctime}. В модуле "{name}" в строке {lineno:03d}, функция "{funcName}()," ' \
         'в {created} секунд, записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', filename="logErrorsRectangle", level=logging.NOTSET, encoding="utf-8")
logger = logging.getLogger(__name__)


class NegativeValueError(Exception):
    def __init__(self, message=None):
        super().__init__(message)


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            logger.error(f'Ширина должна быть положительной, а не {width} -- Rectangle({width}, {height})')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(f'Высота должна быть положительной, а не {height} -- Rectangle({width}, {height})')
                raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            logger.info(f"Переустановили ширину {value} -- Rectangle({self._width}, {self._height})")
            self._width = value
        else:
            logger.error(f'Ширина должна быть положительной, а не {value}  -- Rectangle({self._width}, {self._height})')
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            logger.info(f"Переустановили длину {value} -- Rectangle({self._width}, {self._height})")
            self._height = value
        else:
            logger.error(f'Высота должна быть положительной, а не {value}')
            raise NegativeValueError(f'Высота должна быть положительной, а не {value} -- Rectangle({self._width}, {self._height})')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


def parser():
    new_parser = argparse.ArgumentParser(description='Сreates a Кectangle and calculates its perimeter and area')
    new_parser.add_argument('-width', metavar='width', type=int, help='enter width for Rectangle(width, height)',
                            default=1)
    new_parser.add_argument('-height', metavar='height', type=int, help='enter height for Rectangle(width, height)',
                            default=2)
    args = new_parser.parse_args()
    rec = Rectangle(args.width, args.height)
    return f"perimeter - {rec.perimeter()}, area - {rec.area()}"


if __name__ == '__main__':
    Rectangle(1, 4)
    print(parser())
