def my_for(iterable, func):
    iterator = iter(iterable) # is an iterator
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            print('END OF ITERATION')
            break
        else:
            func(thing)


if __name__ == '__main__':
    my_for('hello', print)
