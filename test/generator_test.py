import unittest
import json

from analyzer.reader import TP3SInstanceEncoder, TP3SReader
from generator.generator import InstanceGenerator


class GeneratorTest(unittest.TestCase):
    OUT_DIR = r"C:\Users\yuhui\Documents\Python Scripts\TP3S_analyzer\inouts\{name}.tp3s"

    def test_generator(self):
        generator = InstanceGenerator(100)
        inst = generator.gen_inst()
        assert inst.num_test == 100

    def test_inst_write_to_and_back(self):
        generator = InstanceGenerator(50)
        inst = generator.gen_inst()
        with open(GeneratorTest.OUT_DIR.format(name="sim"), 'w') as f:
            json.dump(inst, cls=TP3SInstanceEncoder, fp=f)

        # read back
        reader = TP3SReader([GeneratorTest.OUT_DIR.format(name="sim")])
        inst_list = reader.read_instances()
        inst = inst_list[0]
        assert inst.num_test == 50

if __name__ == '__main__':
    unittest.main()
