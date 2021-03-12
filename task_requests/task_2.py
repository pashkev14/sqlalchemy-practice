def main():
    file = input()
    global_init(file)
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == "module_1", User.speciality.notlike("%engineer%"),
                                           User.position.notlike("%engineer%")):
        print(user.id)


if __name__ == '__main__':
    main()
