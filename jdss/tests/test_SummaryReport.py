from unittest import TestCase
from jdss import SummaryReport


class test_SummaryReport(TestCase):
    def test_one_section(self):
        report = SummaryReport()
        report.add_section()
        xml = report.generate()
        self.assertEqual(xml, '<section name="" fontcolor=""></section>')

    def test_one_tabs(self):
        report = SummaryReport()
        section = report.add_section()
        section.add_tabs()
        xml = report.generate()
        self.assertEqual(xml, '<section name="" fontcolor=""><tabs></tabs></section>')

    def test_one_tab(self):
        report = SummaryReport()
        section = report.add_section()
        tabs = section.add_tabs()
        tabs.add_tab('foo')
        xml = report.generate()
        self.assertEqual(xml, '<section name="" fontcolor=""><tabs><tab name="foo"></tab></tabs></section>')

    def test_one_field(self):
        report = SummaryReport()
        section = report.add_section()
        tabs = section.add_tabs()
        tab = tabs.add_tab('foo')
        tab.add_field('spam', 'eggs')
        xml = report.generate()
        self.assertEqual(xml, '<section name="" fontcolor=""><tabs><tab name="foo"><field name="spam">eggs</field></tab></tabs></section>')

    def test_table(self):
        report = SummaryReport()
        section = report.add_section()
        table = section.add_table()
        row = table.add_row()
        row.add_cell('foo', 'bar')
        xml = report.generate()
        self.assertEqual(
            xml,
            '<section name="" fontcolor=""><table sorttable="yes"><tr><td value="foo" align="center" href="bar"/></tr></table></section>'
        )