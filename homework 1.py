Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_distance_at_angle(scan_data, angle):
...     """
...     Returns the distance measured by the Lidar sensor at a given angle in radians.
... 
...     :param scan_data: sensor_msgs/LaserScan data
...     :param angle: angle in radians
...     :return: distance at given angle in meters
...     """
...     index = int((angle - scan_data.angle_min) / scan_data.angle_increment)
...     return scan_data.ranges[index]
... def get_distances_in_range(scan_data, start_angle, end_angle):
...     """
...     Returns a list of distances measured by the Lidar sensor over a range of angles.
... 
...     :param scan_data: sensor_msgs/LaserScan data
...     :param start_angle: start angle in radians
...     :param end_angle: end angle in radians
...     :return: list of distances in meters
...     """
...     start_index = int((start_angle - scan_data.angle_min) / scan_data.angle_increment)
...     end_index = int((end_angle - scan_data.angle_min) / scan_data.angle_increment)
...     return scan_data.ranges[start_index:end_index+1]
... def get_gap_size_ahead(scan_data, distance_threshold):
...     """
...     Returns the size of the gap/opening in front of the robot, in meters, based on a given distance threshold.
... 
...     :param scan_data: sensor_msgs/LaserScan data
...     :param distance_threshold: distance threshold in meters
...     :return: size of the gap/opening in meters
...     """
...     indices_within_threshold = [i for i, dist in enumerate(scan_data.ranges) if dist <= distance_threshold]
...     if not indices_within_threshold:
...         return None
...     gap_size = max([len(list(group)) for key, group in itertools.groupby(indices_within_threshold)]) * scan_data.angle_increment * distance_threshold
...     return gap_size
