def countdown(n):
    logging.debug("Counting down")
    while n > 0:
        try:
            yield n
        except GeneratorExit:
            logging.error("GeneratorExit")
        n -= 1


if __name__ == '__main__':
    c = countdown(10)
    logging.debug("value: %d", c.next())