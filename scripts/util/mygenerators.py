import names
import random
import string
import hashlib
import base64
import os

import datetime
from typing import List, Iterator, Union, Optional


class FirstnameGenerator:
    def __iter__(self):
        return self

    def __next__(self):
        return "'" + names.get_first_name() + "'"


class LastnameGenerator:
    def __iter__(self):
        return self

    def __next__(self):
        return "'" + names.get_last_name() + "'"


class NameGenerator:
    def __iter__(self):
        return self

    def __next__(self):
        return "'" + names.get_full_name() + "'"


class ProductGenerator:
    def __iter__(self):
        return self

    def __next__(self):
        return "'" + names.get_full_name() + "'"


class CategoryGenerator:
    def __iter__(self):
        return self

    def __next__(self):
        return "'" + names.get_full_name() + "'"


class NullGenerator:
    def __iter__(self):
        return self

    def __next__(self):
        return "NULL"
class BrandGenerator:
    def __init__(self, choices: List[str]):
        self.choices = choices

    def __iter__(self):
        return self

    def __next__(self):
        if self.choices:
            value = random.choice(self.choices)  # Choose a random brand from the choices
            self.choices.remove(value)  # Remove the chosen brand from the choices list
            return "'" + value + "'"
        else:
            raise StopIteration

class ChoiceGenerator:
    def __init__(self, choices: List[str]):
        self.choices = choices

    def __iter__(self):
        return self

    def __next__(self):
        return "'" + random.choices(self.choices)[0] + "'"


class ChoiceGeneratorInteger:
    def __init__(self, choices: List[Union[int, float]]):
        self.choices = choices

    def __iter__(self):
        return self

    def __next__(self):
        return str(random.choices(self.choices)[0])


class EmailGenerator:
    def __init__(
            self, mailservers: Optional[List[str]] = None, domains: Optional[List[str]] = None
    ):
        self.mailservers = mailservers or ["gmail"]
        self.domains = domains or ["com"]

    def __iter__(self):
        return self

    def __next__(self):
        # TODO: make email look meaningful
        size = random.randint(10, 20)
        return (
                "'"
                + (
                    f"{''.join(random.choices(string.ascii_letters, k=size))}"
                    f"@{random.choices(self.mailservers)[0]}"
                    f".{random.choices(self.domains)[0]}"
                )
                + "'"
        )


class AutoIncermentGenerator:
    def __init__(self, n: int = 1):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.n
        self.n += 1
        return str(tmp)


class DateGenerator:
    def __init__(self, start: datetime.datetime, end: datetime.datetime):
        self.range = end - start
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        offset = random.randint(0, int(self.range.total_seconds() * 1000))
        return (
                "'"
                + (self.start + datetime.timedelta(milliseconds=offset)).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
                + "'"
        )


class IntegerNumberGenerator:
    def __init__(self, start: int = 0, end: int = 10):
        self.start = start
        self.range = end - start

    def __iter__(self):
        return self

    def __next__(self):
        offset = random.randint(0, self.range)
        return str(self.start + offset)


class FloatNumberGenerator:
    def __init__(self, start: float = 0, end: float = 10.0, precision: int = 5):
        self.start = start
        self.range = end - start
        self.precision = precision

    def __iter__(self):
        return self

    def __next__(self):
        offset = random.random() * self.range + self.start
        return f"{offset:.{self.precision}f}"


class StaticNumberGenerator:
    def __init__(self, val):
        self.val = val

    def __iter__(self):
        return self

    def __next__(self):
        return str(self.val)


class PhoneGenerator:
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)
        last = str(random.randint(1, 9998)).zfill(4)
        while last in ["1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888"]:
            last = str(random.randint(1, 9998)).zfill(4)
        return "'" + f"{first}-{second}-{last}" + "'"


class PasswordHashGenerator:
    def __init__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        password = "admin"
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), salt, 1000, dklen=32
        )
        return "'" + key.hex() + "'"


# ------------------------------------------------------------------------------


def insert_into_table(name: str, generators: List[Iterator[str]], n: int = 10):
    res = f"INSERT INTO {name} VALUES\n"
    for i in range(n):
        tmp = "("
        for idx, func in enumerate(generators, 0):
            tmp += next(func)
            if idx != len(generators) - 1:
                tmp += ", "
        # Formatting
        if i == n - 1:
            tmp += ")\n"
        else:
            tmp += "),\n"
        res += tmp
    res += ";"
    return res

# Example:
# gens = [
#     NameGenerator(),
#     ChoiceGenerator(["hello", "bye"]),
#     EmailGenerator(),
#     DateGenerator(
#         datetime.datetime(year=2010, month=1, day=1),
#         datetime.datetime(year=2020, month=1, day=1),
#     ),
#     NumberGenerator(start=1, end=100),
# ]
# print(insert_into_table(name="post", generators=gens, n=20))
