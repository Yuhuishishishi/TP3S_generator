import random

from analyzer.reader import Vehicle, TestRequest, Instance


def _gen_individual_test(tid):
    prep = round(random.triangular(10, 24))
    tat = round(random.triangular(3, 5))
    analysis = round(random.triangular(4, 6))

    r_type = random.random()
    if r_type < 0.6:
        release = 0
    else:
        release = round(random.uniform(60, 100))

    width = round(random.triangular(20, 150))

    deadline = release + width
    return TestRequest(tid, release, prep, tat, analysis, deadline)


class InstanceGenerator:
    PREP_RNG = 10, 24
    TAT_RNG = 3, 5
    ANA_RNG = 4, 6

    VEHICLE_RATE = 5
    WINDOW_WIDTH = 20, 150
    TEST_RELEASE_RNG = 60, 100

    def __init__(self, num_test):
        self.num_test = num_test

    def gen_inst(self):
        test_arr = self._gen_test_arr()
        vehicle_arr = self._gen_vehicle_arr()
        rehit_rules = self._gen_rehit_rules()
        return Instance(test_arr, vehicle_arr, rehit_rules)

    def _gen_test_arr(self):
        test_arr = []
        for i in range(self.num_test):
            test = _gen_individual_test(i)
            test_arr.append(test)
        return test_arr

    def _gen_vehicle_arr(self):
        num_to_gen = int(self.num_test * 1.5)
        num_weeks = num_to_gen / InstanceGenerator.VEHICLE_RATE
        vehicle_arr = []
        vid = 0
        for i in range(num_weeks):
            for j in range(InstanceGenerator.VEHICLE_RATE):
                vehicle_arr.append(Vehicle(vid, i * InstanceGenerator.VEHICLE_RATE))
                vid += 1

        return vehicle_arr

    def _gen_rehit_rules(self):
        rehit_rules = {}
        tid_list = range(self.num_test)
        for i in range(self.num_test):
            r_type = random.random()
            if r_type < 0.5:
                # no follow-ups
                map(lambda x: rehit_rules.update({x: False}), [(i,t) for t in tid_list])
            else:
                num_comp = random.randrange(1, self.num_test)
                comp_tid = random.sample(tid_list, num_comp)
                map(lambda x: rehit_rules.update({x: True}), [(i, t) for t in tid_list if t in comp_tid])
                map(lambda x: rehit_rules.update({x: False}), [(i,t) for t in tid_list if t not in comp_tid])
        return rehit_rules



