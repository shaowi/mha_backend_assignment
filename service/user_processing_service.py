from model.user import User


# Service class to process user data
class UserProcessingService:
    def __init__(self):
        self.infants_and_toddlers = "Infants and Toddlers (0-3)"
        self.preschoolers = "Preschoolers (3-5)"
        self.children = "Children (6-12)"
        self.adolescents = "Adolescents (13-18)"
        self.young_adults = "Young Adults (19-29)"
        self.adults = "Adults (30-59)"
        self.middle_aged_adults = "Middle-aged Adults (40-59)"
        self.seniors = "Seniors (60-79)"
        self.elderly = "Elderly (80+)"
        self.centenarians = "Centenarians (100+)"

        self.age_categories = {
            self.infants_and_toddlers: 0,
            self.preschoolers: 0,
            self.children: 0,
            self.adolescents: 0,
            self.young_adults: 0,
            self.adults: 0,
            self.middle_aged_adults: 0,
            self.seniors: 0,
            self.elderly: 0,
            self.centenarians: 0,
        }

    def process_user_age(self, user: User):
        if 0 <= user.age <= 3:
            self.age_categories[self.infants_and_toddlers] += 1
        elif 3 < user.age <= 5:
            self.age_categories[self.preschoolers] += 1
        elif 5 < user.age <= 12:
            self.age_categories[self.children] += 1
        elif 12 < user.age <= 18:
            self.age_categories[self.adolescents] += 1
        elif 18 < user.age <= 29:
            self.age_categories[self.young_adults] += 1
        elif 29 < user.age <= 59:
            self.age_categories[self.adults] += 1
        elif 59 < user.age <= 79:
            self.age_categories[self.seniors] += 1
        elif 79 < user.age <= 100:
            self.age_categories[self.elderly] += 1
        else:
            self.age_categories[self.centenarians] += 1

    def get_user_age_categories_str(self):
        output = ""
        for category, count in self.age_categories.items():
            output += f"{category}: {count}\n"
        return output
