# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # start_hour:start_minute - end_hour:end_minute
    start_hour = 1
    start_minute = 7
    end_hour = 1
    end_minute = 59

    start_frame = (60 * start_hour + start_minute) * 2 * 30
    end_frame = (60 * end_hour + end_minute) * 2 * 30

    # 帯域が埋まった時間をファイルに出力
    f = open('annotation/16_04_05_annotation.txt', 'w')
    i = start_frame
    while i <= end_frame:
        f.write(str(i) + "\n")
        i += 1
    f.close()
