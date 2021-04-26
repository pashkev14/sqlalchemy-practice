def main():
    file = input()
    global_init(file)
    db_sess = create_session()
    teams = db_sess.query(Jobs).all()
    max_collabs = max([len(i.collaborators.split(', ')) for i in teams])
    team_leads = []
    for i in teams:
        if len(i.collaborators.split(', ')) == max_collabs:
            leader = db_sess.query(User).filter(User.id == i.team_leader).first()
            if f"{leader.name} {leader.surname}" not in team_leads:
                team_leads.append(f"{leader.name} {leader.surname}")
    print('\n'.join(team_leads))


if __name__ == '__main__':
    main()
