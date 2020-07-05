class Newssource: # Newssource class to define Newssource Objects

    def __init__(self,id,title,description,urlToImage,publishedAt,url): #we define a Movie class and then we create an __init__ method and we pass in the six parameters we want inside our newssource objects.



        self.id =id
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.url = url