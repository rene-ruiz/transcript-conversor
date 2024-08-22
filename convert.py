import json

with open('transcript.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

transcript_data = data['data']

dialogue_sequence = []

for segment in transcript_data:
    for word_info in segment:
        speaker = word_info['speaker']
        word = word_info['word']
        if len(dialogue_sequence) == 0 or dialogue_sequence[-1]['speaker'] != speaker:
            dialogue_sequence.append({'speaker': speaker, 'words': [word]})
        else:
            dialogue_sequence[-1]['words'].append(word)

transcript_text = ""
for entry in dialogue_sequence:
    speaker = entry['speaker']
    sentence = ' '.join(entry['words'])
    transcript_text += f"{speaker}: {sentence}\n\n"


with open('transcript.txt', 'w', encoding='utf-8') as file:
    file.write(transcript_text)
