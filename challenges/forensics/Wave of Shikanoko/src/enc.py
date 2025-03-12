import wave
song = wave.open("flag.wav", mode='rb')
frame_bytes = bytearray(list(song.readframes(song.getnframes())))

string='YCEP25{Sh1kan0k0_1s_W4v1ng}'
string = string + int((len(frame_bytes)-(len(string)*8*8))/8) *'#'
bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in string])))

for i, bit in enumerate(bits):
    frame_bytes[i] = (frame_bytes[i] & 254) | bit
frame_modified = bytes(frame_bytes)

with wave.open('song_embedded.wav', 'wb') as fd:
    fd.setparams(song.getparams())
    fd.writeframes(frame_modified)
song.close()