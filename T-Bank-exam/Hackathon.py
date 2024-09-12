start_time = input()
n = int(input())
teams = {}

    
def count_penalty(start_time, request_time):

    h,m,s = map(int,start_time.split(':'))
    minutes = h*60+m
    h,m,s = map(int,request_time.split(':'))
    re_minutes = h*60+m

    if re_minutes < minutes:
        re_minutes += 24 * 60

    return re_minutes - minutes

def team_stats(teams, team_name, server_id, request_time, start_time, result):
    if team_name not in teams:
        teams[team_name] = {'servers': set(), 'penalty': 0, 'attempts': {}}
    if server_id not in teams[team_name]['attempts']:
        teams[team_name]['attempts'][server_id] = 0
    
    if result == 'ACCESSED':
        if server_id not in teams[team_name]['servers']:
            teams[team_name]['servers'].add(server_id)
            teams[team_name]['penalty'] += count_penalty(start_time, request_time)
            teams[team_name]['penalty'] += teams[team_name]['attempts'][server_id] * 20
    elif result in ('DENIED', 'FORBIDEN'):
        teams[team_name]['attempts'][server_id] += 1

def winner_sorter(teams):
    sorted_teams = sorted(teams.items(), key=lambda item: (-len(item[1]['servers']),item[1]['penalty'], item[0]))
    prev_result = None
    rank = 0
    for i, (team_name, data) in enumerate(sorted_teams):
        current_result = (-len(data['servers']), data['penalty'])
        if current_result != prev_result:
            rank = i + 1
            prev_result = current_result
        print(f"{rank} \"{team_name}\" {len(data['servers'])} {data['penalty']}") 


for _ in range(n):
    team_name, request_time, server_id, result = input().split()
    team_name = team_name[1:-1]
    team_stats(teams, team_name, server_id, request_time, start_time, result)

winner_sorter(teams)