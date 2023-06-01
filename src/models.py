from django.db import models


class ElevatorSystem(models.Model):
    name = models.CharField(max_length=25)
    maximum_floors = models.PositiveIntegerField()
    number_of_elevators = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return f"{self.name} Elevator System Number {self.id}"


class Elevator(models.Model):
    class RunningStatus(models.IntegerChoices):
        GOING_UP = 1, 'Going Up'
        STANDING_STILL = 0, 'Standing Still'
        GOING_DOWN = -1, 'Going Down'
    
    elevator_system = models.ForeignKey(ElevatorSystem, on_delete=models.CASCADE)
    elevator_number = models.IntegerField()
    current_floor = models.PositiveSmallIntegerField(default=0)
    is_operational = models.BooleanField(default=True)
    is_door_open = models.BooleanField(default=True)
    running_status = models.IntegerField(choices=RunningStatus.choices, default=RunningStatus.STANDING_STILL)
    
    def __str__(self) -> str:
        return f"Elevator Number {self.elevator_number}"


class ElevatorRequest(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    requested_floor = models.PositiveSmallIntegerField()
    destination_floor = models.PositiveSmallIntegerField()
    request_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.elevator} is requested at floor {self.requested_floor}"
