from setuptools import setup

long_desc = open('README.md').read()
print(long_desc)

setup(name='cryptomus',
      version='1.1',
      description='Python SDK for Cryptomus.com API',
      long_description_content_type='text/markdown',
      long_description=long_desc,
      packages=['cryptomus'],
      keywords=['Cryptomus', 'Cryptomus.com', 'API'],
      author='Daniil Gord',
      author_email='9or9or9@mail.ru',
      zip_safe=False,
      install_requires=['requests']
      )
