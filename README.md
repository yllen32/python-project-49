### Hexlet tests and linter status:

[![Actions Status](https://github.com/yllen32/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/yllen32/python-project-49/actions)

# Игра "Проверка на чётность"

Добро пожаловать в игру "Проверка на чётность"! В этой игре вам будут показываться случайные числа, и ваша задача - определить, является ли число чётным или нечётным.

## Установка

1. Убедитесь, что у вас установлен Poetry. Если его нет, следуйте инструкциям по установке, доступным [здесь](https://python-poetry.org/docs/#installation).

2. Склонируйте репозиторий с игрой на свой компьютер:

```bash
git clone https://github.com/your-username/brain-even.git
```

Перейдите в директорию игры:

```bash

cd brain-even
```

Установите зависимости игры с помощью Poetry:


```bash

poetry install
```

### Запуск игры

Активируйте виртуальное окружение Poetry:

```bash

poetry shell
```

Запустите игру с помощью следующей команды:

```bash

python brain_even.py
```

Вас попросят ввести ваше имя:

```bash

Welcome to the Brain Games!
May I have your name? John
```

После ввода имени, игра начнется. Вам будет показано случайное число, и вам нужно будет ввести "yes", если число чётное, или "no", если число нечётное:

```bash

Hello, John!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: yes
```

Если вы даете неверный ответ, игра завершится и выведется сообщение:

```bash
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, John!
```

Если вы даете верный ответ, вы увидите сообщение "Correct!" и игра продолжится со следующим числом.

Чтобы выиграть игру, необходимо дать правильный ответ на три вопроса подряд. После успешного прохождения игры, вы увидите поздравление:

```bash
Congratulations, John!
```

Игра завершится, и вы можете сыграть ещё раз или выйти из игры.