from setuptools import setup, find_packages

setup(name="net_mess_server",
      version="0.1.2",
      description="Network mess Server",
      author="Maks-R",
      author_email="ya@maks47.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )