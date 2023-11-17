#I = [2, 3[ U ]0, 1] U [-10, -2]



x = float(input("Entrez un réel : "))

if (-10 <= x < -2) or (0 < x <= 1) or (2 <= x < 3):
    print("x appartient à I")
else:
    print("x n'appartient pas à I")

