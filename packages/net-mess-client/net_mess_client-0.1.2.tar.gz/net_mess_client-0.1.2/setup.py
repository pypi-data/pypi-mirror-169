from setuptools import setup, find_packages

setup(name="net_mess_client",
      version="0.1.2",
      description="Network mess Client",
      author="Maks-R",
      author_email="ya@maks47.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )