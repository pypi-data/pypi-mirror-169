from setuptools import setup, find_packages

setup(name="message_client_py",
      version="1.3.0",
      description="Mess Client",
      author="Aleksey",
      author_email="alexivanov12356@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
