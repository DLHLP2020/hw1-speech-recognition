# Download dataset from Google Drive
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1daFU8tPPUyhN7Fc6JUTohEfHXIn6ZDgq' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1daFU8tPPUyhN7Fc6JUTohEfHXIn6ZDgq" -O HW1-data.tar.gz && rm -rf /tmp/cookies.txt

# Unzip the dataset
tar zxvf HW1-data.tar.gz --no-same-owner > log && rm log

# Create data dir & move the dataset
mkdir data && mv DLHLP data
