#!/bin/bash

RAWDOG=/usr/local/bin/rawdog

if [ -x $RAWDOG ]; then
	$RAWDOG --dir ./rawdog --update --write
fi

