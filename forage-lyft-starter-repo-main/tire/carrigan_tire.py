from tire.tire import Tire


class CarriganEngine(Tire):
    def __init__(self, current_worn, worn_standard):
        self.current_worn = current_worn
        self.worn_standard = worn_standard

    def needs_service(self):
        return self.current_worn > self.worn_standard
