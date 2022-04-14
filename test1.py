import numpy as np
import matplotlib.pyplot as plt

class ptp_line:
    def __init__(self, *args):
        self.final = list(args)
        self.current = [0, 0]
        self.F = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current != self.final:
            if self.F >= 0:
                self.current[0] += 1
                self.F -= self.final[1]
            else:
                self.current[1] += 1
                self.F += self.final[0]
            print('current point', self.current)
            return self.current
        else:
            raise StopIteration

class ptp_circle:
    def __init__(self,  radius, flag = False):
        self.flag = flag
        self.final = [0, radius]
        self.current = [radius, 0]
        self.F = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current != self.final:
            if not self.flag:
                if self.F >= 0:
                    self.F = self.F - 2*self.current[0] + 1
                    self.current[0] -= 1
                else:
                    self.F = self.F + 2*self.current[1] + 1
                    self.current[1] += 1
            else:
                if self.F >= 0:
                    self.F = self.F - 2*self.current[1] + 1
                    self.current[1] -= 1
                else:
                    self.F = self.F + 2*self.current[0] + 1
                    self.current[0] += 1
            print('current point', self.current)
            return self.current
        else:
            raise StopIteration

class MyNumbers:
    def __init__(self, a):
        self.a = a
    def __iter__(self):
        return self
    def __next__(self):
        if self.a <= 20:
          x = self.a
          self.a += 1
          return x
        else:
          raise StopIteration

#plot line
xf = 50
yf = 40
myclass = ptp_line(50, 40)
k = yf/xf
myiter = iter(myclass)
x = [0]
y = [0]
for i in myiter:
    x.append(i[0])
    y.append(i[1])
t = np.linspace(0, 50, len(x))
f = t*k
fig = plt.figure(figsize=(10, 10))
plt.plot(x, y, '-o')
plt.plot(t, f, 'r')
plt.show()

#plot circle
radius = 50
myclass = ptp_circle(radius, False)
myiter = iter(myclass)
x = [radius]
y = [0]
for i in myiter:
    x.append(i[0])
    y.append(i[1])
t = np.linspace(1, radius, len(x))
f = np.array([pow(pow(radius, 2) - pow(i, 2), 0.5) for i in t])
fig = plt.figure(figsize=(10, 10))
plt.plot(x, y, '-o')
plt.plot(t, f, 'r')
plt.show()
