import setuptools


with open("README.md", "r") as txt:
    long_description = txt.read()

setuptools.setup(
    name='AutoPostTelegram',
    version='0.0.6',
    description='An Telegram Auto Post Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    author='Aasfcyberking',
    author_email='aasfvl@gmail.com',
    url='https://telegram.me/Aasf_CyberKing',
    packages=setuptools.find_packages(),
    install_requires= ['requests'],
    python_requires='>=3.6'
)
