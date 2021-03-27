# Vehicle-counter
Model approach:
- Use BackgroundSubtractorMOG2 to apply to frame
- Bounding rectangle around contours (green box)
- Ignoring small contours
- Take centroid to track (red dot)
- Append centroid to validVehicles
- Check centroid passing line
- Print total vehicles 
- Destroy windows
