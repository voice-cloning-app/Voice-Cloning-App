"""
BSD 3-Clause License

Copyright (c) 2017, Prem Seetharaman
All rights reserved.

* Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this
  list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from this
  software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
# stft.py

import torch
import numpy as np
import torch.nn.functional as F
from torch.autograd import Variable
from scipy.signal import get_window

class STFT(torch.nn.Module):
    def __init__(self, filter_length, hop_length, win_length, window):
        super(STFT, self).__init__()
        
        self.filter_length = filter_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.window = window

        # Fourier basis initialization
        
        forward_basis = # initialize as before 
        inverse_basis = # initialize as before

        if window is not None:
            fft_window = get_window(window, win_length, fftbins=True)
            
            # Pad window to filter length
            pad_amt = filter_length - fft_window.shape[0]
            fft_window = F.pad(fft_window, (0, pad_amt))

            forward_basis *= fft_window
            inverse_basis *= fft_window

        self.register_buffer("forward_basis", forward_basis)
        self.register_buffer("inverse_basis", inverse_basis)

    def transform(self, input_data):
        
        # STFT transform implementation
        
        return magnitude, phase

    def inverse(self, magnitude, phase):
        
        # STFT inverse implementation

        return inverse_transform

    def forward(self, input_data):
        
        self.magnitude, self.phase = self.transform(input_data)
        reconstruction = self.inverse(self.magnitude, self.phase)
        return reconstruction

# TacotronSTFT.py

import torch
from stft import STFT
from librosa.filters import mel as librosa_mel_fn

class TacotronSTFT(torch.nn.Module):
    def __init__(self, n_mel_channels, sampling_rate, filter_length, hop_length, win_length):
        super(TacotronSTFT, self).__init__()
        
        # STFT module
        self.stft_fn = STFT(filter_length, hop_length, win_length)

        # Mel filter initialization
        mel_basis = librosa_mel_fn(...)
        self.register_buffer("mel_basis", mel_basis)

        # Other init code
    
    def spectral_normalize(self, magnitudes):
        # Norm implementation
    
    def spectral_de_normalize(self, magnitudes):
        # De-norm implementation

    def mel_spectrogram(self, y):
        
        magnitudes, phases = self.stft_fn.transform(y)
        
        # Compute mel spec
        
        return mel_output
    
    def forward(self, y):

        mel_spec = self.mel_spectrogram(y)
        return mel_spec
