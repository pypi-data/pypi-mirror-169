from setuptools import setup, find_packages

setup(name="message_server_py",
      version="1.3.0",
      description="Mess Server",
      author="Aleksey",
      author_email="alexivanov12356@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      scripts=['server/server_run']
      )
