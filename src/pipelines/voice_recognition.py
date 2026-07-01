from resemblyzer import VoiceEncoder, preprocess_wav 

import numpy as np 
import io
import librosa
import streamlit as st 

# =============================================================================
# Librosa
# =============================================================================
# Librosa is a Python library used for audio processing and analysis.
#
# In this project, Librosa is responsible for loading and preprocessing audio.
#
# Main responsibilities:
# • Load audio files (.wav, .mp3, etc.)
# • Convert audio into a numerical waveform (NumPy array)
# • Resample audio to a fixed sampling rate (e.g., 16000 Hz)
# • Convert stereo audio into mono if required
# • Perform audio feature extraction (MFCC, Spectrogram, Chroma, etc.)
#
# Think of Librosa as the "Audio Preprocessing Library".
#
# Example:
# waveform, sample_rate = librosa.load("audio.wav", sr=16000)
#
# Output:
# waveform     -> NumPy array containing the audio samples
# sample_rate  -> Number of samples per second (e.g., 16000 Hz)
# =============================================================================


# =============================================================================
# Resemblyzer
# =============================================================================
# Resemblyzer is a deep learning library specifically designed for speaker
# recognition and speaker verification.
#
# It uses a pretrained neural network (Voice Encoder) to convert a person's
# voice into a fixed-length numerical representation called a Speaker Embedding.
#
# Main responsibilities:
# • Extract speaker embeddings from audio
# • Identify speakers from stored voice embeddings
#
# Think of Resemblyzer as the "Speaker Feature Extractor".
#
# Workflow:
# Audio (.wav)
#        │
#        ▼
#   Resemblyzer Voice Encoder
#        │
#        ▼
# Speaker Embedding (256-dimensional vector)
#
# Similar voices  → High similarity score (close to 1)
# Different voices → Low similarity score (close to 0)
# =============================================================================



# Load the main voice embedding model 
@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder()


# Generate a speaker embedding from the recorded audio. 
def get_voice_embedding(audio_bytes):

    try:
        # Retrieve the cached Voice Encoder embedding model.
        encoder = load_voice_encoder()

        # Wrap raw audio bytes in an in-memory file object so librosa
        # can read it like a normal audio file.

        # here sr=16000 means over microphonse capture 16000 amptitude instanve of voice persecond and all of voice instance store inside the RAM 
        
        # Librosa decodes the audio file and returns the waveform
        # as a NumPy array of floating-point samples.
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
    
        # Normalize and preprocess the waveform before extracting the speaker embedding.
        wav = preprocess_wav(audio)
        
        # Generate a 256-dimensional speaker embedding. 
        embedding = encoder.embed_utterance(wav)

        return embedding.tolist()
    
    except Exception:
        st.error("Voice recognition error!")
        return None
    

# Compare the input speaker embedding against all registered
# student embeddings and return the best match.
def identify_speaker(new_embedding, candidates_dict, threshold=0.65):

    # if embedding of speaker is not exist or no students exist 
    if new_embedding is None or not candidates_dict:
        return None, 0.0
    
    best_student_id = None
    best_score = -1.0

    for sid, stored_embedding in candidates_dict.items():

        # Skip students without a stored embedding.
        if stored_embedding:

            # Speaker embeddings returned by Resemblyzer are L2-normalized (||v|| = 1).
            # Dot Product Formula:
            #     A · B = |A| |B| cos(θ)
            #
            # Since |A| = |B| = 1:
            #     A · B = 1 × 1 × cos(θ)
            #           = cos(θ)
            #
            # Therefore, np.dot(new_embedding, stored_embedding)
            # directly computes the cosine similarity between the two speakers.
            similarity = np.dot(new_embedding, stored_embedding)

            if similarity > best_score:
                best_score = similarity
                best_student_id = sid

    # Accept the match only if the similarity score exceeds the configured threshold.
    if best_score >= threshold:
        return best_student_id, best_score

    return None, best_score


# Process a classroom recording containing multiple students.
# Each speech segment is extracted and matched against the
# registered student embeddings.

# to identify each student inside the recoreded voice we use this function 
def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):

    try:
        # load the voice embedding model 
        encoder = load_voice_encoder()

        # load audio with librosa
        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)

        # Split the recording into individual speech segments based on periods of silence

        # Students typically speak one after another
        # Silent intervals naturally separate different speakers

        # librosa.effects.split() detects non-silent regions
        # Segments separated by silence become individual speech clips

        # top_db=30 treats low-volume audio as silence.
        # librosa returns only the non-silent speech segments
        # Each segment contains the start and end sample indices of a detected speech region.
        segments = librosa.effects.split(audio, top_db=30)

        identified_students = {}

        # identify each student voice 
        for start, end in segments:
            
            # if sound duration is very less like 0.5sec so we ignore this sound 
            if (end-start) < sr * 0.5:
                continue

            # Extract the current speech segment from the full recording
            segment_audio = audio[start:end]

            # normalize this audio for better embeddings 
            wav = preprocess_wav(segment_audio)
            
            # Generate the speaker embedding for the current segment
            embedding = encoder.embed_utterance(wav)

            # identify student voice 
            sid, score = identify_speaker(embedding, candidates_dict, threshold)

            if sid:
                if sid not in identified_students or score > identified_students[sid]:
                    identified_students[sid] = score

        return identified_students
    
    except Exception:
        st.error("Bulk processing error!")
        return {}