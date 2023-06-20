# Interface with a NewPort Motion Controller over USB using Python.

Fork of [python_newport_controller](https://github.com/bdhammel/python_newport_controller) script.

Interactive Shell allowing to send NewPort commands to USB NewFocus Controllers (see bottom of page).
This process uses Python3, with the [pyUSB](https://github.com/pyusb/pyusb) module.

**Note** This script has only been tested with a single [closed-loop Picomotor controller (model 8745 and 8742)](https://www.newport.com/Closed-Loop-Picomotor-Motion-Controller/1023364/1033/info.aspx).

### Install

#### Install pyUSB

```bash
$ pip install newport_shell
```

### Using the Python Code

Launch the code by typing the following into terminal

```bash
$ python3 -m newport_shell
```

You should see this prompt open up, asking you to identify the motor to connect to.

```bash
Connected to Motor Controller Model 8742. Firmware Version 2.2 08/01/13

Motor #1: 'Standard' Motor
Motor #2: No motor connected
Motor #3: No motor connected
Motor #4: No motor connected

        Picomotor Command Line
        ---------------------------

        Enter a valid NewFocus command, or 'quit' to exit the program.

        Common Commands:
            xMV[+-]: .....Indefinitely move motor 'x' in + or - direction
                 ST: .....Stop all motor movement
              xPRnn: .....Move motor 'x' 'nn' steps



Input > 1MV+
Input > ST
Input >
```


For a full list of commands on the 8745 controller, see section 6.2 in the [user manual](https://assets.newport.com/webDocuments-EN/images/8743_CL_User_Manual_revA.pdf)
