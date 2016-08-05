# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import os


def plot_source_ip_ent(dirname, filename):
    """
    source IPアドレスのエントロピーのグラフをプロット
    """

    # テキストファイルの読み込み
    f = open(dirname + filename)
    lines = f.readlines()
    f.close()

    # カンマ区切りで分割
    elapsed_time = [float(line.split(",")[0]) for line in lines]
    source_ip_ent = [float(line.split(",")[2]) for line in lines]

    # グラフプロット
    plt.clf()
    plt.plot(elapsed_time, source_ip_ent, color='g')
    plt.xlim([0, max(elapsed_time)])
    plt.xlabel('Time [sec]', size=15)
    plt.ylabel('Entropy', size=15)
    plt.xticks([3600, 3600 * 2, 3600 * 3, 3600 * 4, 3600 * 5, 3600 * 6, 3600 * 7, 3600 * 8, 3600 * 9, 3600 * 10, 3600 * 11, 3600 * 12,  3600 * 13, 3600 * 14, 3600 * 15, 3600 * 16, 3600 * 17, 3600 * 18, 3600 *
                19, 3600 * 20, 3600 * 21, 3600 * 22, 3600 * 23, 3600 * 24], ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"])
    plt.grid(True)
    plt.title('Entropy of source IP (' + filename.split(".")[0] + ')')
    plt.savefig("graph/source_ip_ent/source_ip_ent_" +
                filename.split(".")[0] + ".png", format='png', dpi=200)
    # plt.show()


def hist_source_ip_ent(dirname, filename):
    """
    source IPアドレスのエントロピーのグヒストグラムをプロット
    """

    # テキストファイルの読み込み
    f = open(dirname + filename)
    lines = f.readlines()
    f.close()

    # カンマ区切りで分割
    elapsed_time = [float(line.split(",")[0]) for line in lines]
    source_ip_ent = [float(line.split(",")[2]) for line in lines]

    # ヒストグラム
    plt.clf()
    plt.hist(source_ip_ent, bins=40, color='g')
    plt.xlabel('Entropy', size=15)
    plt.ylabel('Frame Number', size=15)
    plt.grid(True)
    plt.title('Histgram of entropy of source IP (' +
              filename.split(".")[0] + ')')
    plt.savefig("graph/hist_source_ip_ent/hist_source_ip_ent_" +
                filename.split(".")[0] + ".png", format='png', dpi=200)
    # plt.show()


if __name__ == "__main__":
    # ディレクトリ下のすべてのpcapファイルを名前順に読み込む
    dirname = 'analyzed_data/'
    filename = [filename for filename in os.listdir(dirname)]
    filename.sort()

    for i in range(len(filename)):
        if filename[i] != ".DS_Store":
            plot_source_ip_ent(dirname, filename[i])
            hist_source_ip_ent(dirname, filename[i])
