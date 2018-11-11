import numpy as np
import pandas as pd

kms_otvod_table = pd.read_excel('otvod.xlsx')
col_kms_otvod = kms_otvod_table.columns
kms_otvod_tab = np.array(kms_otvod_table)


def kms_otvod(a, b, angle):
    if angle != 90 and angle != 45:
        return
    row1 = kms_otvod_tab[:, 0]
    a_i = (row1 >= a).argmax()
    b_i = (col_kms_otvod >= b).argmax()
    if angle == 90:
        return kms_otvod_tab[a_i, b_i]
    if angle == 45:
        return kms_otvod_tab[a_i + 1, b_i]


kms_nagn_tr_pr_table = pd.read_excel('nagn_tr_pr.xlsx')
col_kms_nagn_tr_pr = kms_nagn_tr_pr_table.columns
kms_nagn_tr_pr_tab = np.array(kms_nagn_tr_pr_table)


def kms_nagn_tr_pr(i, j):  # i - расх отв/ствол j - пл прох/ствол
    row1 = kms_nagn_tr_pr_tab[:,0]
    i_ind = (abs(row1-i-0.000001)).argmin()
    j_ind = (abs(col_kms_nagn_tr_pr-j-0.01)).argmin()
    return kms_nagn_tr_pr_tab[i_ind, j_ind]


kms_nagn_tr_otv_table = pd.read_excel('nagn_tr_otv.xlsx')
col_kms_nagn_tr_otv = kms_nagn_tr_otv_table.columns
kms_nagn_tr_otv_tab = np.array(kms_nagn_tr_otv_table)


def kms_nagn_tr_otv(i, j):  # i - расх отв/ствол j - пл отв/ствол
    row1 = kms_nagn_tr_otv_tab[:, 0]
    i_ind = (abs(row1-i-0.000001)).argmin()
    j_ind = (abs(col_kms_nagn_tr_otv-j-0.01)).argmin()
    return kms_nagn_tr_otv_tab[i_ind, j_ind]


kms_vs_tr_pr_table = pd.read_excel('vs_tr_pr.xlsx')
col_kms_vs_tr_pr = kms_vs_tr_pr_table.columns
kms_vs_tr_pr_tab = np.array(kms_vs_tr_pr_table)


def kms_vs_tr_pr(i, j, k):  # i - пл прох/ствол j - расх отв/ствол k - пл отв/ствол
    row1 = kms_vs_tr_pr_tab[:, 0]
    row2 = kms_vs_tr_pr_tab[:, 1]
    i_ind = (abs(row1-i-0.0000001)).argmin()
    j_ind = (abs(row2-j-0.0000001)).argmin()
    k_ind = (abs(col_kms_vs_tr_pr-k-0.0000001)).argmin()
    return kms_vs_tr_pr_tab[i_ind + j_ind, k_ind]


kms_vs_tr_otv_table = pd.read_excel('vs_tr_otv.xlsx')
col_kms_vs_tr_otv = kms_vs_tr_otv_table.columns
kms_vs_tr_otv_tab = np.array(kms_vs_tr_otv_table)


def kms_vs_tr_otv(i, j, k):  # i - пл прох/ствол j - расх отв/ствол k - пл отв/ствол
    row1 = kms_vs_tr_otv_tab[:, 0]
    row2 = kms_vs_tr_otv_tab[:, 1]
    i_ind = (abs(row1-i-0.0000001)).argmin()
    j_ind = (abs(row2-j-0.0000001)).argmin()
    k_ind = (abs(col_kms_vs_tr_otv-k-0.0000001)).argmin()
    return kms_vs_tr_otv_tab[i_ind + j_ind, k_ind]
