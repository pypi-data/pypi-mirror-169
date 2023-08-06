# BlaBlaMower

>This project is for respond to the BlaBlaCar technical test that they have asked me to work on. The specifications are on this file [*specs/BlaBlaCar_Technical Test.md*](/specs/BlaBlaCar_Technical%20Test.md)

Program for mowing a rectangular lawn surface with multiple mowers.

[CHANGELOG](./CHANGELOG.md)

## Installation

> pip and python3.8+ is required

### pypi
```shell
$> pip install blablamower
```

### Release
```shell
$> wget https://github.com/renardguill/BlaBlaMower/releases/download/v1.0.0/blablamower-1.0.0-py3-none-any.whl
$> pip install blablamower-1.0.0-py3-none-any.whl
```

### Source code

> poetry is needed
```shell
$> git clone https://github.com/renardguill/BlaBlaMower.git
$> cd BlaBlaMower
$> poetry build
$> pip install dist/blablamower-1.0.0-py3-none-any.whl
```

## Update

### pypi
```shell
$> pip install blablamower --upgrade
```


## Usage

The program expect an input file constructed in the following manner: :

>The first line corresponds to the upper right corner of the lawn. The bottom left corner is
implicitly (0, 0).
The rest of the file describes the multiple mowers that are on the lawn. Each mower is described
on two lines:
The first line contains the mower's starting position and orientation in the format "X Y O". X and
Y are the coordinates and O is the orientation.
The second line contains the instructions for the mower to navigate the lawn. The instructions
are not separated by spaces.

exemple :
```txt
5 5
1 2 N
LFLFLFLFF
3 3 E
FFRFFRFRRF
```

```shell
$> blablamower ./inputfile.txt
```