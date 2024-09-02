import cv2
import os

folder_dir = '/Users/sivaprasanth/Desktop/Hackathon/Image Dataset/Normal Skin'
output_dir = '/Users/sivaprasanth/Desktop/Hackathon/Image Dataset/Processed/Normal Skin'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

images = [image_filename for image_filename in os.listdir(folder_dir) if not image_filename.startswith(".")]
for index, image_filename in enumerate(images):
    image_path = os.path.join(folder_dir, image_filename)
    
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print(f"Failed to load image: {image_path}")
        continue  # Skip to the next image
    
    # Check if the image has valid dimensions
    if image.shape[0] == 0 or image.shape[1] == 0:
        print(f"Invalid image dimensions: {image_path}")
        continue  # Skip to the next image
    
    # Resize the image using OpenCV
    resized_image = cv2.resize(image, (224, 224))
    
    output_filename = image_filename  # Create a unique filename
    output_path = os.path.join(output_dir, output_filename)
    
    # Save the resized image using OpenCV
    cv2.imwrite(output_path, resized_image)
