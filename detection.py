# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

precisions, recalls, f_measures = [], [], []
threshold_start = 0
threshold_end = 10
threshold = 3


def detection_grid(filename, annotation):
    # テキストファイルの読み込み（分析データ）
    f = open(filename)
    lines = f.readlines()
    f.close()

    # カンマ区切りで分割
    elapsed_time = [float(line.split(",")[0]) for line in lines]
    source_ip_ent = [float(line.split(",")[2]) for line in lines]
    # source_port_ent = [float(line.split(",")[4]) for line in lines]

    # テキストファイルの読み込み（アノテーションデータ）
    f = open(annotation)
    lines = f.readlines()
    f.close()
    attacked_time = [int(line) for line in lines]
    # print attacked_time

    global precisions, recalls, f_measures
    global threshold_start
    global threshold_end
    precisions_day, recalls_day, f_measures_day = [], [], []

    for i in xrange((threshold_end - threshold_start) * 10):
        tp, tn, fp, fn = 0, 0, 0, 0

        for (time, ent) in zip(elapsed_time, source_ip_ent):
            # for (time, ent) in zip(elapsed_time, source_port_ent):
            # 閾値を超えたら（下回ったら）攻撃と判断
            if ent > threshold_start + i * 0.1:
                # if ent < threshold_start + i * 0.1:
                # print time
                # 本当に攻撃
                if time in attacked_time:
                    tp += 1
                # 正常を攻撃とミス
                else:
                    fp += 1
            # 正常と判断
            else:
                # 攻撃を正常とミス
                if time in attacked_time:
                    fn += 1
                # 本当に正常
                else:
                    tn += 1

        # 精度を計算
        precision = float(tp) / (tp + fn) if (tp + fn) != 0 else 0
        recall = float(tp) / (tp + fp) if (tp + fp) != 0 else 0
        f_measure = float(2 * precision * recall) / (precision +
                                                     recall) if (precision + recall) != 0 else 0
        precisions_day.append(precision)
        recalls_day.append(recall)
        f_measures_day.append(f_measure)

    precisions.append(precisions_day)
    recalls.append(recalls_day)
    f_measures.append(f_measures_day)


def detection(filename, annotation):
    # テキストファイルの読み込み（分析データ）
    f = open(filename)
    lines = f.readlines()
    f.close()

    # カンマ区切りで分割
    elapsed_time = [float(line.split(",")[0]) for line in lines]
    # source_ip_ent = [float(line.split(",")[2]) for line in lines]
    source_port_ent = [float(line.split(",")[4]) for line in lines]

    # テキストファイルの読み込み（アノテーションデータ）
    f = open(annotation)
    lines = f.readlines()
    f.close()
    attacked_time = [int(line) for line in lines]
    # print attacked_time

    global threshold
    tp, tn, fp, fn = 0, 0, 0, 0

    # for (time, ent) in zip(elapsed_time, source_ip_ent):
    for (time, ent) in zip(elapsed_time, source_port_ent):
        # 閾値を超えたら（下回ったら）攻撃と判断
        # if ent > threshold:
        if ent < threshold:
            # print time
            # 本当に攻撃
            if time in attacked_time:
                tp += 1
            # 正常を攻撃とミス
            else:
                fp += 1
        # 正常と判断
        else:
            # 攻撃を正常とミス
            if time in attacked_time:
                fn += 1
            # 本当に正常
            else:
                tn += 1

    # 精度を計算
    precision = float(tp) / (tp + fn) if (tp + fn) != 0 else 0
    recall = float(tp) / (tp + fp) if (tp + fp) != 0 else 0
    f_measure = float(2 * precision * recall) / (precision +
                                                 recall) if (precision + recall) != 0 else 0

    print filename
    print "precision:%f" % precision
    print "recall:%f" % recall
    print "f_measure:%s" % f_measure


if __name__ == "__main__":
    days = ['05', '09', '13', '17', '18', '20', '28']

    for day in days:
        filename = 'analyzed_data/16_04_' + day + '.txt'
        annotation = 'annotation/16_04_' + day + '_annotation.txt'
        # detection_grid(filename, annotation)
        detection(filename, annotation)

    # グラフプロット
    # thresholds = [threshold_start + i *
    #               0.1 for i in xrange(len(f_measures[0]))]
    # for i in xrange(len(days)):
    #     plt.plot(thresholds, f_measures[i], label='04/' + days[i])
    # plt.xlabel('Threshold of entropy', size=15)
    # plt.ylabel('F-measure', size=15)
    # plt.grid(True)
    # plt.legend(loc='upper left')
    # plt.title('F-measure (Entropy of source IP address)')
    # plt.savefig("../graph/accuracy/f_measures_ip.png", format='png', dpi=200)
    # plt.title('F-measure (Entropy of source port number)')
    # plt.savefig("../graph/accuracy/f_measures_port.png", format='png', dpi=200)
    # plt.show()
