import cv2
import numpy as np

# Load the image
image = cv2.imread('Imagen2.jpg')
image_copy = image.copy()

# Create a mask same size as image
mask = np.zeros(image.shape[:2], np.uint8)

# Create foreground and background model
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

# Interactively select the bounding box
rect = cv2.selectROI(image)
cv2.destroyAllWindows()  # Close the ROI selection window

# Run GrabCut
cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# Create a window for the user to draw on
cv2.namedWindow('Draw on the image to refine the result')

drawing = False
value = 1

# Define the drawing callback
def draw_callback(event, x, y, flags, param):
    global drawing, value
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        value = 1
    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        value = 0
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(mask, (x, y), 5, value, -1)
    elif event == cv2.EVENT_LBUTTONUP or event == cv2.EVENT_RBUTTONUP:
        drawing = False

# Set the callback
cv2.setMouseCallback('Draw on the image to refine the result', draw_callback)

# Let the user draw on the image
while True:
    image_temp = image_copy.copy()
    image_temp[mask == 1] = [0, 255, 0]
    image_temp[mask == 0] = [0, 0, 255]
    cv2.imshow('Draw on the image to refine the result', image_temp)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()  # Close the drawing window

# Run GrabCut again with the new mask
cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)

# Apply the mask to get segmented image
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
image = image*mask2[:,:,np.newaxis]

# Convert image to RGBA color space
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

# Set alpha channel to 0 where background was removed
image[mask2 == 0] = [0, 0, 0, 0]

# Save the image
cv2.imwrite('image_without_bg.png', image)

# Display the image
cv2.imshow('Image without Background', image)
cv2.waitKey(0)
cv2.destroyAllWindows()