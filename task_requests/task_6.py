def main():
    file = input()
    global_init(file)
    db_sess = create_session()
    max_team_size = max(list(map(lambda x: len(x.collaborators.split(", ")), db_sess.query(Jobs))))
    for job in db_sess.query(Jobs).filter(len(Jobs.collaborators.split(', ')) == max_team_size):
        for user in db_sess.query(User).filter(job.team_leader == User.id):
            print(user.surname, user.name)


if __name__ == '__main__':
    main()
