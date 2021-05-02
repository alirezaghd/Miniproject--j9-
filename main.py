from Class_Media import Meida
from Class_Actor import Actor
from Class_Film import Film
from Class_Series import Series
from Class_Documentary import Documentary
from Class_Clip import Clip


def read_from_db():
    products=[]
    fl=open('datamedia.csv')
    big_text=fl.read()
    products_list=big_text.split('\n')
    for i in range(len(products_list)):
        info=products_list[i].split(',')
        cst=[]
        cs=0
        if info[1] == 'Film' :
            cast=info[6].split('-')
            for j in range(len(cast)):
                cs+= 1
                act=Actor(cast[j])
                cst.append(act)
    
            f = Film(id=info[0],category=info[1],name=info[2],director= info[3],IMDB=info[4],url=info[5],casts=cast,duration=info[7],year=info[8])
            products.append(f)
        elif info[1] == 'Series' :
            f = Series(id=info[0],category=info[1],name=info[2],director= info[3],IMDB=info[4],url=info[5],casts=cast, duration=info[7],episod = info[8])
            products.append(f)
        elif info[1] == 'Documentary' :
            products.append(Documentary(id=info[0],category=info[1],name=info[2],director= info[3],IMDB=info[4],url=info[5],casts=cast, duration=info[7],Topic = info[8]))
        elif info[1] == 'Clip' :
            products.append(Clip(id=info[0],category=info[1],name=info[2],director= info[3],IMDB=info[4],url=info[5],casts=cast, duration=info[7],company = info[8]))
        
      

    return products

media=read_from_db()


def add():
    global c
    c=[]
    while True:
        category = input('Enter category(Film/Series/Documentary/Clip) : ')
        id = input('number id : ')
        name=input('Enter name : ')
        director=input('Enter director : ')
        imdb=input('Enter imdb : ')
        url=input('Enter url : ')
        if category  == 'Series':
            duration = None
        else:
            duration=input('Enter duration : ')
        casts=[]
        
        read_from_db()
       
        while True:
            if category  == 'Documentary' or category  == 'Clip':
                newcast = None

            else:
                newcast=input('enter cast:')
                act=Actor(newcast)
                c.append(act)
                ans=input('more cast?(y/n)')
                if ans=='n':
                    break
        if category=='Film':
            year =input('number of year: ')
            media.append(Film(id= id,category=category,name=name,director=director,IMDB=imdb,url=url,casts=casts,duration=duration,year=year))
            break
        elif category=='Series':
            episod=input('number of episod: ')
            media.append(Series(id= id,category=category,name=name,director=director,IMDB=imdb,url=url,casts=casts,duration=duration,episod=episod))
            break
        elif category=='Documentary':
            topic=input('enter topic: ')
 
            media.append(Documentary(id= id,category=category,name=name,director=director,IMDB=imdb,url=url,casts=None,duration=duration,Topic=topic))

            break
        elif category =='Clip':
            company = input('enter company: ')
            media.append(Clip(id= id,category=category,name=name,director=director,IMDB=imdb,url=url,casts=None,duration=duration,company=company))

            break
        else:
            print('invalid category!')


def write_media():
    fl=open('datamedia.csv','w')
    fl.writable=True
    c=0
    for media_obj in media:
        cast=[]
        counter= media_obj.id
        if media_obj.category =='Film':
            c+=1
            fl.write(str(media_obj.id)+','+media_obj.category+','+media_obj.name+','+media_obj.director+','+str(media_obj.IMDB)+','+media_obj.url+','+str(media_obj.duration)+','+str(media_obj.year)+',')
            for ct in media_obj.casts:
                counter+=1
                fl.write(ct.name)
                if counter<len(media_obj.casts):
                    fl.write('-')
            if c<len(media):
                fl.write('\n')
        elif media_obj.category=='Series':
            c+=1
            fl.write(str(media_obj.id)+','+media_obj.category+','+media_obj.name+','+media_obj.director+','+str(media_obj.IMDB)+','+media_obj.url+','+str(media_obj.duration)+','+str(media_obj.episod)+',')
            for ct in media_obj.casts:
                counter+=1
                fl.write(ct.name)
                if counter<len(media_obj.casts):
                    fl.write('-')
            if c<len(hole_medias):
                fl.write('\n')

        elif media_obj.kind=='Documentary':
            c+=1
            fl.write(str(media_obj.id)+','+media_obj.category+','+media_obj.name+','+media_obj.director+','+str(media_obj.IMDB)+','+media_obj.url+','+str(media_obj.duration)+','+media_obj.Topic+',')
            for ct in media_obj.casts:
                counter+=1
                fl.write(ct.name)
                if counter<len(media_obj.casts):
                    fl.write('-')
            if c<len(hole_medias):
                fl.write('\n')

        elif media_obj.kind=='Clip':
            c+=1
            fl.write(str(media_obj.id)+','+media_obj.category+','+media_obj.name+','+media_obj.director+','+str(media_obj.IMDB)+','+media_obj.url+','+str(media_obj.duration)+','+media_obj.company+',')
            for ct in media_obj.casts:
                counter+=1
                fl.write(ct.name)
                if counter<len(media_obj.casts):
                    fl.write('-')
                
            if c<len(hole_medias):
                fl.write('\n')
    fl.close()
 
def search():
    k=input('enter category:(Film/Series/Documentary/Clip)')
    for media_obj in hole_medias:
        if media_obj.kind==k:
            media_obj.show_info()

def showMediaList():
    for pro in media:
        pro.showInfo()

def Remove():
    name=input('enter name:')
    for media_obj in media:
        if media_obj.name==name:
            media.remove(media_obj)

def download():
    name=input('enter name:')
    for media_obj in media:
        if media_obj.name==name:
            media_obj.download()
            print('download sucsses ')
            break
    else:
        print('invalid name....')

def show_menu():
    print('1-Add ')
    print('2-Search ')
    print('3-Download ')
    print('4-Remove ')
    print('5-Show info')
    print('6-Exit ')
        




while True:
    show_menu()
    user=int(input())

    if user==1:
        add()

    elif user==2:
        search()

    elif user==3:
        download()
    
    elif user==4:
        Remove()
    elif user==5:
        showMediaList()
    
    elif user==6:
        a=input('save changhes ? (y/n)')
        if a=='n':
            exit()
        elif a=='y':
            write_media()
            exit()





