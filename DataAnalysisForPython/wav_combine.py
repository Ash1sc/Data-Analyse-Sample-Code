
import os
import soundfile as sf
import numpy as np

# 定义转换采样率的函数，接收3个变量：原音频路径、重新采样后的音频存储路径、目标采样率


def wav_concatenate(path_1, path_2, new_dir_path):
    wavfile_1 = path_1.split('/')[-1]  # 提取音频1的文件名，如“1.wav"
    wavfile_2 = path_2.split('/')[-1]  # 提取音频2的文件名，如“2.wav"
    new_file_name = wavfile_1.split('.')[0] + '_' + wavfile_2.split('.')[0] + \
        '.wav'  # 此行代码用于对拼接后的文件进行重命名，此处是将需要拼接的两个文件名用'_'连接起来

    signal_1, sr1 = sf.read(path_1)  # 调用soundfile载入音频
    signal_2, sr2 = sf.read(path_2)  # 调用soundfile载入音频

    if sr1 == sr2:  # 判断待拼接的两则音频采样率是否一致，若一致则拼接
        new_signal = np.concatenate((signal_1, signal_2), axis=0)
        new_path = os.path.join(new_dir_path, new_file_name)
        print(new_path)

        sf.write(new_path, new_signal, sr1)

    else:
        print("所需拼接的音频采样率不一致，需检查一下哈~")


if __name__ == '__main__':
    path_1 = 'D:/拼接测试/今天的天气是.wav'  # 指定通用的拼接音频文件
    dir_path = "D:/拼接测试/待拼接文件夹/"  # 指定待拼接的音频文件夹路径
    wav_list = os.listdir(dir_path)

    # 指定转换后的音频文件夹路径
    new_dir_path = "D:/拼接测试/已拼接文件夹/"  # 指定拼接完成后，存储音频的文件夹路径
    os.makedirs(new_dir_path, exist_ok=True)

    # 开始以对原音频文件夹内的音频进行“一对多”的批量拼接
    for i in wav_list:
        path_2 = os.path.join(dir_path, i)
        wav_concatenate(path_1, path_2, new_dir_path)
