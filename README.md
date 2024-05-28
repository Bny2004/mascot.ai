# mascot.ai

> [!IMPORTANT]
Right now, just and only run `tts_engine.py`. Even though we are importing all other files into `mascot.ai.py` (main file or entry point), the idea isn't clear and without running **VTubeStudio** first, `mascot.ai.py` will not run as we might expect. There is nothing I can do as I can't even run **VTubeStudio** and my IDE at the same time.

- Right now it requires additional software like **Voicemeeter** to make, for example the terminal this program ran from, act as the microphone source for the **VTubeStudio**.

- There is no real interaction or anything useful going on with this and **VTubeStudio** at the moment.

    - But for this, I'll need additional information, like what is the end goal of this script/program?

    - Depending on that, either we can keep going with **Voicemeeter** setup and let this script only handle two parts: Getting the YouTube Live chat messages and Reading them alound (TTS).

    - OR, implement something like, this programms own audio driver that can on it's own can act as the microphone.

    - We certainly don't need or care about it's interaction with **VTubeStudio** (if all the above cases satisfy).

- Also then, what do we want this program to achieve in interaction with **VTubeStudio**?

    - ?

- We need the model inside the **VTubeStudio** to speak/talk the message sent on the Live chat, right?

    - So, we will also want the model to, like move or blink or just do something instead of just standing there, right?

    - If that's the case, we'll need to feed/send some kind of tracking data into **VTubeStudio**. As I saw someone played a random video of someone and made the video as the camera input for the model's movement using **OBS Virtual Camera**.

    - So, if we do the similar, than we don't have to care about the model's movement (beside emotes) using this program, right?

- BUT, to really make sense of "**ai**" in the name of this project/program/script:

    - We can send custom tracking data to **VTubeStudio** including the emotes and stuff by analyzing the sentiments of the text/message (in the chat).

    - I've seen a Python library which satisfies our requirements of analyzing the sentiments of the given text, BUT it's unmaintained + if we try to still use it, IT USES MICROSOFT AZURE AND REQUIRES A SUBSCRIPTION. Mean, MONY!!! (T_T)

    - Beside that, I am not sure if it's possible to send custom tracking data to **VTubeStudio** and HOW !
