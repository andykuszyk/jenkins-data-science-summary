class SummaryReportLeafBase:
    def __init__(self):
        self._start = []
        self._end = []

    def _generate_start(self):
        report = ''
        for r in self._start:
            report += r
        return report

    def _generate_end(self):
        report = ''
        end = list(self._end)
        end.reverse()
        for r in end:
            report += r
        return report

    def generate(self):
        report = ''
        report += self._generate_start()
        report += self._generate_end()
        return report


class SummaryReportNodeBase(SummaryReportLeafBase):
    def __init__(self):
        super().__init__()
        self._children = []

    def generate(self):
        report = ''
        report += self._generate_start()
        for child in self._children:
            report += child.generate()
        report += self._generate_end()
        return report


class SummaryReportSection(SummaryReportNodeBase):
    def __init__(self):
        super().__init__()
        self._start.append('<section name="" fontcolor="">')
        self._end.append('</section>')

    def add_tabs(self):
        tabs = SummaryReportTabs()
        self._children.append(tabs)
        return tabs


class SummaryReportTabs(SummaryReportNodeBase):
    def __init__(self):
        super().__init__()
        self._start.append('<tabs>')
        self._end.append('</tabs>')

    def add_tab(self, name):
        tab = SummaryReportTab(name)
        self._children.append(tab)
        return tab


class SummaryReportTab(SummaryReportNodeBase):
    def __init__(self, name):
        super().__init__()
        self._start.append('<tab name="{}">'.format(name))
        self._end.append('</tab>')

    def add_field(self, name, value):
        field = SummaryReportField(name, value)
        self._children.append(field)
        return field

class SummaryReportField(SummaryReportLeafBase):
    def __init__(self, name, value):
        super().__init__()
        self._start.append('<field name="{}">{}'.format(name, value))
        self._end.append('</field>')


class SummaryReport(SummaryReportNodeBase):
    def __init__(self):
        super().__init__()

    def add_section(self):
        section = SummaryReportSection()
        self._children.append(section)
        return section
