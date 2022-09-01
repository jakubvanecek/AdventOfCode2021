with open('Source/SourceDay6', 'r') as file:
    line = file.read().split(',')

class Lanternfish:
    def __init__(self, first_timer_value):
        self.internal_timer = first_timer_value

    def run_cycle(self):
        self.internal_timer = self.internal_timer - 1

    def renew_cycle(self):
        self.internal_timer = 6

    def new_child(self, community_members):
        fish[community_members] = Lanternfish(8)

    def live_cycle(self,community_members):
        if self.internal_timer > 0:
            self.run_cycle()
            return community_members
        else:
            self.renew_cycle()
            self.new_child(community_members)
            new_community_members = community_members + 1
            return new_community_members

    def result(self):
        return self.internal_timer

fish = dict()
community_members = 0
number_of_days = 80
result = 0

for parameter in line:
    fish[community_members] = Lanternfish(int(parameter))
    community_members = community_members + 1

for day in range(0, 80):
    for member in range(0, community_members):
        community_members = fish[member].live_cycle(community_members)

for member in range(0, community_members):
    result = result + fish[member].result()

print(community_members)
print(result)
