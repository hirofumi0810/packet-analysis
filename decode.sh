#!/bin/sh

# pcapファイルを復号・解凍
decode() {
    for filepath in $1*
    do
        filename=`basename $filepath .pcap.gz.enc`
        openssl enc -d -aes-256-cbc -in $filepath -k r92PsuZlx > $1$filename'.pcap.gz'
        gunzip $1$filename'.pcap.gz'
    done
}

# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-20/"
# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-10/"
# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-11/"
# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-21/"
# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-22/"
# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-23/"
# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-24/"
# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-25/"
# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-26/"
# decode "/Users/admin/Documents/lecture/M1前期/53_金3_分野別演習/pcap-intern/04-27/"

exit 0










