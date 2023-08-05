from setuptools import setup,find_packages
classifiers = [
'Development Status :: 5 - Production/Stable',
'Environment :: Win32 (MS Windows)',
'Intended Audience :: Education',
'Operating System :: Microsoft :: Windows :: Windows 10',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python :: 3.9'
]
setup(
    name='i_just_flexed_on_u',
    version='0.0.1',
    description='Evaluates Logical Expressions',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type="text/markdown",
    url='',
    author='Saransh Singh Dhapola',
    author_email='Saranshdhapola2002@gmail.com',
    License='MIT',
    classifiers=classifiers,
    keyword='Logical Expression',
    packages=find_packages(),
    install_requires=['']
)