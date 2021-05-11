class Job_Offer:
    def __init__(self, id, title, description, key_words_list):
        self.id = id
        self.title = title
        self.descrption = description
        self.key_words_list = key_words_list

    def show_title(self, id):
        if self.id == id:
            return self.title

    def show_descrption(self, id):
        if self.id == id:
            return self.descrption

    def fiter(self, filters):
        for f in filters:
            if f in self.key_words_list:
                return self

    



