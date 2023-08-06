from setuptools import setup, find_packages

setup(name="pyqt_db_server",
      version="0.1",
      description="first",
      author="Lesnikov Konstantin",
      author_email="tr1nz@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      # scripts=['server/server_run']
      )
