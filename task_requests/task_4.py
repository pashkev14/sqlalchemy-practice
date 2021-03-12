def main():
    file = input()
    global_init(file)
    db_sess = create_session()
    for user in db_sess.query(User).filter((User.position.like("%chief%") | (User.position.like("%middle%")))):
        print(f"{user} {user.position}")


if __name__ == '__main__':
    main()
