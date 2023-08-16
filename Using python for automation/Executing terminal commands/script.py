import subprocess
subprocess.run('pwd')

listFiles = subprocess.run(['ls', '-la'],capture_output=True, text=True)
#Printing data stored in text
print(listFiles.stdout)
tree = subprocess.run('tree',capture_output=True)
#priting tree as a stored variable (in bytes originally)
print(tree.stdout.decode()) 

#Running the example script 3 times
for i in range(0,3):
    subprocess.check_call(['python3', 'example.py'])