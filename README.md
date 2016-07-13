Super Lame, Broseph
===================

* **NOTE:** *This is the product of 15 minutes in ipython and is rather horrid.*

Ever forget your GPG passphrase but happen to have an idea of what combinations/permutations the password most likely is?

Yeah, neither did my, erm, my friend. Yeah, you don't know him.

Anyways, it's a pain to try them all by hand.

This is the hacky toolkit I used for such a situation, maybe it will help someone else.

`fuzzy.py`: After trying to relearn `crunch` syntax for the 100th time, I just gave up and wrote
a dead simple fuzzer that matched my needs exactly.

`wuzzy.sh`: Dead simple loop to try passwords against gpg and break on success.

```sh
cp -av tokens.example tokens

vim tokens  # add permutations

cat tokens | ./fuzzy.py | ./wuzzy.sh
```

This is all very slow, and is not exactly meant for brute forcing, but more of giving you a dead easy way to lay out permutations from a known list.
