import requests


class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "***************************************"  # Kullanıcıya özel api token'ı

    # İstek üzerine istenilen kullancının bazı bilgilerini getiren metot.
    def get_user(self, name):
        response = requests.get(self.api_url + "/users/" + name)
        return response.json()

    # İstek üzerine istenilen kullancının Repository'lerini getiren metot.
    def get_repositories(self, name):
        response = requests.get(self.api_url + '/users/' + name + "/repos")
        return response.json()

    # İstek üzerine istenilen kullancının Repository'lerine bir yenisini ekleyen metot.
    def create_repository(self, repo_name):
        response = requests.post(
            self.api_url + "/user/repos?access_token=" +
            self.token, json={"name": repo_name,
                              "description": "api deneme"}
        )
        return response.json()


github = Github()
while True:
    choice = input("\n1- Find User\n2- Get Repositories\n"
                   "3- Create Repository\n4- Exit\n"
                   "YOUR CHOICE: ")

    if choice == "4":
        break
    else:
        if choice == "1":
            name = input("Username: ")
            result = github.get_user(name)
            print(f"\nName: {result['name']}\n"
                  f"Followers: {result['followers']}\n"
                  f"Repositories: {result['public_repos']}\n")
        elif choice == "2":
            name = input("Username: ")
            result = github.get_repositories(name)
            for j, i in enumerate(result):
                print("\n", str(j+1) + ')' + i["name"], end="\n")
        elif choice == "3":
            repo_name = input("Repository Name: ")
            result = github.create_repository(repo_name)
            print(result["name"] + " is created !!")
        else:
            print("WRONG CHOICE")

