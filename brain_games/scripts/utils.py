import prompt


def greeting_user() -> str:
    """Print grettings in to console and ask user_name, return username"""
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
