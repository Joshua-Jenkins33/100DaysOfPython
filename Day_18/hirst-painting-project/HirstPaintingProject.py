import colorgram

colors = colorgram.extract('hirst.jpg', 6)
real_colors = []

for obj in colors:
  real_colors.append(obj.rgb)

print(real_colors[0])