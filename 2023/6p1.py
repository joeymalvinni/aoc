time, distance = open(0).read().strip().splitlines()

ans = 1

distance = distance.split("Distance: ")[1].split()

for i, t in enumerate(time.split("Time: ")[1].split()):
    w = 0 # ways to win
    for x in range(1, int(t)):
        # x is the button press time
        if (int(distance[i]) < x*(int(t) - x)):
            w += 1

    ans *= w

print(ans)
