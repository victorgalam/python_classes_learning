class Time:
    def __init__(self, hour, minutes):
        self.hour = hour
        self.minutes = minutes

    # We assume that self time is earlier than other time
    # Example:
    #   self = 06:30  other = 07:20 -->  7-6=1 -> 1*60=60,  20 - 30 = -10  -->  60 + -10 = 50
    def difference(self, other):
        delta_hours = other.hour - self.hour
        delta_minutes = other.minutes - self.minutes
        total_delta_minutes = delta_hours * 60 + delta_minutes
        return total_delta_minutes


if __name__ == '__main__':
    # time1 = Time(6, 30)
    # time2 = Time(7, 20)
    # diff_minutes = time1.difference(time2)
    # print(diff_minutes)

    for i in range(100):
        received_hour = int(input("Enter hour of received product: "))
        received_minute = int(input("Enter minute of received product: "))
        time_received = Time(received_hour, received_minute)
        delivered_hour = int(input("Enter hour of delivered product: "))
        delivered_minute = int(input("Enter minute of delivered product: "))
        time_delivered = Time(delivered_hour, delivered_minute)
        if time_received.difference(time_delivered) <= 180:
            print("Delivered on time")
        else:
            print("Late delivery!!!")

