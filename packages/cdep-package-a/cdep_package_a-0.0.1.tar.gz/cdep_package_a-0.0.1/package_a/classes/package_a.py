class PackageA:
    def __init__(self, username: str):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def url(self, username: str):
        self._username = username