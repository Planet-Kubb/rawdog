#!/bin/bash

if [ ! -d ./rawdog/feeds ]; then
	echo "Deleting all cached feeds..."
	rm ./rawdog/feeds/*
fi

if [ -e ./rawdog/state ]; then
	echo "Deleting rawdog state file..."
	rm ./rawdog/state
fi

