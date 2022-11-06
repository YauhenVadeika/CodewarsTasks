# my task solution
def bouncing_ball(h, bounce, window):
    if h != 0 and bounce > 0 and bounce < 1 and window < h:
        count = 1
        current = h * bounce
        while current > window:
            current *= bounce
            count += 2
        return count
    else:
        return -1


print(bouncing_ball(30, 0.75, 1.5))


# codewars task best solution
def bouncingBall(h, bounce, window):
    seen = -1

    if 0 < bounce < 1:
        while h > window > 0:
            seen += 2
            h *= bounce

    return seen


# codewars task best solution
def bouncingBall(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    return 2 + bouncingBall(h * bounce, bounce, window)
