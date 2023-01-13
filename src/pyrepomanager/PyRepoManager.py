import requests
from .GHConnect import GHConnect
from subprocess import check_output, CalledProcessError
from .Repository import Repository
from .check_packages import check_gh_installed


class PyRepoManager(GHConnect):
    def __init__(self, gh_username: str, gh_user_token: str):
        """
        :param gh_username: Git Hub username
        :param gh_user_token: Git Hub Personal Access Token (https://github.com/settings/tokens
        """
        assert gh_username.__class__ == str, "The gh_username parameter must be a string"
        assert gh_user_token.__class__ == str, "The gh_user_token parameter must be a string"

        check_gh_installed()

        super().__init__(
            gh_username=gh_username,
            gh_user_token=gh_user_token
        )

    @staticmethod
    def __get_repo_attr(repo: str) -> list[str]:
        split_repo = repo.split('\t')
        repo_full_name = split_repo[0].split('/')
        repo_owner = repo_full_name[0]
        repo_name = repo_full_name[1]
        repo_description = split_repo[1]
        repo_visibility = split_repo[2]
        repo_last_commit = split_repo[3]
        repo_link = f"https://github.com/{split_repo[0]}.git"

        return [repo_owner, repo_name, repo_description, repo_visibility, repo_last_commit, repo_link]

    def __create_repo_list(self, repos: list) -> list:
        repo_list = []
        for repo in repos:
            [owner, name, description, visibility, last_commit, link] = self.__get_repo_attr(repo)
            repo_list.append(Repository(
                repo_owner=owner,
                name=name,
                description=description,
                visibility=visibility,
                last_commit=last_commit,
                link=link
            ))
        return repo_list

    def get_user_data(self) -> tuple[dict, int]:
        url = f"https://api.github.com/users/{self.gh_username}"
        req = requests.get(url)
        data, status_code = req.json(), req.status_code

        return data, status_code

    def get_repo_list(self) -> list:
        """
        :return: Returns the list of repositories (instances of the Repository class) of the authenticated user
        """
        repos = check_output(['gh', 'repo', 'list']).decode().split('\n')
        if repos[-1] == '':
            repos.pop()
        repo_list = self.__create_repo_list(repos)

        return repo_list
