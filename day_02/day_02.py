import math
import copy

def check_safety( reports:list ):
    if len(reports) < 2:
        return True
    isIncreasing = None
    previous_report = reports[0]
    for report in reports[1:]:
        if report > previous_report:
            if isIncreasing is None:
                isIncreasing = True
            if isIncreasing == False:
                return False
        elif report == previous_report:
            return False
        else:
            if isIncreasing:
                return False
            elif isIncreasing is None:
                isIncreasing = False
        diff = abs(report - previous_report)
        if diff > 3 or diff < 1:
            return False
        previous_report = report
    return True



lines = open('day_02/day_02_input.txt').read().splitlines()
# print(lines)


reports = []
for index, line in enumerate(lines):
    # print(line)
    reports.append( [int(report) for report in line.split(" ")])
print('reports')
print(reports)
print('------------------------')
safe_reports = 0
for report in reports:

    report_subsets = [report]

    for i in range(len(report)):
        report_copy = copy.deepcopy(report)
        report_copy.pop(i)
        report_subsets.append( report_copy )

    print(report_subsets)
    hasOkReport = False
    for curr in report_subsets:
        if check_safety(curr):
            hasOkReport = True
    if hasOkReport:
        safe_reports += 1
print(safe_reports)