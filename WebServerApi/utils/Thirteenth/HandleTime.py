class HandleTime:
    def __init__(self, start, end):
        self.startyear = int(start[0:4])
        self.endyear = int(end[0:4])
        self.startMonth = int(start[-2:])
        self.endMonth = int(end[-2:])
        self.init()

    def init(self):
        self.clock = " 00:00:00"
        self.months = ["-01-31", "-02-28", "-03-31", "-04-30", "-05-31", "-06-30",
                       "-07-31", "-08-31", "-09-30", "-10-31", "-11-30", "-12-31"]

    def hanle(self):
        data = []
        temp = self.startyear
        while temp < self.endyear:
            if temp != self.startyear:
                for i in self.months:
                    data.append(str(temp) + i + self.clock)
            else:
                for i in self.months[self.startMonth - 1:]:
                    data.append(str(temp) + i + self.clock)
            temp += 1
        for i in self.months[0:self.endMonth]:
            data.append(str(self.endyear) + i + self.clock)

        return data

    def reversehandle(self, t):
        year = t[:4]
        month = t[5:7]
        return year+month
