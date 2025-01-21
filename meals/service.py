from meals.repository import MealsRepository

class MealsService:

    def __init__(self):
        self.meals_repository = MealsRepository()

    def get_meals(self):
        return self.meals_repository.get_meals()
    
    def create_meal(self, name, description, date, time, in_diet):
        meal = dict(
            name=name,
            description=description,
            date=date,
            time=time,
            in_diet=in_diet
        )
        return self.meals_repository.create_meal(meal)