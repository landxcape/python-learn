# from time import time_ns, strftime, gmtime
import matplotlib.pyplot as plt


fig = plt.figure()
graph = fig.add_subplot(1, 1, 1)


class Vehicle:
    def __init__(self, v_id):
        self.v_id = v_id

    def position(self, node):
        self.node = node

    def travel_time(self, t_time):
        self.t_time = t_time


def traffic_light(time_elapsed):
    light = 'red'
    # change traffic light after every interval
    if(int(time_elapsed / traffic_signal_interval) % 2 == 0):
        light = 'green'
    return light


vehicle_in = []
queue = []
node1_yaxis = []
node2_yaxis = []

# vehicle_interval = int(input('Enter vehicle interval (in sec): '))
# queue_interval = int(input('Enter queue interval (in sec): '))
# total_time = int(input('Enter total time (in sec): '))
# traffic_signal_interval = int(
#     input('Enter traffic signal interval (in sec): '))
# travel_time = int(input('Enter travel time (in sec): '))

vehicle_interval = 5
queue_interval = 2
total_time = 120
traffic_signal_interval = 30
travel_time = 10

# per loop is one second
time_axis = 0
while(time_axis < total_time):
    # entry vehicle after every vehicle interval
    if(time_axis % vehicle_interval == 0):
        # entry_time = strftime('%H:%M:%S', gmtime(int(time_ns() * 1e-9)))
        v_id = f'vehicle-{time_axis}'
        v = Vehicle(v_id=v_id)
        v.position(1)
        v.travel_time(travel_time)
        vehicle_in.append(v)

    # if there is a vehicle in node 1
    if(vehicle_in):
        # wait for travel time
        for v in vehicle_in:
            if(v.t_time <= 1):
                # if the traffic light is red
                if(traffic_light(time_axis) == 'red'):
                    v.position(2)
                    queue.append(vehicle_in.pop(0))

                # if the traffic light is green
                elif(traffic_light(time_axis) == 'green'):
                    # or set position to 3 and skip queue as the vehicle doesnot stop at green
                    v.position(2)
                    queue.append(vehicle_in.pop(0))
            v.t_time -= 1

    # tf there is vehicle in node 2
    if(queue):
        # if traffic light is green
        if(traffic_light(time_axis) == 'green'):
            if((time_axis) % queue_interval == 0):
                queue.pop(0)

    # print('time remaining: ', total_time - time_axis)
    # adding the number of vehicles in node 1 to list
    node1_yaxis.append(len(vehicle_in))
    # adding the number of vehicles in node 2 (queue) to list
    node2_yaxis.append(len(queue))

    time_axis += 1
    # for v in vehicle_in:

graph.clear()
graph.grid(True)
graph.plot(range(time_axis), node1_yaxis, "-b", label="node1")
graph.plot(range(time_axis), node2_yaxis, "-r", label="node2")
plt.legend(loc="upper left")
plt.show()
