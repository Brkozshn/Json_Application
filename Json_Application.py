import json
import os


class User:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open("users.json","r",encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)              #json stringten python objesine dönüştürme
                    newUser = User(username=user['username'],password=user['password'],email=user['email'])             # bu şekilde username gibi bilgilerine ulaşılabilir.
                    self.users.append(newUser)
            print(self.users)

    def register(self,user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanici olusuturuldu.")
        pass


    def login(self,username,password):
       
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('login yapildi.')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Çikiş yapildi.')

    def identity(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('Giriş yapilmadi.')

    def savetoFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))        #json dump fonksiyonu için class bilgisini user.__dict__ ile dictionary'e çevirdik.
        with open("users.json","w") as file:
           json.dump(list,file)                           #json dump fonksiyonu dosyaya dictionary bilgisini kayıt etti.


repository = UserRepository()


while True:
    print('Menu'.center(50,'*'))
    secim = input('1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nseçiminiz: ')
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input('usernama: ')                        #register
            password = input('password: ')
            email = input('email: ')    
            user = User(username=username,password=password,email=email)
            repository.register(user)

        elif secim == '2':
            if repository.isLoggedIn:
                print('Zaten login oldunuz.')
            else:
                username = input('username: ')          #login
                password = input('password: ')
                repository.login(username,password)  

        elif secim == '3':
            repository.logout()                                                #logout
        elif secim == '4':
            repository.identity()                               #Identity (display username)
        else:
            print("Yanlis secim")
