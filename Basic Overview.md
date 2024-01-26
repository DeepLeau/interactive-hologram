<a name="br1"></a> 

Basic Overview

The interacꢀve hologram is a plaꢁorm that enables objects to be viewed with an illusion of

depth and interacted with in real ꢀme using hand detecꢀon.

Thanks to this plaꢁorm, it is possible to visualize complex objects and learn more about their

various characterisꢀcs, as well as adding informaꢀon to a tangible object placed at the

center of the pyramid.

Get to know more about the interacꢀve hologram project on DVIC website (link of the page

soon…)

Clone the Code

To clone the project:

Clone the repository: git clone

https://github.com/GaetanCrd/InteractiveHologram/tree/main

Install the required libraries (cv2, mediapipe, pyautogui, tensorflow, audioop, pyaudio)

Adjust thresholds to suit your hardware (seuil de déclenchement du clic pouce/index, seuil

de déclenchement du clic avec l’audio => voir les commentaires du code)

Note that this Python code is designed to work with a speciﬁc Figma ﬁle:



<a name="br2"></a> 

For example, during an audio peak, the InteractiveHolo.pycode triggers a click on the

coordinates x,y=90,990

So, a buꢂon has been placed on these coordinates in the Figma ﬁle to trigger an acꢀon

Files Provided in the GitHub

InteractiveHolo.py: Main Python ﬁle used to run the interacꢀve hologram. In pracꢀcal

terms, it allows you to:

Control the computer mouse using the hand detected by the webcam.

Click by pinching the thumb and index ﬁnger.

Trigger a click by creaꢀng a sound peak on the webcam microphone.

AudioID: Python ﬁle used to detect all the audio devices connected to your computer and

their IDs, useful for seꢃng up the InteractiveHolo.pycode with your variables.

AfterEffect\_Github: The AꢄerEﬀect ﬁles used to create the videos used on Figma + the

source media used in the AꢄerEﬀect ﬁles.

Figma\_Github: .mp4 videos exported from AꢄerEﬀect and used in the Figma.

Hardware: A Webcam + Screen System

The interacꢀve hologram funcꢀon thanks to 1 webcam, 1 displaying screen and 1 control

monitor :

Webcam : to capture the video stream of hands and sound peaks.

Displaying screen : directly implemented in the hologram.

Control monitor : allowing you to run the Python code and the Figma ﬁle.



<a name="br3"></a> 

Launch the Interacꢀve Hologram

1\. Wiring

Make sure that when the Python code is launched it detects the webcam and the webcam

microphone.

1\.1 Webcam

Line 59 of the code InteractiveHolo.py: Modify the variable to ﬁnd your webcam; a window

with a video stream should open if the webcam is correctly detected.



<a name="br4"></a> 

1\.2 Micro

Line 14 of the code InteractiveHolo.py: Modify the variable to ﬁnd your webcam's

microphone; use the audioID.pycode provided in the GitHub repo to idenꢀfy all your audio

devices and their IDs.

2\. Control Monitor

2\.1 Figma

Get the ﬁle from this public link (you'll need a Figma account). Normally, the ﬁle is published,

so it's public. If you can't get it, you can send me a request on <thomas.bodenan@gmail.com>

link -> [InteracꢀveHologramV2-(Community)](https://www.figma.com/file/djTwNBUoWC2nPRA5BrAYd0/InteractiveHologramV2-\(Community\)?type=design&mode=design&t=z7bf9A173N1yEMxa-1)

2\.2 Python

Make sure that you have correctly imported all the necessary libraries and that you can run

the InteractiveHolo.pycode without error. Run it from a code editor or directly from the

terminal.

Launch the Figma model using the play buꢂon at the top right of the window, uncheck

"hotspot hints on click" and "Figma UI" in the opꢀons, and set it to full screen by clicking F.

You can now control the Figma model using your hand.

