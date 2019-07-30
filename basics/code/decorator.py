from functools import wraps


def be_polite(used_functions):
    print(f'trial_before_method output {used_functions()}')
    @wraps(used_functions)
    def wrapper(*args, **kwargs):
        """ This is comments of wrapper"""
        print('before the sentences ')
        used_functions(*args, **kwargs)
        print('after the sentences')
    print(f'trial_after_method output {used_functions()}')
    return wrapper


@be_polite
def greet():
    """ This is comments on greet method """
    print('this is the greet method!')
    return None


@be_polite
def rage():
    """ This is comments on rage method """
    print('RAGE!!!!!!!!!')
    return 'not happy'


if __name__ == '__main__':
    greet()
    rage()

    print(greet.__doc__)
    print(greet.__name__)
    help(greet)
