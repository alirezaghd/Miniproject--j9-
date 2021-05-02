from Class_Media import Meida

class Clip(Meida):
    def __init__(self,id ,category , name  , director , IMDB, url ,casts , duration ,company):
        super().__init__(id ,category , name  , director , IMDB, url ,casts , duration)
        self.company = company

    def showInfo(self):
                

        print('-----------------------------------------------------')
        print('ID : ',self.id)
        print('category : ',self.category)
        print('name:',self.name)
        print('director:',self.director)
        print('imdb:',self.IMDB)
        print('duration:',self.duration)
        print('url:',self.url)
        print('company:',self.company)
        print('-----------------------------------------------------')

