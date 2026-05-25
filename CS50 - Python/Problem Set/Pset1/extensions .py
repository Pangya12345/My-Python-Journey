input_make = input("File name: ").strip() # --------> Ask user file input

# check the condition (with upper case sensivity)
if ".jpeg" in input_make or ".jpg" in input_make or ".JPG" in input_make or ".JPEG" in input_make:
  print("image/jpeg")

elif ".zip" in input_make or ".ZIP" in input_make:
  print("application/zip")
  
elif ".gif" in input_make or ".GIF" in input_make:
  print("image/gif")

elif ".png" in input_make or ".PNG" in input_make:
  print("image/png")

elif ".pdf" in input_make or ".PDF" in input_make:
  print("application/pdf")

elif ".txt" in input_make or ".TXT" in input_make:
  print("text/plain")

# What to do if the condition does not match
else:
  print("application/octet-stream")

