import os
nama = input("username : ")
email = input("email : ")
os.system('git config --global user.name "{nama}"')
os.system('git config --global user.email {email}')
os.system('git init')
os.system('git add .')
comit = input('MESAGE COMMIT : ')
os.system('git commit - m "{comit}"')
gitlink = input(" GIT Link/token : ")
os.system('git remote add origin {gitlink}')

while True:
    branch = input(' (1) master (2) main \n : ')
    if(branch.lower() == '1'):
        os.system('git branch -M master')
        break
    else:
        os.system('git branch -M main')
        break
os.system('git push -f origin main')