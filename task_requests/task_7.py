def main():
    file = input()
    global_init(file)
    db_sess = create_session()
    for user in db_sess.query(User).filter(User.address == "module_3", User.age < 21):
        user.address = "module_3"
    db_sess.commit()


if __name__ == '__main__':
    main()
