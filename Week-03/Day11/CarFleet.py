class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if len(position) == 0: return 0

        time_left = []

        for i in range(len(position)):
            current_time_left = (target - position[i]) / speed[i]
            time_left.append([position[i], current_time_left])

        time_left.sort(reverse=True)

        no_car_fleet = 1
        prev_time = time_left[0][1]
        for i in range(1, len(time_left)):
            if prev_time < time_left[i][1]:
                no_car_fleet += 1
                prev_time = time_left[i][1]

        return no_car_fleet