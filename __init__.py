#!/usr/bin/env python

__license__   = 'GPL v3'
__copyright__ = '2015, Marek Gibek'
__docformat__ = 'restructuredtext en'

from calibre.ebooks.metadata.sources.base import Source

class LubimyCzytac(Source):
	name                    = 'LubimyCzytac'
	description             = _('Downloads metadata and covers from LubimyCzytac.pl')
	author                  = 'Marek Gibek'
	version                 = (1, 0, 0)
	minimum_calibre_version = (0, 8, 15)

	capabilities = frozenset(['identify', 'cover'])
	touched_fields = frozenset(['title', 'authors', 'identifier:lubimyczytac', 'identifier:isbn', 'rating', 'comments', 'publisher', 'pubdate', 'series', 'series_index', 'tags', 'languages'])
	has_html_comments = True
	supports_gzip_transfer_encoding = True

def identify(self, log, result_queue, abort, title=None, authors=None, identifiers={}, timeout=30):
	log.info('identify')
