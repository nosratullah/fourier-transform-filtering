# fourier-transform-filtering
## Fourier-transform:

Fourier transform is basically the same thing as convolution is, but with only a few differences.
Instead of the simple line kernel, in Fourier transform the kernel is a sin wave with a specific frequency
Instead of just only one kernel, in Fourier transform we use many kernels (sine waves with different frequencies) to cover a range of frequencies.

<img src="https://miro.medium.com/max/4732/1*4vLPVnMgHcGILkBDuXJBiQ.png">

The above figure is just a simple convolution to show how Fourier-transform works, but to get precise result we have to consider technical details and calculate the convolution of a much wider range of sin waves with different frequencies.
The focus of this post is on filtering frequencies and why we need it. And I’m sure you can find dozens of good tutorials on how to take Fourier transform of your data/signals. here is a good source to find out more:
https://towardsdatascience.com/fast-fourier-transform-937926e591cb
