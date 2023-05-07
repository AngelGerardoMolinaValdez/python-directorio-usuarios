def show_error_message(description : str) -> None:
    """imprime el mensaje de error con emojis ❌

    Args:
        description (str): el mensaje de error
    """
    emoji_error = "🚫"
    print('\n')
    print(emoji_error, description, emoji_error, end='\n' * 2)
