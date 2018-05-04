from setuptools import setup


def readme():
    with open('README.txt') as f:
        return f.read()

setup(name='tester',
      version='0.1',
      description='to test the upload module',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='learning module bundling',
      url='https://github.com/anestin-femi',
      author='anestn femi',
      author_email='apmetdrm@example.com',
      license='MIT',
      packages=['tester'],
      include_package_data=True,
      zip_safe=False)