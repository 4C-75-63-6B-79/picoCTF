usernames = open('./solution/usernames.txt', 'r').readlines();
passwords = open('./solution/passwords.txt', 'r').readlines();

for i in range(0, len(usernames)):
    usernames[i] = usernames[i][0:-1];

for i in range(0, len(passwords)):
    passwords[i] = passwords[i][0:-1];

credentials = dict(zip(usernames, passwords));

print(credentials["cultiris"]);

