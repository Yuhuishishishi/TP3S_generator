import json


class TestRequest:
    def __init__(self, tid, release, prep, tat, analysis, deadline):
        self.tid = tid
        self.release = release
        self.prep = prep
        self.tat = tat
        self.analysis = analysis
        self.deadline = deadline

    @property
    def dur(self):
        return self.prep + self.tat + self.analysis

    def __repr__(self):
        return str(self.tid), str(self.release), str(self.dur), str(self.deadline)


class Vehicle:
    def __init__(self, vid, release):
        self.vid = vid
        self.release = release

    def __repr__(self):
        return str(self.vid), str(self.release)


class Instance:
    def __init__(self, test_arr, vehicle_arr, rehit_rules):
        self.test_arr = test_arr
        self.vehicle_arr = vehicle_arr
        self.rehit_rules = rehit_rules

        # general information
        self.num_test = len(test_arr)
        self.num_vehicle = len(vehicle_arr)


class TP3SReader:
    def __init__(self, path_list):
        self.path_list = path_list
        self.inst_list = []

    def read_instances(self):
        for path in self.path_list:
            with open(path) as f:
                data = f.read()
            j = json.loads(data)
            inst = _create_instance_from_json(j)
            self.inst_list.append(inst)

        return self.inst_list


def _create_instance_from_json(j):
    test_arr = _parse_tests(j)
    vehicle_arr = _parse_vehicles(j)
    rehit_rules = _parse_rehit_rules(j)
    inst = Instance(test_arr, vehicle_arr, rehit_rules)
    return inst


def _parse_vehicles(j):
    data = j["vehicles"]
    vehicle_arr = [Vehicle(v["vehicle_id"], v["release"]) for v in data]
    vehicle_arr.sort(key=lambda x: x.release)
    return vehicle_arr


def _parse_tests(j):
    test_arr = []
    data = j["tests"]
    for t in data:
        tid = t["test_id"]
        prep = t["prep"]
        tat = t["tat"]
        analysis = t["analysis"]
        release = t["release"]
        deadline = t["deadline"]

        new_test = TestRequest(tid, release, prep, tat, analysis, deadline)
        test_arr.append(new_test)
    # sorting
    test_arr.sort(key=lambda x: x.tid)
    return test_arr


def _parse_rehit_rules(j):
    data = j["rehit"]
    rehit_rules = {}
    for k, inner in data.iteritems():
        id1 = int(k)
        for k2, rule in inner.iteritems():
            id2 = int(k2)
            rehit_rules[id1, id2] = rule
    return rehit_rules
