import serial
import matplotlib.pyplot as plt
import time

ser = serial.Serial("COM3", 9600, timeout=1)
time.sleep(2)

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r-')
xdata, ydata = [], []
count = 0
MAX_POINTS = 100  # <-- only keep last 100 points

while True:
    data = ser.readline().decode(errors='ignore').strip()
    if "Distance:" in data:
        try:
            distance = int(data.split()[1])
            print("Got:", distance)

            xdata.append(count)
            ydata.append(distance)

            # Keep only last MAX_POINTS points
            if len(xdata) > MAX_POINTS:
                xdata = xdata[-MAX_POINTS:]
                ydata = ydata[-MAX_POINTS:]

            line.set_xdata(xdata)
            line.set_ydata(ydata)
            ax.relim()
            ax.autoscale_view()

            plt.draw()
            plt.pause(0.01)

            count += 1
        except:
            pass

