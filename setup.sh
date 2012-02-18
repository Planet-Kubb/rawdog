#!/bin/bash

if [ ! -d ./rawdog/feeds ]; then
	echo "Creating directory for rawdog to cache feeds..."
	mkdir ./rawdog/feeds
fi

