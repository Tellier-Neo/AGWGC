class assault_rifle:
    def __init__(self):
        self.name = "Assault Rifle"
        self.damage = 30
        self.range = 150
        self.fire_rate = 600  # rounds per minute
        self.ammo_capacity = 30
        self.reload_time = 2.5  # seconds

    def shoot(self):
        print(f"Shooting {self.name} for {self.damage} damage.")

    def reload(self):
        print(f"Reloading {self.name}, takes {self.reload_time} seconds.")