from typing import Callable, Literal
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element
from abc import ABC
from typing import ClassVar, Type


class BaseWidget(ABC):
    pass


class ChildrenWidget(BaseWidget):
    children: list[BaseWidget] = []

    def __init__(self, *args):
        self.children = list(args)

    def add(self, children: BaseWidget):
        self.children.append(children)


class If(ChildrenWidget):
    test: str
    orelse: list[BaseWidget]


class View(ChildrenWidget):
    width: int
    direction: Literal['row', 'column']

    def __init__(self, *args):
        super().__init__(*args)


class Keyboard(View):
    children: list = []

    def __init__(self, *args, width: int | None = None):
        super().__init__(*args)
        self.children = list(args)
        self.width = width


class Button(BaseWidget):
    title: str
    on_click: Callable

    def __init__(self, title: str, on_click: Callable | str | None = None):
        self.title = title
        self.on_click = on_click


Keyboard(
    Button('One', lambda: print('Hello World')),
    Button('Two', lambda: print('Hello World')),
    Button('Two', lambda: print('Hello World')),
    Button('Two', lambda: print('Hello World')),
    Button('Two', lambda: print('Hello World')),
    Keyboard(
        Button('Another', lambda: print('Another')),
        Button('Another', lambda: print('Another')),
        Button('Another', lambda: print('Another')),
        Button('Another', lambda: print('Another')),
    ),
    width=5,
)


