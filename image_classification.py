import matplotlib.pyplot as plt
import cv2

# Load the image using OpenCV
image = cv2.imread(r'/Users/sivaprasanth/Desktop/Hackathon/Image Dataset/HIV/moll-cont__ProtectWyJQcm90ZWN0Il0_FocusFillWzI5NCwyMjIsIngiLDFd.jpg')

# Convert BGR to RGB (OpenCV loads images in BGR by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(image_rgb)
plt.axis('off')  # Turn off axis numbers and ticks
plt.show()