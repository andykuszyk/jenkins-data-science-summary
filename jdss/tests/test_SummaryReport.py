from unittest import TestCase
from jdss import SummaryReport


class test_SummaryReport(TestCase):
    def test_one_section(self):
        report = SummaryReport()
        report.add_section()
        xml = report.generate()
        self.assertEqual(xml, '<section name="" fontcolor=""></section>')