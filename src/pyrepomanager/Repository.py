import webbrowser


class Repository:
    __all_repos = []

    def __init__(self,
                 name: str,
                 repo_owner: str,
                 description: str,
                 visibility: str,
                 link: str,
                 last_commit: str
                 ):

        self.__name = name
        self.__repo_owner = repo_owner
        self.__description = description
        self.__visibility = visibility
        self.__link = link
        self.__last_commit = last_commit

        Repository.__all_repos.append(self)

    # Getters

    @property
    def name(self):
        return self.__name

    @property
    def repo_owner(self):
        return self.__repo_owner

    @property
    def description(self):
        return self.__description

    @property
    def visibility(self):
        return self.__visibility

    @property
    def link(self):
        return self.__link

    def browse(self):
        webbrowser.open_new(self.__link)

    def __repr__(self):
        return f'Repository({self.__name}, {self.__repo_owner}, ' \
               f'{self.__description if self.__description else "No description"})'
