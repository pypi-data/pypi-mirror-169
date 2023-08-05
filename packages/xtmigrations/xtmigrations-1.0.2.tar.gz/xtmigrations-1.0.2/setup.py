from setuptools import setup, find_packages

setup(
    name='xtmigrations',
    version='1.0.2',
    license='Apache license 2.0',
    author="Startech M",
    author_email='startechm@proton.me',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    url='https://github.com/startechm/xtmigrations',
    keywords='XTMigrations migration sql db upgrade',
    install_requires=[
          'psycopg2',  # TODO: add mysql / mariadb driver
      ],
)
