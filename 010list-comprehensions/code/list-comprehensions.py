if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    cuboid_x = [x for x in range(x) if x != n]
    cuboid_y = [y for x in range(y) if y != n]
    cuboid_z = [z for z in range(z) if z != n]
    print(cuboid_x, cuboid_y, cuboid_z)