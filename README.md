
# CoderDojo Sonic Pi/Bare Touch music sequencer
A Sonic Pi music sequencer with conductive-paint, touch-sensitive control pads.   

The code and workshop were developed by [Jonathan Hogg](http://www.jonathanhogg.com/) for the CoderDojo Glasgow Science Centre Dojos on Saturday 30 Feb 2016.  This README is an expanded description of the workshop with added diagrams, etc.

Here's a link to a [short video](https://www.facebook.com/CoderdojoScotland/videos/vb.209977582476439/683765638430962/?type=2&theater&notif_t=like) of the workshop on the day.

## Licence

This work is licensed under the following [License](./LICENSE)

# Equipment

For the Sequencer
* Computer (laptop or Raspberry Pi)
* Sonic Pi 
* Arduino IDE  [Download and set up instructions here](http://www.bareconductive.com/make/setting-up-arduino-with-your-touch-board/)

For the Bare Conductive touch pads
* [Bare Touch board](http://www.bareconductive.com/shop/touch-board/)
* [Bare Conductive paint](http://www.bareconductive.com/shop/electric-paint-50ml/)
* Large sheet of paper
* 12 Crocodile clips
* Felt tip pens
* Paintbrushes


For the Disco Light
* Jonathan made some custom hardware to drive a DMX light from a USB output, so the code here won't be any use without it. You could, however, write some code yourself to drive an off-the shelf DMX light.


# Instructions

## Control Pad

We're going to start by making the Control Pad for our sequencer - mainly because it's going to take a while for the paint to dry.

[Control Pad Instructions](./ControlPad.md)

# Sequencer

### What is a Sequencer?

The loop pedal that musicians like KT Tunstall and Ed Sheeran use is essentially a sequencer.  It plays a loop of sounds that you can add to while it's playing:


[![KT Tunstall Loop pedal video](http://glasgow.coderdojo.co/DigitalDJ/tunstall.jpg)](https://www.youtube.com/watch?v=r7XIQ_6J2do)

Loop pedals record the sound live and add it in, but we're going to use some sounds and samples that are already provided with Sonic Pi.

[Sequencer Instructions](./Sequencer.md)



## Connecting the Control Pad with the Touch Board


Next we want to connect the sequencer to the Control Pad (assuming it has dried - the Bare Conductive paint is washable, but quite messy when wet).   

The Touch Board uses capacitative touch, a method that uses the electrical conductivity of the human body, to tell whether or not someone is touching its sensors.  Capacitative touch is also the method used by touchscreens in mobile phones.

[TouchBoard Instructions](./Connect.md)

## Extra Stuff

[Additional features you could add](./Extras.md)

## Authors
 
[Jonathan Hogg](http://www.jonathanhogg.com/) <br/>
[Claire Quigley](https://github.com/alcluith) <br/>




