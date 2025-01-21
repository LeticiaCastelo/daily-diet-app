from meals.repository import MealsRepository

class MealsService:

    def __init__(self):
        self.meals_repository = MealsRepository()

    def get_meals(self):
        return self.meals_repository.get_meals()
    
    def create_meal(self, name):
        meal = dict(
            name=name,
        )
        return self.meals_repository.create_meal(meal)