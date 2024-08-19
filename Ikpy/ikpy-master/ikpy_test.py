from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from ikpy.utils import plot
import math

my_robot_arm = Chain(name='my_robot_arm', links=[
    OriginLink(),
    URDFLink(
      name="first_link",
      origin_translation=[0, 0, 0],
      origin_orientation=[0, 0, 0],
      rotation=[0, 0, 1],
    ),
    URDFLink(
      name="second_link",
      origin_translation=[0, 0, 0.4],
      origin_orientation=[0, 0, math.pi],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="third_link",
      origin_translation=[0, 0, 0.4],
      origin_orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="fourth_link",
      origin_translation=[0, 0, 0.3],
      origin_orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    )
])

# left_arm_chain.forward_kinematics([0] * 7)
# my_robot_arm.inverse_kinematics([2, 2, 2])

ax = plt.figure().add_subplot(111, projection='3d')

my_robot_arm.plot(my_robot_arm.inverse_kinematics([0.3, 0.2,0.4]), ax)
plt.show()
