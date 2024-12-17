from datetime import datetime

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generated.laserscan_raw_pb2 import LaserScanRaw
from google.protobuf.timestamp_pb2 import Timestamp

def create_sample_laserscan():
    # Create a LaserScanRaw message
    laserscan = LaserScanRaw()

    # Set the timestamp
    timestamp = Timestamp()
    timestamp.FromDatetime(datetime.utcnow())
    laserscan.timestamp.CopyFrom(timestamp)

    # Set angles and range limits
    laserscan.angle_min = 0.0
    laserscan.angle_max = 6.28319  # 2π radians for a full 360-degree scan
    laserscan.angle_increment = 0.01745  # 1 degree in radians
    laserscan.range_min = 0.15  # Minimum measurable range in meters
    laserscan.range_max = 12.0  # Maximum measurable range in meters

    # Add some sample ranges and intensities
    laserscan.ranges.extend([1.0, 1.2, 1.5, 1.7, 2.0])
    laserscan.intensities.extend([120, 130, 140, 150, 160])

    # Set the checksum
    laserscan.checksum = 12345

    return laserscan

def test_laserscan():
    # Create a sample LaserScanRaw message
    laserscan = create_sample_laserscan()

    # Serialize the message to a byte string
    serialized_data = laserscan.SerializeToString()
    print("Serialized Data:", serialized_data)

    # Deserialize the message from the byte string
    deserialized_laserscan = LaserScanRaw()
    deserialized_laserscan.ParseFromString(serialized_data)

    # Print the deserialized message
    print("Deserialized LaserScanRaw Message:")
    print(deserialized_laserscan)

if __name__ == "__main__":
    test_laserscan()


"""
1. create_sample_laserscan:

    Constructs a LaserScanRaw message.
    Populates fields like timestamp, angle_min, angle_max, ranges, and intensities.

2. Serialization:

    Converts the LaserScanRaw message into a compact byte string using SerializeToString.

3. Deserialization:

    Reconstructs the LaserScanRaw message from the serialized byte string using ParseFromString.

4. Validation:

    Prints the deserialized message to ensure it matches the original.
"""