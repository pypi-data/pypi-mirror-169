from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.types.inline_keyboard import InlineKeyboardMarkup
from .nodes import Tag



def create_component(children, props) -> Component:
    return Component(children, props)


def render(root: Tag) -> ReplyKeyboardMarkup | ReplyKeyboardRemove | InlineKeyboardMarkup:
    tree = None

    message = root.find('Message')
    if message is not None:
        keyboard = message.find('KeyBoard')
        text = message.find('Text')



    raise NameError(f"Root node can be only <Message/> or <KeyBoard/> components")

