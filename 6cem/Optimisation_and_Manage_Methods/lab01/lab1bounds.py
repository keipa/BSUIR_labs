from numpy import *


def musign(a):
    if a > 0:
        return -1
    else:
        return 1

def simplex(m, n, A, b, c, x_0, J, d_down, d_up):
    iter_count = 0
    J -= 1
    while True:
        Theta = []
        B = linalg.inv(A[:, J])
        u = c[J].dot(B)
        not_J = delete(arange(n), J)
        deltas = list(map(lambda _not_j: u.dot(A[:, _not_j]) - c[_not_j], list(not_J)))
        min_delta_ind = not_J[argmin(deltas)]
        isOpt = True
        # for d, _x in zip(deltas, x_0):
        xnj = x_0[not_J]
        ddnj = d_down[not_J]
        dunj = d_up[not_J]
        j0 = 0
        for _x, _del, _dd, _du in zip(xnj, deltas, ddnj, dunj):
            if _x<=_dd and _del <= 0:

                isOpt = False
            if _x>=_du and _del>=0:
                isOpt = False
        k = argmin(deltas)
        if isOpt:
            print(list(map(lambda _x: round(float(_x), 3), list(x_0))), "- оптимальный план")
            print("Максимальная прибыль : ", c.dot(x_0))
            print("Количество итераций : ", iter_count)
            return list(map(lambda _x: round(float(_x), 3), list(x_0))), c.dot(x_0), iter_count
            break
        mu = (musign(min(deltas)))
        l = zeros(len(c))
        l[min_delta_ind] = mu;
        l[J]= -B.dot(A[min_delta_ind]).dot(mu)
        for _l, _J in zip(_l, _J):
            _l = -B.dot(A[min_delta_ind]).dot(mu)

        z = B.dot(A[:, min_delta_ind])
        if not all(_z <= 0 for _z in list(z)):
            print("Нет решений.")
            break
        for j, _z in zip(J, z):
            if _z > 0:
                Theta.append(x_0[j] / _z)
            else:
                Theta.append(inf)
        s = argmin(Theta)  # Theta arg equal Jb arg
        x_0[not_J] = 0
        x_0[min_delta_ind] = min(Theta)
        for index, _z in zip(J, z):
            x_0[index] -= min(Theta) * _z
        J[s] = min_delta_ind
        iter_count += 1
