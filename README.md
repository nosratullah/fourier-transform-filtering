# fourier-transform-filtering
## Fourier-transform:

Fourier transform is basically the same thing as convolution is, but with only a few differences.
Instead of the simple line kernel, in Fourier transform the kernel is a sin wave with a specific frequency
Instead of just only one kernel, in Fourier transform we use many kernels (sine waves with different frequencies) to cover a range of frequencies.

<img src="https://miro.medium.com/max/4732/1*4vLPVnMgHcGILkBDuXJBiQ.png">

The above figure is just a simple convolution to show how Fourier-transform works, but to get precise result we have to consider technical details and calculate the convolution of a much wider range of sin waves with different frequencies.
The focus of this post is on filtering frequencies and why we need it. And I’m sure you can find dozens of good tutorials on how to take Fourier transform of your data/signals. here is a good source to find out more:
https://towardsdatascience.com/fast-fourier-transform-937926e591cb

## Filtering:
Having multiple sin waves creating one signal is common when you deal with signals. For instance, while your brain does a task, different regions in your brain working together to achieve that task. Those different areas of your brain are usually oscillating in different frequencies and the result of it creates a complicated signal which you see in the EEG signal.
As a neuroscience student, I have to consider these cooperations and to study only one area of the brain, I may need to filter out other sources. But these technic has a wide application in telecommunication, smoothing data by sub-pressing noises and in general studying any time-series which has periodic sources as well. Talking of noise, as we saw above the convolution of a simple line shape kernel with a signal also smooth the signal and remove the sharp edges of the signal. But convolution is not the best method of reducing the noise when it comes to perfection.
<img src="https://miro.medium.com/max/4984/1*A5sQQLqezMgUEAxxzgv81g.png">
