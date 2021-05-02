import pytube

class Meida():

        def __init__(self, id ,category , name  , director , IMDB, url ,casts , duration ):
            self.id = id
            self.name = name
            self.category = category
            self.director = director
            self.IMDB = IMDB
            self.url = url
            self.duration = duration
            self.casts = casts
            

            
            

        
        def download(self):
            pytube.YouTube(self.url).streams.first().download()


            







