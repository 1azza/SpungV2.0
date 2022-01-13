class Error(Exception):

    pass


class ValueTooSmallError(Error):

    pass


class InvalidBotToken(Error):
    print('Please enter a bot token')
