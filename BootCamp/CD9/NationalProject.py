import math


def national(days):
    days = days.split()
    days = [int(days[i]) for i in range(len(days))]
    required_good = math.ceil(days[0] / 2)

    if days[1] >= required_good:
        return days[0]
    else:
        required_good_seasons = math.ceil(required_good / days[1])
        bad_days_in_between = days[2] * (required_good_seasons - 1)
        days_needed_to_reach_required_good = bad_days_in_between + required_good

        if days_needed_to_reach_required_good < days[0]:
            return days[0]
        else:
            return days_needed_to_reach_required_good


def main():
    test = eval(input())
    for i in range(test):
        s = input()
        print(national(s))


main()
