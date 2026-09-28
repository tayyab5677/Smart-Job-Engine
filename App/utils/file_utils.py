def save_file(file_name,content):
    with open(file_name,"w")as file:
        file.write(content)
def read_file(filename):
    with open(filename,"r")as file:
        return file.read()
