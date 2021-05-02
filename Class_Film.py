from Class_Media import Meida

class Film(Meida):
    def __init__(self,id ,category , name  , director , IMDB, url ,casts , duration ,year):
        super().__init__( id ,category , name  , director , IMDB, url ,casts , duration)
        self.year = year

    def showInfo(self):
        print('-----------------------------------------------------')
        print('ID : ',self.id)
        print('category : ',self.category)
        print('name:',self.name)
        print('director:',self.director)
        print('imdb:',self.IMDB)
        print('duration:',self.duration)
        print('url:',self.url)
        print('year:',self.year)
        print('casts:',self.casts)
        print('-----------------------------------------------------')
        
 



        









