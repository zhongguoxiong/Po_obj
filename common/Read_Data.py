import yaml,os
def read_yml_data(filename):
    file_path=os.getcwd()+os.sep+"Data"+os.sep+filename+".yml"
    with open(file_path,"r") as f:
       return yaml.load(f)
