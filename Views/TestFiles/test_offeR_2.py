import datetime

from Projekt_zespołowy.models import JobOffer
# dane testowe - do usunięcia po konfiguracji modeli


def split_benefits(self):
    return self.additionalBenefits.split(',')

def split_nth(self):
    return self.niceToHave.split(",")


title = "Job offer ring"
date1 = datetime.date(2021, 5, 10)
date2 = datetime.date(2021, 5, 20)
description = "    One Ring to rule them all, One ring to find them; One ring to bring them all and in the darkness bind them. " \
                                 "vulputate, nunc nibh rhoncus dui, at congue ligula sem at diam. Fusce libero ligula, " \
                                 "mollis in sapien eu, interdum dignissim neque. Duis et enim a nunc dictum rutrum sed " \
                                 "in eros. Sed ultricies quis neque sed imperdiet. Cras feugiat ac urna a ultrices. Nam " \
                                 "ac lacus vitae quam ullamcorper venenatis. Suspendisse potenti. Nam scelerisque est " \
                                 "lectus, vel dictum est mattis vel. Pellentesque ultricies elit neque, sit amet vehicula " \
                                 "eros accumsan nec. Pellentesque rhoncus fermentum magna, at ultrices eros consequat nec. " \
                                 "Nunc ut congue purus, eget dignissim dui. Mauris ut ex nec dolor imperdiet vehicula vel " \
                                 "quis quam. Proin non accumsan ipsum, feugiat semper elit. Vivamus elementum risus purus, " \
                                 "eu efficitur ligula tincidunt eu.Vivamus tristique tortor non pharetra sollicitudin. " \
                                 "Sed eu gravida quam. Ut metus nunc, porttitor at ante a, finibus laoreet nisi. Nullam " \
                                 "venenatis accumsan facilisis. Vestibulum volutpat massa eu pellentesque venenatis. " \
                                 "Aenean fermentum, ante sit amet euismod vehicula, nisi arcu elementum est, at consequat " \
                                 "nulla tortor ac tellus. Donec vitae rhoncus lacus. Phasellus venenatis congue orci, vel " \
                                 "venenatis lectus mattis at. Cras dolor dolor, tristique sed velit vel, cursus consectetur justo. " \
                                 "Aenean pharetra metus in congue vulputate. Etiam commodo in magna nec rhoncus."
additional = "first,second,third,fourth"
nice = "something,nice,to,have"
second_offer = JobOffer(title, True, date1, date2, description, 8000, 15000, additional, nice)