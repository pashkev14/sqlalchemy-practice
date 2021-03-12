def main():
    file = input()
    global_init(file)
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == "module_1"):
        print(user)


if __name__ == '__main__':
    main()
