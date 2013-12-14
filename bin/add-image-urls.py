#!/usr/bin/env python

import sys
import time
import os
import os.path
import logging
import csv
import Flickr.API
import json
import pprint

def crawl(p):

    for root, dirs, files in os.walk(p):

        for f in files:
            path = os.path.join(root, f)
            path = os.path.realpath(path)
            yield path


def parse(path, api):

    logging.info("parsing %s" % path)

    fh = open(path, 'r')
    reader = csv.DictReader(fh, delimiter='\t')

    tmp = "%s.tmp" % path
    writer = None

    if os.path.exists(tmp):
        logging.info("%s already exists so I guess %s is being processed, skipping" % (tmp, path))
        return

    sizes = ('small', 'medium', 'large', 'original')
    props = ('source', 'height', 'width')

    for row in reader:

        if row.get('flickr_original_source', False):
            logging.info("already processed %s, skipping" % path)
            return

        if not writer:

            fieldnames = row.keys()
    
            for sz in sizes:
                for prop in props:
                    
                    key = "flickr_%s_%s" % (sz, prop)
                    fieldnames.append(key)

            out = open(tmp, 'w')

            writer = csv.DictWriter(out, fieldnames, delimiter='\t')
            writer.writeheader()

        #

        id = row['flickr_id']
        logging.debug("get sizes for %s" % id)

        method = 'flickr.photos.getSizes'

        args = {
            'method': method,
            'photo_id': id,
            'format': 'json',
            'nojsoncallback': 1
        }

        keep_trying = True
        try_again = 5

        while keep_trying:

            try:
                rsp = api.execute_method(method=method, args=args, sign=False)
                data = json.load(rsp)
                keep_trying = False
                break
            except Expcetion, e:
                logging.error("API call failed: %s" % e)
                time.sleep(try_again)

        for sz in data['sizes']['size']:
            
            label = sz['label'].lower()

            if not label in sizes:
                continue

            for prop in props:

                key = 'flickr_%s_%s' % (label, prop)
                row[key] = sz[prop]

        writer.writerow(row)

    os.rename(tmp, path)
    time.sleep(1)

if __name__ == '__main__':

    import optparse

    parser = optparse.OptionParser()

    parser.add_option('-a', '--api-key', dest='apikey', action='store', help='A valid Flickr API key')
    parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False, help='be chatty (default is false)')
        
    options, args = parser.parse_args()

    if options.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    whoami = sys.argv[0]
    whoami = os.path.realpath(whoami)
    bin = os.path.dirname(whoami)
    root = os.path.dirname(bin)

    api = Flickr.API.API(options.apikey)

    for path in crawl(root):

        if not path.endswith(".tsv"):
            continue

        parse(path, api)
