# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scapy.all import *
import os
from datetime import *
import time
import sys
from entropy import entropy

####################
# 定数
####################
TIME_FRAME = 30  # 分析する時間間隔

####################
# グローバル変数
####################
start_time = 0  # 開始時間
time_count = 0  # 時間フレームのカウンタ
dic_source_ip = defaultdict(int)  # パケット数をカウントする辞書
dic_source_port = defaultdict(int)
dic_protocol = defaultdict(int)

#########################
# グラフプロットする配列
#########################
elapsed_time = []  # 経過時間
# sourceIP
source_ip_var, source_ip_ent = [], []
# sourceポート
source_port_var, source_port_ent = [], []
# プロトコル別
icmp = []  # (1)
ip = []  # (4)
tcp = []  # (6)
udp = []  # (17)
# 全体
all_packets = []


###########################################
# sourceIP毎に分散・エントロピーを計測
# sourceポート毎に分散・エントロピーを計測
# プロトコル毎にパケット数を計測
# 全体のパケット数を計測
###########################################
def packet_analysis(packets):
    global start_time, time_count
    global dic_source_ip, dic_source_port, dic_protocol
    global elapsed_time
    global source_ip_var, source_ip_ent
    global source_port_var, source_port_ent
    global icmp, ip, tcp, udp
    global all_packets
    packet_num = 0

    # 出現回数計測
    for pkt in packets:
        # 開始時間の記録
        if start_time == 0:
            start_time = pkt.time

        # EtherTypeが 0x0800 でないものは無視
        if pkt.type == 2048:
            # TIME_FRAME秒ごとに計測
            if pkt.time - start_time >= TIME_FRAME * time_count:
                # 経過時間
                # elapsed_time.append(pkt.time - start_time)
                elapsed_time.append(pkt.time - start_time)

                # sourceIP分散
                source_ip_var.append(np.var(np.array(dic_source_ip.values())))

                # sourceIPエントロピー
                # 確率分布は出現確率とする
                source_ip_ent.append(entropy(dic_source_ip.values()))

                # sourceポート分散
                source_port_var.append(
                    np.var(np.array(dic_source_port.values())))

                # sourceポートエントロピー
                # 確率分布は出現確率とする
                source_port_ent.append(entropy(dic_source_port.values()))

                # プロトコル
                icmp.append(dic_protocol[1])
                ip.append(dic_protocol[4])
                tcp.append(dic_protocol[6])
                udp.append(dic_protocol[17])

                # 全体パケット数
                all_packets.append(packet_num)

                # カウンタ上げる・辞書リセット
                time_count += 1
                dic_source_ip = defaultdict(int)
                dic_source_port = defaultdict(int)
                dic_packet = defaultdict(int)
                packet_num = 0

            dic_source_ip[pkt['IP'].src] += 1
            if hasattr(pkt['IP'], "sport"):
                dic_source_port[pkt['IP'].sport] += 1
            dic_protocol[pkt['IP'].proto] += 1
            packet_num += 1


if __name__ == "__main__":
    process_start = time.clock()

    # コマンドラインから引数（分析する日）を取得
    argvs = sys.argv
    argc = len(argvs)
    if argc != 2:
        print 'Usage: # python %s analysis_day (01 or 12 or 15_1 etc.)' % argvs[0]
        quit()

    # ディレクトリ下のすべてのpcapファイルを名前順に読み込む
    # dirname = '/home/lab5/inaguma/Documents/ddos/packet-intern/04-' + argvs[1] + '/'
    dirname = '/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/packet_analysis/04-01/'
    filename = [filename for filename in os.listdir(dirname)]
    filename.sort()
    print dirname

    # pcapファイルの読み込み
    for i in range(len(filename)):
        if filename[i] != ".DS_Store":
            print filename[i]
            with PcapReader(dirname + filename[i]) as packets:
                packet_analysis(packets)

    # 分析内容をファイルに出力
    # 経過時間, sourceIPのvar, ent,
    # icmp, ip, tcp, udp, all_packets
    f = open('16_04_' + argvs[1] + '.txt', 'w')
    for i in range(len(elapsed_time)):
        f.write(str(elapsed_time[i]) + "," + str(source_ip_var[i]) + "," + str(source_ip_ent[i]) + "," + str(source_port_var[i]) + "," + str(
            source_port_ent[i]) + "," + str(icmp[i]) + "," + str(ip[i]) + "," + str(tcp[i]) + "," + str(udp[i]) + "," + str(all_packets[i]) + "\n")
    f.close()

    process_time = time.clock() - process_start
    print "実行時間：%d" % process_time
