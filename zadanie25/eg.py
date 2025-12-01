import sys

from rich import print
from time import sleep


def type_line(text, char_delay):
    for char in text:
        print(f'[bold cyan]{char}[/bold cyan]', end = '')
        sleep(char_delay)
    print()


def printlyrics():
    lines = [
        ("Коси, моя коса, блядь, пока роса (Хм-м)", 0.1),
        ("Этим белым нужен трэп, этим белым не до сна", 0.1),
        ("Один в поле тоже воин (Фа), моя молва ясна (Фа)", 0.1),
        ("Full of G's and dirty bitches (Фа), пополняется казна (Фа, фа, фа)", 0.1),
        ("Поддержи комфорт, пока я держу район", 0.1),
        ("Заряди меня пиздец, у нас целый батальон (Пау, пау)", 0.1),
        ("Мне не слить моих кентов, я сливаю миллион", 0.1),
        ("Только чистая семья, только чистое бельё (У-у-у)", 0.1),
    ]

    for line, char_delay in lines:
        type_line(line, char_delay)
        sleep(0.2)


printlyrics()