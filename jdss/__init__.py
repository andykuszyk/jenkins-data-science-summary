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
        self._start += '<section name="" fontcolor="">'
        self._end += '</section>'


class SummaryReport(SummaryReportNodeBase):
    def __init__(self):
        super().__init__()

    def add_section(self):
        section = SummaryReportSection()
        self._children.append(section)
        return section
