#!/bin/env csh

foreach file ( `ls Euler*.ipynb` )
   echo $file
   jupyter nbconvert $file --to rst
end

echo 'You should mv *.rst to the required source directory now."
