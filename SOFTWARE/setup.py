from setuptools import find_packages, setup


def read(path):
    with open(path, 'r') as f:
        return f.read()


setup(
    name='colosseum_shaker_ui',
    version='0.1.0',
    url='https://github.com/ckim3-mit/colosseum',
    author='Kyung Hoi (Joseph) Min, Yeokyoung (Anne) Kil, A. Sina Booeshaghi, Chan Gi Kim',
    author_email='phoenixter96@gmail.com, ykil@caltech.edu, abooesha@caltech.edu, ckim3@mit.edu',
    maintainer='n/a',
    maintainer_email='n/a',
    description='colosseum system - open source fraction collector for laboratories turned into a tube shaker',
    long_description='',
    long_description_content_type='text/markdown',
    keywords='',
    python_requires='>=3.6',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=read('requirements.txt').strip().split('\n'),
    entry_points={
        'console_scripts': ['colosseum=colosseum_ui.run:run'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Hardware :: Hardware Drivers'
    ],
)
