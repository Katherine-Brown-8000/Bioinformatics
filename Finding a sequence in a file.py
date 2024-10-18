file_name = r"C:\Users\username\Desktop\Python code files\lanbda_virus.txt"

def read_file(file):
    with open(file_name, 'r') as file:
        content = file.read().strip()
        return content

seq = read_file(file_name)

genome = ''
for line in seq:
    if not line.startswith('>'):
        genome += line.strip()

target_seq = 'ATCG'
count = genome.count(target_seq)


print(f"The seq {target_seq} appears {count} times")
