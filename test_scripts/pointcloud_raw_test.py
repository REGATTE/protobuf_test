from datetime import datetime

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from google.protobuf.timestamp_pb2 import Timestamp
from generated.pointcloud_raw_pb2 import PointCloudRaw

def create_sample_pointcloud():
    # Create a PointCloudRaw message
    pointcloud = PointCloudRaw()

    # Set the timestamp
    timestamp = Timestamp()
    timestamp.FromDatetime(datetime.utcnow())
    pointcloud.timestamp.CopyFrom(timestamp)

    # Set the header
    pointcloud.header = 12345

    # Add sample points to the point cloud
    point1 = PointCloudRaw.Point(x=1.0, y=2.0, z=0.5, intensity=150.0, classification=1)
    point2 = PointCloudRaw.Point(x=1.5, y=2.5, z=0.6, intensity=145.0, classification=2)
    point3 = PointCloudRaw.Point(x=2.0, y=3.0, z=0.7, intensity=140.0, classification=0)
    pointcloud.points.extend([point1, point2, point3])

    # Set the frame ID
    pointcloud.frame_id = "lidar_frame"

    # Set the checksum
    pointcloud.checksum = 67890

    return pointcloud

def test_pointcloud_raw():
    # Create a sample PointCloudRaw message
    pointcloud = create_sample_pointcloud()

    # Serialize the message to a byte string
    serialized_data = pointcloud.SerializeToString()
    print("Serialized Data:", serialized_data)

    # Deserialize the message from the byte string
    deserialized_pointcloud = PointCloudRaw()
    deserialized_pointcloud.ParseFromString(serialized_data)

    # Print the deserialized message
    print("Deserialized PointCloudRaw Message:")
    print(deserialized_pointcloud)

    # Verify that the original and deserialized messages are identical
    assert pointcloud == deserialized_pointcloud, "Deserialized message does not match the original"

if __name__ == "__main__":
    test_pointcloud_raw()
