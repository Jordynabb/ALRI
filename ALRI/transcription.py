
class Transcription:

    def __init__(self):
        self.ID = None
        self.transcriber_name = None
        self.date = None
        self.cleaned_text_clown = None
        self.cleaned_text_ghost = None

    #Methods
    def extract_transcript_ID(self, text): #obtain id from file
        
        #file.seek(0)
        original_text = text

        substring = "Session ID: "
        for line in text.split("\n"):
            print("A")
            if(substring in line):
                print("B") # Never even Gets here
                return line.replace(substring, "").strip()   
        text = original_text 
        return None;   
        
    def extract_transcriber_name(self, file): #obtain transcriber name from file

        file.seek(0)
        substring = "Transcriber: "
        line = file.readline()
        return line.replace(substring, "").strip()
        
    def extract_transcript_date(self, file): #obtain transcriber date from file

        file.seek(0)
        substring = "Transcription date: "
        line = file.readline()
        while(line):
            if(substring in line):
                return line.replace(substring, "").strip()
            line = file.readline()

    #set object values
    def set_transcript_ID(self, text):
        self.ID = self.extract_transcript_ID(text)
        #print("Testing class method:", self.ID)

    def set_transcriber_name(self, file):
        self.transcriber_name = self.extract_transcriber_name(file)

    def set_transcript_date(self, file):
        self.date = self.extract_transcript_date(file)

    def set_cleaned_text(self, clown_text, ghost_text):
        self.cleaned_text_clown = clown_text
        self.cleaned_text_ghost = ghost_text



class Transcription_manager:  
    #method for interacting with the dictionary of transcriptions

    #global dictionary for storing transcriptions
    transcriptions = {}
    size = 0

    def add_transcription(self, transcription):
        if(transcription.ID in Transcription_manager.transcriptions):
            raise ValueError("transcription already stored")
        else:
            Transcription_manager.transcriptions[transcription.ID] = transcription
            Transcription_manager.size += 1

    def remove_transcription(self, transcription):
        if(transcription.ID not in Transcription_manager.transcriptions):
            raise ValueError("transcription not found")
        else:
            del Transcription_manager.transcriptions[transcription.ID]
            Transcription_manager.size -= 1

    def search_transcription(self, transcription):
        if(transcription.ID in Transcription_manager.transcriptions):
            print("FOUND")
        else:
            raise ValueError("transcription not found")
   
    def clear_all(self):
        Transcription_manager.transcriptions.clear()
        Transcription_manager.size = 0

    def print_all(self):
        if Transcription_manager.size != 0:
            for transcription in Transcription_manager.transcriptions.values():
                print(transcription.ID, transcription.transcriber_name)
        else:
            raise ValueError("No stored transcriptions")
    
    def show_text(self, transcription):
        print(transcription.transcriber_name, "-", transcription.ID, ": ")
        print("cleaned text (clown):", transcription.cleaned_text_clown)
        print("cleaned text (ghost):", transcription.cleaned_text_ghost, "\n")

    def show_all_text(self):
        if Transcription_manager.size != 0:
            for transcription in Transcription_manager.transcriptions.values():
                self.show_text(transcription)
        else:   
            raise ValueError("No stored transcriptions")
