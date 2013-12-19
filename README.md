Flickr Common Manifests
=======================

Manifests of the public domain images uploaded to Flickr Commons, with descriptive information about the books they were taken from.

Please read the following for a better idea of why we are doing this:

http://britishlibrary.typepad.co.uk/digital-scholarship/2013/12/a-million-first-steps.html

Structure
=========

book_metadata.json
------------------

A large hash in the following form:

    {
    "000000037" : {  ... bundle of metadata for book with ID 000000037 ... },
    "000000206" : { ... etc ... },
    ...
    }

The fields are as follows:

    'identifier' - The book ID, eg 000000206
    'title' - a bit of a misnomer. The book might have more than a single title attributed to it,
              and other details, inferred by a cataloguer/librarian might be added to it.
              Typically, these addition details will be enclosed by '[]' brackets
    'authors' - (Named people who are 'personal' contributors). If the metadata states a particular
                role should be attributed to them, then this is marked also.
    'corporate' - as above, but corporate bodies rather than individuals.
    'place' - Place of publishing or manufacture
    'datefield' - The details from the published date field
    'date' - A date inferred by me by sweeping through fields where this information may likely hide such as
             'publisher'.
    'publisher' - The stated publisher of the work
    'edition' - Edition of the work
    'issuance' - Issuance, typically 'monograph'
    'shelfmarks' - Shelfmark, or marks of where the physical original 'lives'.
    'flickr_url_to_book_images' - link to the tag page that shows all the images taken from this book

Most fields, except 'date', 'edition', 'issuance', are potential multivalued and have been generated as lists of values ordered in the same manner that they were in the metadata that accompanied these scans.

*NB* The metadata is for all the books that were scanned as part of the Microsoft Live Search Books project. Not all of these books had illustrations in them that were detected. The 'flickr\_url\_to\_book\_images' field is generated from the identifier of the book, and so there may be nothing on Flickr for that book!

[YEAR]_[Image size].tsv
-----------------------

All TSV files are in UTF-8 encoding and are split by year, and by size of illustration. 

- Small images are anything below 800x600 (480,000 in pixel area) This has nothing to do with the aspect ratio of the image i.e. they can be long and thin.
- Medium are between small and 'plate' size
- 'Plates' are any images larger than 1000x1000 (1,000,000 pixel area)

Each image is represented by a single row in the manifest. The columns are:

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
     - And, thanks to [Aaron Straup Cope](@straup), the rows now include direct links to the files, as well as the pixel sizes of them:
    flickr_original_source:    URL to jpg file (the original, and largest resolution)
    flickr_original_height:    Height in px of original
    flickr_original_width:     Width in px of original
    flickr_large_source:       And so on.
    flickr_large_height
    flickr_large_width
    flickr_medium_source
    flickr_medium_height
    flickr_medium_width
    flickr_small_source
    flickr_small_height
    flickr_small_width 

NB As @straup himself notes, this adds bloat to the list and I agree with him on that, but also on the fact that this keeps it simple and grokkable and should allow anyone else wanting to do stats on the set to not have to hit Flickr's API to get this sort of info.

You can retrieve the PDF of the book by appending the BL\_DLS\_ID to the following URL:

http://access.bl.uk/item/pdf/...

e.g. from the first line of '1846_plates.tsv':

    11047063964     http://www.flickr.com/photos/britishlibrary/11047063964 001365762       Travels in the interior of Brazil, principally through the northern provinces and the Gold and Diamond districts, 1838-41       GARDNER, George F.L.S   London          1846    0       0000241        ark:/81055/vdc_000000056040     lsidyv3c0ae38a

You can get the PDF of "Travels in the interior of Brazil, principally through the northern provinces and the Gold and Diamond districts, 1838-41" by GARDNER, George F.L.S by going to the following URL:

http://access.bl.uk/item/pdf/lsidyv3c0ae38a
