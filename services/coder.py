import ollama
import re
import os


class Coder: 
    def __init__(self):
        with open('/home/scum/Projects/Icode/services/model.txt', "r") as i:
            self.model = i.readlines()
    def getModel(self):
        print(self.model)
    def init(self, projectName, workingDir, req):
        initialPrompt = "Your job is to create project architecture given a certain request. You are to use this project name: " +  projectName + " and this working directory: " + workingDir + " to build the file structure needed for this project. All files for this project will be under the /currentWorkingDirectory/projectname. Think as long as you need but you will Create a .md for said folder with the architecture for the project that contains all information needed. Then generate commands needed to initialize the project. This is the project request: [" + req + "]. IT MUST BE A PROJECT REQUEST. Do not write code or tests. Just an md and commands. So within the md your gonna put a project description, architecture, filesystem, and how to start the project. all of this will be wrapped in <INFORMATION></INFORMATION> to be able to parse through your response quick." + "Also create a bash script to fully initialize the generated architecture and create code for each file to make the project work. The bash file will inject source code into each file to comply with architecture and project needs. Return everything the bash file needs to have in between two elements as such <BASH></BASH>. The current working Directory is: [" + workingDir + projectName + "]. Generate nothing else but what is asked in this prompt. This is not a tutorial. You are CREATING the bash file. And again the bash file you generate will be wrapped around <BASH></BASH>. And Dont forget, if this project permits it, to echo in the code to each file needed using this bash file"

        pattern1 = r"\<INFORMATION>(.*?)\</INFORMATION>"
        pattern2 = r"\<BASH>(.*?)\</BASH>"
        res = ollama.generate(model=self.model[0], prompt=initialPrompt, think=False)
        match1 = re.search(pattern1, str(res))
        match2 = re.search(pattern2, str(res))
        try:
            if match1:
                result = match1.group(1)
                os.mkdir(projectName)
                os.mkdir(projectName + "/icode")
                with open(workingDir + projectName + "/icode/ARCHITECTURE.md", 'wb') as i:
                    i.write(result.replace('\\n', '\n').encode("utf-8"))

            if match2:
                result = match2.group(1)
                with open(workingDir + projectName + "/icode/init.sh", 'wb') as i:
                    i.write(result.replace('\\n', '\n').replace("\\'", "'").replace('\\t', 't').encode("utf-8"))
        except:
            return 1



        




        

