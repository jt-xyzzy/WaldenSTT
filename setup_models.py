import os
from pywhispercpp.model import Model

f = "test.wav"

tiny_model = Model(
    model="tiny",
    models_dir="MODELS",
    params_sampling_strategy=0,
    redirect_whispercpp_logs_to=False
)
turbo_model = Model(
model="large-v3-turbo",
models_dir="MODELS",
params_sampling_strategy=0,
redirect_whispercpp_logs_to=False
)

def download_models(x):
    segments = x.transcribe(f)
    for segment in segments:
        print(segment.text)

os.system("clear")

print("Testing download of tiny model...")
try:
    download_models(tiny_model)
    print("downloaded tiny model successfully")
except:
    print("Problem occurred while downloading tiny model")
download_models(basic)
print("")

print("Testing download of turbo model...")
try:
    download_models(turbo_model)
    print("downloaded turbo model successfully")
except:
    print("Problem occurred while downloading baseline model")

print("\nSetup complete. Enjoy WaldenSTT Turbo!")
