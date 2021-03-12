def main():
    file = input()
    global_init(file)
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.age < 18):
        print(f"{user} {user.age} years")


if __name__ == '__main__':
    main()
