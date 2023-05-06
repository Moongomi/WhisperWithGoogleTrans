# WhisperWithGoogleTrans

I added a function to request the translation of SRT files that come out after converting voice to text using Whisper AI.

## Requirement

* Python 3.8-3.10
* ffmpeg
* pysrt
* googletrans

You can download and install (or update to) the latest release of Whisper with the following command:

    pip install -U openai-whisper

Alternatively, the following command will pull and install the latest commit from this repository, along with its Python dependencies:

    pip install git+https://github.com/openai/whisper.git 

To update the package to the latest version of this repository, please run:

    pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

It also requires the command-line tool [`ffmpeg`](https://ffmpeg.org/) to be installed on your system, which is available from most package managers:

```bash
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

To install the package to the pysrt please run:

    pip install pysrt

To install the package to the googletrans please run:

    pip install googletrans==4.0.0rc1

You may need [`rust`](http://rust-lang.org) installed as well, in case [tiktoken](https://github.com/openai/tiktoken) does not provide a pre-built wheel for your platform. If you see installation errors during the `pip install` command above, please follow the [Getting started page](https://www.rust-lang.org/learn/get-started) to install Rust development environment. Additionally, you may need to configure the `PATH` environment variable, e.g. `export PATH="$HOME/.cargo/bin:$PATH"`. If the installation fails with `No module named 'setuptools_rust'`, you need to install `setuptools_rust`, e.g. by running:

```bash
pip install setuptools-rust
```


## Command-line usage

change directory:

    cd whispertranslate

The following command will transcribe speech in audio files, using the `medium` model:

    python cli.py audio.flac audio.mp3 audio.wav --model medium

The default setting (which selects the `small` model) works well for transcribing English. To transcribe an audio file containing non-English speech, you can specify the language using the `--language` option:

    python cli.py japanese.wav --language Japanese

See [tokenizer.py](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py) for the list of all available languages.   
   
Adding `--translang language` will translate the speech into language:

    python cli.py japanese.wav --language Japanese --translang ko

See [googletrans](https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages) for the list of all available translate languages.   

You can use --dualsrt [Y/N] to create subtitles for original and translated words at the same time. (For Y), if you select the option of N, a separate srt file of the original and the srt file of the translation will be created.

    python cli.py japanese.wav --language Japanese --translang ko --dualsrt Y

Run the following to view all available options:

    python cli.py --help


## Available models and languages

There are five model sizes, four with English-only versions, offering speed and accuracy tradeoffs. Below are the names of the available models and their approximate memory requirements and relative speed. 


|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

The `.en` models for English-only applications tend to perform better, especially for the `tiny.en` and `base.en` models. We observed that the difference becomes less significant for the `small.en` and `medium.en` models.
