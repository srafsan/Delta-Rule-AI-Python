th, alpha = .5, .2
delta = []
x1, x2, z = [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 1]
w1, w2, fw1, fw2, Y = [], [], [], [], []
pre_fw1 = .1
pre_fw2 = .3

for step in range(4):
    w1.clear(), w2.clear(), Y.clear(), delta.clear(), fw1.clear(), fw2.clear()
    for i in range(4):
        w1.append(pre_fw1)
        w2.append(pre_fw2)
        if ((x1[i] * w1[i]) + (x2[i] * w2[i])) > th:
            Y.append(1)
        else:
            Y.append(0)
        delta.append(round((float(z[i]) - float(Y[i])), 1))
        fw1.append(round(w1[i] + (alpha * delta[i] * x1[i]), 1))
        fw2.append(round(w2[i] + (alpha * delta[i] * x2[i]), 1))
        pre_fw1 = fw1[i]
        pre_fw2 = fw2[i]
    print("\n")
    print("----Step:", step + 1, "----")
    print("Initial W1:", w1)
    print("Initial W2:", w2)
    print("Y:", Y)
    print("Delta:", delta)
    print("Final W1:", fw1)
    print("Final W2:", fw2