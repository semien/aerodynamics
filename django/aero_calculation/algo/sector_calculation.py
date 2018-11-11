import numpy as np
import pandas as pd


def calculate(sections, filename):
    table1 = pd.read_excel('aero_calculation/tables/table1.xlsx')
    col1 = table1.columns
    t1 = np.array(table1)

    table2 = pd.read_excel('aero_calculation/tables/table2.xlsx')
    col2 = table2.columns
    t2 = np.array(table2)

    table3 = pd.read_excel('aero_calculation/tables/table3.xlsx')
    col3 = table3.columns
    t3 = np.array(table3)

    def interpol2_3(d_e, v_f):
        def find6i(d_e):
            if col2.contains(d_e):
                a = (col2 == d_e).argmax()
                return a, a, 1
            else:
                a = (col2 > d_e).argmax()
                kf = (d_e - col2[a - 1]) / (col2[a] - col2[a - 1])
                return a - 1, a, kf

        def find6j(v_f):
            row1 = t2[:, 0]
            if (row1 == v_f).max() == True:
                a = (row1 == v_f).argmax() + 2
                return a, a, 1
            else:
                a = (row1 > v_f).argmax() + 2
                kf = (v_f - row1[a - 3]) / (row1[a] - row1[a - 3])
                return a - 3, a, kf

        i_1, i_2, ki = find6i(d_e)
        j_1, j_2, kj = find6j(v_f)
        A = (1 - ki) * (1 - kj) * t2[j_1, i_1]
        B = (1 - kj) * ki * t2[j_1, i_2]
        C = kj * (1 - ki) * t2[j_2, i_1]
        D = ki * kj * t2[j_2, i_2]
        return A + B + C + D

    def interpol3(K, v_f):
        def find7i(K):
            if col3.contains(K):
                a = (col3 == K).argmax()
                return a, a, 1
            else:
                a = (col3 > K).argmax()
                kf = (K - col3[a - 1]) / (col3[a] - col3[a - 1])
                return a - 1, a, kf

        def find7j(v_f):
            row1 = t3[:, 0]
            if (row1 == v_f).max() == True:
                a = (row1 == v_f).argmax()
                return a, a, 1
            else:
                a = (row1 > v_f).argmax()
                kf = (v_f - row1[a - 1]) / (row1[a] - row1[a - 1])
                return a - 1, a, kf

        i_1, i_2, ki = find7i(K)
        j_1, j_2, kj = find7j(v_f)
        A = (1 - ki) * (1 - kj) * t3[j_1, i_1]
        B = (1 - kj) * ki * t3[j_1, i_2]
        C = kj * (1 - ki) * t3[j_2, i_1]
        D = ki * kj * t3[j_2, i_2]
        return A + B + C + D

    def sector_calculation(t_v, c, l, v, K):
        F = c / (3600 * v)  # 1
        near_F = (abs(t1[:, 2] - F)).argmin()  # 2
        a, b, F_n = t1[near_F]  # 3
        v_f = c / (3600 * F_n)  # 4
        d_e = 2 * a * b / (a + b)  # 5
        R = interpol2_3(d_e, v_f)  # 6
        B = interpol3(K, v_f)  # 7
        Ptr = l * R * B  # 8
        Pt = 1.2 * 293 / (273 + t_v)  # 9
        Pg = Pt * (v_f ** 2) / 2  # 10
        return [a, b, d_e, F, F_n, v_f, R, B, Ptr, Pt, Pg]

    answ_columns = ['a', 'b', 'd_e', 'F', 'F_n', 'v_f', 'R', 'B', 'P_tr', 'P_t', 'P_g']
    answers = []

    for section in sections:
        t_v = float(section.temperature)
        c = float(section.consumption)
        l = float(section.length)
        v = float(section.recommended_speed)
        K = float(section.coeff_roughness)
        answ = sector_calculation(t_v, c, l, v, K)
        answers += [answ]

    n = len(answers)
    df = pd.DataFrame(data=answers, columns=answ_columns, index=np.arange(1, n + 1))
    df.to_excel('aero_calculation/tmpfiles/'+filename)
