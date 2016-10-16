import unittest

from analyzer.analyzer import TP3SAnalyzer
from analyzer.reader import TP3SReader


class AnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        base_file_path = "C:\Users\yuhui\Documents\Python Scripts\TP3S_analyzer\inouts\{inst_id}.tp3s"
        self.paths = []
        for i in range(152, 159):
            act_path = base_file_path.format(inst_id=str(i))
            self.paths.append(act_path)

    def general_info_test(self):
        reader = TP3SReader(self.paths)
        inst_list = reader.read_instances()

        for inst in inst_list:
            analyzer = TP3SAnalyzer(inst)
            analyzer.general_info()
            analyzer.test_dur_dist()
            assert analyzer


if __name__ == '__main__':
    unittest.main()
