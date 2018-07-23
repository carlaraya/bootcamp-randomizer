import random, time

with open('art.txt') as art_file:
    logos = art_file.read().split('------')
logos = dict([logo.strip().split('\n', 1) for logo in logos])

teams = []
while True:
    print(chr(27) + "[2J")
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
    time.sleep(3)

with open('groupings.txt', 'r') as groupings, open('groupings_sorted.txt', 'w') as groupings_sorted:
    gs = groupings.read().strip().split('\n')
    gs = [team + '\n' + '\n'.join([g.split(' : ')[0] for g in gs if team in g]) + '\n' for team in logos]
    groupings_sorted.write('\n'.join(gs))
