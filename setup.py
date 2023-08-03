from setuptools import find_packages,setup
from typing import List



Hyphen_E_dot ="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req  in requirements]

        if Hyphen_E_dot in requirements:
            requirements.remove(Hyphen_E_dot)
    
    return requirements
            

#This setup() is the metadat information about the project.
setup(
name="Generic_ML_Project",
version="0.0.1",
author="Tminus0",
author_email="shubham.patil041@gmail.com",
packages=find_packages(),
install_requires = get_requirements("requirements.txt")
)