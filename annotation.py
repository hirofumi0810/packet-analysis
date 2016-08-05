# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # 攻撃時間をアノテーション（[開始時間(時),開始時間(分),継続時間(分)]）
    attacked_time = [[1, 7, 52], [8, 5, 47], [
        10, 22, 52], [14, 27, 4], [6, 33, 2], [0, 37, 1], [10, 5, 14]]

    # 攻撃を受けた日
    attacked_days = ['05', '09', '13', '17', '18', '20', '28']

    for i in range(len(attacked_time)):
        start_frame = (60 * attacked_time[i][0] + attacked_time[i][1]) * 60
        end_frame = start_frame + attacked_time[i][2] * 60

        # 帯域が埋まった時間をファイルに出力
        f = open('annotation/16_04_' +
                 attacked_days[i] + '_annotation.txt', 'w')
        i = start_frame
        while i <= end_frame:
            f.write(str(i) + "\n")
            i += 1
        f.close()
