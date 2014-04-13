scene.forward = vec(0,-.3,-1)

G = 6.7e-11

giant = sphere( pos=vec(-1e11,0,0), size=vec(1,1,1)*4e10, color=color.red )
giant.mass = 2e30
giant.p = vec(0, 0, -1e4) * giant.mass
attach_trail(giant, {retain:150})

dwarf = sphere( pos=vec(1.5e11,0,0), size=vec(1,1,1)*2e10, color=color.yellow )
dwarf.mass = 1e30
dwarf.p = -giant.p
attach_trail(dwarf, {type:"spheres", pps:20, retain:40})

dt = 1e5
while true:
    rate(200,wait)
    dist = dwarf.pos - giant.pos
    coeff = G * giant.mass * dwarf.mass
    force = dist * coeff / pow(mag(dist),3) 
    giant.p = giant.p + force*dt
    dwarf.p = dwarf.p - force*dt
    stars = [giant, dwarf]
            
    for  w, star in enumerate(stars):
        star.pos = star.pos + (star.p/star.mass) * dt
