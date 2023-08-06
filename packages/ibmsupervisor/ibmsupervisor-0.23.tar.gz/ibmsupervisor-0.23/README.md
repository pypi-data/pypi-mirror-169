This project allows decoding the password from the SPI NOR flash chip dump of an IBM ThinkPad 365XD. It might work on different models as well. Shorting the pins of the EEPROM at the right time during boot might also work for bypassing the supervisor password, but this is relatively hard to due to the position of the EEPROM. If you have a programmer and can desolder a chip, I recommend this method.

[Location of the EEPROM](https://web.archive.org/save/https://i.redd.it/qyqta64bwme31.jpg)

The code has only been tested with the IBM ThinkPad 365XD, which has an ST93C46C Microwire (SPI) EEPROM. It has also only been tested on a US int keyboard and will likely break on something else.

## Prerequisites 
You need to dump the EEPROM before using this program. I used the TL866+ after desoldering the chip. Attaching the wires with a SOIC-8 clip did not work for me. For this particular ThinkPad model, the command was:

`sudo minipro --device "ST93C46C(x8)@SOIC8" --read password.rom`

Python 3 is also needed.

## Usage
Install this tool using Pip:
```
pip3 install ibmsupervisor
ibmsupervisor password.rom
```
The above assumes that `~/.local/bin` is part of your PATH variable and that `python3-pip` is installed.

You can also clone this repo and do the following:
```
chmod +x ./password.py
./password.py password.rom
```

## Common problems
* If the ThinkPad prints "178" when booting, the EEPROM is very likely not making contact after you have soldered it back on the PCB.
* If the TL866 gives a file full of 0xFF bytes, the pins haven't made good contact.
* In case the ThinkPad gives a CRC error after reading the data but you have not changed anything, you can flash the okeee.rom to the chip. This has been tested on another ThinkPad 365XD and is known to work. As the filename implies, the supervisor password that is contained in this rom is "okeee" without the quotes. Note that you should keep the dump you made, because that one very likely contains the HDD password that you will need to boot from it.

## Notes
In the `bin` folder, the `abcdefdg.rom` has been extracted from a machine and `okeee.rom` is known to work on a different machine as well. `44keee.rom` is a broken test example. `nzhnzh.rom` is likely broken as well, with a corrupt CRC.

## Links
* [minipro by David Griffith](https://gitlab.com/DavidGriffith/minipro)
* [365XD user guide](https://web.archive.org/web/20161230160352/http://greyghost.mooo.com/pccbbs/mobiles/36xusegd.pdf)
