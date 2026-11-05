# CoreXY 3D printer

A CoreXY 3D printer with a **500 x 500 x 500 mm** build volume, running Marlin on an Arduino Mega
with a RAMPS board.

Tinkerers' Laboratory project, IIT Bombay, May 2025 to Jul 2025. Solo build.

## What I did

I built the printer on my own and ran test prints on it.

## Hardware

- CoreXY frame and motion system for a 500 x 500 x 500 mm build volume
- Arduino Mega with a RAMPS board
- Marlin firmware, set up for CoreXY kinematics

## CoreXY in short

The two motors for X and Y stay fixed on the frame and move the print head through two belts.
The catch is that neither motor drives X or Y on its own:

```
A = X + Y
B = X - Y
```

A pure X move turns both motors the same way. A pure Y move turns them opposite ways. Marlin does
this conversion itself once `COREXY` is enabled in its configuration.

## corexy.py

`corexy.py` is a short script written in 2026 for this repo. It is not part of the printer's
firmware or the original project files. It prints the motor moves for a few head moves:

```
$ python3 corexy.py
  dX    dY  ->    dA    dB
 100     0  ->   100   100
   0   100  ->   100  -100
 100   100  ->   200     0
 -50    25  ->   -25   -75
```
