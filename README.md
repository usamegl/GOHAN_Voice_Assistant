# Voice_Assistant
A voice assistant program written in python.








                                                                                                                        
                                                                                                                        
        GGGGGGGGGGGGG     OOOOOOOOO     HHHHHHHHH     HHHHHHHHH               AAA               NNNNNNNN        NNNNNNNN
     GGG::::::::::::G   OO:::::::::OO   H:::::::H     H:::::::H              A:::A              N:::::::N       N::::::N
   GG:::::::::::::::G OO:::::::::::::OO H:::::::H     H:::::::H             A:::::A             N::::::::N      N::::::N
  G:::::GGGGGGGG::::GO:::::::OOO:::::::OHH::::::H     H::::::HH            A:::::::A            N:::::::::N     N::::::N
 G:::::G       GGGGGGO::::::O   O::::::O  H:::::H     H:::::H             A:::::::::A           N::::::::::N    N::::::N
G:::::G              O:::::O     O:::::O  H:::::H     H:::::H            A:::::A:::::A          N:::::::::::N   N::::::N
G:::::G              O:::::O     O:::::O  H::::::HHHHH::::::H           A:::::A A:::::A         N:::::::N::::N  N::::::N
G:::::G    GGGGGGGGGGO:::::O     O:::::O  H:::::::::::::::::H          A:::::A   A:::::A        N::::::N N::::N N::::::N
G:::::G    G::::::::GO:::::O     O:::::O  H:::::::::::::::::H         A:::::A     A:::::A       N::::::N  N::::N:::::::N
G:::::G    GGGGG::::GO:::::O     O:::::O  H::::::HHHHH::::::H        A:::::AAAAAAAAA:::::A      N::::::N   N:::::::::::N
G:::::G        G::::GO:::::O     O:::::O  H:::::H     H:::::H       A:::::::::::::::::::::A     N::::::N    N::::::::::N
 G:::::G       G::::GO::::::O   O::::::O  H:::::H     H:::::H      A:::::AAAAAAAAAAAAA:::::A    N::::::N     N:::::::::N
  G:::::GGGGGGGG::::GO:::::::OOO:::::::OHH::::::H     H::::::HH   A:::::A             A:::::A   N::::::N      N::::::::N
   GG:::::::::::::::G OO:::::::::::::OO H:::::::H     H:::::::H  A:::::A               A:::::A  N::::::N       N:::::::N
     GGG::::::GGG:::G   OO:::::::::OO   H:::::::H     H:::::::H A:::::A                 A:::::A N::::::N        N::::::N
        GGGGGG   GGGG     OOOOOOOOO     HHHHHHHHH     HHHHHHHHHAAAAAAA                   AAAAAAANNNNNNNN         NNNNNNN
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                        
                                                                                                                   









First of all, it is necessary to import several libraries in order for the program to run.

import pyaudio
from playsound import playsound
from gtts import gTTS
import speech_recognition
import os

It's important to use the correct python version for pyaudio, I'm using 3.10.5. I leave a link here for you to find the correct version: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
And then throw it into your existing project file and
pip3 install pyaudio
It will suffice to say.

For example, when you say "gohan", you can change it to say "Hi Osama" etc. in the code.


And finally, I must say this. I used this voice assistant ready from google.







Öncelikle programın çalışabilmesi için birkaç kütüphaneyi import etmek gerekiyor.

import pyaudio
from playsound import playsound
from gtts import gTTS 
import speech_recognition 
import os

pyaudio için doğru python sürümünü kullanmak önemli, ben 3.10.5 kullanıyorum. Sizlerin de doğru sürümü bulması için buraya link bırakıyorum: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
Ve sonrasında var olan proje dosyanız içine atıp
pip3 install pyaudio 
demeniz yeterli olacaktır.

Örneğin "gohan" dediğinde "Hi Usame" demesini vesaire de siz kod içersinde değiştirebilirsiniz.


Ve son olarak şunu söylemeliyim. Bu ses asistanını da google'dan hazır bir şekilde alıp kullandım.













