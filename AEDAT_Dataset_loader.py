import aedat
# import cv2
# import dv
# import numpy as np
from dv import LegacyAedatFile, AedatFile

with LegacyAedatFile("cc1111.aedat") as f:
    for event in f:
        # cv2.imshow('out', event.image)
        print(event)
        # print(event.timestamp)
        #break

print("")

#
# with AedatFile("cc1111.aedat4") as f:
#     print(f['frames'])
#     # loop through the "events" stream as numpy packets
#     for e in f['events'].numpy():
#         print(e)
#         break



decoder = aedat.Decoder("cc1111.aedat4")
print(decoder.id_to_stream())
print("")

for packet in decoder:
    print(packet)
    break
    # if "frame" in packet:
    #     print("Frame loop")
    #     image = packet["frame"]["pixels"]
    #     if packet["frame"]["format"] == "RGB":
    #         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    #     elif packet["frame"]["format"] == "RGBA":
    #         image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)
    #     # cv2.imwrite(f"{index}.png", image)
