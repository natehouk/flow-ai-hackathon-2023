import requests
import wave
import os
    
def extract_audio(input_path,output_file,nseconds,pos=0):
     with wave.open(input_path, 'rb') as wav_file:
        params = wav_file.getparams()
        total_frames = params.nframes
        frame_rate = params.framerate
        total_length = total_frames / (frame_rate)
        num_frames = frame_rate * nseconds
    
        print(total_frames,total_length)
        if pos < total_frames:
            wav_file.setpos(pos)
            current_pos = pos + (nseconds*frame_rate)
            frames = wav_file.readframes(num_frames)
            
            with wave.open(output_file, 'wb') as output_wav:
                output_wav.setparams(params)
                
                output_wav.writeframes(frames)

            whisper_api_key = os.environ.get("WHISPER_API_KEY")
            url = "https://transcribe.whisperapi.com"
            headers = {
            'Authorization': f"Bearer {whisper_api_key}", 
            }
            file = {'file': open(output_file, 'rb')}

            data = {
              "diarization": "false",
              "initialPrompt": "",
              "task": "transcribe", #default is transcribe. Other option is "translate"
            }

            response = requests.post(url, headers=headers, files=file, data=data)
            # import time
            # from datetime import datetime
            # print(response.json())
            if current_pos >= total_frames:
                # return f"text-{datetime.now()}",current_pos, True
                return response.json()["text"], current_pos, True    
            return response.json()["text"], current_pos, False
            # return f"text-{datetime.now()}",current_pos, False
        else:
            # change later
            return False,pos, False

#extract_audio("/Users/sarvesh/Sarvesh/Code/textstreaming/whisper/input-data.wav","/Users/sarvesh/Sarvesh/Code/textstreaming/whisper/output.wav",30)

