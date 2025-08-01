# WaldenSTT

WaldenSTT is a graphical interface for [absadiki's pywhispercpp](https://github.com/absadiki/pywhispercpp/), a speech to text tool
which itself is built on  [whisper.cpp](https://github.com/ggerganov/whisper.cpp)

WaldenSTT was created by JT for the folks at CiTR to make it easier to autogenerate text transcriptions of podcasts.

# Quick Start

## Install WaldenSTT

```
bash setup.sh
```

OR

```
python3 -m venv venv
source venv/bin/activate
pip install pywhispercpp
python3 setup_models.py
```

## Run the program:

```
bash WaldenSTT.sh
```

or run the WaldenSTT.sh program as an executable.

## Instructions

You might need to install pip. To do that, follow the instructions on python.org:
https://packaging.python.org/en/latest/tutorials/installing-packages/

Next, you need to insitall the pywhispercpp package.

## pywhispercpp Installation

### Via Pip

* Basic pre-built version available using pip

```shell
pip install pywhispercpp
```

### From source

* For the best performance, you need to install the package from source:
  
  ```shell
  pip install git+https://github.com/absadiki/pywhispercpp
  ```

### License

WaldenSTT and pywhispercpp are under the same license as [whisper.cpp](https://github.com/ggerganov/whisper.cpp/blob/master/LICENSE) (MIT  [License](./LICENSE)).

### Resources

More info on [available-models-and-languages](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages) from open github.com/openai/whisper