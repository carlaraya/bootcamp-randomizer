import random

with open('art.txt') as art_file:
    logos = art_file.read().split('------')
logos = dict([logo.strip().split('\n', 1) for logo in logos])

teams = []
while True:
    name = input('Enter your name: ')
    if name.lower() == 'exit':
        break
    if teams == []:
        teams = list(logos.keys())
        random.shuffle(teams)
    assigned_team = teams.pop()
    print("Congrats, you are now part of the team: %s!" % assigned_team)
    print(logos[assigned_team])
    with open('groupings.txt', 'a') as groupings:
        groupings.write('%s : %s\n' % (name, assigned_team))