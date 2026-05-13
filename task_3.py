class PointsForPlace:
    @staticmethod
    def get_points_for_place(place:int) -> int:
        points = 0
        if  1 <= place <= 100:
            points = 101 - place
        elif place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters:int) -> float:
        points = 0
        if meters > 0:
            points = meters * 0.5
        else:
            print('Количество метров не может быть отрицательным')
        return points

class TotalPoints(PointsForMeters, PointsForPlace):
    @staticmethod
    def get_total_points(meters:int, place:int) -> float:
        total = PointsForPlace.get_points_for_place(place) + PointsForMeters.get_points_for_meters(meters)
        return total

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))