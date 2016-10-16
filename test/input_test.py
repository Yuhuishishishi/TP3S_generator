import unittest

from analyzer.reader import TP3SReader


class InputTestCase(unittest.TestCase):

    def setUp(self):
        base_file_path = "C:\Users\yuhui\Documents\Python Scripts\TP3S_analyzer\inouts\{inst_id}.tp3s"
        self.paths = []
        for i in range(152, 159):
            act_path = base_file_path.format(inst_id=str(i))
            self.paths.append(act_path)

    def test_read(self):
        reader = TP3SReader(self.paths)
        inst_list = reader.read_instances()
        assert len(inst_list) > 0
        for inst in inst_list:
            assert inst.num_test > 0
            assert inst.num_vehicle > 0


if __name__ == '__main__':
    unittest.main()
