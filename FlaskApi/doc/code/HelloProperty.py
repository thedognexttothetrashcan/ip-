import hashlib


class User():

    def __init__(self, u_password):
        self._u_password = u_password

    @property
    def u_password(self):
        return self._u_password

    @u_password.setter
    def u_password(self, password):
        print("setter")
        self._u_password = hashlib.new("md5", password.encode("utf-8")).hexdigest()


if __name__ == '__main__':
    user = User("110")

    user.u_password = "120"

    print(user.u_password)