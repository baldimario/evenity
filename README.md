# Evenity - Pluggable event hook libary

## Installation
```sh
pip install evenity
```

## Usage
See examples folder at [https://github.com/baldimario/evenity](https://github.com/baldimario/evenity)

### simple.py 
This file contains an implementation of observers and observable
It shows how simple is to implement your own observable and register all the observers as you want

## kafka.py
This script contains an implementations of some listeners (observers) for the kafka plugin

This subscribe some listeners for the KafkaObservableConsumer listening for events from many topics

## ftp.py 
ftp.py contains an example listener for the ftp observable

This can be useful wen you want to handle file uploaded in an event way

## shell.py
This file contains an example listener for the shell observable

The use case is to read an output steam from a program (or fifo file) and receive an event for each line printed

## telegram.py
This script contains an example listener for telegram bot events (updates, texts and commands)

The observers will be notified for each telegram bot event
