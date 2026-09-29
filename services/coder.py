import ollama

with open('./model.txt', "r") as model:
    agent = model

class Coder: 
    def __init__(self, model=agent):
      self.model = model 

    def getModel(self):
        print(self.model)

    def init(self, projectName, workingDir, req):
        initialPrompt = "Your job is to create project architecture given a certain request. You are to use this project name: " +  projectName + " and this working directory: " + workingDir + " to build the file structure needed for this project. All files for this project will be under the /currentWorkingDirectory/projectname. Create a .md within said folder with the architecture for the project that contains all information needed. Think as long as you need. Now under the md split it off with a line of hashtags and if needed, generate commands needed to initialize the project. This is the project request: " + req
        #res = ollama.generate(model=self.model, prompt=initialPrompt)
        #return res



