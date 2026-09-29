import os
from services import coder

dir_path = os.getcwd() + '/'

#with open(dir_path + 'test.py') as filepath:
    #content = filepath.read().encode('UTF8')

def main():
    agent = coder.Coder()
    agent.getModel()

    projectName = "TableHockey"
    projectRequest = "Create a table hockey game I can play by myself against AI using javascript html and css"
    agent.init(projectName, dir_path, projectRequest)
    return 0


if __name__ == "__main__":
    main()
