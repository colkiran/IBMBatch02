
import logging

logging.basicConfig(level=logging.DEBUG, filename="mylogs.log",
            format="%(process)d %(asctime)s : %(levelname)s : %(message)s : %(filename)s : %(lineno)d")

inv = 1
num = 2

try:
    inv = 1 / num
except ZeroDivisionError as z:
    print(logging.debug(z))
except TypeError as t:
    print(logging.warn(t))
except Exception as e:
    print(logging.error(e))
else:
    logging.info(f"inverse of {num} is {inv}")
finally:
    print("finally block......")