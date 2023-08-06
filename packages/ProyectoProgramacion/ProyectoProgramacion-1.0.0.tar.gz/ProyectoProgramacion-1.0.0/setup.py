from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='ProyectoProgramacion',
    packages=['ProyectoProgramacion'],  # this must be the same as the name above
    version='1.0.0',
    description='Esta es la descripcion de mi paquete',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Cristian Rivera, Marcos David, Keren Pajon',
    author_email='',
    # use the URL to the github repo
    url='https://github.com/CristianR746/CircuitoPrograma.git',
    download_url='https://github.com/CristianR746/CircuitoPrograma.git',
    keywords=['testing', 'logging', 'example'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)



