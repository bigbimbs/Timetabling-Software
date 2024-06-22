from Schedule import Schedule
from Schedule import data
class Population:
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size): self._schedules.append(Schedule().initialize())
    
    def get_schedules(self): return self._schedules