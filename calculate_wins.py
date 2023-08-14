import pandas as pd
import numpy as np
import os


def calculate_wins(df_path):
    # load all historical lottery draws
    df_wins = pd.read_csv("ab 2022.csv").to_numpy()

    df_win_matrix = pd.DataFrame({
        '5 aus 50': [5, 5, 5, 4, 4, 3, 4, 2, 3, 3, 1, 2],
        '2 aus 12': [2, 1, 0, 2, 1, 2, 0, 2, 1, 0, 2, 1],
    })

    win_lists = df_win_matrix.values.tolist()

    win_score = {
        '[5, 2]': 12,
        '[5, 1]': 11,
        '[5, 0]': 10,
        '[4, 2]': 9,
        '[4, 1]': 8,
        '[3, 2]': 7,
        '[4, 0]': 6,
        '[2, 2]': 5,
        '[3, 1]': 4,
        '[3, 0]': 3,
        '[1, 2]': 2,
        '[2, 1]': 1,
    }



    path = os.path.join("all_possibilities", df_path)
    df_tipps = pd.read_csv(path, sep=',')
    df_tipps[['Anzahl', 'Score']] = np.nan

    col_list = df_tipps.columns

    df_tipps = df_tipps.to_numpy()

    for t_series in df_tipps:
        t_50 = set(t_series[:5])
        t_12 = set(t_series[5:7])

        if (len(t_50) != 5) or (len(t_12) != 2):
            continue

        count = 0
        score = 0

        for z_series in df_wins:
            z_50 = set(z_series[1:6])
            z_12 = set(z_series[6:8])

            c_50 = len(t_50.intersection(z_50))
            c_12 = len(t_12.intersection(z_12))

            c_list = list([c_50, c_12])

            if c_list in win_lists:
                count += 1
                score += win_score[str(c_list)]

        t_series[[-2, -1]] = count, score



    df_tipps_temp = pd.DataFrame(df_tipps, columns=col_list)
    # df_tipps_temp.to_csv(os.path.join("alle_Möglichkeiten_mit_score", f"mit_score_{df_path}"), index=None)
    df_tipps_temp.to_csv(os.path.join("all_possibilities", f"mit_score_{df_path}"), index=None)
    os.remove(os.path.join("all_possibilities", df_path))

    del df_tipps_temp
