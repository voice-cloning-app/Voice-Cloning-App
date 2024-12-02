# Synthesising the voice
With trained model weights we can now implement the TTS app for our generated voice model.

## Arguments
- **model_path**: The path to your generated model
- **vocoder_model_path**: The path to your vocoder model ([default hifigan model found here](https://archive.org/download/voice-cloning-app-hifigan/pretrained/UNIVERSAL_V1/g_02500000))
- **hifigan_config_path**: The path to your hifigan config ([default hifigan config found here](https://archive.org/download/voice-cloning-app-hifigan/pretrained/UNIVERSAL_V1/config.json))
- **text**: Text you wish to synthesize
- **graph_output_path (optional)**: Path to save alignment graph to
- **audio_output_path (optional)**: Path to save generated audio to
- **silence_padding (optional)** : Seconds of silence to seperate each clip by with multi-line synthesis (default is 0.15)
- **sample_rate (optional)** : Audio sample rate (default is 22050)
- **max_decoder_steps (optional)** : Max decoder steps controls sequence length and memory usage during inference. Increasing this will use more memory but may allow for longer sentences. (default is 1000)

## How to run
`python synthesize.py -m checkpoint_500000 -vm g_02500000 -hc config.json -t "Hello everyone, how are you?" -g graph.png -a audio.wav`
