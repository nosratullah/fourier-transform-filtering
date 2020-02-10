import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def dotProduct(a,b):
    dot = 0
    if (len(a) == len(b)):
        for i in range(len(a)):
            dot += a[i] * b[i]
    elif (len(a) > len(b)):
        for i in range(len(b)):
            dot += a[i] * b[i]
    elif (len(b) > len(a)):
        for i in range(len(a)):
            dot += a[i] * b[i]

    return dot

sns.set_style("dark")
colorPallete = [u'#BF2932',u'#949494']
signal = np.zeros(100)
signal[20:40] = 1

kernel = np.linspace(0,1,5)
plt.subplot(311)
plt.title('Convolution',loc='left')
plt.plot(signal,label='signal',color=colorPallete[0])
plt.grid(alpha=1,color='w',linestyle='--')
plt.legend(loc='upper right')

plt.subplot(312)
plt.plot(kernel,label='kernel',color=colorPallete[1])
plt.xlim(0,len(signal))
plt.grid(alpha=1,color='w',linestyle='--')
plt.legend(loc='upper right')



plt.savefig('conv.pdf')
