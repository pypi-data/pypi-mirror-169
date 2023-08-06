import os
import shutil

from datetime import datetime

class Controller():
    def __init__(self) -> None:
        pass

    def printHeader(self, path, name):
        print("################################################################################")
        print("")
        print("Repository Setup by 5f0")
        print("Creates the basic repository structure for python projects")
        print("")
        print("Current working directory: " + os.getcwd())
        print("")
        print("Target directory: " + path)
        print("Name of new repository: " + name)
        print("")
        print("Creation Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print("################################################################################")
        print("")

    def createRepo(self, repositoryDir, name):
        if(not os.path.isdir(repositoryDir)):

            # 0.) Create repo dir
            mainDir = os.mkdir(repositoryDir)

            # 1.) Create sub dirs
            exampleDir = os.path.join(repositoryDir, "example")
            os.mkdir(exampleDir)

            srcDir = os.path.join(repositoryDir, "src")
            os.mkdir(srcDir)

            packageDir = os.path.join(srcDir, name)
            os.mkdir(packageDir)

            # 2.) Add files to package dir

            # This is the path of the directory in which Controller is located
            # this path is used to get the files path
            p = os.path.dirname(__file__)

            shutil.copy(os.path.join(p, "files", "__init__.py"), os.path.join(packageDir, "__init__.py"))
            shutil.copy(os.path.join(p, "files", "__main__.py"), os.path.join(packageDir, "__main__.py"))
            shutil.copy(os.path.join(p, "files", "Controller.py"), os.path.join(packageDir, "Controller.py"))
            
            # 3.) Add other files
            shutil.copy(os.path.join(p, "files", ".gitignore"), os.path.join(repositoryDir, ".gitignore"))
            shutil.copy(os.path.join(p, "files", "LICENSE.md"), os.path.join(repositoryDir, "LICENSE.md"))
            shutil.copy(os.path.join(p, "files", "README.md"), os.path.join(repositoryDir, "README.md"))
            shutil.copy(os.path.join(p, "files", "setup.py"), os.path.join(repositoryDir, "setup.py"))


            print("Repository of created successfully under " + repositoryDir + "!")
        else:
            print(repositoryDir + " already available!")

        print("")
        print("################################################################################")
        print()