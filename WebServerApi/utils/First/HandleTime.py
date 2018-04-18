class HandleTime:
    def __init__(self, start, end):
        self.startyear = int(start[0:4])
        self.endyear = int(end[0:4])
        self.startMonth = int(start[-2:])
        self.endMonth = int(end[-2:])
        self.init()

    def init(self):
        self.months_begin = ["-01-01", "-02-01", "-03-01", "-04-01", "-05-01", "-06-01",
                             "-07-01", "-08-01", "-09-01", "-10-01", "-11-01", "-12-01"]
        self.months_end = ["-01-31", "-02-28", "-03-31", "-04-30", "-05-31", "-06-30",
                           "-07-31", "-08-31", "-09-30", "-10-31", "-11-30", "-12-31"]

    def handle(self):
        data = []
        temp = self.startyear
        while temp < self.endyear:
            if temp != self.startyear:
                for i, value in enumerate(self.months_end):
                    a = (str(temp) + self.months_begin[i], str(temp) + value)
                    data.append(a)
            else:
                i = self.startMonth - 1
                for value in self.months_end[self.startMonth - 1:]:
                    a = (str(temp) + self.months_begin[i], str(temp) + value)
                    data.append(a)
                    i += 1
            temp += 1

        if self.startyear == self.endyear:
            for i, value in enumerate(self.months_end[self.startMonth-1:self.endMonth]):
                a = (str(temp) + self.months_begin[i+self.startMonth-1], str(self.endyear) + value)
                data.append(a)
        else:
            for i, value in enumerate(self.months_end[0:self.endMonth]):
                a = (str(temp) + self.months_begin[i], str(self.endyear) + value)
                data.append(a)

        return data

    def reversehandle(self, t):
        year = t[:4]
        month = t[5:7]
        return year + month


if __name__ == "__main__":
    ha = HandleTime('201610', '201612')
    print(ha.handle())
