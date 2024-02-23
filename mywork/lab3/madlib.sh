#!/bin/bash

clear
echo "Let's build a mad lib"

read -p "1. Please give me an adjective: " ADJ1
read -p "2. Please give me an adjective: " ADJ2
read -p "3. Please give me a verb: " VERB1
read -p "4. Please give me a verb: " VERB2
read -p "5. Please give me a noun: " NOUN1
read -p "6. Please give me a noun: " NOUN2 
read -p "7. Please give me a noun: " NOUN3
read -p "8. Please give me a adverb: " ADV1

echo "Once upon a time there was a $ADJ1 $NOUN1 who was really good at $ADV1 $VERB1. He even $VERB2 a bash script about it, and  it had a $ADJ2 $NOUN2. Ultimately, it was a love letter to $NOUN3. The end!"
