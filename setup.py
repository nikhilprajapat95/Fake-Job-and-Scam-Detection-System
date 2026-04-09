from setuptools import find_packages, setup

def get_requirements(file_path):
    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="fake_job_detection",
    version="0.0.1",
    author="Nikhil Prajapat",
    author_email="nikhilprajapat955@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)