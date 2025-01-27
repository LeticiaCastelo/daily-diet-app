from home.repository import HomeRepository

class HomeService:

    def __init__(self):
        self.home_repository = HomeRepository()

    def get_meals(self):
        return self.home_repository.get_meals()