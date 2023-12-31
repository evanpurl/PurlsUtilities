from distutils.core import setup

setup(
    name='PurlsUtilities',  # How you named your package folder (MyLib)
    packages=['PurlsUtilities'],  # Chose the same as "name"
    version='0.2',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='PurlsUtilities is a library created to make the storage and other tasks of a discord bot easier for me, allowing for less code.',
    # Give a short description about your library
    author='Purls',  # Type in your name
    author_email='None',  # Type in your E-Mail
    url='https://github.com/evanpurl/PurlsUtilities',  # Provide either the link to your GitHub or to your website
    download_url='https://github.com/evanpurl/PurlsUtilities/archive/refs/tags/0.2.tar.gz',  # I explain this later on
    keywords=['Discord', 'Discord.py', 'Discord Bot'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'discord.py',
        'python-dotenv',
        'aiomysql',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.10',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
