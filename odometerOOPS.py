class odometer :
    reading
    def __init__(self, n) :
        digit = 1;
        odometer_temp = "";
        for digit in range(1,n+1):
            odometer_temp += str(digit);
            digit += 1
        self.reading=odometer_temp

    def isAscending(self):
        i = 1;
        self.reading = str(self.reading)
        for i in range(1,len(self.reading)):
            if self.reading[i] <= self.reading[i-1]:
                return False;
        return True;

    def nextReading(self):
        if (self.reading == 789):
            return 123
        self.reading += 1
        while (not(isAscending())):
            self.reading += 1;
        return self.reading;

    def prevReading(self):
        if self.reading == 123:
            return 789
        self.reading -= 1;
        while (not(isAscending())):
            self.reading -= 1
        return self.reading;

    def next_n_readings(self,n):
        nextnreadings = [];
        for i in range(n):
            self.reading = nextReading();
            nextnreadings.append(self.reading);
        return nextnreadings;

    def prev_n_readings(self, n):
        prevnreadings = [];
        for i in range(n):
            self.reading = prevReading();
            prevnreadings.append(self.reading);
        return prevnreadings;

    def findDistance(self, reading1,reading2):
        count = 0;
        while(reading1 != reading2):
            reading1 = nextReading();
            count += 1
        return count;
