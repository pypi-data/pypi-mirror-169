from setuptools import find_packages, setup


setup(
    name='chromium_auto_installer',
    classifiers=[
        'License :: Freely Distributable'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    version='1.0.1',
    description='Auto chromium installer.',
    author='kiki-kanri',
    author_email='a470666@gmail.com',
    keywords=['chromium auto-installer', 'pyppeteer'],
    install_requires=[
        'requests'
    ],
    python_requires=">=3.7.0"
)
