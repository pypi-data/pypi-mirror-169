from setuptools import setup, find_packages

setup(name="project_test_client",
      version="0.0.2",
      description="project_test_client",
      author="Pavel_Zabrovskiy",
      author_email="pavel.zabrovskiy@bk.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
