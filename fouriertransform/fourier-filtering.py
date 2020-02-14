# Libraries you'll need for this process:
import numpy as np
import pandas as pd
from scipy.signal import find_peaks,blackman
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import seaborn as sns

def sigmoid(len):
    x = np.linspace(-6,+6,len)
    y = 1/(1 + np.exp(-x))
    return -y + 1

def filtering(signal, range=20, type = 'gaussian'):
    N = signal.size
    # sampling rate
    T = 1.0 / 1000.0
    time_domain = np.linspace(0, 1 / (2*T), N-1)
    signal_fft = fft(signal)
    signal_fft = signal_fft[1:N]
    signal_fft_abs = np.abs(signal_fft[:N//2])
    fft_peak = np.argmax(signal_fft_abs)
    #fft_peak = 400
    if (type == 'gaussian'):
        blackman_ = blackman(2*range)
        sameSizeKernel = np.zeros(len(signal_fft))
        sameSizeKernel[fft_peak-range:fft_peak+range] = blackman_
    if ( type == 'lowpass'):
        sigmoid_ = sigmoid(2*range)
        sameSizeKernel = np.ones(len(signal_fft))
        sameSizeKernel[fft_peak:fft_peak+len(sigmoid_)] = sigmoid_
        sameSizeKernel[fft_peak+len(sigmoid_):] = 0

    filtered = np.multiply(sameSizeKernel,signal_fft.real)

    #filtered[:fft_peak-range] = 0
    #filtered[fft_peak+range:] = 0
    inverse_signal = ifft(filtered)
    #fft = np.abs(fft[0:N//2])
    return inverse_signal.real

data = pd.read_csv('/Users/nosratullah/Documents/Lectures/iasbs/season 5/Medium/furier-filtering/lfp.csv')
lfp = np.array(data['ex_lfp'])
lfp_gaussian_filtered = filtering(lfp, 300, 'gaussian')
lfp_lowpass_filtered = filtering(lfp, 300, 'lowpass')

#Plotting part
sns.set_style("dark")
colorPallete = [u'#BF2932',u'#949494',u'#7F222E']
plt.figure(figsize=(20,8))

plt.subplot(311)
plt.title('Fourier-transform filtering',loc='left')
plt.plot(lfp[2500:3000], color=colorPallete[0],label='Raw Signal')
plt.ylabel('mV')
plt.legend(loc='upper right')
plt.grid(alpha=1,color='w',linestyle='--')
plt.subplot(312)
plt.ylabel('mV')
plt.plot(lfp_gaussian_filtered[2500:3000],color=colorPallete[1],label='With bandpass filter')
plt.legend(loc='upper right')
plt.grid(alpha=1,color='w',linestyle='--')
plt.subplot(313)
plt.ylabel('mV')
plt.xlabel('time (ms)')
plt.plot(lfp_lowpass_filtered[2500:3000],color=colorPallete[1],label='With lowpass filter')
plt.legend(loc='upper right')
plt.grid(alpha=1,color='w',linestyle='--')
plt.savefig('final_plot.png')
#plt.show()
