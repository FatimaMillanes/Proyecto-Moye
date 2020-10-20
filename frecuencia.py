import sys 
sys.path.insert(1,'dsp-modulo')

from tkinter import *
from tkinter.filedialog import askopenfilename

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from thinkdsp import read_wave
import numpy

principal = Tk()
principal.title("Análisis / Cifrado - Equipo 4")

strDireccionArchivo = StringVar()
strDireccionArchivo.set("Direccion del archivo:")

strSecuencia = StringVar()
strSecuencia.set("Número de contenido en el audio:")

def abrirArchivo():
    direccionArchivo = askopenfilename()
    strDireccionArchivo.set("Direccion del archivo: " + direccionArchivo)

    segmentoTamaño = 0.4
    letrasTamaño = 4

    palabra = "HOLA"
    wavePalabra = read_wave(direccionArchivo)
    segmentosLetras = []
    
    segmentosLetras.append(wavePalabra.segment(start=0, duration=0.5))


    frecuenciasSegmentos = [2000, 2400, 2800, 3200]
    frecuenciasNumLetras = [200, 300, 400, 500, 600, 700, 800]
    tolerancia = 10

    for segmento in segmentosLetras:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 500:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        tamSegmento = 0.4
        cantidadLetras = 4
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciasSegmentos:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    tamSegmento = frecuenciaDTMF
            for frecuenciaDTMF in frecuenciasNumLetras:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    cantidadLetras = frecuenciaDTMF

        if tamSegmento == 2000:
            segmentoTamaño = 0.3
        elif tamSegmento == 2400:
            segmentoTamaño = 0.4
        elif tamSegmento == 2800:
            segmentoTamaño = 0.5
        elif tamSegmento == 3200:
            segmentoTamaño = 0.6

        if cantidadLetras == 200:
            letrasTamaño = 2
        elif cantidadLetras == 300:
            letrasTamaño = 3
        elif cantidadLetras == 400:
            letrasTamaño = 4
        elif cantidadLetras == 500:
            letrasTamaño = 5
        elif cantidadLetras == 600:
            letrasTamaño = 6
        elif cantidadLetras == 700:
            letrasTamaño = 7
        elif cantidadLetras == 800:
            letrasTamaño = 8

    
    segmentoLetras = []
    for i in range(letrasTamaño):
        segmentoLetras.append(wavePalabra.segment(start=0.5+i*segmentoTamaño, duration=segmentoTamaño))
    

    frecuenciaLetras = [2200, 2000, 5600, 4000, 4200, 1800, 5200, 4400, 5400, 2400, 1400, 1600, 6000, 4600, 3400, 3800, 2600, 3200, 5000, 1200, 5800, 3600, 2800, 3000, 4800, 1000]


    for segmento in segmentoLetras:
        espectroSegmento = segmento.make_spectrum()
        frecuenciasDominantes = []
        i = 0
        for amplitudEspectral in espectroSegmento.hs:
            if numpy.abs(amplitudEspectral) > 500:
                frecuenciasDominantes.append(espectroSegmento.fs[i])
            i = i + 1
        letras = 0
        for frecuencia in frecuenciasDominantes:
            for frecuenciaDTMF in frecuenciaLetras:
                if frecuencia > frecuenciaDTMF - tolerancia and frecuencia < frecuenciaDTMF + tolerancia:
                    letras = frecuenciaDTMF
        
        if letras == 2200:
            palabra = palabra + "A"
        elif letras == 2000:
            palabra = palabra + "B"
        elif letras == 5600:
            palabra = palabra + "C"
        elif letras == 4000:
            palabra = palabra + "D"
        elif letras == 42000:
            palabra = palabra + "E"
        elif letras == 1800:
            palabra = palabra + "F"
        elif letras == 5200:
            palabra = palabra + "G"
        elif letras == 4400:
            palabra = palabra + "H"
        elif letras == 5400:
            palabra = palabra + "I"
        elif letras == 2400:
            palabra = palabra + "J"
        elif letras == 1400:
            palabra = palabra + "K"
        elif letras == 1600:
            palabra = palabra + "L"
        elif letras == 6000:
            palabra = palabra + "M"
        elif letras == 4600:
            palabra = palabra + "N"
        elif letras == 3400:
            palabra = palabra + "O"
        elif letras == 3800:
            palabra = palabra + "P"
        elif letras == 2600:
            palabra = palabra + "Q"
        elif letras == 3200:
            palabra = palabra + "R"
        elif letras == 5000:
            palabra = palabra + "S"
        elif letras == 1200:
            palabra = palabra + "T"
        elif letras == 5800:
            palabra = palabra + "U"
        elif letras == 3600:
            palabra = palabra + "V"
        elif letras == 2800:
            palabra = palabra + "W"
        elif letras == 3000:
            palabra = palabra + "X"
        elif letras == 4800:
            palabra = palabra + "Y"
        elif letras == 1000:
            palabra = palabra + "Z"

    strSecuencia.set("Número de contenido en el audio: " + palabra)

    figure = Figure(figsize = (5,3), dpi = 100)
    figure.add_subplot(111).plot(wavePalabra.ts, wavePalabra.ys)

    canvas = FigureCanvasTkAgg(figure, master = principal)
    canvas.draw()
    canvas.get_tk_widget().pack()


btnAbrir = Button(principal, text = "Abrir archivo wav", command = abrirArchivo)
btnAbrir.pack()

lblArchivo = Label(principal, textvariable = strDireccionArchivo)
lblArchivo.pack()

lblSecuenciaNumeros = Label(principal, textvariable = strSecuencia)
lblSecuenciaNumeros.pack()

mainloop()