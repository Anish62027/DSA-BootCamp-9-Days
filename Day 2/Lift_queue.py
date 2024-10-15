import queue

class Lift:
    def __init__(self, floors=10):
        self.current_floor = 0
        self.total_floors = floors
        self.requests = queue.Queue()

    def request_floor(self, floor):
        if 0 <= floor < self.total_floors: 
            self.requests.put(floor)  
            print(f"Floor {floor} requested.")
        else:
            print(f"Invalid request. Please select a floor between 0 and {self.total_floors - 1}.")

    def move_lift(self):
        while not self.requests.empty(): 
            next_floor = self.requests.get()  
            print(f"Moving from floor {self.current_floor} to floor {next_floor}.")
            self.current_floor = next_floor 
            print(f"Lift has reached floor {self.current_floor}.")


lift = Lift(floors=10)  


lift.request_floor(3)
lift.request_floor(7)
lift.request_floor(1)

lift.move_lift()
