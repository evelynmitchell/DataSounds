========
Usage
========

.. code-block:: python 

    from DataSounds.sounds import get_music, w2Midi
    import numpy as np

    data = np.random.rand(24)
    music = get_music(data)
    w2Midi('my_musica_data', music)

`w2Midi` writes a .midi file inside the current directory. In this case
*my_music_data.midi* will be saved on disk. Enjoy it!

