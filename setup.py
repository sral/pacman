from setuptools import setup

setup(name="pacman",
      version="0.1",
      description="",
      license="GPLv3",
      author="Lars Djerf",
      author_email="lars.djerf@gmail.com",
      url="http://github.com/sral/pacman",
      install_requires=["pygame"],
      packages=["pacman", "pacman.tests"],
      test_suite="pacman.tests",
      include_package_data=True,
      package_data={
            "pacman": ["data/*.gif"],
        },
      entry_points={
            "gui_scripts": ["pacman = pacman.pacman:main"]
        })