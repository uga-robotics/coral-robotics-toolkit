from setuptools import setup, find_packages

setup(
    name="coral-robotics-toolkit",
    version='0.2.0',
    packages=find_packages(),
    author="Hunter Halloran (Jyumpp)",
    author_email="hdh20267@uga.edu",
    install_requires=[
        'setuptools',
        'pyserial',
        'python-periphery',
    ],
    description="Stuff for using the Coral Dev Board for robotics.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    download_url='not-a-website.com',
    url="not-a-git-repo.com",
    keywords="servo, bot, robotics, coral, motor, robot",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
