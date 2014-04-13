b = box(color=color.blue, size=vec(1,2,1))

while true:
    b.rotate(angle=0.01, axis=vec(0,-1,0))
    rate(200,wait)
