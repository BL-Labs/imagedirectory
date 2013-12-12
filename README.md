Flickr Common Manifests
=======================

Manifests of the public domain images uploaded to Flickr Commons, with descriptive information about the books they were taken from.

Structure
=========

All TSV files are in UTF-8 encoding and are split by year, and by size of illustration. 

- Small images are anything below 800x600 (480,000 in pixel area) This has nothing to do with the aspect ratio of the image i.e. they can be long and thin.
- Medium are between small and 'plate' size
- 'Plates' are any images larger than 1000x1000 (1,000,000 pixel area)

Each image is represented by a single row in the manifest. From left to right, the columns are:

    flickr_id:       The 'photo' identifier on flickr
    flickr_url:      A handy URL to the image for convenience
    book_identifier: The internal 'sysnum' for the record of the book in the BL's cataloguing system
    title:           The title of the work the image was drawn from
    first_author:    The first listed author/contributor in the work's record
    pubplace:        Place of Publication
    publisher:       Publisher
    date:            Date of Publication
    volume:          Which book volume the image was taken from 
    page:            Which page
    image_idx:       What image number on the page (useful when multiple are present. Arbitrary but unique to an image.)
    ARK_id_of_book:  ARK identifier for the digitised version of the work [NB known ~20% of the time]
    BL_DLS_ID:       Digital Library Service identifier.(Starts with 'lsidyv...') [NB known ~20% of the time]

NB You can retrieve the PDF of the book by appending the BL\_DLS\_ID to the following URL:

http://access.bl.uk/item/pdf/...

e.g. from the first line of '1846_plates.tsv':

    11047063964     http://www.flickr.com/photos/britishlibrary/11047063964 001365762       Travels in the interior of Brazil, principally through the northern provinces and the Gold and Diamond districts, 1838-41       GARDNER, George F.L.S   London          1846    0       0000241        ark:/81055/vdc_000000056040     lsidyv3c0ae38a

You can get the PDF of "Travels in the interior of Brazil, principally through the northern provinces and the Gold and Diamond districts, 1838-41" by GARDNER, George F.L.S by going to the following URL:

http://access.bl.uk/item/pdf/lsidyv3c0ae38a
