#!/bin/bash

aws s3 cp $1 s3://ds2002-ryb8jt/
aws s3 presign --expires-in 604800  s3://ds2002-ryb8jt/$1

# https://ds2002-ryb8jt.s3.us-east-1.amazonaws.com/dog.jpg?X-Amz-Algorithm=AWS$
