# fun_flipper
general purpose character corruption tool, designed for binary &amp; binary-like file format fuzzing

use `fun_flipper.py IN_FILE OUT_FILE {#BITFLIPS}`, the `{}` are optional arguments.

if no bitflip count is specified, 1% of the characters will be flipped `(bitflip count = 1% * len(in_text))`

## idea
flip characters, for testing purposes.

example:

```bash
gzip to_hack.gz /bin/bash
while true
do
  ./fun_flipper.py to_hack.gz haxxx.gz
  gzip -d haxxx.gz
  if [ $? -gt 127 ]
  then
    name=$RANDOM$RANDOM$RANDOM$RANDOM__PWND.gz
    echo "[*] bug found. writing to "$name
    mv haxxx.gz $name
  fi
done
```

this simply makes a `.gz` of `/bin/bash`, and runs `fun_flipper` to create a test scenario.

then, if the `gzip` command exits with `> 127`, we know there was a crash, so we put it to a named file.

very very fun.

## REMEMBER
this is a "dumb" fuzzer!

it has no knowledge of syntax and/or file structure, in fact, it's philosophy is to destroy that file structure to find bugs!

as such, a tool like `AFL` is much better suited to most tasks, where as `fun_flipper` could be used for say, fuzzing (THE STUCTURE OF) `.dmg` files.

## DISCLAIMER
this software should work OK, but in the case it breaks and your dick shatters or you get your dick stuck in a ceiling fan or toaster, or another "funny" dick related injury, I AM NOT LIABLE! I HAVE WARNED YOU! DO NOT RUN THIS ON `/dev/sda` or `/dev/disk0` AND COME CRYING TO ME LIKE A LITTLE SHIT! IF YOU WIN A DARWIN (heh) AWARD BECAUSE OF THIS SOFTWARE IT ISN'T MY FUCKING FAULT! DO NOT COME CRYING TO ME! thanks
