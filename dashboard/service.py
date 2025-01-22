from dashboard.repository import DashboardRepository

class DashboardService:

    def __init__(self):
        self.dashbord_repository = DashboardRepository()

    def get_meals(self):
        return self.dashbord_repository.get_meals()