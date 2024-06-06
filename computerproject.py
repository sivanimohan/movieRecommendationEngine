import csv
f=open(r'C:\Users\Sivani\Desktop\Comp Project\imdbmoviesaltered.csv',encoding='utf-8')
csvreader=csv.reader(f)

def basic(genre,language,rating): #Movie recommendation engine
    c=0
    for movie in csvreader:
        if genre.title() in movie[3]:
            if movie[6]==language.title():
                        if float(movie[11])>=rating:
                             c+=1
                             print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
           print("\n","Sorry,the engine couldn't curate the list of movies :( (Try again with different parameters)")
           print("\n")
           
def info(film): #To find the details of a movie
           c=0
           for movie in csvreader:
                  if film in movie[1]:
                          c+=1
                          print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
           if c==0:
                   print("\n","Sorry,the movie is not found :( (Make sure you have typed the name of the movie accurately)")
                   print("\n")
                   
def director(role): #To display the filmography of a director
    c=0
    for movie in csvreader:
        if role in movie[7] :
                 c+=1
                 print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
           print("\n","Sorry,the engine couldn't find the filmography of",role," :( (Try again with another director or make sure you have typed the name of the director accurately  )")
           print("\n")
           
def writer(role): #To display the filmography of a writer
    c=0
    for movie in csvreader:
        if role in movie[8] :
                 c+=1
                 print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
           print("\n","Sorry,the engine couldn't find the filmography of" ,role," :( (Try again with another writer or make sure you have typed the name of the writer accurately  )")
           print("\n")
           
def actor(role): #To display the filmography of an actor
    c=0
    for movie in csvreader:
        if role in movie[9] :
                 c+=1
                 print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
           print("\n","Sorry,the engine couldn't find the filmography of ",role," :( (Try again with another actor or make sure you have typed the name of the actor accurately  )")
           print("\n")
           
def plot(film): #To view the plot of a movie
    c=0
    for movie in csvreader:
        if movie[1]==film:
                 c+=1
                 print("\n","Movie Name:",movie[1],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
           print("\n","Sorry,the movie is not found :( (Make sure you have typed the name of the movie accurately)")
           print("\n")
           
def toppest(year): #To display the highest rated movies of a year
     c=0
     for movie in csvreader:
            if movie[2]==year:
                if float(movie[11])>=7.5:
                         c+=1
                         print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")                        
     if c==0:
           print("\n","Sorry,the engine couldn't curate the list of the highest rated movies of" ,year, ":( (Try again with a different year between 1874 and 2020)")
           print("\n")
           
def lang(language): #To display the highest rated movies of a language
     c=0
     for movie in csvreader:
            if movie[6]==language.title():
                if float(movie[11])>=8:
                         c+=1
                         print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
     if c==0:
            print("\n","Sorry,the engine couldn't curate the list of the highest rated",language,"movies :( (Try again with a different language.Make sure you have typed the name of the language accurately )")
            print("\n")
            
def region(country): #To display the highest rated movies of a country
    c=0
    for movie in csvreader:
            if movie[5]==country.title():
                if float(movie[11])>=8:
                         c+=1
                         print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
           print("\n","Sorry,the engine couldn't curate the list of highest rated movies of",country,"  :( (Try again with a different country.Make sure you have typed the name of the country accurately )")
           print("\n")
           
def gen(genre): #To display the highest rated movies of a genre/category
          c=0
          for movie in csvreader:
                 if genre.title() in movie[3]:
                       if float(movie[11])>=8:
                             c+=1
                             print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")                     
          if c==0:
               print("\n","Sorry,the engine couldn't curate the list of highest rated " ,genre,"movies :( (Try again with a different genre/category.Make sure you have typed a valid genre/category")
               print("\n")
               
def year_lang(lang,language): #To display all the movies released in a year of a language
     c=0
     for movie in csvreader:
          if movie[2]==year:
             if movie[6]==language.title():
                         c+=1
                         print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
     if c==0:
           print("\n","Sorry,the engine couldn't curate the list of movies :( (Try again with a different year between 1874 and 2020 or with a different language)")
           print("\n")
           
def top_lang(lang,language): #To display the highest rated movies in a year of a language
     c=0
     for movie in csvreader:
          if movie[2]==year:
             if movie[6]==language.title():
                 if float(movie[11])>=7:
                         c+=1
                         print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
     if c==0:
           print("\n","Sorry,the engine couldn't curate the list of movies :( (Try again with a different year between 1874 and 2020 or with a different language)")
           print("\n")
           
def duration(genre,language,duration1,duration2): #To find movies of your required duration
    c=0
    for movie in csvreader:
        if genre.title() in movie[3]:
                if movie[6]==language.title():
                       if float(movie[4])>=duration1*60 and float(movie[4])<=duration2*60:
                              c+=1
                              print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
           print("\n","Sorry,the engine couldn't curate the list of movies of your required duration :( (Try again with different genre/category or make sure you have inputted the duration in hours)")          
           print("\n")
           
def clone(name): #To display movies with the same name
    c=0
    for movie in csvreader:
        if movie[1]==name:
              c+=1
              print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==1 or c==0:
           print("\n","Seems like there are no other movies with the same name :(")
           print("\n")
           
def coactors(actor1,actor2): #To find the movies with two actors of your choice
         c=0
         for movie in csvreader:
               if actor1 in movie[9]:
                       if actor2 in movie[9]:
                                 c+=1
                                 print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
         if c==0:
                 print("\n","Seems like there are no movies in which both the actors have worked together :( . (Make sure you have typed the names of the actors correctly or try again with any other actors)")
                 print("\n")
                 
def mixed_genre(language,genre1,genre2): #To find movies having mixed genre/category of your choice
    c=0
    for movie in csvreader:
        if movie[6]==language.title():
               if genre1.title() in movie[3]:
                       if genre2.title() in movie[3]:
                                c+=1
                                print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:    
          print("\n","Seems like there are no movies in which there is a mix of these two genres :( . (Make sure you have entered valid genres/categories or try again with any other genres\categories )")
          print("\n")
          
def actor_director(actor,director): #To display the film collaborations of an actor and a director
    c=0
    for movie in csvreader:
          if actor in movie[9] :  
                  if director in movie[7] :
                         c+=1
                         print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
                 print("\n","Seems like there are no movies in which both the actor and the director have worked together :( . (Make sure you have typed the names of the actor and the director correctly or try again with any other actor and director)")
                 print("\n")
                 
def actor_writer(actor,writer): #To display the film collaborations of an actor and a writer
    c=0
    for movie in csvreader:
          if actor in movie[9] :  
                  if writer in movie[8] :
                         c+=1
                         print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")

    if c==0:
                 print("\n","Seems like there are no movies in which both the actor and the writer have worked together :( . (Make sure you have typed the names of the actor and the writer correctly or try again with any other actor and writer)")
                 print("\n")
                 
def director_writer(director,writer): #To display the film collaborations of a director and a writer
    c=0
    for movie in csvreader:
          if director in movie[7] :  
                  if writer in movie[8] :
                         c+=1
                         print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
                 print("\n","Seems like there are no movies in which both the director and the writer have worked together :( . (Make sure you have typed the names of the director and the writer correctly or try again with any other director and writer)")
                 print("\n")
                 
def dwa(director,writer,actor): #To display the film collaborations of an actor, a director and a writer
    c=0
    for movie in csvreader:
           if director in movie[7] : 
                  if actor in movie[9] :  
                          if writer in movie[8] :
                                   c+=1
                                   print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
                 print("\n","Seems like there are no movies in which they all have worked together :( . (Make sure you have typed the names of the actor , the director and the writer correctly or try again with any other actor,director and writer)")
                 print("\n")
                 
def best(language,genre): #To display the highest rated movies of a language and a genre/category
     c=0
     for movie in csvreader:
         if genre.title() in movie[3]:
               if movie[6]==language.title():
                   if float(movie[11])>=7:
                             c+=1
                             print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
     if c==0:
              print("\n","Sorry,the engine couldn't curate the list of  movies :( (Try again with different genre/category )")          
              print("\n")
              
def keyword(key,language): #To find movies using keywords in the plot
    c=0
    for movie in csvreader:
        if movie[6]==language.title():
                  if key in movie[10] :
                                 c+=1
                                 print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")

    if c==0:
           print("\n","Sorry,the engine couldn't find any movies with the keyword,",key," in the plot description :( (Try again with a different keyword)")          
           print("\n")
           
def rate(genre,language,minrating,maxrating): #
    c=0
    for movie in csvreader:
        if genre.title() in movie[3]:
                if movie[6]==language.title():
                       if float(movie[11])>=minrating and float(movie[11])<=maxrating:
                              c+=1
                              print("\n","Movie Name:",movie[1],"\n","Year:",movie[2],"\n","Genre:",movie[3],"\n","Duration:",(int(movie[4])//60),"hours",int(movie[4])%60,"minutes","\n","Country:",movie[5],"\n","Language:",movie[6],"\n","Director:",movie[7],"\n","Writer:",movie[8],"\n","Cast:",movie[9],"\n","Plot:",movie[10],"\n","Rating:",movie[11],"\n",end="\n")
    if c==0:
           print("\n","Sorry,the engine couldn't curate the list of movies :( (Try again with different genre/category or make sure you have inputted the rating in between 1 and 10 )")          
           print("\n") 
           
print("Hello!!! Welcome to the Movie Recommendation System!!!")
print("The information and the results you are going to get will be highly based on the IMDB movie dataset.No personal reviews or opinions are included here.The ratings provided in the database is based on the IMDB RATINGS")
print("\n")
print("1.Movie recommendation engine")
print("2.To find the details of a movie")
print("3.To display the filmography of a director")
print("4.To display the filmography of a writer")
print("5.To display the filmography of an actor")
print("6.To view the plot of a movie")
print("7.To display the highest rated movies of a year")
print("8.To display the highest rated movies of a language")
print("9.To display the highest rated movies of a country")
print("10.To display the highest rated movies of a genre/category")
print("11.To display all the movies released in a year of a language")
print("12.To display the highest rated movies in a year of a language")
print("13.To find movies of your required duration")
print("14.To display movies with the same name")
print("15.To find movies with two actors of your choice")
print("16.To find movies having mixed genres/categories of your choice")
print("17.To display the film collabarations of an actor and a director")
print("18.To display the film collabarations of an actor and a writer")
print("19.To display the film collabarations of a director and a writer ")
print("20.To display the film collabarations of an actor,a director and a writer")
print("21.To display the highest rated movies of a language and a genre/category")
print("22.To find movies using keywords in the plot description")
print("23.To find movies of your required rating")
print("\n")

ch="y"
while ch.lower()=="y":
    f.seek(0)
    i=int(input("Enter your choice from the list of applications given above:"))
    print("\n")
    
    if i==1:
        print("You have chosen the movie recommendation engine.You can enter your choice of language,genre/category and the minimum rating and the engine is going to display a list of movies that the engine thinks you would love to watch:)")
        genre=input("Enter the genre/category of your choice:")
        language=input("Enter the language of your choice:")
        rating=float(input("Enter the minimum rating required:"))
        basic(genre,language,rating)

    if i==2:
        print("You have chosen the application to display the details of a movie.You just have to type the name of the movie and the details of the movie including the release year,genre/category,language,plot,rating,cast,director,writer and duration will be displayed.(Make sure you type the name of the movie correctly , with the proper cases and symbols, or else there might occur an error in the ouput)")
        film=input("Enter the name of the film:")
        info(film)

    if i==3:
        print("You have chosen the application to display the filmography of a director. Enter the name of the director of your choice and the application is going to display the works of the director.(Make sure you type the name of the director correctly , with the proper cases , symbols and surname, or else there might occur an error in the ouput)")
        role=input("Enter the director's name:")
        director(role)

    if i==4:
        print("You have chosen the application to display the filmography of a writer. Enter the name of the writer of your choice and the application is going to display the works of the writer.(Make sure you type the name of the writer correctly , with the proper cases , symbols and surname, or else there might occur an error in the ouput)")
        role=input("Enter the writer's name:")
        writer(role)

    if i==5:
        print("You have chosen the application to display the filmography of an actor. Enter the name of the actor of your choice and the application is going to display the works of the actor.(Make sure you type the name of the actor correctly , with the proper cases , symbols and surname, or else there might occur an error in the ouput)")
        role=input("Enter the actor's name:")
        actor(role)

    if i==6:
        print("You have chosen the application to view the plot of a movie. Enter the name of the movie and the application is going to display the plot of the movie.(Make sure you type the name of the movie correctly , with the proper cases and symbols, or else there might occur an error in the ouput)")
        film=input("Enter the name of the film:")
        plot(film)

    if i==7:
        print("You have chosen the application to display the highest rated movies of a year.You have to enter a specific year and the system will provide you with the highest rated movies of that year.(Make sure you enter a year between 1874 and 2020 as the database contains movies in this time gap)")
        year=input("Enter the year of your choice :")
        toppest(year)

    if i==8:
        print("You have chosen the application to display the highest rated movies of a language.You have to enter a specific language and the system will provide you with the highest rated movies of that language.")
        language=input("Enter the language of the film:")
        lang(language)

    if i==9:
        print("You have chosen the application to display the highest rated movies of a country.You have to enter a specific country and the system will provide you with the highest rated movies of that country.")
        country=input("Enter the country's name:")
        region(country)
    
    if i==10:
        print("You have chosen the application to display the highest rated movies of a genre/category.You have to enter a specific genre/category and the system will provide you with the highest rated movies of that genre/category.(Make sure you enter valid genres/categories)")
        genre=input("Enter genre\category of the film:")
        gen(genre)

    if i==11:
        print("You have chosen the application to display all the movies released in a year of a language.You have to enter a specific year and a language and the system will provide you with the list of all movies that released in the year of the language.(Make sure you enter a year between 1874 and 2020 as the database contains movies in this time gap)") 
        language=input("Enter the language of the film:")
        year=input("Enter the year:")
        year_lang(year,language)

    if i==12:
        print("You have chosen the application to display  the highest rated movies released in a year of a language.You have to enter a specific year and a language and the system will provide you with the list of all the highest rated movies that released in the year of the language.(Make sure you enter a year between 1874 and 2020 as the database contains movies in this time gap)") 
        language=input("Enter the language of the film:")
        year=input("Enter the year:")
        top_lang(year,language)

    if i==13:
        print("You have chosen the application to display the movies of your required duration.You have to enter your minimum required duration, maximum required duration,language and genre and the system will provide you with the list of all the movies in your choice of duration.(Make sure you enter valid genres/categories and duration in hours) ") 
        genre=input("Enter genre\category of the film:")
        language=input("Enter the language of the film:")
        duration1=float(input("Enter the minimum duration in hours:"))
        duration2=float(input("Enter the maximum duration in hours:"))
        duration (genre,language,duration1,duration2)    

    if i==14:
         print("You have chosen the application to display the movies with the same name. Just enter the movie you want to search and the system will show the movies which have the same name as the movie name you entered")
         name=input("Enter the name of the movie:")
         clone(name)

    if i==15:
        print("You have chosen the application to display the movies with the two actors of your choice. Just enter the names of two actors of your choice and the system will show the movies in which both the actors have worked together.(Make sure you type the names of the actors correctly , with the proper cases , symbols and surname, or else there might occur an error in the ouput).")
        actor1=input("Enter the first actors name:")
        actor2=input("Enter the second actors name:")
        coactors(actor1,actor2)

    if i==16:
        print("You have chosen the application to display the movies with the two genres\categories of your choice. Just enter the two genres\categories of your choice and the system will show the movies in which there is a mix of the given genres.(Make sure you enter valid genres/categories )")
        language=input("Enter the language of the film:")
        genre1=input("Enter the first genre:")
        genre2=input("Enter the second genre:")
        mixed_genre(language,genre1,genre2)

    if i==17:
        print("You have chosen the application to display the movies with  an actor and a director of your choice. You have to enter the names of an actor and a director of your choice and the system will display the movies in which both the actor and the director have worked together.(Make sure you type the names of the actor and the director correctly , with the proper cases , symbols and surname, or else there might occur an error in the ouput).")
        actor=input("Enter the actor's name:")
        director=input("Enter the director's name:")
        actor_director(actor,director)

    if i==18:
        print("You have chosen the application to display the movies with  an actor and a writer of your choice. You have to enter the names of an actor and a writer of your choice and the system will display the movies in which both the actor and the writer have worked together.(Make sure you type the names of the actor and the writer correctly , with the proper cases , symbols and surname, or else there might occur an error in the ouput).")
        actor=input("Enter the actor's name:")
        writer=input("Enter the writer's name:")
        actor_writer(actor,writer)
        
    if i==19:
        print("You have chosen the application to display the movies with  a writer and a director of your choice. You have to enter the names of a writer and a director of your choice and the system will display the movies in which both the writer and the director have worked together.(Make sure you type the names of the writer and the director correctly , with the proper cases , symbols and surname, or else there might occur an error in the ouput).")
        director=input("Enter the director's name:")
        writer=input("Enter the writer's name:")
        director_writer(director,writer)
        
    if i==20:
        print("You have chosen the application to display the movies with an actor, a writer and a director of your choice. You have to enter the names of an actor, a writer and a director of your choice and the system will display the movies in which they all have worked together.(Make sure you type the names of the actor , the writer and the director correctly , with the proper cases , symbols and surname, or else there might occur an error in the ouput).")
        director=input("Enter the director's name:")
        writer=input("Enter the writer's name:")
        actor=input("Enter the actor's name:")
        dwa(director,writer,actor)
        
    if i==21:
        print("You have chosen the application to display  the highest rated movies of a language and a genre/category.You have to enter a genre/category and a language and the system will provide you with the list of all the highest rated movies of the specified language and genre\category.(Make sure you enter valid genres/categories)") 
        language=input("Enter the language of the film:")
        genre=input("Enter genre\category of the film:")
        best(language,genre)
        
    if i==22:
        print("You have chosen the application to display the list of movies having a specific word(keyword).You have to enter a specific keyword and the system will provide you with the list of all the movies that has this keyword in their plot description.")
        key=input("Enter keyword:")
        language=input("Enter the language of the film:")
        keyword(key,language)
        
    if i==23:
        print("You have chosen the application to display the movies of your required rating.You have to enter your minimum required rating, maximum required rating,language and genre and the system will provide you with the list of all the movies in your choice of rating.(Make sure you enter valid genres/categories and rating in between 1 and 10) ") 
        genre=input("Enter genre\category of the film:")
        language=input("Enter the language of the film:")
        minrating=float(input("Enter minimum rating:"))
        maxrating=float(input("Enter maximum rating:"))
        rate(genre,language,minrating,maxrating)
        
    ch=input("Enter 'y' to continue with the system or enter any other key to exit from the system:")
    print("\n")
