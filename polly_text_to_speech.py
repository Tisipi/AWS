import boto3

print("Convert text to speech")

polly = boto3.client("polly")
voice_output = polly.synthesize_speech(
    Text="Hi Mister Tisipi!", OutputFormat="mp3", VoiceId="Brian"
)
audio = voice_output["AudioStream"].read()
with open("audio.mp3", "wb") as file:
    file.write(audio)
