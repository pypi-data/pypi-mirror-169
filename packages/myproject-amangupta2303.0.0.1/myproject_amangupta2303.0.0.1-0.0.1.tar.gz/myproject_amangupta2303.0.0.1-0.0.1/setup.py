from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Unix',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License'
]

setup(
    name='myproject_amangupta2303.0.0.1',
    version='0.0.1',
    description='A short summary about your package',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author='Aman Gupta',
    author_email='gupta.aman2303@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['calculator', 'tutorial', 'Aman_gupta'],
    packages=find_packages(),
)
