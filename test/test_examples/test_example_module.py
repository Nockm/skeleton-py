import unittest

from libs.examples.example_module import get_sum_of_numbers
from libs.system.file_data_io import load_json, make_empty_dir, save_json


class TestExamples_ExampleModule(unittest.TestCase):
    def test_get_sum_of_numbers(self):
        input: list[str] = load_json(["test/test_examples/input/input.json"])
        output = get_sum_of_numbers(input)  # type: ignore
        out_dir = make_empty_dir(["test/test_examples/output_expected"])
        save_json([out_dir, "output.json"], output)
