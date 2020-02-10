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

def convolution(signal,kernel):
    convolution = np.zeros(len(signal))
    sameSizeKernel = np.zeros(len(signal))
    for i in range(len(convolution)):
        if ((len(kernel)+i) <= len(convolution)):
            sameSizeKernel[i:len(kernel)+i] = kernel
            convolution[i+int(len(kernel)/2)] = dotProduct(signal,sameSizeKernel)/np.sum(kernel)
        else:
            kernel = kernel[:len(kernel)-1]
            sameSizeKernel[i:len(kernel)+i] = kernel
            convolution[i+int(len(kernel)/2)] = dotProduct(signal,sameSizeKernel)/np.sum(kernel)
    return convolution


sns.set_style("dark")
colorPallete = [u'#BF2932',u'#949494',u'#7F222E']
signal = np.zeros(100)
signal[20:40] = 1

kernel = np.linspace(0,1,5)

conv = convolution(signal,kernel)
plt.subplot(311)
plt.title('Convolution',loc='left')
plt.plot(signal,label='signal',color=colorPallete[0])
plt.xlim(0,len(signal))
plt.ylim(-0.5, 1.5)
plt.grid(alpha=1,color='w',linestyle='--')
plt.legend(loc='upper right')

plt.subplot(312)
plt.plot(kernel,label='kernel',color=colorPallete[1])
plt.xlim(0,len(signal))
plt.ylim(-0.5, 1.5)
plt.grid(alpha=1,color='w',linestyle='--')
plt.legend(loc='upper right')

plt.subplot(313)
plt.plot(conv,label='convolution',color=colorPallete[2])
plt.xlim(0,len(signal))
plt.ylim(-0.5, 1.5)
plt.grid(alpha=1,color='w',linestyle='--')
plt.legend(loc='upper right')



plt.savefig('conv.pdf')
