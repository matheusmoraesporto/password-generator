# What is it?
It's a basic password generator originated from an academic study, about how to generate random and strong passwords. This implementation was based on [Bitwarden](https://bitwarden.com/), that generate random passwords based in user policies configuration. After generate the password, a brute force algorithm will test how many time it could identify the generated password, to help how strong it is.

## How to run?
You can run it in a terminal using this example input:
````
python3 password-tester.py --size=5 --num=1 --upper=1 --lower=1 --char=1
````
It's **mandatory** to inform all these parameters, that means:
  - `--size` = the password lenght
  - `--num` = 1 to use number in the password, 0 not uses
  - `--upper` = 1 to use uppercase letters in the password, 0 not uses
  - `--lower` = 1 to use lowercase letters in the password, 0 not uses
  - `--char` = 1 to use characters in the password, 0 not uses
  
  ### Dependencies
    - tqdm
  
