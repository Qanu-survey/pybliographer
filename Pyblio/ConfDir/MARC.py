from Pyblio import Config

Config.define ('marc/mapping',
               """ A hash table containing field names correspondances """,
               Config.Dict (Config.String (), Config.String ()))

Config.set ('marc/mapping', {
    '001' : 'Control Number',
    '003' : 'Control Number Identifier',
    '005' : 'Date and Time of Latest Transaction',
    '007' : 'Physical Description Fixed Field - General Information',
    '008' : 'Fixed-Length Data Elements',
    '010' : 'Library of Congress Control Number',
    '014' : 'Link to Bibliographic Record for Serial or Multipart Item',
    '015' : 'National bibliography number',
    '016' : 'National Bibliographic Agency Control Number',
    '017' : 'Copyright or Legal Deposit Number',

    '020' : 'International Standard Book Number',
    '022' : 'International Standard Serial Number',
    '028' : 'Publisher Number',
    '035' : 'System Control Number',
    '037' : 'Source of acquisition',
    '040' : 'Cataloging Source',
    '041' : 'Language code',
    '042' : 'Authentication Code',
    '043' : 'Geographic Area Code',
    '045' : 'Time Period of Heading',
    '047' : 'Form of Musical Composition Code',

    '050' : 'Library of Congress Call Number',
    '052' : 'Geographic Classification',
    '053' : 'LC Classification Number',
    '055' : 'National Library of Canada Call Number',
    '058' : 'LC Classification Number Assigned in Canada [obsolete] [CAN/MARC only]',
    '060' : 'National Library of Medicine Call Number',
    '063' : 'NLM Classification Number Assigned by NLM [obsolete] [CAN/MARC only]',
    '066' : 'Character Sets Present',
    '068' : 'NLM Classification Number Assigned in Canada [obsolete] [CAN/MARC only]',
    '070' : 'National Agricultural Library Call Number',
    '072' : 'Subject Category Code',
    '073' : 'Subdivision Usage',
    '080' : 'Universal Decimal Classification Number',
    '082' : 'Dewey Decimal Call Number',
    '083' : 'Dewey Decimal Classification Number',
    '086' : 'Government Document Call Number',
    '087' : 'Government Document Classification Number',
    '088' : 'Document Shelving Number (CODOC) [obsolete] [CAN/MARC only]',
    '090' : 'Local Call Numbers',
    '091' : 'Local Call Numbers',
    '092' : 'Local Call Numbers',
    '093' : 'Local Call Numbers',
    '094' : 'Local Call Numbers',
    '095' : 'Local Call Numbers',
    '096' : 'Local Call Numbers',
    '097' : 'Local Call Numbers',
    '098' : 'Local Call Numbers',
    '099' : 'Local Call Numbers',

    '100' : 'Heading - Personal Name',
    '100a' : 'Author',
    '100b' : 'Author Numeration',
    '100c' : 'Author Title',
    '100d' : 'Author Date of Birth/Death',
    '100q' : 'Author Full Name',
    '110' : 'Heading - Corporate Name',
    '111' : 'Heading - Meeting Name',
    '130' : 'Heading - Uniform Title',
    '140' : 'Uniform Title [obsolete] [CAN/MARC only]',
    '143' : 'Collective Title [obsolete] [CAN/MARC only]',
    '150' : 'Heading - Topical Term',
    '151' : 'Heading - Geographic Name',
    '155' : 'Heading - Genre/Form Term',
    '180' : 'Heading - General Subdivision',
    '181' : 'Heading - Geographic Subdivision',
    '182' : 'Heading - Chronological Subdivision',
    '185' : 'Heading - Form Subdivision',

    '222' : 'Key Title',
    '240' : 'Uniform Title',
    '240a' : 'Uniform Title',
    '240l' : 'Language',
    '240f' : 'Date',
    '242' : 'Translation of Title by Cataloging Agency',
    '243' : 'Collective Uniform Title',
    '245' : 'Title Statement',
    '245a' : 'Title',
    '245b' : 'Subtitle',
    '245c' : 'Editor',
    '246' : 'Varying Forms of Title',
    '247' : 'Former Title or Title Variations',
    '250' : 'Edition Statement',
    '254' : 'Musical Presentation Statement',
    '257' : 'Country of producing entity for archival films',
    '260' : 'Complex See Reference - Subject',
    '260a' : 'Address',
    '260b' : 'Publisher',
    '260c' : 'Date',

    '300' : 'Physical Description',
    '300a' : 'Number of Pages',
    '300b' : 'Illustrations',
    '300c' : 'Dimensions',
    '300e' : 'Accompanying Material',
    '306' : 'Playing Time',
    '307' : 'Hours, etc.',
    '360' : 'Complex See Also Reference - Subject',

    '400' : 'See From Tracing - Personal Name',
    '410' : 'See From Tracing - Corporate Name',
    '411' : 'See From Tracing - Meeting Name',
    '430' : 'See From Tracing - Uniform Title',
    '440' : 'Series Statement/Added Entry - Title',
    '450' : 'See From Tracing - Topical Term',
    '451' : 'See From Tracing - Geographic Name',
    '455' : 'See From Tracing - Genre/Form Term',
    '480' : 'See From Tracing - General Subdivision',
    '481' : 'See From Tracing - Geographic Subdivision',
    '482' : 'See From Tracing - Chronological Subdivision',
    '485' : 'See From Tracing - Form Subdivision',
    '490' : 'Series Statement',

    '500' : 'See Also From Tracing - Personal Name',
    '504' : 'Bibliography, etc. note',
    '505' : 'Formatted contents note',
    '508' : 'Creation/Production Credits Note',
    '510' : 'Citations/References Note',
    '511' : 'See Also From Tracing - Meeting Name',
    '520' : 'Summary, etc. note',
    '530' : 'See Also From Tracing - Uniform Title',
    '541' : 'Immediate source of acquisition note',
    '550' : 'See Also From Tracing - Topical Term',
    '551' : 'See Also From Tracing - Geographic Name',
    '555' : 'See Also From Tracing - Genre/Form Term',
    '580' : 'See Also From Tracing - General Subdivision',
    '581' : 'See Also From Tracing - Geographic Subdivision',
    '582' : 'See Also From Tracing - Chronological Subdivision',
    '585' : 'See Also From Tracing - Form Subdivision',

    '600' : 'Subject added entry-personal name',
    '640' : 'Series Dates of Publication and/or Sequential Designation',
    '641' : 'Series Numbering Peculiarities',
    '642' : 'Series Numbering Example',
    '643' : 'Series Place and Publisher/Issuing Body',
    '644' : 'Series Analysis Practice',
    '645' : 'Series Tracing Practice',
    '646' : 'Series Classification Practice',
    '650' : 'Keywords',#'Subject Added Entry - Topical Term',
    '655' : 'Index term-genre/form',
    '663' : 'Complex See Also Reference - Name',
    '664' : 'Complex See Reference - Name',
    '665' : 'History Reference',
    '666' : 'General Explanatory Reference - Name',
    '667' : 'Nonpublic General Note',
    '670' : 'Source Data Found',
    '671' : 'Note - Work Catalogued (Names/Titles) [obsolete] [CAN/MARC only]',
    '675' : 'Source Data Not Found',
    '676' : 'Note - Cataloging Rules (Names/Titles) [obsolete] [CAN/MARC only]',
    '678' : 'Biographical or Historical Data',
    '680' : 'Public General Note',
    '681' : 'Subject Example Tracing Note',
    '682' : 'Deleted Heading Information',
    '685' : 'Note - Source Data Found (Subjects) [obsolete] [CAN/MARC only]',
    '686' : 'Note - Source Data Not Found (Subjects) [obsolete] [CAN/MARC only]',
    '687' : 'Note - Usage (Subjects) [obsolete] [CAN/MARC only]',
    '688' : 'Application History Note',

    '700' : 'Established Heading Linking Entry - Personal Name',
    '710' : 'Established Heading Linking Entry - Corporate Name',
    '711' : 'Established Heading Linking Entry - Meeting Name',
    '730' : 'Established Heading Linking Entry - Uniform Title',
    '740' : 'Added Entry - Uncontrolled Related/Analytical Title',
    '750' : 'Established Heading Linking Entry - Topical Term',
    '751' : 'Established Heading Linking Entry - Geographic Name',
    '755' : 'Established Heading Linking Entry - Genre/Form Term',
    '780' : 'Subdivision Linking Entry - General Subdivision',
    '781' : 'Subdivision Linking Entry - Geographic Subdivision',
    '782' : 'Subdivision Linking Entry - Chronological Subdivision',
    '785' : 'Subdivision Linking Entry - Form Subdivision',
    '788' : 'Complex Linking Entry Data',

    '830' : 'Series added entry-uniform title',
    '852' : 'Location',
    '856' : 'Electronic Location and Access',
    '856u' : 'URL',
    '880' : 'Alternate Graphic Representation',

    '900' : 'Local data element A',
    '901' : 'Local data element B',
    '903' : 'Local data element C',
    '904' : 'Local data element D',
    '905' : 'Local data element E',
    '906' : 'Local data element F',
    '907' : 'Local data element G',
    '908' : 'Put command parameter',
    '920' : 'Collective Biography',
    '922' : 'Availability of service copies',
    '925' : 'Series Statement of Reproduction',
    '952' : 'Cluster member',
    '953' : 'Therapeutic Classification',
    '955' : 'Copy-level information',
    '985' : 'Local Record History',
    '991' : 'Group'
    })