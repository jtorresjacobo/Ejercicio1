from pydub import AudioSegment

def speed_change(sound,speed,destino):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    slow_sound=sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
    slow_sound.export(destino,format="wav")

    # convert the sound with altered frame rate to a standard frame rate
    # so that regular playback programs will work right. They often only
    # know how to play audio at standard frame rate (like 44.1k)
