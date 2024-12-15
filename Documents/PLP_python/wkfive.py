class Book:
    def __init__(self, label, writer, price):
      
        self.label = label
        self.writer = writer
        self.price = price

    def receive_overview(self):
        
        return f"'{self.label}' written by {self.writer} is listing for ${self.price:.2f}."

    def __str__(self):
       
        return f"Book: {self.label} by {self.writer} - ${self.price:.2f}"



class EBook(Book):
    def __init__(self, label, writer, price, file_size, format):
       
        super().__init__(label, writer, price)
        self.file_size = file_size 
        self.format = format 

    def download(self):
     
        return f"You are downloading '{self.label}' as a {self.format} file ({self.file_size}MB)..."

    def __str__(self):
       
        return (
            super().__str__()
            + f" [This eBook: {self.file_size}MB, Format: {self.format}]"
        )



class AudioBook(Book):
    def __init__(self, label, writer, price, duration, narrator):
       
        super().__init__(label, writer, price)
        self.duration = duration 
        self.narrator = narrator 

    def test_copy(self):
     
        return f"Playing a sample of '{self.label}' narrated by {self.narrator}."

    def __str__(self):
       
        return (
            super().__str__()
            + f" [AudioBook: {self.duration} hours, Narrator: {self.narrator}]"
        )



if __name__ == "__main__":
   
    physical_book = Book("Batten-Corbet-Lucey", "De Gruyter", 18.99)
    print(physical_book)
    print(physical_book.receive_overview())
    
    ebook = EBook("Studies in Health Economics", "De Gruyter", 12.19, 1.2, "EPUB")
    print("\n" + str(ebook))
    print(ebook.download())

    
    audiobook = AudioBook(
        "Becoming", "Michelle Obama", 19.99, 19.5, "Michelle Obama"
    )
    print("\n" + str(audiobook))
    print(audiobook.test_copy())
