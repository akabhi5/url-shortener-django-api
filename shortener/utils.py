import random
import string


def generate_short_link():
    length = 8
    link = ''.join(random.choice(string.ascii_lowercase + string.digits)
                   for _ in range(length))
    return link


# print(generate_short_link())
