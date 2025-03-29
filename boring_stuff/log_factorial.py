import logging

# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format='{asctime} - {levelname} - {message}', style="{")
logging.disable()
logging.debug('Start of program')
def factorial(n):
    logging.debug(f'Start of factorial({n})')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print()
print(factorial(5))
logging.debug('End of program')