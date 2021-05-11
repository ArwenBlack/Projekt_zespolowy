class Job_Offer:
    def __init__(self, id, title, description, key_words_list):
        self.id = id
        self.title = title
        self.descrption = description
        self.key_words_list = key_words_list

    def show_title(self, id):
        return self.title

    def show_descrption(self, id):
        return self.descrption


