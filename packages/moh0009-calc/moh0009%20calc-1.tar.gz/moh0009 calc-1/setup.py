from setuptools import setup,find_packages

calssifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3"

]

setup(
    name = "moh0009 calc",
    version = "1",
    description = "calculator",
    long_description = """
Calc library

this libaray  for calculation numbers with python

here is the functions: 

calc.add(number 1 , number 2)
calc.subtract(number 1 , number 2)
calc.multiply(number 1 , number 2)
calc.division(number 1 , number 2)


example :

from calc import calc
print(calc.add(12,5))

the output well be 17

for any issues write it here https://github.com/moh0009/Calc/issues


see my replit https://replit.com/@moh0009 and my github https://github.com/moh0009

change log


1.0  (4/4/2022)
---------------
-frist release
    """,
    url ="https://github.com/moh0009/Calc" ,
    long_description_content_type = "text/x-rst",
    author="moh0009",
    author_email = "23ii.mancy@gmail.com",
    license = "MIT",
    classifiers = calssifiers,
    keywords = ["calculator","calc"],
    packages = find_packages(),
    install_requires = [""]
)
