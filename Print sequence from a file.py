file_name = r"C:\Users\scien\Desktop\Python code files\lanbda_virus.txt"

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read().strip()
        return content

seq = read_file(file_name)

print(seq)
