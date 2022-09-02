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

print('Result part1:' + str(result))

class LanterfishHuge:
    def __init__(self, internal_timer):
        self.internal_timer = internal_timer
        self.stack = 1

    def new_fish(self, community_members, internal_timer):
        huge_fish[community_members] = LanterfishHuge(internal_timer)
        new_community_members = community_members + 1
        return new_community_members

    def check_internal_timer(self, timer_value):
        if self.internal_timer == timer_value:
            return True

    def new_to_stack(self, to_stack):
        self.stack = self.stack + to_stack

    def run_cycle(self):
        self.internal_timer = self.internal_timer - 1

    def renew_cycle(self):
        self.internal_timer = 6

    def life_cycle(self, to_stack):
        if self.internal_timer > 0:
            self.run_cycle()
            return to_stack
        else:
            self.renew_cycle()
            return self.stack + to_stack

    def result(self):
        return self.stack

huge_fish = dict()
community_members = 0
number_of_days = 256
result = 0

for day in range(0, number_of_days):
    if day == 0:
        for parameter in line:
            if community_members == 0:
                huge_fish[0] = LanterfishHuge(int(parameter))
                community_members = community_members + 1
            else:
                for member in range(0, community_members):
                    if(huge_fish[member].check_internal_timer(int(parameter)) == True):
                        huge_fish[member].new_to_stack(1)
                        add_next = False
                        break
                    else:
                        add_next = True
                if add_next == True:
                    huge_fish[community_members] = LanterfishHuge(int(parameter))
                    community_members = community_members + 1
                    add_next = False
                continue
        add_new = 0
        for member in range(0, community_members):
            add_new = huge_fish[member].life_cycle(add_new)
        if add_new > 0:
            for member in range(0, community_members):
                if (huge_fish[member].check_internal_timer(8) == True):
                    huge_fish[member].new_to_stack(add_new)
                    add_next = False
                    break
                else:
                    add_next = True
            if add_next == True:
                huge_fish[community_members] = LanterfishHuge(8)
                community_members = community_members + 1
                add_next = False
                continue
    else:
        add_new = 0
        for member in range(0, community_members):
            add_new = huge_fish[member].life_cycle(add_new)
        if add_new > 0:
            for member in range(0, community_members):
                if (huge_fish[member].check_internal_timer(8) == True):
                    huge_fish[member].new_to_stack(add_new)
                    add_next = False
                    break
                else:
                    add_next = True
            if add_next == True:
                huge_fish[community_members] = LanterfishHuge(8)
                huge_fish[community_members].new_to_stack(add_new - 1)
                community_members = community_members + 1
                add_next = False
                continue


for member in range(0, community_members):
    result = result + huge_fish[member].result()

print('Result part2:' + str(result))
