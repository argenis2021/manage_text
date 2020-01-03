import csv, operator

f1 = open('/tmp/tel_todo.csv', 'r')
f2 = open('google_tel_todos.csv', 'w')
entrada = csv.DictReader(f1)
f2.write('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,Phone 1 - Type,Phone 1 - Value'+'\n')
for reg in entrada:
    f2.write('11AA '+reg['cliente']+',,,,,,,,,,,,,,,,,,,,,,,,,Avenida B,,,* Avenida B ::: * Avenida B,Mobile,'+reg['telefono']+'\n')
f1.close()
f2.close()