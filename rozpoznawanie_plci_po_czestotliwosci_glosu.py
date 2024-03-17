import sys
import numpy as np
import scipy.io.wavfile
import scipy.fft
import scipy.signal
import warnings


warnings.filterwarnings("ignore")
def HPS(sygnal, klatki, n):
        #spektrum
        spektrum = np.abs(scipy.fft.fft(sygnal))

        #generowanie harmonicznych
        harmoniczne = np.copy(spektrum)

        for i in range(2, 5): #5
            indeksy = spektrum[::i]
            dod = indeksy[:len(harmoniczne)]
            harmoniczne[:len(indeksy)] *= dod
        start = 70 * (n//klatki)
        #print(start)
        x = harmoniczne[start:]

        max = np.argmax(x)
        rezultat = (max + start) / (n//klatki)

        return rezultat


def main():
    audio_file_path = sys.argv[1]
    Odp = audio_file_path[-5]

    klatki, sygnal = scipy.io.wavfile.read(audio_file_path)
    sygnal = np.array(sygnal)
    N = len(sygnal)
    sygnal = sygnal.astype(np.float64)
    sygnal /= np.max(np.abs(sygnal))

    sygnal = sygnal * np.kaiser(N, 14)
    #np.kaiser(N, 14)-82 dla beta-0 tak jak ones, beta-5 80, beta-10 81, beta-15 82, beta-20
    #np.blackman(N)-80
    #np.hamming(N)-80
    #np.hanning(N)-78
    #np.ones(N)-82
    x = HPS(sygnal, klatki, N)

    wynik = ""
    #print(round(x, 2))
    if x < 176 and x > 80:
        print("M")
        wynik = "M"
    else:
        print("K")
        wynik = "K"


    #if Odp == wynik:
    #    #print("no elegancko\n")
    #    counter = counter + 1
    #else:
    #    print("no tak se\n")



if __name__ == "__main__":

    main()



