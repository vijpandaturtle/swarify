# Music Practice App
Building a music practice app for indian music

## Dependencies 
1. Tensorflow/Keras 
2. Fluidsynth 
3. Magenta 
4. PyFluidsynth

## Features 
- Setting of tempo according to kalams 
- Octaves from below pa to above pa 
- Choosing ragas 
- 1 note - generate random notes (specified length)
- 2 notes - random/alankars 
- 3 notes - random/alankars 
- 4 notes - random/alankars
- 5 notes - random/alankars
- 6 notes - random/alankars
- 7 notes - random/alankars 
- Combo of different note patterns 
(depends on time signature)
- Transcription and creation of new data for learning rules and flow of a raga 
- Singing analysis 

 
Programmatic generation of paltas 
Random/Freestyle generation requires more data

eg 
set of notes
aro = [SRGMPDNS]
avro = [SNDPMGRS]

class Alankar:
	def __init__(self, aro, avro):
		self.aro = aro
		self.avro = avro 
	def ascending(self, aro):


def ascending(aro, pattern_no):
	for i in range(pattern_no):
		 
