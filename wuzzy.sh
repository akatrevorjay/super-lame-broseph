#!/usr/bin/env bash
set -o pipefail

KEYID="$1"

while read; do
    echo "$REPLY" \
    | gpg2 -q --sign -u "$KEYID\!" \
              --pinentry-mode loopback --passphrase-fd 0 \
              --output /dev/null --yes \
              input.txt >/dev/null
    if [[ $? ]]; then
        echo -n "Passphrase found: " >&2
        echo "$REPLY"
        exit 0
    fi
done

echo "I have failed you, master" >&2
exit 1
